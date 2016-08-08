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
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

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

print(circular_primes())