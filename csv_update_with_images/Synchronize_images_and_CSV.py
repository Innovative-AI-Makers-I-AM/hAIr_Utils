import os
import pandas as pd

# CSV 파일 경로와 이미지 디렉토리 경로 설정
csv_file_path = 'hairstyles_filtered.csv'
image_dir = 'images'

# CSV 파일 불러오기
df = pd.read_csv(csv_file_path)

# 이미지 디렉토리 내의 파일 목록 얻기
image_files = {os.path.join(image_dir, f) for f in os.listdir(image_dir)}

# CSV 파일에서 'image_path' 열과 비교하여 존재하지 않는 파일 제거
df_filtered = df[df['image_path'].isin(image_files)]

# 결과를 새로운 CSV 파일로 저장
filtered_csv_file_path = 'new_hairstyles_filtered.csv'
df_filtered.to_csv(filtered_csv_file_path, index=False)