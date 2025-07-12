import numpy as np
import wave
from gtts import gTTS
from pydub import AudioSegment
import os
from google.colab import drive

drive.mount('/content/drive')

# 사용자 입력
bpm = float(input("메트로놈 속도 (BPM)를 입력하세요: "))
duration_minutes = float(input("작동 시간(분)을 입력하세요: "))
duration_seconds = duration_minutes * 60

# 박자 계산
beat_duration = 60 / bpm
total_beats = int(duration_seconds / beat_duration)

# 오디오 세팅
sample_rate = 44100
frequency = 1500
click_duration = 0.03
click_samples = int(sample_rate * click_duration)
t_click = np.arange(click_samples) / sample_rate
click_wave = np.sin(2 * np.pi * frequency * t_click) * 1.0
click_wave = np.int16(click_wave * 32767)

# 박자별 오디오
audio_segment = np.zeros(int(beat_duration * sample_rate), dtype=np.int16)
audio_segment[:click_samples] = click_wave

# 메트로놈 생성 (초기)
metronome = np.zeros(total_beats * int(beat_duration * sample_rate), dtype=np.int16)
for i in range(total_beats):
    start_idx = int(i * beat_duration * sample_rate)
    metronome[start_idx:start_idx + click_samples] = click_wave

# 15분마다 시간 알림 음성 추가하기
interval_beats = int((15 * 60) / beat_duration)  # 15분 간격 박자 수
for i in range(1, total_beats // interval_beats + 1):
    time_str = f"{i*15} 분 경과"
    tts = gTTS(text=time_str, lang='ko')
    tts.save("/content/temp_time.mp3")
    time_audio = AudioSegment.from_mp3("/content/temp_time.mp3")
    time_audio = time_audio.set_frame_rate(sample_rate).set_channels(1).set_sample_width(2)
    # 시간 음성 오디오를 numpy array로 변환
    time_np = np.array(time_audio.get_array_of_samples())
    # 위치 계산
    start_sample = int(i * interval_beats * beat_duration * sample_rate)
    end_sample = start_sample + len(time_np)
    if end_sample > len(metronome):
        break
    # 삽입 (현재 오디오에 병합)
    # 볼륨 조절이 필요할 경우
    metronome[start_sample:end_sample] = time_np

# 저장
file_path = "/content/metronome_with_time.wav"
with wave.open(file_path, 'w') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)
    wf.writeframes(metronome.tobytes())

# 구글 드라이브 저장
drive_path = '/content/drive/My Drive/metronome_with_time.wav'
import shutil
shutil.copy(file_path, drive_path)

print("완료! 파일 위치:", drive_path)

