import curses
from curses import wrapper
import time

def main(stdscr):

    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)

    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    RED_AND_WHITE = curses.color_pair(3)

    # stdscr.clear()
    # stdscr.addstr(10, 10, "hello world", GREEN_AND_BLACK)
    # stdscr.addstr(15, 25, "Faiz is great!", BLUE_AND_YELLOW | curses.A_BOLD)
    # stdscr.refresh()
    # stdscr.getch()

    #For loop using stdscr
    # for i in range(100):
    #     stdscr.clear()
    #     color = BLUE_AND_YELLOW

    #     if i % 2 == 0:
    #         color = GREEN_AND_BLACK
    #     stdscr.addstr(f"Count: {i}", color)
    #     stdscr.refresh()    
    #     time.sleep(0.1)

    # counter_win = curses.newwin(1, 20, 10, 10)
    ## The first pair is the size of the window, and the second pair is y/x coordinate ## from the screen.
    # stdscr.addstr("hello world")
    # stdscr.refresh()

    #For loop using a new window
    # for i in range(100):
    #     counter_win.clear()
    #     color = BLUE_AND_YELLOW

    #     if i % 2 == 0:
    #         color = GREEN_AND_BLACK
    #     counter_win.addstr(f"Count: {i}", color)
    #     counter_win.refresh()    
    #     time.sleep(0.1)

    pad = curses.newpad(100, 100)
    # The size of the pad
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(67 + j)
            pad.addstr(char, GREEN_AND_BLACK)

    for i in range(50):
        stdscr.clear()
        stdscr.refresh()
        # pad.refresh(0, i, 5 + i, i, 10 + i, 25 + i)
        pad.refresh(i, 0, 0, 0, 20, 20)
        time.sleep(0.2)

    
    #First coordinates y/x : Coordinates of where we want start showing padded content.
    #Second coordinates y/x : Coordinates of where we want start display showing padded 

    stdscr.getch()

wrapper(main)

 