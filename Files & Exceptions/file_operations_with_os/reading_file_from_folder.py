import os
from pydub import AudioSegment

audio_dir = '/media/tony/ddrive/Private/ME/Call Recordings/Call Recordings Mom (1)'
output_dir = 'file_operations_with_os/converted_audio'  # Convert files in the same directory, you can change this path

for file in os.listdir(audio_dir):
    if file.endswith('.m4a'):
        # Get the full path of the input file
        input_path = os.path.join(audio_dir, file)
        
        # Create output filename by replacing .m4a with .wav
        output_filename = file.replace('.m4a', '.wav')
        output_path = os.path.join(output_dir, output_filename)
        
        try:
            print(f"Converting: {file}")
            # Load the audio file
            sound = AudioSegment.from_file(input_path, format="m4a")
            # Export as WAV
            sound.export(output_path, format="wav")
            print(f"Converted successfully: {output_filename}")
        except Exception as e:
            print(f"Error converting {file}: {str(e)}")
            