import sys
sys.setrecursionlimit(2000000)


class TreeNode:
    def __init__(self, value, color, upper_edge=None):
        self.key = value
        self.children = []
        self.color = color
        self.upper_edge = upper_edge


def inorder_traversal_to_sum_length(node, total_black):
    global length
    if node.color == 1:
        black_under = 1
    else:
        black_under = 0
    if len(node.children) != 0:
        for child in node.children:
            black_under += inorder_traversal_to_sum_length(child, total_black)
    if node.upper_edge is not None:
        length += (total_black - black_under) * black_under * node.upper_edge
    return black_under


length = 0
node_num = int(input())
tree_list = [None] * (node_num + 3)
color_list = list(map(int, input().split()))
total_black = sum(color_list)
node = TreeNode(1, color_list[0])
tree_list[1] = node  
for i in range(node_num - 1):

    each_node_pro = list(map(int, input().split()))
    node = TreeNode(i + 2, color_list[i+1], each_node_pro[1])
    tree_list[i+2] = node
    tree_list[each_node_pro[0]].children.append(node)

inorder_traversal_to_sum_length(tree_list[1], total_black)

print(length)