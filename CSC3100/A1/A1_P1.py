length = input()
prim_str_list = input().split()
unsort_list = []
count = 0

for i in prim_str_list:
    num = int(i)
    unsort_list.append(num)


def merge(list):
    global count
    if len(list) == 1:
        return list
    if len(list) % 2 == 0:
        mid = int(len(list) / 2)
    else:
        mid = len(list) // 2
    left_list = list[: mid]
    right_list = list[mid:]
    merge(left_list)
    merge(right_list)

    i = 0
    j = 0
    k = -1
    while i < len(left_list) and j < len(right_list):
        k += 1
        if left_list[i] <= right_list[j]:
            list[k] = left_list[i]
            i += 1
        else:
            list[k] = right_list[j]
            j += 1
            count += (len(left_list) - i)
    while i < len(left_list):
        k += 1
        list[k] = left_list[i]
        i += 1
    while j < len(right_list):
        k += 1
        list[k] = right_list[j]
        j += 1


merge(unsort_list)
print(count)
