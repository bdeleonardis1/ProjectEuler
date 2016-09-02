import math
import string

#Problem 41
def pandigital_primes():
	for i in range(9, 0, -1):
		nums = []
		for j in range(i, 0, -1):
			nums.append(j)

		temp = generate_polynomials(nums)
		if temp != None:
			return temp

#Helper for 41
def generate_polynomials(nums):
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

		temp = ""
		for num in nums:
			temp += str(num)

		if is_prime(int(temp)):
			return temp

#Helper for 41
def is_prime(num):
	for i in range(2, int(math.sqrt(num))):
		if num % i == 0:
			#print("num: " + str(num) + " i: " + str(i) + " num % i " + str(num % i) + " num / i " + str(num / i))
			return False
	return True

#Problem 42
def coded_triangle_numbers():
	file = open('Forty2Input.txt')
	words = list(file.read().split(","))

	count = 0

	for word in words:
		word = word.replace('"', '')
		score = word_score(word)

		if is_triangle(score):
			count += 1

	return count

#Helper for 42
def word_score(word):
	score = 0
	for char in word:
		score += ord(char) - 64
	return score

#Helper for 42
def is_triangle(num):
	num *= 2
	for i in range(1, num // 2 + 1):
		if i * (i + 1) == num:
			return True

	return False


print(coded_triangle_numbers())