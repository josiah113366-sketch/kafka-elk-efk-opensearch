"""
Smart Factory Sensor 로그 생성기 
- 해당 파이썬 파일은 장비로 이해 -> 장비가 신호/로그 발생 -> 감지 -> 데이터 파이프라인 전개 구조 
- 로그 파일
  - sensor_json.log : JSONL 포맷 
  - sensor_text.log : Text 포맷
  - 각 파일이 10MB 도달하면 로테이션 시도 -> xxx-1, xxx-2, ... 파일 신규로 생성
  - 최대 유지 파일 수는 5개 설정, 6개가 되면 가장 오래된 파일 1개를 삭제
"""
# 1. 모듈 가져오기 
import datetime
import json
import logging
import os 
import random
import time
from logging.handlers import RotatingFileHandler

# 2. 환경 변수, 상수(고정값) 세팅
LOG_DIR = "./sensor_logs"        # 도커 컴포즈가 생성했음, 본 파일, Fluent-Bit가 참조함
MAX_LOG_BYTES = 10 * 1024 * 1024 # 10MB 
BACKUP_COUNT = 5                 # 로그 파일 최대 개수
os.makedirs(LOG_DIR, exist_ok=True) # 로그 파일이 생기는 폴더 생성 시도

# 3-2. 로그 발생
def generate_logs():
  pass

# 3-1. 메인 함수 
def main() -> None:
  try: 
    while True: # 공장 통상 24시간 가동. 무중단, 강제 종료(셧다운) 외엔 종료 없음 
      # 로그 발생
      generate_logs()
      # 잠시 대기 -> 테스트 상 텀 부여
      time.sleep(2) # 명시적 대기 -> 추후 조정 
  except Exception as e:
    print("종료 처리", e)

# 3. 엔트리 포인트 (프로그램 시작점)
if __name__ == "__main__":
  print("센서 로그 발생 시작. 종료 Ctrl + C")
  main()