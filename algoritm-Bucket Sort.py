a = [3, 7, 0, 5, 2, 8, 9, 1, 4, 6, 10]
buckets = [ [] for i in range(11)]
for num in a:
    buckets[num].append(num)
for i in range(len(buckets)):
    buckets[i] = sorted(buckets[i])
sorted_a = []
for bucket in buckets:
    sorted_a += bucket

print(sorted_a)or
