import os
import whisper

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Input folder and output path setup
segment_folder = os.path.join(script_dir, "split_segments")
output_folder = os.path.join(script_dir, "transcripts")
output_file = os.path.join(output_folder, "full_transcription.txt")

# Load Whisper model (small models are faster)
model = whisper.load_model("base")  # Can also use "small" or "medium"

# Ensure the output directory exists
os.makedirs(output_folder, exist_ok=True)

# Check if the input folder exists
if not os.path.exists(segment_folder):
    print(f"❌ Input directory '{segment_folder}' does not exist.")
    print(f"🔧 Please make sure the required folder and files are available.")
    exit(1)

# List and sort segment files
segment_files = sorted([
    f for f in os.listdir(segment_folder)
    if f.endswith(".m4a")
])

# Accumulate all text
all_text = []

print(f"🔍 Processing {len(segment_files)} segment files...")

# Process each segment audio file
for idx, filename in enumerate(segment_files, start=1):
    segment_path = os.path.join(segment_folder, filename)
    print(f"🎙️ ({idx}/{len(segment_files)}) Processing: {filename}")

    try:
        result = model.transcribe(segment_path, language="ko")
        all_text.append(f"\n--- [Segment {idx:02}] {filename} ---\n")
        all_text.append(result["text"])
    except Exception as e:
        print(f"⚠️ Error while processing {filename}: {e}")

# Save the text results to a file
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(all_text))

print(f"\n✅ Transcription saved to '{output_file}'.")
