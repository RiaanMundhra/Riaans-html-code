l  = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 361, 400]

def separate(nums):
    odd = []
    even = []
    for n in nums:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    return odd, even

odd_nums, even_nums = separate(l)

print("Odd squares are:", odd_nums)
print("Even squares are:", even_nums)