import curses
from curses import wrapper

def draw_menu(win, options, opc):
    win.clear()
    win.border(0)
    y, x = 1, 2 
    for idx, option in enumerate(options):
        if idx == opc:
            win.attron(curses.color_pair(1))
            win.addstr(y, x, option)
            win.attroff(curses.color_pair(1))
        else:
            win.addstr(y, x, option)
        x += len(option) + 2 
    win.refresh()

def exercisesMenu(stdscr, height, width):
    stdscr.clear()
    stdscr.refresh()

    min_height = 30
    min_width = 80

    if height < min_height or width < min_width:
        stdscr.clear()
        error_msg = "Terminal size is too small. Please resize your terminal."
        stdscr.addstr(0, 0, error_msg, curses.color_pair(2))
        stdscr.refresh()
        stdscr.getch()
        return

    exercises_Win = curses.newwin(height - 2, width - 2, 1, 1)
    exercises_Win.border(0)
    exercises_Win.addstr(0, 2, " EXERCISES ", curses.A_BOLD)

    list_Win = curses.newwin(height - 9, width - 4, 3, 2)
    list_Win.border(0)
    list_Win.addstr(0, 2, " LISTA ", curses.A_BOLD)

    options_Win = curses.newwin(7, width - 4, height - 6, 2)
    options_Win.border(0)
    options_Win.addstr(0, 2, " OPTIONS ", curses.A_BOLD)

    options_opc = ['[1] Select  ', '[2] Edit  ', '[3] Delete  ', '[4] Exit']

    options_idx = 0
    draw_menu(options_Win, options_opc, options_idx)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_LEFT:
            options_idx = (options_idx - 1) % len(options_opc)
        elif key == curses.KEY_RIGHT:
            options_idx = (options_idx + 1) % len(options_opc)
        elif key == 10 or key == 13:
            if options_idx == 3:
                break

        draw_menu(options_Win, options_opc, options_idx)

        exercises_Win.refresh()
        options_Win.refresh()
        list_Win.refresh()

def startMenu(stdscr, opc, height, width):

    min_height = 30
    min_width = 80

    if height < min_height or width < min_width:
        stdscr.clear()
        error_msg = "Terminal size is too small. Please resize your terminal."
        stdscr.addstr(0, 0, error_msg, curses.color_pair(2))
        stdscr.refresh()
        stdscr.getch()
        return

    title = (" __ __  __   __ ___    __    _  _   _____   _   __  _   ___\n"
             "|  V  | \\ `v' /| _ \\  /__\\  | || | |_   _| | | |  \\| | | __|\n"
             "| \\_/ |  `. .' | v / | \\/ | | \\/ |   | |   | | | | ' | | _|\n"
             "|_| |_|   !_!  |_|_\\  \\__/   \\__/    |_|   |_| |_|\\__| |___|")
    stdscr.addstr(title, curses.color_pair(1))

    options = ['\n\n[1] Exercises\n', '[2] Studies\n', '[3] Exit']
    for idx, option in enumerate(options):
        if idx == opc:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(option)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(option)

    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)  # Desabilitar cursor
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK) # Cor Azul id:1
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) # Cor Vermelha id:2

    opc = 0
    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx() # altura, largura
        startMenu(stdscr, opc, height, width)

        key = stdscr.getch()

        if key == curses.KEY_UP:
            opc = (opc - 1) % 3
        elif key == curses.KEY_DOWN:
            opc = (opc + 1) % 3
        elif key == 10 or key == 13:
            if opc == 2:
                break
            elif opc == 0:
                exercisesMenu(stdscr, height, width)
            elif opc == 1:
                pass

        stdscr.refresh()

wrapper(main)
