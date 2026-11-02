class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        dist = [float('inf')] * n
        dist[0] = 0
        distance = 0

        for _ in range(n):
            # pick: cheapest unvisited point (no inner loop, dist already knows)
            best = -1
            for i in range(n):
                if not visited[i] and (best == -1 or dist[i] < dist[best]):
                    best = i

            visited[best] = True
            distance += dist[best]

            # update: everyone left only checks against the new point
            bx, by = points[best]
            for i in range(n):
                if not visited[i]:
                    d = abs(points[i][0] - bx) + abs(points[i][1] - by)
                    dist[i] = min(dist[i], d)

        return distance