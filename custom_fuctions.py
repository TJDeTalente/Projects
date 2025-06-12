def custom_len(data):
    count = 0
    for _ in data:
        count += 1
    return count

print(custom_len([1,2,3,4,5]))

def custom_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(custom_sum([8,6,4,7,2,5]))

def custom_min(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
    return smallest

print(custom_min([8,6,4,7,2,5]))

def custom_sorted(data, reverse=False):
    is_string = isinstance(data, str)
    items = list(data)

    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (items[j] > items[j + 1] and not reverse) or (items[j] < items[j + 1] and reverse):
                items[j], items[j + 1] = items[j + 1], items[j]

    return ''.join(items) if is_string else items

print(custom_sorted([4, 1, 5, 2]))

def custom_reversed(data):
    if isinstance(data, str):
        return data[::-1]
    elif isinstance(data, list):
        return data[::-1]
    else:
        raise TypeError('data must be str or list')

print(custom_reversed([4, 1, 5, 2]))