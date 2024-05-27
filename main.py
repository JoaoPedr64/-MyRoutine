import curses
from curses import wrapper

def exercisesMenu(stdscr):
    height, width = stdscr.getmaxyx() # altura, largura
    stdscr.clear()
    stdscr.refresh()

    exercises_Win = curses.newwin(height - 2, width - 2, 1, 1)
    exercises_Win.border(0)
    exercises_Win.addstr(0, 2, " EXERCISES ", curses.A_BOLD)

    list_Win = curses.newwin(height - 9, width - 4, 3, 2)
    list_Win.border(0)
    list_Win.addstr(0, 2, " LISTA ", curses.A_BOLD)

    options_Win = curses.newwin(height - 9, width - 4, 100, 2)
    options_Win.border(0)
    options_Win.addstr(0, 2, " OPTIONS ", curses.A_BOLD)

    exercises_Win.refresh()
    list_Win.refresh()
    options_Win.refresh()
    exercises_Win.getch()

def startMenu(stdscr, opc):
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

def main(stdscr):
    curses.curs_set(0)  # Desabilitar cursor
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK) # Cor Azul id:1

    opc = 0
    while True:
        stdscr.clear()
        startMenu(stdscr, opc)

        key = stdscr.getch()

        if key == curses.KEY_UP:
            opc = (opc - 1) % 3
        elif key == curses.KEY_DOWN:
            opc = (opc + 1) % 3
        elif key == 10 or key == 13:
            if opc == 2:
                break
            elif opc == 0:
                exercisesMenu(stdscr)
            elif opc == 1:
                pass

        stdscr.refresh()

wrapper(main)
