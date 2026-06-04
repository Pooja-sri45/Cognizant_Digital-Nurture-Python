def sum_of_odds(start, end):
    if start > end:
        return "Invalid range"

    total = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            continue   
        total += i
    return total

start = 1
end = 10
result = sum_of_odds(start, end)
print("Sum of odd numbers from", start, "to", end, "is:", result)