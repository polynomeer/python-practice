import os
import whisper

# Load the Whisper model (you can change to "small", "medium", etc.)
model = whisper.load_model("base")

# Input and output paths
segment_folder = "split_segments"
output_folder = "transcripts"
output_text = os.path.join(output_folder, "full_transcription.txt")
progress_log = os.path.join(output_folder, "processed.log")

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

# Open the output and progress log files
with open(output_text, "a", encoding="utf-8") as out_file, \
        open(progress_log, "a", encoding="utf-8") as log_file:
    print(f"🔍 Found {len(segment_files)} files. {len(processed_segments)} already processed.\n")

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
