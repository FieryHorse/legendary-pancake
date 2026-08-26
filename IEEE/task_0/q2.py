original = list(map(int, input().split()))
def process_list(numbers):
    copy = numbers.copy()
    for i in range(len(numbers)):
        if numbers[i] < 0:
            copy.remove(numbers[i])
    copy.append(0)
    copy.sort()
    return copy
result = process_list(original)
print("Original:", original)
print("Result:", result)