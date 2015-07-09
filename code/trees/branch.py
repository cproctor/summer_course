
class Branch:
    
    def __init__(self, depth=0):
        self.branches = []
        self.depth = depth
        self.has_kitten = False

    def attach(self, other_branch):
        other_branch.depth = self.depth + 1
        self.branches.append(other_branch)

    def show(self):
        if not self.has_kitten:
            print((" " * self.depth * 4) + "- not here...")
        else:
            print((" " * self.depth * 4) + "- MEOW")
        for branch in self.branches:
            branch.show()
