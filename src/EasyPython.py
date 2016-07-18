# Problems 11 - 20

# ------------
# Problem 11
# ------------
def large_prod_in_grid(grid):
    maximum = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if j + 3 < len(grid[i]):
                total = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
                if total > maximum:
                    maximum = total

            if i + 3 < len(grid):
                total = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
                if total > maximum:
                    maximum = total

            if i + 3 < len(grid) and j + 3 < len(grid[i]):
                total = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
                if total > maximum:
                    maximum = total

            if i + 3 < len(grid) and j - 3 > 0:
                total = grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3]
                if total > maximum:
                    maximum = total
    return maximum


# -----------
# Problem 12
# -----------
def high_div_triangular_num(divisors):
    tot = 0
    count = 1
    while True:
        tot += count
        if len(num_factors(tot)) >= divisors:
            return tot
        count += 1


# helper for problem 12
def num_factors(num):
    return set(x for tup in ([i, num // i] for i in range(1, int(num ** 0.5) + 1) if num % i == 0) for x in tup)


# ----------------------
# Problem 13
# ----------------------
def large_sum(nums):
    total = 0
    for i in nums:
        total += i

    total = str(total)[0:10]

    return total


