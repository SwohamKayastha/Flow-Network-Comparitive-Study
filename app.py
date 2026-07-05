import streamlit as st
from src.graph.tntp_parser import parse_tntp
from src.algorithms.ford_fulkerson import FordFulkerson
from src.visualization.plots import (
    bottleneck_per_iteration,
    path_length_per_iteration,
    cumulative_flow,
)

from src.visualization.network_explorer import (
    render_network_explorer,
    render_relevant_subgraph,
)

st.set_page_config(page_title="Flow Network Visualizer", layout="wide")
st.title("Flow Network Visualizer")

# --- Dataset selection ---
DATASETS = {
    "Anaheim": "dataset/anaheim/Anaheim_net.tntp",
}

dataset_name = st.sidebar.selectbox("Dataset", list(DATASETS.keys()))
graph = parse_tntp(DATASETS[dataset_name])

# --- Sidebar stats ---
st.sidebar.subheader("Network Stats")
st.sidebar.write(f"Total Zones (Sources/Sinks): **{graph.graph['num_zones']}**")
st.sidebar.write(f"Total Nodes: **{graph.number_of_nodes()}**")
st.sidebar.write(f"Total Links (Edges): **{graph.number_of_edges()}**")

st.sidebar.subheader("Legend")
st.sidebar.markdown("🔴 Source / Sink (Zone)")
st.sidebar.markdown("🔵 Intersection (Thru Node)")
st.sidebar.caption("Edge thickness represents capacity")

# --- Tabs ---
tab1, tab2 = st.tabs(["Network Explorer", "Run Ford-Fulkerson (DFS)"])

with tab1:
    st.subheader("Full Network Overview")
    render_network_explorer(graph)

with tab2:
    st.subheader("Run Ford-Fulkerson")

    zone_nodes = sorted(graph.graph['zone_nodes'])

    col1, col2 = st.columns(2)
    with col1:
        source = st.selectbox("Source (zone)", zone_nodes, index=0)
    with col2:
        sink = st.selectbox("Sink (zone)", zone_nodes, index=len(zone_nodes) - 1)

    if st.button("Run Ford-Fulkerson"):
        if source == sink:
            st.error("Source and sink must be different nodes.")
        else:
            with st.spinner("Running DFS-based Ford-Fulkerson..."):
                ff = FordFulkerson(graph, source, sink)
                result = ff.run()

            m1, m2, m3 = st.columns(3)
            m1.metric("Max Flow", f"{result['max_flow']:.0f}")
            m2.metric("Iterations", result["iterations"])
            m3.metric("Runtime (ms)", f"{result['runtime_ms']:.2f}")

            if result["iterations"] == 0:
                st.warning("No path found between source and sink.")
            else:
                last_path = result["iteration_log"][-1]["path"]

                st.subheader("Explored Subgraph")
                render_relevant_subgraph(graph, source, sink, ff.all_visited, highlight_path=last_path)

                st.subheader("Iteration Metrics")
                st.plotly_chart(bottleneck_per_iteration(result), use_container_width=True)
                st.plotly_chart(path_length_per_iteration(result), use_container_width=True)
                st.plotly_chart(cumulative_flow(result), use_container_width=True)

                with st.expander("Raw iteration log"):
                    st.dataframe(result["iteration_log"])