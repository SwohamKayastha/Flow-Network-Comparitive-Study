import plotly.graph_objects as go


def bottleneck_per_iteration(result):
    iters = result["iteration_log"]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(range(1, len(iters) + 1)),
        y=[it["bottleneck"] for it in iters],
        mode="lines+markers",
        name="Bottleneck capacity"
    ))
    fig.update_layout(
        title="Bottleneck Capacity per Augmenting Path (DFS)",
        xaxis_title="Iteration",
        yaxis_title="Bottleneck value"
    )
    return fig


def path_length_per_iteration(result):
    iters = result["iteration_log"]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=list(range(1, len(iters) + 1)),
        y=[it["length"] for it in iters],
    ))
    fig.update_layout(
        title="Path Length per Augmenting Path (DFS)",
        xaxis_title="Iteration",
        yaxis_title="Path length (edges)"
    )
    return fig


def cumulative_flow(result):
    iters = result["iteration_log"]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(range(1, len(iters) + 1)),
        y=[it["cumulative_flow"] for it in iters],
        mode="lines+markers",
        name="Cumulative flow"
    ))
    fig.update_layout(
        title="Cumulative Flow Growth (DFS)",
        xaxis_title="Iteration",
        yaxis_title="Total flow so far"
    )
    return fig