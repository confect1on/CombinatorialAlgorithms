def generate_combinations(n, k):
    a = [i for i in range(0, k + 1)]
    res = []
    p = k
    if k > n:
        return []
    if k == n or k == 0:
        return [a.copy()[1:]]
    while True:
        res.append(a.copy()[1:])
        if a[k] == n:
            p -= 1
        else:
            p = k
        if p >= 1:
            for i in range(k, p - 1, -1):
                a[i] = a[p] + i - p + 1
        else:
            break
    return res


def distance(x, y):
    from math import sqrt
    return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


def check_equilateral_triangle(x, y, z, eps=1e-8):
    dxy = distance(x, y)
    dxz = distance(x, z)
    dyz = distance(y, z)
    if abs(dxy - dxz) < eps and abs(dxy < dyz) < eps and abs(dxz - dyz) < eps:
        return True
    else:
        return False


def regular_set(points):
    if len(points) < 3:
        return False
    flag = True
    for triplet in generate_combinations(len(points), 3):
        a = triplet[0] - 1
        b = triplet[1] - 1
        c = triplet[2] - 1
        print(points[a], points[b], points[c])
        flag = check_equilateral_triangle(points[a], points[b], points[c])
        if not flag:
            break
    return flag


def generate_permutation(n: int):
    result = []
    current = [i + 1 for i in range(n)]
    result.append(current.copy())
    while True:
        i = -1
        for k in range(n - 2, -1, -1):
            if current[k] < current[k + 1]:
                i = k
                break

        if i == -1:
            break
        j = i + 1
        min_value = 100000000
        for k in range(i + 1, n):
            if (current[i] < current[k] and current[k] < min_value):
                j = k
                min_value = current[k]
        current[i], current[j] = current[j], current[i]
        current[i + 1:n] = reversed(current[i + 1:n])
        result.append(current.copy())

    return result


def quadratic_assignment_problem(n: int, c, v, a):

    permutations = generate_permutation(n)
    optimal_cost = 1_000_000_000
    optimal_permutation = None
    for permutation in permutations:
        is_incorrect_permutation = False
        for city, factory in enumerate(permutation):
            if a[factory - 1][city]:
                is_incorrect_permutation = True
                break
        if is_incorrect_permutation:
            continue

        cost_sum = 0
        for i in range(n):
            for j in range(n):
                cost_sum += c[i][j] * v[permutation[i] - 1][permutation[j] - 1]
        if (cost_sum < optimal_cost):
            optimal_permutation = permutation
            optimal_cost = cost_sum

    return optimal_permutation

# from math import sin, pi
# SIN = sin(pi / 3)
# print(alg3_1(3, 3))
# var = regular_set(
#     [
#         (0, 0),
#         (6, 0),
#         (3, 6 * SIN),
#     ]
# )
# print(var)
# print(regular_set(
#     [
#         (0, 0),
#         (0, 1)
#     ]
# ))
