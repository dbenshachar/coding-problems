from tree import node
from queue import Queue

def print_depth_first_recursion(head : node):
    if head is None:
        return None
    
    if head.value is not None:
        print(head.value, end=" ")

    if head.left is not None:
        print_depth_first_recursion(head.left)
    
    if head.right is not None:
        print_depth_first_recursion(head.right)
    
    return None

#      1
#    2   3
#   4 5 ? 6

def _run_test_1(print_depth_first):
    print("Test 1 output: ", end="")
    tree = node(1,
                left=node(2,
                        left=node(3),
                        right=node(4)),
                right=node(5,
                        left=None,
                        right=node(6)),
            )
    print_depth_first(tree)
    print("")

def _run_test_2(print_depth_first):
    print("Test 2 output: ", end="")
    tree = node(value=None, left=None, right=None)
    print_depth_first(tree)
    print("")

def _run_test_3(print_depth_first):
    print("Test 3 output: ", end="")
    tree = node(1,
                left=node(2,
                        left=node(2, left=node(3), right=node(4)),
                        right=node(5)),
                right=node(6,
                        left=None,
                        right=None),
            )
    print_depth_first(tree)
    print("")

def _run_test_4(print_depth_first):
    print("Test 4 output: ", end="")
    tree = node(1,
                left=node(2,
                        left=node(3, left=node(4, left=node(5, left=node(6)))),
                        right=None,
                )
            )
    print_depth_first(tree)
    print("")

def _run_test_5(print_depth_first):
    print("Test 5 output: ", end="")
    tree = node(1,
                right=node(2,
                        left=node(3, right=node(4, right=node(5, right=node(6)))),
                        right=None,
                )
            )
    print_depth_first(tree)
    print("")

def _run_test_6(print_depth_first):
    print("Test 6 output: ", end="")
    tree = node(value=None, left=node(1), right=None)
    print_depth_first(tree)
    print("")

def _run_test_7(print_depth_first):
    print("Test 7 output: ", end="")
    tree = node(value=None, left=None, right=node(1))
    print_depth_first(tree)
    print("")

def _run_test_8(print_depth_first):
    print("Test 8 output: ", end="")
    tree = node(1,
                right=node(2,
                        left=node(None, left=node(None, left=node(3))),
                        right=None,
                )
            )
    print_depth_first(tree)
    print("")

def _run_test_9(print_depth_first):
    print("Test 9 output: ", end="")
    tree = node(None,
                right=node(2,
                        left=node(None, left=node(None, left=node(3))),
                        right=None,
                ),
                left=node(None, right=node(1))
            )
    print_depth_first(tree)
    print("")

def _run_test_10(print_depth_first):
    print("Test 10 output: ", end="")
    tree = None
    print_depth_first(tree)
    print("")

if __name__ == "__main__":
    fn = print_depth_first_recursion
    _run_test_1(fn)
    _run_test_2(fn)
    _run_test_3(fn)
    _run_test_4(fn)
    _run_test_5(fn)
    _run_test_6(fn)
    _run_test_7(fn)
    _run_test_8(fn)
    _run_test_9(fn)
    _run_test_10(fn)