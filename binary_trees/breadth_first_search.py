from tree import node
from queue import Queue

def print_breadth_first(head : node):
    if head is None:
        return
    q = Queue()
    q.put(head)
    while not q.empty():
        head = q.get()
        if head.value is not None:
            print(head.value, end=" ")

        if head.left is not None:
            q.put(head.left)
        if head.right is not None:
            q.put(head.right)

            

#      1
#    2   3
#   4 5 ? 6

def _run_test_1():
    print("Test 1 output: ", end="")
    tree = node(1,
                left=node(2,
                        left=node(4),
                        right=node(5)),
                right=node(3,
                        left=None,
                        right=node(6)),
            )
    print_breadth_first(tree)
    print("")

def _run_test_2():
    print("Test 2 output: ", end="")
    tree = node(value=None, left=None, right=None)
    print_breadth_first(tree)
    print("")

def _run_test_3():
    print("Test 3 output: ", end="")
    tree = node(1,
                left=node(2,
                        left=node(4, left=node(6), right=node(7)),
                        right=node(5)),
                right=node(3,
                        left=None,
                        right=None),
            )
    print_breadth_first(tree)
    print("")

def _run_test_4():
    print("Test 4 output: ", end="")
    tree = node(1,
                left=node(2,
                        left=node(3, left=node(4, left=node(5, left=node(6)))),
                        right=None,
                )
            )
    print_breadth_first(tree)
    print("")

def _run_test_5():
    print("Test 5 output: ", end="")
    tree = node(1,
                right=node(2,
                        left=node(3, right=node(4, right=node(5, right=node(6)))),
                        right=None,
                )
            )
    print_breadth_first(tree)
    print("")

def _run_test_6():
    print("Test 6 output: ", end="")
    tree = node(value=None, left=node(1), right=None)
    print_breadth_first(tree)
    print("")

def _run_test_7():
    print("Test 7 output: ", end="")
    tree = node(value=None, left=None, right=node(1))
    print_breadth_first(tree)
    print("")

def _run_test_8():
    print("Test 8 output: ", end="")
    tree = node(1,
                right=node(2,
                        left=node(None, left=node(None, left=node(3))),
                        right=None,
                )
            )
    print_breadth_first(tree)
    print("")

def _run_test_9():
    print("Test 9 output: ", end="")
    tree = node(None,
                left=node(None, right=node(2)),
                right=node(1,
                        left=node(None, left=node(None, left=node(3))),
                        right=None,
                ),
            )
    print_breadth_first(tree)
    print("")

def _run_test_10():
    print("Test 10 output: ", end="")
    tree = None
    print_breadth_first(tree)
    print("")

if __name__ == "__main__":
    _run_test_1()
    _run_test_2()
    _run_test_3()
    _run_test_4()
    _run_test_5()
    _run_test_6()
    _run_test_7()
    _run_test_8()
    _run_test_9()
    _run_test_10()