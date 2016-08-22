import math

#------------
#Problem 32
#------------
def pandigital_product():
    tot = 0
    for i in range(1000, 80000):
        if getFactors(i):
            tot += i

    return tot

#Helper for 32
def getFactors(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            #print("i: " + str(i) + " num / i: " + str(num / i))
            if is_pandigital(i, int(num / i), num):
                return True

    return False

#Helper for 32
def is_pandigital(a, b, c):
    a = str(a)
    b = str(b)
    c = str(c)

    nums = set()
    for char in a:
        nums.add(char)

    for char in b:
        nums.add(char)

    for char in c:
        nums.add(char)

    if len(nums) == 9 and '0' not in nums and (len(a) + len(b) + len(c)) == 9:
        return True
    else:
        return False

#------------
#Problem 33
#------------
def digit_cancelling_fractions():
    num_tot = 1
    den_tot = 1
    for num in range(10, 100):
        for den in range(num + 1, 100):
            if str(num)[0] == str(den)[1] or str(num)[1] == str(den)[0]:
                if int(str(den)[0]) != 0 and num / den == int(str(num)[1]) / int(str(den)[0]):
                    num_tot *= num
                    den_tot *= den
                elif int(str(den)[1]) != 0 and num / den == int(str(num)[0]) / int(str(den)[1]):
                    num_tot *= num
                    den_tot *= den

    gcd = 0
    for i in range(num_tot, 0, -1):
        if num_tot % i == 0 and den_tot % i == 0:
            gcd = i
            break

    return den_tot / gcd

#-----------
#Problem 34
#-----------
def digit_factorials():
    answer = 0
    for i in range(10, 2540161): #upper bound is 9! * 7 (because 9! * 8 is still only 7 digits
        tot = 0
        for num in str(i):
            tot += math.factorial(int(num))
        if i == tot:
            answer += i
    return answer

#------------
#Problem 35
#------------
def circular_primes():
    count = 0
    for i in range(2, 1000000):
        if is_prime(i):
            l = rotations(i)
            circular = True
            for n in l:
                if(not is_prime(int(n))):
                    circular = False
            if circular:
                count += 1
    return count

#Helper for 35
def rotations(s):
    s = str(s)
    rotations = []
    for i in range(1, len(s)):
        rotations.append(s[(len(s) - i): len(s)] + s[0:(len(s) - i)])
    return rotations

#Helper for 35
def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

#-----------
#Problem 36
#-----------
def double_base_palindrome():
    tot = 0
    for i in range(1, 1000000):
        if is_palindrome(i):
            if is_palindrome(bin(i)[2:len(bin(i))]):
                tot += i

    return tot

#Helper for 36
def is_palindrome(num):
    num = str(num)
    for i in range(0, int(len(num) / 2)):
        if num[i] != num[len(num) - i - 1]:
            return False
    return True

#-----------
#Problem 37
#-----------
def truncatable_primes():
    count = 0
    tot = 0
    n = 11
    while count < 11:
        if is_prime(n):
            num = str(n)
            truncatable = True
            for i in range(1, len(num)): #truncating from left
                if not is_prime(int(num[i:len(num)])):
                    truncatable = False

            for i in range(1, len(num)):  # truncating from left
                if not is_prime(int(num[0:len(num) - i])):
                    truncatable = False

            if truncatable:
                tot += n
                count += 1
        n += 1

    return tot

#------------
#Problem 38
#------------
def pandigital_multiples():
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    count = 0
    while True:
        j = len(nums) - 1
        while j > 0 and nums[j] >= nums[j - 1]:
            j -= 1

        if j == 0:
            break

        pivot = j - 1
        k = len(nums) - 1

        while nums[k] >= nums[pivot]:
            k -= 1

        temp = nums[pivot]
        nums[pivot] = nums[k]
        nums[k] = temp

        l = len(nums) - 1
        while j < l:
            temp = nums[j]
            nums[j] = nums[l]
            nums[l] = temp

            j += 1
            l -= 1

        if concat_product(nums):
            break

    return nums

#Helper for 38 - checks if a number is a concatenated product
def concat_product(nums):
    s = ""
    for i in nums:
        s += str(i)
    num = int(s)
    stri = ""

    for i in range(1, 5):
        flag = True
        first = int(s[0: i])
        stri = s[i:len(s)]

        rot = 2
        while len(stri) > 0:
            check = first * rot
            length = len(str(check))
            curr = stri[0:length]
            if check != int(curr):
                flag = False
                break
            rot += 1
            stri = stri[length:len(stri)]

        if flag:
            return True

    return False

#-----------
#Problem 39
#-----------
def integer_right_triangles():
    sums = []
    for i in range(0, 1000):
        sums.append(0)

    for a in range(2, 500):
        for b in range(a, 500):
            for c in range(b, 500):
                if a ** 2 + b ** 2 == c ** 2:
                    perimeter = a + b + c
                    if perimeter <= 1000:
                        sums[perimeter - 1] += 1

    return sums.index(max(sums)) + 1

#-----------
#Problem 40
#-----------
def champ_constant():
    nums = ""
    for i in range(1, 190000):
        nums += str(i)

    tot = 1
    curr = 1
    while curr <= 1000000:
        tot *= int(nums[curr - 1])
        curr *= 10

    return tot

print(champ_constant())

#Random method to generate all of the factors of a string
def factors(n):
    return set(x for tup in ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0) for x in tup)

#Random methods to generate all permutations of a string
def permutation(str):
    permutations("", str)

#Helper for permutation method
def permutations(prefix, str):
    n = len(str)
    if n == 0:
        print(prefix)
    else:
        for i in range(0, n):
            permutations(prefix + str[i], str[0:i] + str[i+1:n])
