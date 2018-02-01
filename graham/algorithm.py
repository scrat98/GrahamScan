import sys
from functools import reduce
from math import acos, sqrt


class GrahamAlgorithm:

    def __init__(self):
        print('GrahamAlgorithm init success')

    def get_convex_indices(self, points):
        TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

        def cmp(a, b):
            return (a > b) - (a < b)

        def turn(p, q, r):
            return cmp((q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]), 0)

        def sort_points(points):
            def slope(index):
                x = points[indices[0]]
                y = points[index]
                return (x[1] - y[1]) / \
                       (x[0] - y[0])

            indices = range(len(points))
            indices = sorted(indices, key=lambda index: points[index])
            indices = indices[:1] + sorted(indices[1:], key=slope)

            return indices

        def keep_left(hull, p):
            while len(hull) > 1 and turn(points[hull[-2]], points[hull[-1]], points[p]) != TURN_LEFT:
                hull.pop()

            hull.append(p)
            return hull

        indices = sort_points(points)
        return reduce(keep_left, indices, [])

    def get_convex_points(self, points):
        indices = self.get_convex_indices(points)
        hull = []

        for index in indices:
            hull.append([points[index][0], points[index][1]])

        return hull

    def get_convex_log(self, points):
        print('log')

    def free_point(a,b,c):
        return (b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])

    def grahamscan(point_array):
        N = len(point_array) #число точек в массиве
        P = range(N) #список номеров точек?

        for i in range(1, N):
            if point_array[P[i][0]]<point_array[P[0][0]]:
                P[i], P[0] = P[0], P[i]


        for i in range(2, N):
            j=i
            while j>1 and(free_point(point_array[P[0]], point_array[P[j-1]], point_array[P[j]])<0):
                P.sort(j)#сортировка???
                j-=1

        St = (P[0],P[1])#стек
        for i in range(2, N):
            while free_point(point_array[St[-2]],point_array[St[-1], point_array[P[i]]])<0:
                del St[-1]
            St.append(P[i])

        return St
