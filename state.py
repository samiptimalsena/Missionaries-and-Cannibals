class State:
    def __init__(self, missionaries, cannibals, boats):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boats = boats
        self.status = "valid"

    def successors(self):
        if self.boats == 1:
            sign = -1
        else:
            sign = 1
        for m in range(3):
            for c in range(3):
                new_state = State(self.missionaries+sign*m, self.cannibals+sign*c, self.boats+sign)
                if m+c >= 1 and m+c <=2 and new_state.isValid():
                    if not new_state.isKilled():
                        new_state.status = "killed"
                    action = [m, c, -1 * sign]
                    yield action, new_state

    def isValid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3 or (self.boats != 0 and self.boats != 1):
            return False   
        return True  

    def isKilled(self):
        if self.cannibals > self.missionaries and self.missionaries > 0:
            return False
        if self.cannibals < self.missionaries and self.missionaries < 3: 
            return False
        return True
    
    def is_goal_state(self):
        return self.cannibals == 0 and self.missionaries == 0 and self.boats == 0

    def __repr__(self):
        return "< State (%d, %d, %d) >" % (self.missionaries, self.cannibals, self.boats)