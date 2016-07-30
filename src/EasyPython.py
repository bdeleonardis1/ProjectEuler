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

#----------------------
#Problem 14
#----------------------
def longest_collatz(cap):
    big = 0
    num = 0
    for i in range(1, cap):
        print(i)
        curr = collatz(i, 0)
        if curr > big:
            big = curr
            num = i

    return num

#Helper for problem 14
def collatz(num, length):
    if num == 1:
        return length
    elif num % 2 == 0:
        return collatz(num / 2, length + 1)
    else:
        return collatz(3 * num + 1, length + 1)

#----------------------------------------------------------------------
#Extremely inefficient brute force solution that is kind of cool for 15
#----------------------------------------------------------------------
def lattice_paths():
    tot = 0
    count = 0
    for i in range(0b11111111111111111111, 0b1111111111111111111100000000000000000001):
        num = str(bin(i))
        num = num[2:]
        while len(num) < 20:
            num = "0" + num

        zeroes = 0
        ones = 0
        for c in num:
            if c == "0":
                ones += 1
            else:
                zeroes += 1

        if ones == zeroes:
            count += 1
        tot += 1
        #1099510579201
        if tot % 10000000 == 0:
            print(bin(tot))
    return count

#-----------------------------------
#Dynamic programming solution for 15
#-----------------------------------
def test_me(grid_size):
    grid_size += 1 #there are 21 x 21 in a 20 # 20 grid
    board = [[0 for i in range(grid_size)] for j in range(grid_size)]
    for i in range(0, grid_size):
        board[i][grid_size - 1] = 1
        board[grid_size - 1][i] = 1

    for r in range(grid_size - 2, -1, -1):
        for c in range(grid_size - 2, -1, -1):
            print("r: %r c: %r" % (r,c))
            board[r][c] = board[r+1][c] + board[r][c+1]

    return board[0][0]

#------------
# #Problem 16
#------------
def power_digit_sum(exponent):
    num = str(2 ** exponent)

    tot = 0
    for c in num:
        tot += int(c)

    return tot

#-----------------
#Problem 17
#-----------------
def num_letter_counts(cap):
    tot = 0
    for i in range (1, cap + 1):
        tot += len(num_in_words(i))

    return tot

#Helper for number 17
def num_in_words(num):
    hard_codes = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine",
                  11: "eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen"}
    if num == 1000:
        return "onethousand"
    elif num > 100 and num % 100 != 0:
        return num_in_words(int(num / 100)) + "hundredand" + num_in_words(num % 100)
    elif num >= 100 and num % 100 == 0:
        return num_in_words(int(num / 100)) + "hundred"
    elif num >= 90:
        return "ninety" + num_in_words(num % 10)
    elif num >= 80:
        return "eighty" + num_in_words(num % 10)
    elif num >= 70:
        return "seventy" + num_in_words(num % 10)
    elif num >= 60:
        return "sixty" + num_in_words(num % 10)
    elif num >= 50:
        return "fifty" + num_in_words(num % 10)
    elif num >= 40:
        return "forty" + num_in_words(num % 10)
    elif num >= 30:
        return "thirty" + num_in_words(num % 10)
    elif num >= 20:
        return "twenty" + num_in_words(num % 10)
    elif num == 18:
        return "eighteen"
    elif num >= 16:
        return num_in_words(num % 10) + "teen"
    elif num == 10:
        return "ten"
    else:
        return hard_codes[num];

#--------------------------------------------------------
#Problem 18 - inefficient brute force method used for 18
#--------------------------------------------------------
def max_path_sum(tri):
    big = 0
    for i in range(0b00000000000000, 0b11111111111111):
        i = bin(i)
        i = i[2:]
        while len(i) < 14:
            i = "0" + i

        index = 0
        row = 1
        curr = tri[0][0]
        for c in i:
            if c == "1":
                index += 1
            curr += int(tri[row][index])
            row += 1

        if curr > big:
            big = curr

    return big

#--------------------------------------------------------------------------------------
#Problem 67 - efficient solution using dynamic programming (could've been used for 18)
#--------------------------------------------------------------------------------------
def efficient_with_dynamic(tri):
    for row in range (len(tri) - 2, -1, -1):
        for col in range(0, len(tri[row])):
            if tri[row + 1][col] > tri[row + 1][col + 1]:
                tri[row][col] += tri[row + 1][col]
            else:
                tri[row][col] += tri[row + 1][col + 1]

    return str(tri[0][0])

#------------
#Problem 19
#------------
def counting_sums():
    num = 0
    days = 1
    for year in range(1901, 2001):
        for month in range(1, 13):
            if month == 4 or month == 6 or month == 9 or month == 11:
                days += 30
            elif month == 2:
                if year % 4 == 0:
                    days += 29
                else:
                    days += 28
            else:
                days += 31

            if (days - 6) % 7 == 0:
                num += 1
    return num


