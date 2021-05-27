import json

f = open('Jakub_Hulek.json', )
data = json.load(f)

def sortFunc(a):
    return int(a)


adjacency_list = list()
for i in data:
    adjacency_list.append(i)
for i in adjacency_list:
    i.sort(reverse=False, key=sortFunc)

for i in range(len(adjacency_list)):
    for j in range(len(adjacency_list[i])):
        print(f'{i} {adjacency_list[i][j]}')


adjacency_matrix = list()

for i in range(len(adjacency_list)):
    to_append = list()
    for j in range(len(adjacency_list)):
        if j in adjacency_list[i]:
            to_append.append(1)
        else:
            to_append.append(0)
    adjacency_matrix.append(to_append)
for i in adjacency_matrix:
    print(i)

incidence_matrix = list()
for i in range(13):
    a = list()
    incidence_matrix.append(a)

for i in range(len(adjacency_matrix)):
    for j in range(i, len(adjacency_matrix[i])):
        if adjacency_matrix[i][j] == 1:
            for k in range(len(incidence_matrix)):
                a = incidence_matrix[k]
                if k == i or k == j:
                    a.append(1)
                else:
                    a.append(0)

for k in range(len(incidence_matrix)):
    print(incidence_matrix[k])

amount_of_edges = list()
for a in adjacency_list:
    amount_of_edges.append(len(a))

print(amount_of_edges)
print(len(incidence_matrix[0]))

