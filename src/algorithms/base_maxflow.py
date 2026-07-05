import time


class BaseMaxFlow:
    def __init__(self, graph, source, sink):
        self.graph = graph
        self.source = source
        self.sink = sink
        self.residual = self._build_residual(graph)
        self.max_flow = 0
        self.iterations = []
        self.all_visited = set()
        self.runtime_ms = 0

    def _build_residual(self, graph):
        R = graph.copy()
        for u, v in list(graph.edges()):
            if not R.has_edge(v, u):
                R.add_edge(v, u, capacity=0)
        return R

    def find_augmenting_path(self):
        raise NotImplementedError

    def run(self):
        start = time.perf_counter()

        while True:
            path = self.find_augmenting_path()
            if path is None:
                break

            bottleneck = min(
                self.residual[u][v]['capacity'] for u, v in zip(path, path[1:])
            )

            for u, v in zip(path, path[1:]):
                self.residual[u][v]['capacity'] -= bottleneck
                self.residual[v][u]['capacity'] += bottleneck

            self.max_flow += bottleneck
            self.iterations.append({
                "path": path,
                "length": len(path) - 1,
                "bottleneck": bottleneck,
                "cumulative_flow": self.max_flow,
            })

        self.runtime_ms = (time.perf_counter() - start) * 1000

        return {
            "max_flow": self.max_flow,
            "iterations": len(self.iterations),
            "runtime_ms": self.runtime_ms,
            "iteration_log": self.iterations,
        }