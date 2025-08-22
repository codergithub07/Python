import os
import json
import cv2
import base64

def encode_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def invert_image_and_update_json(image_path, json_path, output_dir):
    image = cv2.imread(image_path)
    h, w = image.shape[:2]
    image_flipped = cv2.flip(image, 1)

    # Save flipped image
    image_name = os.path.basename(image_path)
    out_img_path = os.path.join(output_dir, image_name)
    cv2.imwrite(out_img_path, image_flipped)

    # Load and update JSON
    with open(json_path, 'r') as f:
        data = json.load(f)

    for shape in data.get("shapes", []):
        shape["points"] = [[w - x, y] for x, y in shape["points"]]

    data["imagePath"] = image_name
    data["imageWidth"] = w
    data["imageHeight"] = h
    data["imageData"] = encode_image_as_base64(out_img_path)

    # Save updated JSON
    json_name = os.path.basename(json_path)
    out_json_path = os.path.join(output_dir, json_name)
    with open(out_json_path, 'w') as f:
        json.dump(data, f, indent=4)

def process_directory(parent_dir):
    # Gather names of already-inverted folders
    inverted_folders = {name for name in os.listdir(parent_dir) if name.startswith("inverted_")}

    # Build a set of originals that already have inverted versions
    used_originals = {name.replace("inverted_", "") for name in inverted_folders}

    for subdir_name in os.listdir(parent_dir):
        if subdir_name.startswith("inverted_"):
            continue  # ⛔ Skip inverted folders

        if subdir_name in used_originals:
            print(f"Skipping '{subdir_name}' (already inverted previously)")
            continue  # ⛔ Skip if it already has an inverted version

        subdir_path = os.path.join(parent_dir, subdir_name)
        if not os.path.isdir(subdir_path):
            continue

        output_subdir = os.path.join(parent_dir, f"inverted_{subdir_name}")
        os.makedirs(output_subdir, exist_ok=True)

        for file in os.listdir(subdir_path):
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(subdir_path, file)
                json_filename = os.path.splitext(file)[0] + '.json'
                json_path = os.path.join(subdir_path, json_filename)

                if os.path.exists(json_path):
                    invert_image_and_update_json(image_path, json_path, output_subdir)
                    print(f"Processed {file} in {subdir_name}")
                else:
                    print(f"No matching JSON for {file} in {subdir_name}")

if __name__ == "__main__":
    parent_directory = "./"
    process_directory(parent_directory)
