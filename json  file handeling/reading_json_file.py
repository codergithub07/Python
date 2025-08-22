import json
import os
import re
import pandas as pd

base_path = r'datasets/intent_classification_dataset'

def parse_snips_data(base_path):
    intents = [x for x in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, x))]
    data = []
    
    for intent in intents:
        intent_path = os.path.join(base_path, intent)
        for file in os.listdir(intent_path):
            if file.startswith('train'):
                file_path = os.path.join(intent_path, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        json_data = json.load(f)
                except UnicodeEncodeError:
                    try:
                        with open(file_path, 'r', encoding='latin-1') as f:
                            json_data = json.load(f)
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")
                        continue
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from {file_path}: {e}")
                    continue
                
                if intent in json_data:
                    examples = json_data[intent]
                
                for example in examples:
                    if 'data' not in example:
                        continue
                    
                    text_parts = []
                    
                    for item in example['data']:
                        if 'text' in item:
                            text_parts.append(item['text'])
                            
                    full_text = ' '.join(text_parts)
                    
                    cleaned_text = re.sub(r'\s+', ' ', full_text).strip()
                    data.append((cleaned_text, intent))

    return pd.DataFrame(data, columns=['text', 'intent'])

def main():
    print("Reading JSON file...")
    data = parse_snips_data(base_path)
    print(data.tail())  # Print last 5 examples for verification

if __name__ == '__main__':
    main()