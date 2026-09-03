def divide_numbers(a: str, b: str) -> None:
    try:
        res = int(a) / int(b)
        print(res)
    except Exception as err:
        print("An error occurred:", err)



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
