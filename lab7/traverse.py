def is_empty(tree):
    """returns true if tree exisists"""
    return not tree


def is_leaf(tree):
    """returns true if tree is an int"""
    return isinstance(tree,int)


def is_branch(tree):
    """returns true if tree is a list"""
    return isinstance(tree,list)


def left_subtree(tree, leaf_fn): 
    """looks thuough the left side of the tree"""

    if isinstance(tree,list) and tree:
            return tree[0]
    return None


def right_subtree(tree, leaf_fn):
    """looks thuough the right side of the tree"""

    if isinstance(tree,list) and tree:
            return tree[2]
    return None


def middle_subtree(tree, leaf_fn):
    """looks at the middle value of a list"""
        
    return tree[1]


def traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn): # skicka in tre funktioner??
    """travels through the tree and returns the value specified by the functions given"""

    if is_empty(tree):
        return empty_tree_fn()

    elif is_leaf(tree):
        return leaf_fn(tree)

    elif is_branch(tree):

        left_tree = left_subtree(tree, leaf_fn)
        middle_node = middle_subtree(tree, leaf_fn)
        right_tree = right_subtree(tree, leaf_fn)

        left_result = traverse(left_tree, inner_node_fn, leaf_fn, empty_tree_fn)
        middle_result = traverse(middle_node, inner_node_fn, leaf_fn, empty_tree_fn)
        right_result = traverse(right_tree, inner_node_fn, leaf_fn, empty_tree_fn)

        return inner_node_fn(middle_result, left_result, right_result)    
      

def contain_key(key,tree):
    """returns true if key is a node in the tree"""

    def empty_tree_fn():
        return False

    def leaf_fn(node):
        return node == key
    
    def inner_node_fn(node, left_tree, right_tree):
        return left_tree or node or right_tree

    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)


def tree_size(tree):
    """returns the amount of nodes in the tree"""

    def empty_tree_fn():
        return 0

    def leaf_fn(node):
        return 1
    
    def inner_node_fn(node, left_tree, right_tree):
        return left_tree + node + right_tree

    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn) 


def tree_depth(tree):
    """returns the depth of the tree"""
    
    def empty_tree_fn():
        return 0
    
    def leaf_fn(node):
        return 1

    def inner_node_fn(node, left_tree, right_tree):
        if tree != []:
            temp1 = left_tree
            temp2 = right_tree

            if temp1 != 0 or temp2 != 0:
                temp1 += 1
                temp2 += 1

            elif temp1 == 0 or temp2 == 0:
                if node != 0:
                    temp1 += 1
                    temp2 += 1

            return temp1 if temp1>temp2 else temp2

    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn) 


def test_func():
    """specific function to run all tests"""
    # print(left_subtree([[1,3,4],5,7]))
    # print(contain_key(2,[[1,3,4],5,7]))
    # print(tree_size([[1,3,4],5,[[],8,[10,[],[]]]]))
    # print(tree_depth([[1,3,[4,6,[[[],3,[1,7,[]]],1,[]]]],5,7]))

    assert contain_key(6, [6, 7, 8]) == True
    assert contain_key(2, [6, 7, [[2, 3, 4], 0, []]]) == True
    assert contain_key(2, [[], 1, 5]) == False
    assert contain_key([], [[], 1, 5]) == False

    assert tree_size([2, 7, []]) == 2
    assert tree_size([[1, 2, []], 4, [[], 5, 6]]) == 5
    assert tree_size([]) == 0

    assert tree_depth(9) == 1
    assert tree_depth([1, 5, [10, 7, 14]]) == 3
    assert tree_depth([[1,3,[4,6,[[[],3,[1,7,[]]],1,[]]]],5,7]) == 7
    assert tree_depth([]) == 0


if __name__ == '__main__':
    test_func()