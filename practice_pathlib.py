from pathlib import Path

# 경로 객체 생성
log_dir = Path('logs')
log_file = Path('logs/app.log')

# 디렉토리 생성
log_dir.mkdir(exist_ok=True)
log_dir.mkdir(parents=True, exist_ok=True)  # 중첩 디렉토리

# 존재 확인
log_file.exists()
log_file.is_file()
log_file.is_dir()

# 경로 조합 (/ 연산자 사용!)
log_path = Path('logs') / 'app.log'
nested = Path('logs') / '2024' / '11' / 'app.log'

# 파일명/확장자
file = Path('report.txt')
print(file.name)       # report.txt
print(file.stem)       # report
print(file.suffix)     # .txt
print(file.parent)     # .

# 파일 읽기/쓰기 (간편!)
log_path.write_text('로그 내용')
content = log_path.read_text()

# glob과 함께 사용
log_files = list(Path('logs').glob('*.log'))
all_logs = list(Path('logs').rglob('*.log'))  # 재귀적 검색

# 홈 디렉토리
home = Path.home()