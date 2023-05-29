numbers = [3, 1, 4, 5, 2]

sorted_numbers = []
while len(numbers) > 0:
min_num = min(numbers)
sorted_numbers.append(min_num)
numbers.remove(min_num)

print(sorted_numbers)
