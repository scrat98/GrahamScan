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
