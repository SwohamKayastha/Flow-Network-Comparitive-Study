import networkx as nx


def parse_tntp(filepath):
    G = nx.DiGraph()
    metadata = {}
    started = False

    with open(filepath) as f:
        for line in f:
            line = line.strip()

            if line.startswith('<'):
                key = line[1:line.index('>')]
                value = line[line.index('>') + 1:].strip().rstrip(';').strip()
                metadata[key] = value
                continue

            if line.startswith('~'):
                started = True
                continue

            if not started or not line:
                continue

            parts = line.rstrip(';').split()
            u, v = int(parts[0]), int(parts[1])
            capacity = float(parts[2])
            length = float(parts[3])
            free_flow_time = float(parts[4])

            G.add_edge(u, v, capacity=capacity, length=length, free_flow_time=free_flow_time)

    num_zones = int(metadata.get('NUMBER OF ZONES', 0))
    G.graph['metadata'] = metadata
    G.graph['num_zones'] = num_zones
    G.graph['zone_nodes'] = set(range(1, num_zones + 1))

    return G