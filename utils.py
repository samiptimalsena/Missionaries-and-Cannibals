# function for creating element(node---->node) of the digraph

def draw_graph_el(dot, parent_node, succ_node):
    p_color = s_color = "#4dbcf7"

    if parent_node.parent_node is None:
        p_color = "#f7ef4d"
    if succ_node.state.status == "killed":
        s_color = "red"

    # creating parent and successor node in graph
    dot.node(str(parent_node), f"{[parent_node.state.missionaries, parent_node.state.cannibals, parent_node.state.boats]}", style="filled", fillcolor=p_color)
    dot.node(str(succ_node), f"{[succ_node.state.missionaries, succ_node.state.cannibals, succ_node.state.boats]}", style="filled", fillcolor=s_color)

    # connecting the above formed nodes
    dot.edge(str(parent_node), str(succ_node), label=f"{succ_node.action}")