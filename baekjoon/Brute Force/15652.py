n, m = map(int, input().split())
check = [False] * (n + 1)
a = [0] * m


def go(index, n, m):

    if index == m:
        print(" ".join(map(str, a)))
        return
    for i in range(1, n + 1):
        if i < a[index - 1]:
            continue

        a[index] = i

        go(index + 1, n, m)
        a[index] = 0


go(0, n, m)
