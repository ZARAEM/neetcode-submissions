def add_two_numbers() -> int:
    given = input()
    given = given.split(",")
    sum = 0
    for i in range(len(given)):
        sum += int(given[i])
    return sum


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
