def solution(number, n, m):
    result = 0
    for i in range(n, 20, n):
        print(i)
        if number == i:
            print("found!")
            result += 0.5
            break

    for i in range(m, 20, m):
        print(i)
        if number == i:
            print("found!")
            result += 0.5
            break

    return result

result = solution(12, 2, 3)
print(result)

# result = solution(55, 10, 5)
# print(result)
