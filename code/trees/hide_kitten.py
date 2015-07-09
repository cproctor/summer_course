
from branch import Branch
from random import choice

def find_clear_branch(root):
    "Returns a branch with two or less branches."
    if len(root.branches) < 3:
        return root
    
    branch_to_explore = choice(root.branches) 
    return find_clear_branch(branch_to_explore)

def build_tree():
    root = Branch()
    branches = [root]
    for _ in range(500):
        new_branch = Branch()
        branches.append(new_branch)
        clear_branch = find_clear_branch(root)
        clear_branch.attach(new_branch)

    secret_branch = choice(branches)
    secret_branch.has_kitten = True
    root.show()
    return root
    
def find_kitten(root):
    "This should return the branch that has the kitten." 
    pass




