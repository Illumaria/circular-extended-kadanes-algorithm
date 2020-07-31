#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import sys


def get_N_K():
    """Read the number of elements and the black sector index"""
    in_lst = sys.stdin.readline().rstrip().split()

    if (len(in_lst) != 2) or (int(in_lst[0]) < 1) or (int(in_lst[1]) < -1):
        return (-1, -2)

    N = int(in_lst[0])
    K = int(in_lst[1])
    return (N, K)


def get_sectors(n: int):
    """Read the sectors"""
    sectors = sys.stdin.readline().rstrip().split()
    if len(sectors) != n:
        return None
    return list(map(int, sectors))


def kadane(s: list):
    """Simple Kadane's algorithm (with respect to all-zeros case)"""
    max_points = -sys.maxsize - 1
    current_sum = 0

    for elem in s:
        current_sum = max(elem, current_sum + elem)
        max_points = max(max_points, current_sum)

    return max_points


def get_max_points(k: int, s: list):
    """Function for maximum points calculation"""
    if k == -1:
        max_kadane = kadane(s)

        max_inv_kadane = sum(s)
        s = [-elem for elem in s]
        max_inv_kadane += kadane(s)

        if max_inv_kadane:
            return max(max_inv_kadane, max_kadane)
        else:
            return max_kadane
    else:
        return max(kadane(s[k+1:]+s[:k]), 0)


if __name__ == "__main__":
    x = int(sys.stdin.readline().rstrip())
    if x < 1:
        sys.exit()

    N_lst = []
    K_lst = []
    S_lst = []
    for i in range(x):
        N, K = get_N_K()
        sectors = get_sectors(N)
        N_lst.append(N)
        K_lst.append(K)
        S_lst.append(sectors)

    for k in range(x):
        results = []
        if (N_lst[k] == -1) or (K_lst[k] == -2) or (not S_lst[k]):
            print(0)
            continue
        print(get_max_points(K_lst[k], S_lst[k]))
