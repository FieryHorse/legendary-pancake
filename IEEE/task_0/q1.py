N = int(input())
my_list = list(map(int, input().split()))
greatest = my_list[0]
for i in range(1, N):
    if my_list[i] > greatest:
        greatest = my_list[i]
print("Largest:", greatest)
least = my_list[0]
for i in range(1, N):
    if my_list[i] < least:
        least = my_list[i]
print("Smallest:", least)
sum = 0
for i in range(N):
    sum += my_list[i]
print("Sum:", sum)
even_count = 0
odd_count = 0
for i in range(N):
    if my_list[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even count:", even_count)
print("Odd count:", odd_count)
print("Reversed:", *(my_list[::-1]))