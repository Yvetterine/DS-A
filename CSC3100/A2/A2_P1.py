class Node:
    def __init__(self, value=None, next_one=None):
        self.value = value
        self.next_one = next_one


class Stack:
    def __init__(self):
        self.head = Node()

    def push(self, value):
        add = Node(value=value)
        add.next_one = self.head.next_one
        self.head.next_one = add

    def pop(self):
        if self.empty_or_not():
            return None
        tmp = self.head.next_one
        self.head.next_one = tmp.next_one
        return tmp.value

    def top(self):
        if self.empty_or_not():
            return None
        return self.head.next_one.value

    def empty_or_not(self):
        return self.head.next_one is None


def main():
    sorted_total_list = []
    length = int(input())
    for i in range(length):
        prim_str_list = input().split()
        each_node_list = [int(prim_str_list[0]), int(prim_str_list[1]), prim_str_list[2], i]

        sorted_total_list.append(each_node_list)
    sorted_total_list.sort()
    stack = Stack()

    for i in range(length):
        check = True
        while stack.empty_or_not() is False:
            if stack.top()[2] == "D" or sorted_total_list[i][2] == "U":
                stack.push(sorted_total_list[i])
                break
            tmp_head = stack.top()
            tmp_out_stack = sorted_total_list[i]
            if tmp_head[1] == tmp_out_stack[1]:
                stack.pop()
                check = False
                break
            elif tmp_head[1] > tmp_out_stack[1]:
                tmp_head[1] -= 1
                break
            elif tmp_head[1] < tmp_out_stack[1]:
                tmp_out_stack[1] -= 1
                stack.pop()
                continue
        if stack.empty_or_not() and check:
            stack.push(sorted_total_list[i])

    print_list = []
    curr = stack.head.next_one
    while curr is not None:
        print_list.append(curr.value)
        curr = curr.next_one

    print_list.sort(key=lambda x: x[3])
    for i in print_list:
        print(i[1])


main()