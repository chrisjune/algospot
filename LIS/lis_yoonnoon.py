import unittest

import bisect


class LISv3:

    def __init__(self, n, data):
        self.n = n
        self.data = data
        self.q = []

    def solution(self):
        for n in self.data:
            if not self.q or n > self.q[-1]:
                self.q.append(n)
            else:
                index = bisect.bisect_left(self.q, n)
                self.q[index] = n
        return len(self.q)


class LISv2:
    def __init__(self, n, data):
        self.n = n
        self.data = data

    def solution(self):
        if self.n == 0:
            return 0
        elif self.n == 1:
            return 1

        dp = [1 for i in range(self.n)]
        for i in range(1, self.n):
            for j in range(i):
                if self.data[i] > self.data[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        res = max(dp)
        return res


class LISv1:
    def __init__(self, n, data):
        self.n = n
        self.data = data
        self.memo = {}

    def solution(self):
        _max = 0
        for i in range(self.n):
            _max = max(self.search_or_cache(i), _max)
        return _max

    def search_or_cache(self, i):
        return self.memo[i] if i in self.memo else self.search(i)

    def search(self, base):
        _max = 0
        for i in range(base + 1, self.n):
            if self.data[i] > self.data[base]:
                _max = max(self.search_or_cache(i), _max)

        self.memo[base] = _max + 1
        return self.memo[base]


def main():
    tc = input()

    for i in range(int(tc)):
        n = int(input())
        data = [int(v) for v in input().split(' ')]
        print(LISv1(n, data).solution())
        print(LISv2(n, data).solution())
        print(LISv3(n, data).solution())


if __name__ == '__main__':
    main()


class Test(unittest.TestCase):

    def test_case1(self):
        n = 4
        data = [1, 2, 3, 4]
        self.assertEqual(LISv1(n, data).solution(), 4)
        self.assertEqual(LISv2(n, data).solution(), 4)
        self.assertEqual(LISv3(n, data).solution(), 4)

    def test_case2(self):
        n = 10
        data = [5, 4, 3, 2, 3, 4, 1, 6, 7, 8]
        self.assertEqual(LISv1(n, data).solution(), 6)
        self.assertEqual(LISv2(n, data).solution(), 6)
        self.assertEqual(LISv3(n, data).solution(), 6)

    def test_case3(self):
        n = 8
        data = [5, 6, 7, 8, 1, 2, 3, 4]
        self.assertEqual(LISv1(n, data).solution(), 4)
        self.assertEqual(LISv2(n, data).solution(), 4)
        self.assertEqual(LISv3(n, data).solution(), 4)

    def test_case4(self):
        n = 8
        data = [10, 9, 2, 5, 3, 7, 101, 18]
        self.assertEqual(LISv1(n, data).solution(), 4)
        self.assertEqual(LISv2(n, data).solution(), 4)
        self.assertEqual(LISv3(n, data).solution(), 4)

    def test_case5(self):
        n = 7
        data = [9, 1, 3, 7, 5, 6, 20]
        self.assertEqual(LISv1(n, data).solution(), 5)
        self.assertEqual(LISv2(n, data).solution(), 5)
        self.assertEqual(LISv3(n, data).solution(), 5)
