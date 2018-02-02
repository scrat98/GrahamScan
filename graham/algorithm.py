import sys
from functools import reduce
from math import atan2


class GrahamAlgorithm:

    def __init__(self):
        print('GrahamAlgorithm init success')

    def get_points_from_data(self, data):
        return data

    def get_convex_indices(self, data):
        TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)
        points = self.get_points_from_data(data)

        def cmp(a, b):
            return (a > b) - (a < b)

        def turn(p, q, r):
            return cmp((q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]), 0)

        def sort_points(points):
            def slope(index):
                x = points[indices[0]]
                y = points[index]
                return atan2(x[0] - y[0], y[1] - x[1])

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

    def get_convex_points(self, data):
        points = self.get_points_from_data(data)
        indices = self.get_convex_indices(points)
        hull = []

        for index in indices:
            hull.append([points[index][0], points[index][1]])

        return hull

    def get_convex_log(self, data):
        TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)
        points = self.get_points_from_data(data)

        # print points
        print('[POINTS ARRAY]')
        for point in points:
            print(' '.join(map(str, point)))

        def cmp(a, b):
            return (a > b) - (a < b)

        def turn(p, q, r):
            return cmp((q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]), 0)

        def sort_points(points):
            def slope(index):
                x = points[indices[0]]
                y = points[index]
                return atan2(x[0] - y[0], y[1] - x[1])

            indices = range(len(points))
            indices = sorted(indices, key=lambda index: points[index])
            indices = indices[:1] + sorted(indices[1:], key=slope)

            return indices

        def keep_left(hull, p):

            while 1:
                if len(hull) > 1:
                    print('check', hull[-2], hull[-1], p)

                if len(hull) > 1 and turn(points[hull[-2]], points[hull[-1]], points[p]) != TURN_LEFT:
                    print('delete', hull[-1])
                    hull.pop()
                else:
                    break

            print('put', p)
            hull.append(p)

            return hull

        indices = sort_points(points)
        # sort points
        print('[SORT POINTS]')
        print(' '.join(map(str, indices)))

        # steps
        print('[STEPS]')
        reduce(keep_left, indices, [])
