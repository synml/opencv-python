import numpy as np
import cv2
from matplotlib import pyplot as plt
from convolution_py import conv2D
from pyplot_template import plt_arch


def laplacian():
    src = cv2.imread('../res/lenna.bmp', cv2.IMREAD_GRAYSCALE)

    mask = np.array([[1, 1, 1],
                     [1, -8, 1],
                     [1, 1, 1]], dtype=np.float32)

    dst = conv2D(src, mask)
    dst = np.clip(dst, 0, 255)

    plt_arch(121, 'Input Image', src)
    plt_arch(122, 'Laplacian', dst)
    plt.show()


def log():
    src = cv2.imread('../res/lenna.bmp', cv2.IMREAD_GRAYSCALE)

    mask = np.array([[0, 0, -1, 0, 0],
                     [0, -1, -2, -1, 0],
                     [-1, -2, 16, -2, -1],
                     [0, -1, -2, -1, 0],
                     [0, 0, -1, 0, 0]], dtype=np.float32)

    dst = conv2D(src, mask)
    dst = np.clip(dst, 0, 255)

    plt_arch(121, 'Input Image', src)
    plt_arch(122, 'LoG', dst)
    plt.show()


def dog():
    src = cv2.imread('../res/lenna.bmp', cv2.IMREAD_GRAYSCALE)

    mask = np.array([[0, 0, -1, -1, -1, 0, 0],
                     [0, -2, -3, -3, -3, -2, 0],
                     [-1, -3, 5, 5, 5, -3, -1],
                     [-1, -3, 5, 16, 5, -3, -1],
                     [-1, -3, 5, 5, 5, -3, -1],
                     [0, -2, -3, -3, -3, -2, 0],
                     [0, 0, -1, -1, -1, 0, 0]], dtype=np.float32)

    dst = conv2D(src, mask)
    dst = np.clip(dst, 0, 255)

    plt_arch(121, 'Input Image', src)
    plt_arch(122, 'DoG', dst)
    plt.show()


def laplacian_cv():
    src = cv2.imread('../res/lenna.bmp', cv2.IMREAD_GRAYSCALE)

    dst = cv2.Laplacian(src, -1)

    plt_arch(121, 'Input Image', src)
    plt_arch(122, 'Laplacian', dst)
    plt.show()


if __name__ == '__main__':
    laplacian()
    log()
    dog()
