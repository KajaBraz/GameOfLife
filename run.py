from game_of_life import fill_the_board, active_neighbours_num, go_round, draw
import time

if __name__ == '__main__':
    b1 = fill_the_board(70, 70)

    b2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    ]

    f1 = open('game_of_life1.txt', 'a')
    f2 = open('game_of_life2.txt', 'a')

    while True:
        s1 = draw(b1)
        s2 = draw(b2)
        f1 = open('game_of_life1.txt', 'a')
        f2 = open('game_of_life2.txt', 'a')
        f1.write(s1)
        f2.write(s2)
        f1.close()
        f2.close()
        b1 = go_round(b1, active_neighbours_num)
        b2 = go_round(b2, active_neighbours_num)
        time.sleep(0.15)
