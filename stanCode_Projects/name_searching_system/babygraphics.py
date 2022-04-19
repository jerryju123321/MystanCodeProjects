"""
File: babygraphics.py
Name: Jerry Ju
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_interval = (width - GRAPH_MARGIN_SIZE * 2) // len(YEARS)
    return GRAPH_MARGIN_SIZE + x_interval * year_index


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Draw horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    # Draw vertical line and mark the year
    for i in range(len(YEARS)):
        x_position = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_position, 0, x_position, CANVAS_HEIGHT)
        canvas.create_text(x_position, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    y_interval = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / MAX_RANK  # The y interval between each rank
    count = 0  # The count of the color

    for name in lookup_names:
        if name in name_data:
            color = COLORS[count]  # Provide the color of the name and the line
            for i in range(len(YEARS)):
                x_position = get_x_coordinate(CANVAS_WIDTH, i)
                year = str(YEARS[i])

                # The condition if the rank is within 1000 in the lookup year
                if year in name_data[name]:
                    rank = int(name_data[name][year])
                    y_position = int(rank * y_interval + GRAPH_MARGIN_SIZE)

                # The condition if the rank is out of 1000 in the lookup year
                else:
                    rank = '*'
                    y_position = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

                # Mark the name and the rank in the lookup year
                canvas.create_text(x_position+TEXT_DX, y_position, text=(name, rank), anchor=tkinter.SW, fill=color)

                # Draw the line between two years
                if i >= 1:
                    canvas.create_line(pre_x, pre_y, x_position, y_position, width=LINE_WIDTH, fill=color)
                pre_x = x_position  # The x position of the previous year
                pre_y = y_position  # The y position of the previous year

            count = (count + 1) % 4  # Change the color following the list order


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
