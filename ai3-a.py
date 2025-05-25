class BlocksWorld:
    def __init__(self):
        self.state = {
            "A": "B",
            "B": "table",
            "C": "table"
        }
        self.goal = {
            "A": "table",
            "B": "C",
            "C": "table"
        }

    def is_goal_state(self, state):
        return state == self.goal

    def move(self, block, destination):
        print(f"Moving {block} from {self.state[block]} to {destination}")
        self.state[block] = destination

    def plan_moves(self):
        potential_state = self.state.copy()
        while not self.is_goal_state(potential_state):
            for block, target in self.goal.items():
                if potential_state[block] != target:
                    self.move(block, target)
                    potential_state[block] = target
        print("Final Goal State Reached:", self.state)

# Run the Blocks World Solver
bw = BlocksWorld()
bw.plan_moves()
