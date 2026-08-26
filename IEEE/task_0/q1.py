N = int(input())
l = list(map(int, input().split()))
greatest = l[0]
for i in range(1, N):
    if l[i] > greatest:
        greatest = l[i]
print("Largest:", greatest)
least = l[0]
for i in range(1, N):
    if l[i] < least:
        least = l[i]
print("Smallest:", least)
sum = 0
for i in range(N):
    sum += l[i]
print("Sum:", sum)
even_count = 0
odd_count = 0
for i in range(N):
    if l[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even count:", even_count)
print("Odd count:", odd_count)
print("Reversed:", l[::-1])

