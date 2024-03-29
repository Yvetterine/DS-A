prim_str_list = input().split()
n = int(prim_str_list[0])
a = int(prim_str_list[1])
b = int(prim_str_list[2])
f_0 = int(prim_str_list[3])
f_1 = int(prim_str_list[4])
m = int(prim_str_list[5])


def two_matrix_mult(matrix_a, matrix_b, mod):
    last = [[0, 0], [0, 0]]
    for row in range(2):
        for column in range(2):
            for k in range(2):
                last[row][column] += ((matrix_a[row][k] % mod) * (matrix_b[k][column] % mod)) % mod
                last[row][column] %= mod
    return last


def mult_matrix_mult(matrix, mult_number, mod):
    if mult_number == 0:
        return [[1, 0], [0, 1]]
    elif mult_number == 1:
        return matrix
    else:
        if mult_number % 2 == 0:
            matrix = mult_matrix_mult(matrix, mult_number // 2, mod)
            result = two_matrix_mult(matrix, matrix, mod)
            return result
        else:
            matrix_org = matrix
            matrix = mult_matrix_mult(matrix, (mult_number - 1) // 2, mod)
            result_tran = two_matrix_mult(matrix, matrix, mod)
            result = two_matrix_mult(result_tran, matrix_org, mod)
            return result


matrix_mult = [[a, b], [1, 0]]
coeff_all = mult_matrix_mult(matrix_mult, n-1, m)
f_1 %= m
f_0 %= m
con = (coeff_all[0][0] * f_1 + coeff_all[0][1] * f_0) % m
print(con)