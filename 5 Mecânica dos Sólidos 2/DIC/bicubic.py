import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
import sys, time
import sympy as sp
import pandas as pd
from statsmodels.tools.eval_measures import mse


# https://github.com/yunabe/codelab/blob/master/misc/terminal_progressbar/progress.py
def get_progressbar_str(progress):
    END = 170
    MAX_LEN = 30
    BAR_LEN = int(MAX_LEN * progress)
    return ('Progress:[' + '=' * BAR_LEN + ('>' if BAR_LEN < MAX_LEN else '') + ' ' * (MAX_LEN - BAR_LEN) + '] %.1f%%'
            % (progress * 100.))


# Interpolation kernel
def u(s, a):
    if (abs(s) >= 0) & (abs(s) <= 1):
        return (a + 2) * (abs(s) ** 3) - (a + 3) * (abs(s) ** 2) + 1
    elif (abs(s) > 1) & (abs(s) <= 2):
        return a * (abs(s) ** 3) - (5 * a) * (abs(s) ** 2) + (8 * a) * abs(s) - 4 * a
    return 0


# Paddnig
def padding(img, H, W, C):
    '''
    Set the boundary of the image to zero, and pad the image with the first/last two col and row.

    :param img: "img" is a numpy array of size H x W x C.
    :param H: "H" is the height of the image.
    :param W: "W" is the width of the image.
    :param C: "C" is the number of channels of the image.
    :return:
    '''
    # Create zero image
    zimg = np.zeros((H + 4, W + 4, C))
    zimg[2:H + 2, 2:W + 2, :C] = img
    # Pad the first/last two col and row
    zimg[2:H + 2, 0:2, :C] = img[:, 0:1, :C]
    zimg[H + 2:H + 4, 2:W + 2, :] = img[H - 1:H, :, :]
    zimg[2:H + 2, W + 2:W + 4, :] = img[:, W - 1:W, :]
    zimg[0:2, 2:W + 2, :C] = img[0:1, :, :C]
    # Pad the missing eight points
    zimg[0:2, 0:2, :C] = img[0, 0, :C]
    zimg[H + 2:H + 4, 0:2, :C] = img[H - 1, 0, :C]
    zimg[H + 2:H + 4, W + 2:W + 4, :C] = img[H - 1, W - 1, :C]
    zimg[0:2, W + 2:W + 4, :C] = img[0, W - 1, :C]
    return zimg


# Bicubic operation
def bicubic(img, ratio, a):
    '''
    Bicubic interpolation



    :param img: "img" is a numpy array of size H x W x C.
    :param ratio: "ratio" is the ratio of the new image size to the original image size.
    :param a: "a" is the parameter of the interpolation kernel.
    :return:
    '''
    # Get image size
    global mat_m
    H, W, C = img.shape

    img = padding(img, H, W, C)
    # Create new image
    dH = math.floor(H * ratio)
    dW = math.floor(W * ratio)
    dst = np.zeros((dH, dW, 3))

    h = 1 / ratio

    print('Start bicubic interpolation', end='\n')
    print('It will take a little while...', end='\n')
    inc = 0
    for c in range(C):
        for j in range(dH):
            for i in range(dW):
                x, y = i * h + 2, j * h + 2

                x1 = 1 + x - math.floor(x)
                x2 = x - math.floor(x)
                x3 = math.floor(x) + 1 - x
                x4 = math.floor(x) + 2 - x

                y1 = 1 + y - math.floor(y)
                y2 = y - math.floor(y)
                y3 = math.floor(y) + 1 - y
                y4 = math.floor(y) + 2 - y

                mat_l = np.matrix([[u(x1, a), u(x2, a), u(x3, a), u(x4, a)]])

                mat_m = np.matrix([[img[int(y - y1), int(x - x1), c], img[int(y - y2), int(x - x1), c],
                                    img[int(y + y3), int(x - x1), c], img[int(y + y4), int(x - x1), c]],
                                   [img[int(y - y1), int(x - x2), c], img[int(y - y2), int(x - x2), c],
                                    img[int(y + y3), int(x - x2), c], img[int(y + y4), int(x - x2), c]],
                                   [img[int(y - y1), int(x + x3), c], img[int(y - y2), int(x + x3), c],
                                    img[int(y + y3), int(x + x3), c], img[int(y + y4), int(x + x3), c]],
                                   [img[int(y - y1), int(x + x4), c], img[int(y - y2), int(x + x4), c],
                                    img[int(y + y3), int(x + x4), c], img[int(y + y4), int(x + x4), c]]])
                mat_r = np.matrix([[u(y1, a)], [u(y2, a)], [u(y3, a)], [u(y4, a)]])

                dst[j, i, c] = np.dot(np.dot(mat_l, mat_m), mat_r)

                # Print progress
                inc = inc + 1
                sys.stderr.write('\r\033[K' + get_progressbar_str(inc / (C * dH * dW)))
                sys.stderr.flush()
    sys.stderr.write('\n')
    sys.stderr.flush()
    return dst, mat_m


def view_bar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    r = '\r[%s%s]%d%%' % ("=" * rate_num, " " * (100 - rate_num), rate_num,)
    sys.stdout.write(r)
    sys.stdout.flush()


def plot(image_raw, image_bicubic):
    # Plot
    fig, ax = plt.subplots(1, 1, sharey=True, figsize=(16, 12))

    x, y = np.arange(0, image_raw.shape[0]), np.arange(0, image_raw.shape[1])
    xx, yy = np.meshgrid(x, y)
    z = np.array(image_raw)
    z = z[:, :, :3]
    img0 = ax[0, 0].scatter(xx, yy, c=z, s=100)
    ax[0, 0].set_title('original points')
    fig.colorbar(img0, ax=ax[0, 0], orientation='vertical', shrink=1, pad=0.01)

    z_new = np.array(image_bicubic)
    img1 = ax[0, 1].imshow(z_new, vmin=z_new.min(), vmax=z_new.max(), origin='lower',
                           extent=[xx.min(), xx.max(), yy.max(), yy.min()])
    ax[0, 1].set_title('bicubic our code')
    fig.colorbar(img1, ax=ax[0, 1], orientation='vertical', shrink=1, pad=0.01)

    plt.subplots_adjust(wspace=0.05, hspace=0.15)

    plt.show()


def coeficients(x_new, y_new):
    x, y = sp.symbols('x y')
    a00, a01, a02, a03, a10, a11, a12, a13, a20, a21, a22, a23, a30, a31, a32, a33 = sp.symbols(
        'a00 a01 a02 a03 a10 a11 a12 a13 a20 a21 a22 a23 a30 a31 a32 a33')

    p = a00 + a01 * y + a02 * y ** 2 + a03 * y ** 3 + a10 * x + a11 * x * y + a12 * x * y ** 2 + a13 * x * y ** 3 + a20 * x ** 2 + a21 * x ** 2 * y + a22 * x ** 2 * y ** 2 + a23 * x ** 2 * y ** 3 + a30 * x ** 3 + a31 * x ** 3 * y + a32 * x ** 3 * y ** 2 + a33 * x ** 3 * y ** 3

    px = sp.diff(p, x)
    py = sp.diff(p, y)
    pxy = sp.diff(p, x, y)

    df = pd.DataFrame(columns=['function', 'evaluation'])

    for i in range(2):
        for j in range(2):
            function = 'p({}, {})'.format(j, i)
            df.loc[len(df)] = [function, p.subs({x: j, y: i})]
    for i in range(2):
        for j in range(2):
            function = 'px({}, {})'.format(j, i)
            df.loc[len(df)] = [function, px.subs({x: j, y: i})]
    for i in range(2):
        for j in range(2):
            function = 'py({}, {})'.format(j, i)
            df.loc[len(df)] = [function, py.subs({x: j, y: i})]
    for i in range(2):
        for j in range(2):
            function = 'pxy({}, {})'.format(j, i)
            df.loc[len(df)] = [function, pxy.subs({x: j, y: i})]

    eqns = df['evaluation'].tolist()
    symbols = [a00, a01, a02, a03, a10, a11, a12, a13, a20, a21, a22, a23, a30, a31, a32, a33]
    A = sp.linear_eq_to_matrix(eqns, *symbols)[0]
    A = np.array(A.inv()).astype(np.float64)

    print(df)

    print(A)
    print(A.shape)
    return 0

def focus_histogram(image):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    laplacian = cv2.Laplacian(gray, cv2.CV_64F)

    variance = np.var(laplacian)

    if variance < 50:
        color = (0, 0, 255)  # red color

    elif 50 <= variance < 100:
        color = (0, 255, 255)  # yellow color

    else:
        color = (0, 255, 0)  # green color

    # Overlay composition
    img_filter = cv2.retangle(img, (0, 0), (img.shape[0], img.shape[1], variance))






if __name__ == '__main__':
    # Read image
    img = cv2.imread('img.png')
    y_0, x_0, h, w = 400, 400, 200, 200
    crop_img = img[y_0:y_0 + h, x_0:x_0 + w]

    # Scale factor (resize pixel resolution)
    ratio = 2
    # Coefficient
    a = -1 / 2

    dst, mat = bicubic(crop_img, ratio, a)
    print('Completed!')
    print('coeficientes: {}'.format(mat))
    plot(crop_img, dst)
    cv2.imwrite('img_corte.png', dst)
