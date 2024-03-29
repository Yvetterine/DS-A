import heapq


def dij(graph_str, line_num, column_num):

    start = graph_str.index("i")
    j_key = None
    j_check = True

    dis_dict = [float("inf") for i in range(len(graph_str))]
    dis_dict[start] = 0

    heap = []
    heapq.heappush(heap, [0, start])

    while len(heap) != 0:
        vert_dis = heapq.heappop(heap)
        curr_vert = vert_dis[1]    # 这个节点的real_位置：0,1,2,……n-1
        curr_dis = vert_dis[0]

        if curr_dis > dis_dict[curr_vert]:
            continue

        tmp_line = curr_vert // column_num
        tmp_col = curr_vert % column_num
        letter = graph_str[curr_vert]
        # nbr_dic = {curr_vert - column_num: 1, curr_vert + column_num: 1, curr_vert - 1: 1, curr_vert + 1: 1}
        nbr_dic = [1, 1, 1, 1]  # wsad
        if letter == "w":
            nbr_dic[0] = 0
        elif letter == "s":
            nbr_dic[1] = 0
        if letter == "a":
            nbr_dic[2] = 0
        elif letter == "d":
            nbr_dic[3] = 0

        while j_check:
            if letter == "j":
                j_key = curr_vert
                j_check = False
            else:
                break

        if tmp_line == 0:
            nbr_dic[0] = None
        elif tmp_line == line_num - 1:
            nbr_dic[1] = None
        if tmp_col == 0:
            nbr_dic[2] = None
        elif tmp_col == column_num - 1:
            nbr_dic[3] = None

        for nbr_key in range(4):
            if nbr_dic[nbr_key] is None:
                continue
            if nbr_key == 0:
                nbr_keys = curr_vert - column_num
            elif nbr_key == 1:
                nbr_keys = curr_vert + column_num
            elif nbr_key == 2:
                nbr_keys = curr_vert - 1
            elif nbr_key == 3:
                nbr_keys = curr_vert + 1
            nbr_dis = dis_dict[nbr_keys]
            new_dis = curr_dis + nbr_dic[nbr_key]
            if nbr_dis > new_dis:
                dis_dict[nbr_keys] = new_dis
                heapq.heappush(heap, [new_dis, nbr_keys])

    return dis_dict[j_key] - 1


size_list = list(map(int, input().split()))
line_total = size_list[0]
column_total = size_list[1]
graph = None
for i in range(line_total):
    if graph is None:
        graph = input()
    else:
        graph += input()

result = dij(graph, line_total, column_total)
print(result)