from state import State
from node import Node
from utils import draw_graph_el

from collections import deque
import graphviz

def main():
    dot = graphviz.Digraph(format='png', strict=True, node_attr={'rankdir': "TB"})

    initial_state = State(3,3,1)
    initial_node = Node(parent_node=None, state=initial_state, action=None)
    
    visited_node = [str(initial_node)]
    fifo = deque([initial_node])

    while True:
        node = fifo.popleft()
        if node.state.is_goal_state():
            dot.node(str(node), f"{[node.state.missionaries, node.state.cannibals, node.state.boats]}",  
                                style="filled", fillcolor="#39d43c")
            break
        if node.state.status == "valid":
            successors =  node.expand()
            fifo.extend(successors)
            for succ_node in successors:
                if not str(succ_node) in visited_node:
                    visited_node.append(str(succ_node))
                    draw_graph_el(dot, node, succ_node)

    dot.render(filename="output/output")

if __name__ == "__main__":
    main()