"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: the background image
    :param figure_img: the figure needed to remove the green screen
    :return: the figure in the background image
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            f_p = figure_img.get_pixel(x, y)
            b_p = background_img.get_pixel(x, y)
            bigger = max(f_p.blue, f_p.red)
            if f_p.green > bigger * 2:
                f_p.red = b_p.red
                f_p.green = b_p.green
                f_p.blue = b_p.blue
    return figure_img


def main():
    """
    This program will replace the green screen in the figure with the background image
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
