from queue import Queue

tmp = list(map(int, input().split()))
vert_num = tmp[0]
edge_num = tmp[1]
k = tmp[2]
start = tmp[3]
nbr_list = [[] for b in range(vert_num + 1)]

for i in range(edge_num):
    each_tmp = list(map(int, input().split()))
    vert_1 = each_tmp[0]
    vert_2 = each_tmp[1]
    nbr_list[vert_1].append(vert_2)
    nbr_list[vert_2].append(vert_1)

for each_vert_nbr in nbr_list[1:]:
    compare_set = set()
    for nbr in each_vert_nbr:
        compare_set.add(nbr * k)
    inter = list(set(each_vert_nbr).intersection(compare_set))
    while len(inter) != 0:
        vert_big = inter.pop()
        vert_small = vert_big // k
        if vert_small not in nbr_list[vert_big]:
            nbr_list[vert_big].append(vert_small)
            nbr_list[vert_small].append(vert_big)

list_color = [0 for b in range(vert_num)]
queue_total = Queue(maxsize=vert_num)
queue_total.put(start)
list_color[start - 1] = 1
out_put = []
while not queue_total.empty():
    result = queue_total.get()
    out_put.append(result)
    nbr_list[result].sort()
    for i in nbr_list[result]:
        if list_color[i - 1] == 0:
            queue_total.put(i)
            list_color[i - 1] = 1

for i in out_put:
    print(i, end=" ")
