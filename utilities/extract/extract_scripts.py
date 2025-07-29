import whisper

# pip install openai-whisper
# pip install ffmpeg-python
# 1. Whisper 모델 불러오기 (base/medium 추천, tiny는 정확도 낮음)
model = whisper.load_model("medium")  # 또는 "base", "small"

# 2. 변환할 m4a 오디오 파일 경로
audio_path = "src.m4a"  # 현재 폴더에 위치할 것

# 3. 음성 인식 실행 (language="ko"로 명시)
result = model.transcribe(audio_path, language="ko")

# 4. 결과 출력
print("🔊 extracted scripts:")
print(result["text"])

# 5. 결과를 txt 파일로 저장
output_path = "transcription.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"\n✅ Extracted scripts save to '{output_path}'")
