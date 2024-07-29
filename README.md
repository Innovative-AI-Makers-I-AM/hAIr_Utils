# hAIr_Utils
hAIr 프로젝트 진행시에 사용했던 기능들

## Crawling
카카오 스타일 북에서 사진과 사진에 해당하는 메타데이터 크롤링https://hairshop.kakao.com/search/style?category=CUT&gender=FEMALE

## 이미지 전처리
크롤링 한 이미지가 HairFastGan에서 동작하는 사진인지 확인하고 처리하는 코드

## Distinguish images.py
이미지들을 스타일별로 구별

## Process_duplicate_images.py
스타일별로 구별된 폴더에서 중복 이미지 처리

## Gather_images_separated_by_folder_into_one.py
폴더별로 구별된 이미지들 하나로 모으기

## Synchronize_images_and_CSV.py
이미지와 CSV 동기화