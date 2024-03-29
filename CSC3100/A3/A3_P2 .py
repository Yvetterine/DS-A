import sys
sys.setrecursionlimit(100010)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add_value(self, add_value):
        z = TreeNode(element=add_value)
        y = None
        x = self.root
        while x is not None:
            y = x
            if add_value < x.element:
                x = x.left_child
            else:
                x = x.right_child
        z.parent = y
        if y is None:
            self.root = z
        else:
            if add_value < y.element:
                y.left_child = z
            else:
                y.right_child = z
        return z

    def inorder(self, x):
        global ahead, closest
        if x is not None:
            self.inorder(x.left_child)
            if ahead is None:
                ahead = x.element
            else:
                tmp_diff = x.element - ahead
                if closest is None:
                    closest = tmp_diff
                else:
                    if closest > tmp_diff:
                        closest = tmp_diff
                ahead = x.element
            self.inorder(x.right_child)

    def successor(self, x):
        y = x.parent
        while y is not None:
            if x == y.right_child:
                x = y
                y = y.parent
            else:
                break
        if y is not None:
            return True, y.element
        else:
            return False, 0

    def predecessor(self, x):
        y = x.parent
        while y is not None:
            if x == y.left_child:
                x = y
                y = y.parent
            else:
                break
        if y is not None:
            return True, y.element
        else:
            return False, 0


class TreeNode:
    def __init__(self, element, left=None, right=None, parent=None):
        self.element = element
        self.left_child = left
        self.right_child = right
        self.parent = parent


def closest_adj_price():
    global first_time_check_adj, closest_adj, check_index
    if first_time_check_adj:
        for index in range(len(glo_list) - 1):
            tmp = abs(glo_list[index] - glo_list[index + 1])
            if closest_adj is None:
                closest_adj = tmp
            else:
                if closest_adj > tmp:
                    closest_adj = tmp
        first_time_check_adj = False
    else:
        for index in range(check_index, len(glo_list) - 1):
            tmp = abs(glo_list[index] - glo_list[index + 1])
            if closest_adj > tmp:
                closest_adj = tmp
    check_index = len(glo_list) - 1
    output_list.append(closest_adj)


def closest_price():
    global first_time_check
    if first_time_check:
        bst.inorder(bst.root)
        first_time_check = False
    output_list.append(closest)


def buy(x):
    global closest
    glo_list.append(x)
    z = bst.add_value(x)
    check_1, value_1 = bst.successor(z)
    check_2, value_2 = bst.predecessor(z)
    if closest is not None:
        if check_1:
            diff_1 = value_1 - x
            closest = min(closest, diff_1)
        if check_2:
            diff_2 = x - value_2
            closest = min(closest, diff_2)



first_time_check_adj = True
first_time_check = True
closest_adj = None
check_index = -1
closest = None
glo_list = []
bst = BinarySearchTree()
ahead = None
output_list = []

len_ori_and_num_opera = input().split()
ori = int(len_ori_and_num_opera[0])
num_opera = int(len_ori_and_num_opera[1])
ori_str_list = input().split()
for i in ori_str_list:
    i = int(i)
    glo_list.append(int(i))
    bst.add_value(i)
for num in range(num_opera):
    opera = input()
    if opera == "CLOSEST_ADJ_PRICE":
        closest_adj_price()
    elif opera == "CLOSEST_PRICE":
        closest_price()
    else:
        value = int(opera.split()[-1])
        buy(value)

for i in output_list:
    print(i)