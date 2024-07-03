from string import ascii_lowercase

def check_prime_number(num):
    if num <=2: return False
    for i in range(2, num):
        if num % i == 0: return False
    return True

def check_palindrome(num):
    nums: list[int] = []
    while num > 0:
        curr = num % 10
        nums.append(curr)
        num //= 10
    lp, rp = 0, len(nums) - 1
    print(nums)
    while lp < rp:
        if nums[lp] is not nums[rp]:
            return False
        lp += 1
        rp -= 1
    return True

def find_max(nums):
    return max(nums)

def find_max_without_max(nums: list) -> int:
    res = nums[0]
    for i in nums:
        if res < i: res = i
    return res

def check_pangram(word):
    return not bool(set(ascii_lowercase).symmetric_difference(word))

def arrange_words_alphabetically_with_hyphen(words):
    words.sort()
    return '-'.join(words)

def check_perfect_number(num) -> bool:
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total == num


# print(check_prime_number(3)) # True
# print(check_prime_number(2)) # False
# print(check_prime_number(6)) # False
# print(find_max([3, 45, 214, 2, 745, 43])) # 745
# print(check_pangram('lsfewoafapqwerads')) #False
# print(check_pangram('abcdefghijklmnopqrstuvwxyzz')) #True
# print(arrange_words_alphabetically_with_hyphen(['sdfasdf', 'sdfasfdg', 'werwer']))
# print(check_perfect_number(6))#True
# print(check_perfect_number(15))#False

