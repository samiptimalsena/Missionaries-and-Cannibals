class Node:
    def __init__(self, parent_node, state, action):
        self.parent_node = parent_node
        self.state = state
        self.action = action

    def expand(self):
        succ_nodes = list()
        for (action, succ_state) in self.state.successors():
            succ_node = Node(parent_node=self, state=succ_state, action=action)
            succ_nodes.append(succ_node)
        return succ_nodes

    def __repr__(self):
        return "< State (%d, %d, %d) >" % (self.state.missionaries, self.state.cannibals, self.state.boats)