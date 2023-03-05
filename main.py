import Lab2
n = 3
c = [
        [0, 1, 2],
        [1, 0, 3],
        [2, 3, 0]
    ]
v = [
        [0, 5, 6],
        [5, 0, 3],
        [6, 3, 0]
    ]
a = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
print(Lab2.quadratic_assignment_problem(n, c, v, a))