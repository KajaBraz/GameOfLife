import random


def fill_the_board(x, y):
    b = []
    for i in range(x):
        b.append([])
        for j in range(y):
            j = random.randrange(2)
            b[i].append(j)
    return b


def active_neighbours_num(b):
    b_copy = b[:][:]
    act_neigh_list = []
    for i in range(len(b_copy)):
        act_neigh = 0
        act_neigh_list.append([])
        for j in range(len(b_copy[i])):
            if j - 1 > -1:
                if b_copy[i][j - 1] == 1:
                    act_neigh += 1
            if j + 1 < len(b_copy[i]):
                if b_copy[i][j + 1] == 1:
                    act_neigh += 1
            if i - 1 > -1:
                if b_copy[i - 1][j] == 1:
                    act_neigh += 1
            if i + 1 < len(b_copy):
                if b_copy[i + 1][j] == 1:
                    act_neigh += 1
            if i - 1 > -1 and j - 1 > -1:
                if b_copy[i - 1][j - 1] == 1:
                    act_neigh += 1
            if i - 1 > -1 and j + 1 < len(b_copy[i]):
                if b_copy[i - 1][j + 1] == 1:
                    act_neigh += 1
            if i + 1 < len(b_copy) and j - 1 > -1:
                if b_copy[i + 1][j - 1] == 1:
                    act_neigh += 1
            if i + 1 < len(b_copy) and j + 1 < len(b_copy[i]):
                if b_copy[i + 1][j + 1] == 1:
                    act_neigh += 1
            act_neigh_list[i].append(act_neigh)
            act_neigh = 0
    return act_neigh_list


def go_round(b, f_ann):
    act_neigh_list = f_ann(b)
    b_copy = b[:][:]
    for i in range(len(b_copy)):
        for j in range(len(b_copy[i])):
            if b_copy[i][j] == 1:
                if act_neigh_list[i][j] not in [2, 3]:
                    b_copy[i][j] = 0
            elif b_copy[i][j] == 0:
                if act_neigh_list[i][j] == 3:
                    b_copy[i][j] = 1
    return b_copy


def draw(b):
    s = '\n'
    for i in b:
        l = ['.' if e == 0 else 'X' for e in i]
        s += ' '.join(l) + '\n'
    s += '\n'
    return s
