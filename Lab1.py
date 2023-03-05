#O(n*2^n)
def algo2_1(n):
    b = [0 for _ in range(n)]
    res = []
    m = None
    #2^n
    while not all(b):
        res.append(b.copy())
        #n
        for i in range(n - 1, -1, -1):
            if b[i] == 0:
                m = i
                break
        b[m] = 1
        #n
        for j in range(m + 1, n):
            b[j] = 0
    res.append(b.copy())
    return res

# print(algo2_1(5))
# #fail
a = [[1, 1, 0, 1, 0, 0, 0, 0, 0],
     [1, 1, 1, 0 ,1 ,0 ,0 ,0 ,0],
     [0, 1, 1, 0, 0, 1, 0, 0, 0],
     [1, 0, 0, 1, 1, 0, 1, 0, 0],
     [0, 1, 0, 1, 1, 1, 0, 1, 0],
     [0, 0, 1, 0, 1, 1, 0, 0, 1],
     [0, 0, 0, 1, 0, 0, 1, 1, 0],
     [0, 0, 0, 0, 1, 0, 1, 1, 1],
     [0, 0, 0, 0, 0, 1, 0, 1, 1],]
# a = [[1, 1, 0, 1, 0, 0, 0, 0, 0],
#      [1, 1, 0, 1 ,0 ,0 ,0 ,0 ,0],
#      [0, 0, 1, 0, 0, 1, 0, 0, 0],
#      [1, 1, 0, 1, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 1, 1, 0, 0, 0],
#      [0, 0, 1, 0, 1, 1, 0, 0, 1],
#      [0, 0, 0, 0, 0, 0, 1, 1, 0],
#      [0, 0, 0, 0, 0, 0, 1, 1, 0],
#      [0, 0, 0, 0, 0, 1, 0, 0, 1],]

c = [1, 1, 1, 2, 1, 1, 1, 1, 1]

def deploy_military_bases(n, neighborhoods_region_relation, loss_by_region):
    optimal_solution = None
    optimal_loss = 1_000_000
    for base_deploy in algo2_1(n):
        # check condition
        cond = True
        for i in range(n):
            cond_sum = 0
            for j in range(n):
                cond_sum += neighborhoods_region_relation[i][j] * base_deploy[j]
            if cond_sum < 1:
                cond = False
                break
        if cond:
            loss = 0
            for i in range(n):
                loss += loss_by_region[i] * base_deploy[i]
            if loss <= optimal_loss:
                if loss == optimal_loss:
                    if sum(optimal_solution) <= sum(base_deploy):
                        continue
                optimal_solution = base_deploy
                optimal_loss = loss
    return optimal_solution

# print(deploy_military_bases(9, a, c))