from scipy.ndimage import zoom, rotate
from PIL import Image
import numpy as np

def my_imresize(img, new_size):
    # Преобразуйте изображение в массив NumPy
    img_array = np.array(img)

    # Вычислите коэффициенты масштабирования для осей X и Y
    scale_x = new_size[1] / img_array.shape[1]
    scale_y = new_size[0] / img_array.shape[0]

    # Измените размер изображения с использованием zoom
    resized_img_array = zoom(img_array, (scale_y, scale_x, 1))

    return resized_img_array

def my_imrotate(img, angle):
    # Преобразуйте изображение в массив NumPy
    img_array = np.array(img)

    # Поворот изображения с использованием rotate
    rotated_img_array = rotate(img_array, angle, reshape=False)

    return rotated_img_array


def my_imread(im_path):
    image = Image.open(im_path)
    return np.array(image)