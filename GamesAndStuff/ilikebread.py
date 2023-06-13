import curses


def diary(stdscr):
    stdscr.addstr(0, 0, "Press any key (except '`' to quit):")
    stdscr.refresh()

    quote = "I like bread."
    row, col = 1, 0

    while True:
        key = stdscr.getch()

        if key == ord('`'):
            break

        stdscr.addstr(row, col, quote[col], curses.A_BOLD)
        stdscr.refresh()

        col += 1
        if col == len(quote):
            col = 0
            stdscr.erase()

if __name__ == '__main__':
    curses.wrapper(diary)