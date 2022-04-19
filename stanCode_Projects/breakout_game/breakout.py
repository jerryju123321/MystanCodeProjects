"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from campy.graphics.gobjects import GLabel
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    """
    This function simulates the breakout game
    """
    graphics = BreakoutGraphics()
    life = NUM_LIVES
    ball_dx = graphics.get_dx()
    ball_dy = graphics.get_dy()
    count = 0  # The count of removed bricks

    # Ball animation
    while True:
        pause(FRAME_RATE)

        # The game start after the mouse click
        if graphics.is_start_game:
            graphics.ball.move(ball_dx, ball_dy)
        if graphics.ball.x < 0 or graphics.ball.x > graphics.window.width - graphics.ball.width:
            ball_dx *= -1
        if graphics.ball.y < 0:
            ball_dy *= -1

        # Check for collisions
        if graphics.is_hit_paddle(graphics.ball.x, graphics.ball.y) and ball_dy > 0:
            ball_dy *= -1
        if graphics.is_hit_and_remove_brick(graphics.ball.x, graphics.ball.y):
            ball_dy *= -1
            count += 1

        # The ball dropped on the floor
        if graphics.ball.y > graphics.window.height - graphics.ball.height:
            life -= 1
            graphics.reset_game()
            ball_dx = graphics.get_dx()

        # The winning condition
        if count == graphics.brick_number:
            win = GLabel('You win!')
            win.font = '-80'
            graphics.window.add(win, x=graphics.window.width/2-140, y=graphics.window.height/2)
            break

        # The losing condition
        if life == 0:
            game_over = GLabel('Game over!')
            game_over.font = '-80'
            graphics.window.add(game_over, x=graphics.window.width/2-200, y=graphics.window.height/2)
            break


if __name__ == '__main__':
    main()
