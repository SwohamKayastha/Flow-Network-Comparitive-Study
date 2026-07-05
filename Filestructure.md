## Dev purpose

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
├── app.py # <- root file
├── results/
├── tests/
├── requirements.txt
└── README.md
```
