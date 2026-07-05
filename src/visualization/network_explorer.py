import networkx as nx
import plotly.graph_objects as go
import streamlit as st


@st.cache_data(show_spinner=False)
def compute_layout(_graph, seed=42):
    """
    Cached so layout is computed once per graph, not on every rerun.
    kamada_kawai is deterministic and fast for a few hundred nodes.
    """
    return nx.kamada_kawai_layout(_graph)


def render_network_explorer(graph, height=700):
    pos = compute_layout(graph)
    zone_nodes = graph.graph.get('zone_nodes', set())

    edge_x, edge_y = [], []
    for u, v in graph.edges():
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color="#888"),
        hoverinfo="none",
        mode="lines"
    )

    node_x, node_y, node_color, node_size, node_text = [], [], [], [], []
    for node in graph.nodes():
        x, y = pos[node]
        is_zone = node in zone_nodes
        node_x.append(x)
        node_y.append(y)
        node_color.append("#e74c3c" if is_zone else "#3498db")
        node_size.append(10 if is_zone else 5)
        node_text.append(f"Node {node} ({'Zone' if is_zone else 'Intersection'})")

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode="markers",
        marker=dict(size=node_size, color=node_color, line=dict(width=0.5, color="white")),
        text=node_text,
        hoverinfo="text"
    )

    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        height=height,
        margin=dict(l=0, r=0, t=0, b=0),
        plot_bgcolor="white",
    )
    st.plotly_chart(fig, use_container_width=True)


def render_relevant_subgraph(graph, source, sink, visited_nodes, highlight_path=None, height=550):
    subgraph_nodes = set(visited_nodes) | {source, sink}
    subgraph = graph.subgraph(subgraph_nodes)
    pos = nx.kamada_kawai_layout(subgraph)  # small subgraph, cheap enough uncached

    path_edges = set(zip(highlight_path, highlight_path[1:])) if highlight_path else set()

    edge_x, edge_y = [], []
    path_x, path_y = [], []
    for u, v in subgraph.edges():
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        if (u, v) in path_edges:
            path_x += [x0, x1, None]
            path_y += [y0, y1, None]
        else:
            edge_x += [x0, x1, None]
            edge_y += [y0, y1, None]

    edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=0.5, color="#ccc"),
                             hoverinfo="none", mode="lines")
    path_trace = go.Scatter(x=path_x, y=path_y, line=dict(width=3, color="#f39c12"),
                             hoverinfo="none", mode="lines")

    node_x, node_y, node_color, node_size, node_text = [], [], [], [], []
    for node in subgraph.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        if node == source:
            node_color.append("#2ecc71"); node_size.append(14)
        elif node == sink:
            node_color.append("#e74c3c"); node_size.append(14)
        else:
            node_color.append("#3498db"); node_size.append(7)
        node_text.append(str(node))

    node_trace = go.Scatter(
        x=node_x, y=node_y, mode="markers+text",
        text=node_text, textposition="top center",
        marker=dict(size=node_size, color=node_color, line=dict(width=0.5, color="white")),
        hoverinfo="text"
    )

    fig = go.Figure(data=[edge_trace, path_trace, node_trace])
    fig.update_layout(
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        height=height,
        margin=dict(l=0, r=0, t=0, b=0),
        plot_bgcolor="white",
    )
    st.plotly_chart(fig, use_container_width=True)