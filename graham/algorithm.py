import sys


class GrahamAlgorithm:

    def __init__(self):
        print('GrahamAlgorithm init success')

    def get_convex_indices(self, points):
        return list(range(0, len(points), 2))

    def get_convex_points(self, points):
        indices = self.get_convex_indices(points)
        ans = []

        for index in indices:
            ans.append([points[index][0], points[index][1]])

        return ans

    def get_convex_log(self, points):
        print('log')
