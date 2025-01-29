import math
from collections import Counter

# 输入句子
sentence = "Count the number of unique permutations of the alphabetic letters in this sentence excluding spaces."

# 提取字母并统计频率
letters = [char.lower() for char in sentence if char.isalpha()]  # 提取字母并忽略大小写
letter_counts = Counter(letters)  # 统计频率

# 计算总字母数
total_letters = sum(letter_counts.values())

# 计算排列数
# P = n! / (a1! * a2! * ... * ak!)
denominator = math.prod(math.factorial(count) for count in letter_counts.values())
unique_permutations = math.factorial(total_letters) // denominator

# 输出结果
print(f"唯一排列数: {unique_permutations}")