"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: the image to be blurred
    :return n_img: the image after blurring procedure
    """
    n_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            n_p = n_img.get_pixel(x, y)  # The pixel of new image
            m_p = img.get_pixel(x, y)  # The middle pixel of the old image
            if x - 1 >= 0:
                lq_p = img.get_pixel(x-1, y)  # The left quadrant pixel of the old image
            if x - 1 >= 0 and y - 1 >= 0:
                luq_p = img.get_pixel(x-1, y)  # The left upper quadrant pixel of the old image
            if x - 1 >= 0 and y <= img.height - 2:
                llq_p = img.get_pixel(x-1, y+1)  # The left lower quadrant pixel of the old image
            if y - 1 >= 0:
                uq_p = img.get_pixel(x, y-1)  # The upper quadrant pixel of the old image
            if y <= img.height - 2:
                lower_p = img.get_pixel(x, y+1)  # The lower quadrant pixel of the old image
            if x <= img.width - 2 and y - 1 >= 0:
                ruq_p = img.get_pixel(x+1, y-1)  # The right upper quadrant pixel of the old image
            if x <= img.width - 2:
                rq_p = img.get_pixel(x+1, y)  # The right quadrant pixel of the old image
            if x <= img.width - 2 and y <= img.height - 2:
                rlq_p = img.get_pixel(x+1, y+1)  # The right lower quadrant pixel of the old image
            if x == 0 and y == 0:
                n_p.red = (m_p.red + rq_p.red + lower_p.red + rlq_p.red) // 4
                n_p.green = (m_p.green + rq_p.green + lower_p.green + rlq_p.green) // 4
                n_p.blue = (m_p.blue + rq_p.blue + lower_p.blue + rlq_p.blue) // 4
            elif x == img.width - 1 and y == 0:
                n_p.red = (m_p.red + lq_p.red + llq_p.red + lower_p.red) // 4
                n_p.green = (m_p.green + lq_p.green + llq_p.green + lower_p.green) // 4
                n_p.blue = (m_p.blue + lq_p.blue + llq_p.blue + lower_p.blue) // 4
            elif x == 0 and y == img.height - 1:
                n_p.red = (m_p.red + rq_p.red + ruq_p.red + uq_p.red) // 4
                n_p.green = (m_p.green + rq_p.green + ruq_p.green + uq_p.green) // 4
                n_p.blue = (m_p.blue + rq_p.blue + ruq_p.blue + uq_p.blue) // 4
            elif x == img.width - 1 and y == img.height - 1:
                n_p.red = (m_p.red + lq_p.red + luq_p.red + uq_p.red) // 4
                n_p.green = (m_p.green + lq_p.green + luq_p.green + uq_p.green) // 4
                n_p.blue = (m_p.blue + lq_p.blue + luq_p.blue + uq_p.blue) // 4
            elif x == 0:
                n_p.red = (m_p.red + uq_p.red + lower_p.red + ruq_p.red + rq_p.red + rlq_p.red) // 6
                n_p.green = (m_p.green + uq_p.green + lower_p.green + ruq_p.green + rq_p.green + rlq_p.green) // 6
                n_p.blue = (m_p.blue + uq_p.blue + lower_p.blue + ruq_p.blue + rq_p.blue + rlq_p.blue) // 6
            elif x == img.width - 1:
                n_p.red = (m_p.red + uq_p.red + lower_p.red + luq_p.red + lq_p.red + llq_p.red) // 6
                n_p.green = (m_p.green + uq_p.green + lower_p.green + luq_p.green + lq_p.green + llq_p.green) // 6
                n_p.blue = (m_p.blue + uq_p.blue + lower_p.blue + luq_p.blue + lq_p.blue + llq_p.blue) // 6
            elif y == 0:
                n_p.red = (m_p.red + lq_p.red + rq_p.red + llq_p.red + lower_p.red + rlq_p.red) // 6
                n_p.green = (m_p.green + lq_p.green + rq_p.green + llq_p.green + lower_p.green + rlq_p.green) // 6
                n_p.blue = (m_p.blue + lq_p.blue + rq_p.blue + llq_p.blue + lower_p.blue + rlq_p.blue) // 6
            elif y == img.height - 1:
                n_p.red = (m_p.red + lq_p.red + rq_p.red + luq_p.red + uq_p.red + ruq_p.red) // 6
                n_p.green = (m_p.green + lq_p.green + rq_p.green + luq_p.green + uq_p.green + ruq_p.green) // 6
                n_p.blue = (m_p.blue + lq_p.blue + rq_p.blue + luq_p.blue + uq_p.blue + ruq_p.blue) // 6
            else:
                n_p.red = (m_p.red + lq_p.red + rq_p.red + llq_p.red + lower_p.red + rlq_p.red + luq_p.red + uq_p.red + ruq_p.red) // 9
                n_p.green = (m_p.green + lq_p.green + rq_p.green + llq_p.green + lower_p.green + rlq_p.green + luq_p.green + uq_p.green + ruq_p.green) // 9
                n_p.blue = (m_p.blue + lq_p.blue + rq_p.blue + llq_p.blue + lower_p.blue + rlq_p.blue + luq_p.blue + uq_p.blue + ruq_p.blue) // 9
    return n_img


def main():
    """
    This program will produce the blurred image
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
