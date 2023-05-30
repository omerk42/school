class State:
    def __init__(self, m_left, c_left, b_pos, m_right, c_right):
        self.m_left = m_left  # number of missionaries on the left bank
        self.c_left = c_left  # number of cannibals on the left bank
        self.b_pos = b_pos    # position of the boat (0 for left bank, 1 for right bank)
        self.m_right = m_right  # number of missionaries on the right bank
        self.c_right = c_right  # number of cannibals on the right bank

    def is_goal(self):
        return self.m_left == 0 and self.c_left == 0
    
    def is_valid(self):
        if self.m_left < 0 or self.c_left < 0 or self.m_right < 0 or self.c_right < 0:
            return False
        if self.m_left > 3 or self.c_left > 3 or self.m_right > 3 or self.c_right > 3:
            return False
        if self.c_left > self.m_left and self.m_left != 0:
            return False
        if self.c_right > self.m_right and self.m_right != 0:
            return False
        return True

    def __eq__(self, other):
        return self.m_left == other.m_left and self.c_left == other.c_left \
               and self.b_pos == other.b_pos and self.m_right == other.m_right \
               and self.c_right == other.c_right

    def __hash__(self):
        return hash((self.m_left, self.c_left, self.b_pos, self.m_right, self.c_right))

def successors(state):
    children = []
    if state.b_pos == 0:  # boat is on the left bank
        for m in range(2):
            for c in range(2):
                new_m_left = state.m_left - m
                new_c_left = state.c_left - c
                new_m_right = state.m_right + m
                new_c_right = state.c_right + c
                new_state = State(new_m_left, new_c_left, 1, new_m_right, new_c_right)
                if new_state.is_valid():
                    children.append(new_state)
    else:  # boat is on the right bank
        for m in range(2):
            for c in range(2):
                new_m_left = state.m_left + m
                new_c_left = state.c_left + c
                new_m_right = state.m_right - m
                new_c_right = state.c_right - c
                new_state = State(new_m_left, new_c_left, 0, new_m_right, new_c_right)
                if new_state.is_valid():
                    children.append(new_state)
    return children

# starting state: 3 missionaries and 3 cannibals on the left bank, boat on the left bank
start_state = State(3, 3, 0, 0, 0)

# example usage: print the successors of the starting state
for child in successors(start_state):
    print(child.m_left, child.c_left, child.b_pos, child.m_right, child.c_right)
