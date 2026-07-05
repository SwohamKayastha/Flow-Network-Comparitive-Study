# Flow Network Comparative Study (Mini Project)

This mini project is a simple and practical comparison of two maximum-flow algorithms:

- Ford-Fulkerson
- Edmonds-Karp

The goal is to study theory and performance on a real-world style network dataset.

## Project Purpose

- Do both algorithms give the same max-flow result?
- Which algorithm runs faster in practice?
- Why does Edmonds-Karp usually perform better on larger or complex networks?

## Real-World Problem We Focus On

Urban traffic flow in a road network.

Mapping to flow-network terms:

- Node = road intersection
- Directed edge = road segment
- Capacity = maximum vehicles per hour on that road
- Source = starting area
- Sink = destination area

This makes the project meaningful and easy to explain in class.

## Dataset To Use

Main dataset file:

- `Flow-Network-Comparitive-Study/dataset/Anaheim_net.tntp`

Dataset type:

- Transportation network (directed graph with capacities)

Dataset format:

- `.tntp` text format
- Common useful columns include:
  - `Init node` (from node)
  - `Term node` (to node)
  - `Capacity` (edge capacity)

For algorithm comparison, we mainly need these 3 fields to build the graph.

## How To Use The Dataset (Simple Steps)

1. Read the `.tntp` file as plain text.
2. Skip metadata/comment/header lines.
3. For each valid row, extract:
   - from node (`Init node`)
   - to node (`Term node`)
   - capacity (`Capacity`)
4. Build a directed graph.
5. Choose source and sink nodes.
6. Run both algorithms on the same graph.
7. Compare outputs and metrics.

## Most Important Metrics After Testing

Top metrics first:

1. Max flow value (correctness check)
2. Runtime (practical performance)
3. Iteration count / augmenting paths used

Other useful metrics:

4. Average bottleneck value per augmentation
5. Average path length chosen
6. Runtime per iteration
7. Min-cut edges (bottleneck roads)

## Expected Final Output

- Clean comparison table of both algorithms
- Graph/plot for runtime and iterations
- Clear conclusion on when each algorithm is suitable
- Mini research-style report draft + presentation support

## Folder Reference

- `Flow-Network-Comparitive-Study/index_with_source.html` (support material for visualization of dataset)
- `Flow-Network-Comparitive-Study/dataset/Anaheim_net.tntp` (main dataset)

```
maxflow-comparison/
├── dataset/
│ └── anaheim/
│ └── Anaheim_net.tntp
│
├── src/
│ ├── graph/
│ │ ├── tntp_parser.py
│ │ └── synthetic_generator.py
│ ├── algorithms/
│ │ ├── base_maxflow.py
│ │ ├── ford_fulkerson.py
│ │ └── edmonds_karp.py
│ ├── metrics/
│ │ └── collector.py
│ ├── experiments/
│ │ └── runner.py
│ └── visualization/
│ └── plots.py
│
├── app.py # ← just one file, at root, nothing fancy
├── results/
├── tests/
├── requirements.txt
└── README.md
```
