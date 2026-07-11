from collections import deque

from src.algorithms.base_maxflow import BaseMaxFlow


class EdmondsKarp(BaseMaxFlow):
    def find_augmenting_path(self):
        visited = {self.source}
        queue = deque([(self.source, [self.source])])

        while queue:
            node, path = queue.popleft()  # BFS: first-in, first-out
            self.all_visited.add(node)

            if node == self.sink:
                return path

            for neighbor in self.residual.neighbors(node):
                if neighbor not in visited and self.residual[node][neighbor]['capacity'] > 0:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None