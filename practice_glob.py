import glob

# 특정 확장자 파일 찾기
log_files = glob.glob('logs/*.log')
txt_files = glob.glob('*.txt')

# 재귀적 검색 (하위 디렉토리 포함)
all_logs = glob.glob('logs/**/*.log', recursive=True)

# 패턴 예시
glob.glob('log_202411*.txt')  # log_20241101.txt, log_20241102.txt 등
glob.glob('data_?.csv')       # data_1.csv, data_2.csv 등
glob.glob('[abc]*.txt')       # a로 시작, b로 시작, c로 시작

# 정렬해서 가져오기
files = sorted(glob.glob('*.log'))