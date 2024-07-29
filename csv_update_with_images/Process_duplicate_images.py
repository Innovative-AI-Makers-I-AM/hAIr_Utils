import os
import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import numpy as np
import shutil
from sklearn.metrics.pairwise import cosine_similarity

# 경로 설정
execution_path = os.getcwd()

# 사전 훈련된 ResNet 모델 로드
model = models.resnet50(pretrained=True)
model.eval()

# 이미지 전처리 함수
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# 이미지 특징 추출 함수
def extract_features(image_path):
    image = Image.open(image_path).convert("RGB")
    image = preprocess(image)
    image = image.unsqueeze(0)
    with torch.no_grad():
        features = model(image)
    return features.squeeze().numpy()

# 유사한 이미지 찾기 함수
def find_similar_images(image_folder, threshold=0.98):
    image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    image_features = {}
    feature_list = []

    # 모든 이미지에 대해 특징 추출
    for image_file in image_files:
        full_image_path = os.path.join(image_folder, image_file)
        features = extract_features(full_image_path)
        image_features[image_file] = features
        feature_list.append(features)

    # 유사한 이미지 그룹화
    similar_images = {}
    feature_array = np.array(feature_list)
    similarities = cosine_similarity(feature_array)

    for idx, image in enumerate(image_files):
        for jdx, similarity in enumerate(similarities[idx]):
            if idx != jdx and similarity >= threshold:
                if image not in similar_images:
                    similar_images[image] = []
                similar_images[image].append(image_files[jdx])

    return similar_images

# 중복 이미지 이동 함수
def move_duplicates(similar_images, folder_path):
    duplicated_folder_path = os.path.join(folder_path, "Duplicated")
    if not os.path.exists(duplicated_folder_path):
        os.makedirs(duplicated_folder_path)

    moved = set()
    for image, duplicates in similar_images.items():
        for duplicate in duplicates:
            if duplicate not in moved and duplicate != image:  # 하나는 남기고 나머지를 이동
                src_path = os.path.join(folder_path, duplicate)
                dst_path = os.path.join(duplicated_folder_path, duplicate)
                shutil.move(src_path, dst_path)
                moved.add(duplicate)
                print(f"Moved: {duplicate} to {duplicated_folder_path}")
        # 원본 이미지는 남겨둠
        moved.add(image)

# organize 폴더 순회 및 중복 이미지 처리 함수
def find_and_move_duplicates(root_folder, threshold=0.98):
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        
        if os.path.isdir(folder_path):
            print(f"Processing folder: {folder_name}")
            similar_images = find_similar_images(folder_path, threshold)
            move_duplicates(similar_images, folder_path)

# organize 폴더 경로 설정
root_folder_path = os.path.join(execution_path, "organize")
find_and_move_duplicates(root_folder_path, threshold=0.98)