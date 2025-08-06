import os
import whisper

# Load the Whisper modelΩ
model = whisper.load_model("base")

# Input and output paths, adjusted for absolute paths to avoid errors
script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
segment_folder = os.path.join(script_dir, "split_segments")
output_folder = os.path.join(script_dir, "transcripts")
output_text = os.path.join(output_folder, "full_transcription.txt")
progress_log = os.path.join(output_folder, "processed.log")

# Ensure the segment_folder exists AND is readable
if not os.path.exists(segment_folder):
    raise FileNotFoundError(f"The folder '{segment_folder}' does not exist. Please check its path.")
if not os.access(segment_folder, os.R_OK):
    raise PermissionError(f"The folder '{segment_folder}' exists but is not readable. Please check permissions.")

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load previously processed segment filenames
processed_segments = set()
if os.path.exists(progress_log):
    with open(progress_log, "r", encoding="utf-8") as f:
        processed_segments = set(line.strip() for line in f if line.strip())

# Get and sort all segment files
segment_files = sorted([
    f for f in os.listdir(segment_folder)
    if f.endswith(".m4a")
])

if not segment_files:
    print(f"🔍 No .m4a files found in '{segment_folder}'.")
else:
    print(f"🔍 Found {len(segment_files)} files. {len(processed_segments)} already processed.\n")

# Open the output and progress log files
with open(output_text, "a", encoding="utf-8") as out_file, \
        open(progress_log, "a", encoding="utf-8") as log_file:
    for idx, filename in enumerate(segment_files, start=1):
        if filename in processed_segments:
            print(f"⏩ Skipping (already processed): {filename}")
            continue

        segment_path = os.path.join(segment_folder, filename)
        print(f"🎙️ ({idx}) Processing: {filename}")

        try:
            # Transcribe the audio file
            result = model.transcribe(segment_path, language="ko")

            # Write the transcription to the output file
            out_file.write(f"\n[Segment: {filename}]\n")
            out_file.write(result["text"] + "\n")
            out_file.flush()  # Ensure progress is saved

            # Log the processed file
            log_file.write(filename + "\n")
            log_file.flush()

        except Exception as e:
            print(f"⚠️ Error processing {filename}: {e}")
