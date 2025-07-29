import os
from math import ceil
import ffmpeg

# 입력 파일과 분할 설정
input_file = "src.m4a"  # 🔁 실제 파일명으로 변경
segment_duration = 600  # 600초 = 10분
output_folder = "split_segments"

# 출력 폴더 생성
os.makedirs(output_folder, exist_ok=True)


# ffmpeg-python로 전체 길이 가져오기
def get_audio_duration(filepath):
    probe = ffmpeg.probe(filepath)
    duration = float(probe['format']['duration'])
    return duration


# 전체 길이 계산
total_duration = get_audio_duration(input_file)
num_segments = ceil(total_duration / segment_duration)

# 분할 실행
for i in range(num_segments):
    start_time = i * segment_duration
    output_path = os.path.join(output_folder, f"segment_{i + 1:02}.m4a")

    command = [
        "ffmpeg",
        "-y",  # 덮어쓰기
        "-i", input_file,
        "-ss", str(start_time),
        "-t", str(segment_duration),
        "-c", "copy",
        output_path
    ]

    print(f"⏳ Segment {i + 1}/{num_segments} 생성 중...")
    os.system(" ".join(command))

print(f"\n✅ 모든 분할 완료! → 폴더: {output_folder}")
