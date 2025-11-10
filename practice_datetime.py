from datetime import datetime, timedelta

# 현재 시간
now = datetime.now()
print(now)  # 2024-11-10 15:30:45.123456

# 포맷팅 (로그 파일명에 자주 사용)
timestamp = now.strftime('%Y%m%d_%H%M%S')
print(timestamp)  # 20241110_153045

log_filename = f'log_{timestamp}.txt'

# 자주 쓰는 포맷
now.strftime('%Y-%m-%d')           # 2024-11-10
now.strftime('%Y-%m-%d %H:%M:%S')  # 2024-11-10 15:30:45
now.strftime('%Y년 %m월 %d일')      # 2024년 11월 10일

# 날짜 계산
yesterday = now - timedelta(days=1)
next_week = now + timedelta(weeks=1)
three_hours_ago = now - timedelta(hours=3)

# 문자열을 datetime으로 변환
date_str = '2024-11-10'
date_obj = datetime.strptime(date_str, '%Y-%m-%d')