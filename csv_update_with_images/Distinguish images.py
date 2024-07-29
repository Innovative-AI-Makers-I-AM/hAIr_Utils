import os
import shutil

# 이미지 파일이 있는 폴더 경로
source_folder = 'images'  # 예: C:/Users/Username/Images

# 파일을 정리할 폴더 경로
destination_base_folder = 'organize'  # 예: C:/Users/Usern                                 ame/OrganizedImages

# 폴더가 없으면 생성
if not os.path.exists(destination_base_folder):
    os.makedirs(destination_base_folder)

# 폴더 내의 파일들 반복
for filename in os.listdir(source_folder):
    if filename.endswith((".jpg", ".jpeg", ".png", ".gif")):  # 이미지 파일 확장자 확인
        # 파일 이름에서 번호 제거
        base_name = filename.rsplit('_', 1)[0]

        # 각 파일 이름에 해당하는 폴더 생성
        target_folder = os.path.join(destination_base_folder, base_name)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        
        # 파일 복사
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(target_folder, filename)
        shutil.copy(source_file, destination_file)

print("이미지 정리가 완료되었습니다.")