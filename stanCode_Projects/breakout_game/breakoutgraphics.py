"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window_width-paddle_width)/2, y=self.window_height-paddle_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=self.window_width/2-ball_radius, y=self.window_height/2-ball_radius)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.set_ball_velocity()

        # Initialize our mouse listeners
        onmouseclicked(self.start_game)
        onmousemoved(self.move_paddle)

        # Detect whether the game start or not
        self.is_start_game = False

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                brick = GRect(brick_width, brick_height)
                self.window.add(brick, x=i*(brick_width+ brick_spacing), y=brick_offset+j*(brick_height+brick_spacing))
                brick.filled = True
                if j <= 1:
                    brick.fill_color = 'red'
                elif 2 <= j <= 3:
                    brick.fill_color = 'orange'
                elif 4 <= j <= 5:
                    brick.fill_color = 'yellow'
                elif 6 <= j <= 7:
                    brick.fill_color = 'green'
                else:
                    brick.fill_color = 'blue'
        self.brick_number = brick_rows * brick_cols

    def move_paddle(self, event):
        """
        :param event: MouseEvent, the x and y position of the mouse
        This function moves the paddle according to the x position of the mouse
        """
        if self.paddle.width/2 <= event.x < self.window.width-self.paddle.width/2:
            self.paddle.x = event.x - self.paddle.width/2

    def start_game(self, event):
        """
        :param event: MouseEvent, the click of the mouse
        This function detect the click of the mouse and start the game
        """
        self.is_start_game = True

    def reset_game(self):
        """
        This function reset the ball position and the ball velocity
        """
        self.window.add(self.ball, x=self.window_width/2-BALL_RADIUS, y=self.window_height/2-BALL_RADIUS)
        self.set_ball_velocity()
        self.is_start_game = False

    def set_ball_velocity(self):
        """
        This function set the ball velocity randomly
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx *= -1
        self.__dy = INITIAL_Y_SPEED

    def is_hit_paddle(self, ball_x, ball_y):
        """
        :param ball_x: int, the x position of the ball
        :param ball_y: int, the y position of the ball
        :return: Bool, whether the ball hit the paddle or not
        """
        # The object meeting at the border of the ball
        ball_llb = self.window.get_object_at(ball_x, ball_y+self.ball.height)  # Left lower border
        ball_lub = self.window.get_object_at(ball_x, ball_y)  # Left upper border
        ball_rlb = self.window.get_object_at(ball_x+self.ball.width, ball_y+self.ball.height)  # Right lower border
        ball_rub = self.window.get_object_at(ball_x+self.ball.width, ball_y)  # Right upper border

        # Detect whether the ball hit the paddle
        if ball_llb is not None and ball_llb == self.paddle:
            return True
        if ball_lub is not None and ball_lub == self.paddle:
            return True
        if ball_rlb is not None and ball_rlb == self.paddle:
            return True
        if ball_rub is not None and ball_rub == self.paddle:
            return True

    def is_hit_and_remove_brick(self, ball_x, ball_y):
        """
        :param ball_x: int, the x position of the ball
        :param ball_y: int, the y position of the ball
        :return: Bool, whether the ball hit and remove the brick or not
        """
        # The object meeting at the border of the ball
        ball_llb = self.window.get_object_at(ball_x, ball_y+self.ball.height)  # Left lower border
        ball_lub = self.window.get_object_at(ball_x, ball_y)  # Left upper border
        ball_rlb = self.window.get_object_at(ball_x+self.ball.width, ball_y+self.ball.height)  # Right lower border
        ball_rub = self.window.get_object_at(ball_x+self.ball.width, ball_y)  # Right upper border

        # Detect whether the ball hit brick
        if ball_llb is not None and ball_llb != self.paddle:
            self.window.remove(ball_llb)
            return True
        if ball_lub is not None and ball_lub != self.paddle:
            self.window.remove(ball_lub)
            return True
        if ball_rlb is not None and ball_rlb != self.paddle:
            self.window.remove(ball_rlb)
            return True
        if ball_rub is not None and ball_rub != self.paddle:
            self.window.remove(ball_rub)
            return True

    def get_dx(self):
        """
        :return: the x velocity
        """
        return self.__dx

    def get_dy(self):
        """
        :return: the y velocity
        """
        return self.__dy