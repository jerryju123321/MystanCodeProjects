"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 225


def main():
    """
    I want to take airplane to travel after the pandemic!!
    """
    background = SimpleImage('image_contest/background.png')
    figure = SimpleImage('image_contest/Jerry.png')
    background.make_as_big_as(figure)
    for x in range(figure.width):
        for y in range(figure.height):
            f_p = figure.get_pixel(x, y)
            b_p = background.get_pixel(x, y)
            if (f_p.green + f_p.red + f_p.blue) // 3 >= THRESHOLD:
                f_p.red = b_p.red
                f_p.green = b_p.green
                f_p.blue = b_p.blue
    figure.show()


if __name__ == '__main__':
    main()
