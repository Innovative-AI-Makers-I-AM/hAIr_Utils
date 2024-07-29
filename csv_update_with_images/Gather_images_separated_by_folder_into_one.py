import os
import shutil

# 경로 설정
execution_path = os.getcwd()

# 모든 이미지를 하나의 폴더로 모으는 함수 (Duplicated 폴더 제외)
def move_all_except_duplicates(root_folder, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        duplicated_folder_path = os.path.join(folder_path, "Duplicated")

        if os.path.isdir(folder_path):
            print(f"Collecting images from folder: {folder_name}")
            for image_name in os.listdir(folder_path):
                src_image_path = os.path.join(folder_path, image_name)
                if os.path.isfile(src_image_path) and not src_image_path.startswith(duplicated_folder_path):
                    dst_image_path = os.path.join(target_folder, image_name)
                    shutil.move(src_image_path, dst_image_path)
                    print(f"Moved: {src_image_path} to {dst_image_path}")

# 실행 함수
def main():
    # organize 폴더 경로 설정
    root_folder_path = os.path.join(execution_path, "organize")
    target_folder_path = os.path.join(execution_path, "Collected")

    # 모든 이미지를 하나의 폴더로 모으기 (Duplicated 폴더 제외)
    move_all_except_duplicates(root_folder_path, target_folder_path)

if __name__ == "__main__":
    main()