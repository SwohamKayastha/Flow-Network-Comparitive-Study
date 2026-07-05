from src.algorithms.base_maxflow import BaseMaxFlow


class FordFulkerson(BaseMaxFlow):
    def find_augmenting_path(self):
        visited = {self.source}
        stack = [(self.source, [self.source])]

        while stack:
            node, path = stack.pop()  # DFS: last-in, first-out
            self.all_visited.add(node)

            if node == self.sink:
                return path

            for neighbor in self.residual.neighbors(node):
                if neighbor not in visited and self.residual[node][neighbor]['capacity'] > 0:
                    visited.add(neighbor)
                    stack.append((neighbor, path + [neighbor]))

        return None