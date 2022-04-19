"""
File: my_drawing.py
Name: Jerry Ju
----------------------

"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLine, GArc
from campy.graphics.gwindow import GWindow
import random


def main():
    """
    Title: Totoro!

    It's been raining non-stop in Taipei recently, so I hope Totoro can come and
    share his umbrella with me.
    """
    window = GWindow(width=800, height=800, title='Totoro')
    # background = GRect(window.width, window.height)
    # background.filled = True
    # background.fill_color = 'darksage'
    # window.add(background)
    umbrella = GOval(400, 200, x=390, y=50)
    umbrella.filled = True
    umbrella.fill_color = 'darkgray'
    window.add(umbrella)
    umbrella1 = GOval(150, 150, x=370, y=120)
    umbrella1.filled = True
    umbrella1.fill_color = 'white'
    umbrella1.color = 'white'
    window.add(umbrella1)
    umbrella2 = GOval(150, 150, x=440, y=130)
    umbrella2.filled = True
    umbrella2.fill_color = 'white'
    umbrella2.color = 'white'
    window.add(umbrella2)
    umbrella3 = GOval(150, 150, x=550, y=130)
    umbrella3.filled = True
    umbrella3.fill_color = 'white'
    umbrella3.color = 'white'
    window.add(umbrella3)
    umbrella4 = GOval(150, 150, x=650, y=130)
    umbrella4.filled = True
    umbrella4.fill_color = 'white'
    umbrella4.color = 'white'
    window.add(umbrella4)
    for i in range(500):
        rand_x = random.randint(0, 799)
        rand_y = random.randint(0, 799)
        length = random.randint(1, 20)
        rain = GOval(1, length, x= rand_x, y=rand_y)
        rain.color = 'steelblue'
        window.add(rain)
    r_claw = GOval(20, 40, x=197, y=660)
    r_claw.filled = True
    r_claw.fill_color = 'black'
    window.add(r_claw)
    r_arm = GOval(150, 320, x=180, y=410)
    r_arm.filled = True
    r_arm.fill_color = 'slategray'
    window.add(r_arm)
    body = GOval(420, 500, x=190, y=350)
    body.filled = True
    body.fill_color = 'slategray'
    window.add(body)
    r_ear = GOval(40, 100, x=300, y=170)
    r_ear.filled = True
    r_ear.fill_color = 'slategray'
    window.add(r_ear)
    l_ear = GOval(40, 100, x=460, y=170)
    l_ear.filled = True
    l_ear.fill_color = 'slategray'
    window.add(l_ear)
    head = GOval(380, 600, x=210, y=240)
    head.filled = True
    head.fill_color = 'slategray'
    head.color = 'slategray'
    window.add(head)
    belly = GOval(350, 400, x=225, y=375)
    belly.filled = True
    belly.fill_color = 'whitesmoke'
    belly.color = 'whitesmoke'
    window.add(belly)
    r_eye = GOval(40, 40, x=300, y=300)
    r_eye.filled = True
    r_eye.fill_color = 'white'
    window.add(r_eye)
    r_eyeball = GOval(20, 20, x=310, y=310)
    r_eyeball.filled = True
    r_eyeball.fill_color = 'black'
    window.add(r_eyeball)
    l_eye = GOval(40, 40, x=460, y=300)
    l_eye.filled = True
    l_eye.fill_color = 'white'
    window.add(l_eye)
    l_eyeball = GOval(20, 20, x=470, y=310)
    l_eyeball.filled = True
    l_eyeball.fill_color = 'black'
    window.add(l_eyeball)
    nose = GOval(50, 20, x=375, y=310)
    nose.filled = True
    nose.fill_color = 'black'
    window.add(nose)
    mouth = GOval(6, 6, x=397, y=360)
    mouth.filled = True
    mouth.fill_color = 'black'
    window.add(mouth)
    hair1 = GLine(290, 340, 210, 330)
    window.add(hair1)
    hair2 = GLine(290, 350, 210, 350)
    window.add(hair2)
    hair3 = GLine(290, 360, 210, 370)
    window.add(hair3)
    hair4 = GLine(510, 340, 590, 330)
    window.add(hair4)
    hair5 = GLine(510, 350, 590, 350)
    window.add(hair5)
    hair6 = GLine(510, 360, 590, 370)
    window.add(hair6)
    belly_fur1 = GPolygon()
    belly_fur1.add_vertex((290, 460))
    belly_fur1.add_vertex((320, 430))
    belly_fur1.add_vertex((350, 460))
    belly_fur1.add_vertex((320, 445))
    belly_fur1.filled = True
    belly_fur1.fill_color = 'slategray'
    window.add(belly_fur1)
    belly_fur2 = GPolygon()
    belly_fur2.add_vertex((370, 460))
    belly_fur2.add_vertex((400, 430))
    belly_fur2.add_vertex((430, 460))
    belly_fur2.add_vertex((400, 445))
    belly_fur2.filled = True
    belly_fur2.fill_color = 'slategray'
    window.add(belly_fur2)
    belly_fur3 = GPolygon()
    belly_fur3.add_vertex((450, 460))
    belly_fur3.add_vertex((480, 430))
    belly_fur3.add_vertex((510, 460))
    belly_fur3.add_vertex((480, 445))
    belly_fur3.filled = True
    belly_fur3.fill_color = 'slategray'
    window.add(belly_fur3)
    belly_fur4 = GPolygon()
    belly_fur4.add_vertex((240, 510))
    belly_fur4.add_vertex((270, 480))
    belly_fur4.add_vertex((300, 510))
    belly_fur4.add_vertex((270, 495))
    belly_fur4.filled = True
    belly_fur4.fill_color = 'slategray'
    window.add(belly_fur4)
    belly_fur5 = GPolygon()
    belly_fur5.add_vertex((320, 510))
    belly_fur5.add_vertex((350, 480))
    belly_fur5.add_vertex((380, 510))
    belly_fur5.add_vertex((350, 495))
    belly_fur5.filled = True
    belly_fur5.fill_color = 'slategray'
    window.add(belly_fur5)
    belly_fur6 = GPolygon()
    belly_fur6.add_vertex((400, 510))
    belly_fur6.add_vertex((430, 480))
    belly_fur6.add_vertex((460, 510))
    belly_fur6.add_vertex((430, 495))
    belly_fur6.filled = True
    belly_fur6.fill_color = 'slategray'
    window.add(belly_fur6)
    belly_fur7 = GPolygon()
    belly_fur7.add_vertex((480, 510))
    belly_fur7.add_vertex((510, 480))
    belly_fur7.add_vertex((540, 510))
    belly_fur7.add_vertex((510, 495))
    belly_fur7.filled = True
    belly_fur7.fill_color = 'slategray'
    window.add(belly_fur7)
    l_arm = GOval(110, 80, x=510, y=425)
    l_arm.filled = True
    l_arm.fill_color = 'slategray'
    window.add(l_arm)
    l_claw1 = GOval(45, 7, x=500, y=445)
    l_claw1.filled = True
    l_claw1.fill_color = 'black'
    window.add(l_claw1)
    l_claw2 = GOval(45, 7, x=500, y=457)
    l_claw2.filled = True
    l_claw2.fill_color = 'black'
    window.add(l_claw2)
    l_claw3 = GOval(45, 7, x=500, y=469)
    l_claw3.filled = True
    l_claw3.fill_color = 'black'
    window.add(l_claw3)
    l_claw4 = GOval(45, 7, x=500, y=481)
    l_claw4.filled = True
    l_claw4.fill_color = 'black'
    window.add(l_claw4)
    stick = GLine(520, 490, 565, 148)
    window.add(stick)
    arc1 = GArc(500, 500, 100, 70)
    window.add(arc1, x=487, y=50)
    arc2 = GArc(500, 500, 5, 80)
    window.add(arc2, x=450, y=50)
    arc3 = GArc(600, 600, 136, 52)
    window.add(arc3, x=570, y=10)
    l_foot = GOval(80, 20, x=270, y=790)
    l_foot.filled = True
    l_foot.fill_color = 'black'
    window.add(l_foot)
    r_foot = GOval(80, 20, x=450, y=790)
    r_foot.filled = True
    r_foot.fill_color = 'black'
    window.add(r_foot)




if __name__ == '__main__':
    main()
