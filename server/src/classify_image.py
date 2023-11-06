import cv2
import numpy as np

def image_classifiaction(filename):
    image = cv2.imread(f'{filename}')

    # 이미지를 그레이스케일로 변환합니다.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 이미지를 이진화합니다.
    _, binary = cv2.threshold(gray, 7, 255, cv2.THRESH_BINARY)


    # 이진화 이미지에서 사료를 나타내는 특정 색상 또는 패턴을 검출합니다.
    # 이 예제에서는 검은색 픽셀을 검출합니다. 색상이나 패턴이 다를 수 있습니다.
    has_pet_food = np.sum(binary < 255) > 0
    print(has_pet_food)

    if has_pet_food:
        print('0')
        return 0
    else:
        print('1')
        return 1