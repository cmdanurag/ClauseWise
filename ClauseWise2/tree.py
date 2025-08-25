from treelib import Tree
import os

def build_tree(path, max_depth=3, tree=None, parent=None, depth=0):
    if tree is None:
        tree = Tree()
        tree.create_node(os.path.basename(path), path)  # root
        parent = path
    if depth < max_depth:
        try:
            for item in os.listdir(path):
                itempath = os.path.join(path, item)
                tree.create_node(item, itempath, parent=parent)
                if os.path.isdir(itempath):
                    build_tree(itempath, max_depth, tree, itempath, depth+1)
        except PermissionError:
            pass
    return tree

t = build_tree(".", max_depth=3)
t.show()
