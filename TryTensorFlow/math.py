""" Множества """
A = {1, 3, 5, 7}
B = {3, 5, 7, 9, 13}

# print(A & (A | B))
# print(A | B | B | A)
# print(A - B)  # разность
# print(A & B)  # пересечение

A1 = set([a for a in range(40, 61) if a != 50])  # проколотая окрестность точки 50 с радиусом 10
B1 = set([b for b in range(49, 56)])  # окрестность точки 52 с радиусом 3
# print(A1 | B1)
# print(A1 & B1)
# print(A1 - B1)
# print(B1 - A1)
