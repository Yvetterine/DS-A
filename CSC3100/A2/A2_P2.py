def largest_rectangle_area(deep):
    stack = []
    max_area = 0
    index = 0

    while index < len(deep):
        if len(stack) == 0 or deep[index] >= deep[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            if len(stack) == 0:
                area = (deep[top_of_stack] * index)
                max_area = max(max_area, area)
                continue
            area = (deep[top_of_stack] * (index - stack[-1] - 1))
            max_area = max(max_area, area)

    while len(stack) != 0:
        top_of_stack = stack.pop()
        if len(stack) == 0:
            area = (deep[top_of_stack] * index)
            max_area = max(max_area, area)
            break
        area = (deep[top_of_stack] * (index - stack[-1] - 1))
        max_area = max(max_area, area)

    return max_area


def main():
    deep_total = []
    result = []
    time = int(input())
    for i in range(time):
        deep_int = []
        width = int(input())
        deep_str = input().split()
        for each_deep in deep_str:
            deep_int.append(int(each_deep))
        deep_total.append(deep_int)

        result.append(largest_rectangle_area(deep_int))
    for result in result:
        print(result)


main()