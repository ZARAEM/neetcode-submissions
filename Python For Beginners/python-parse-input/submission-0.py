from typing import List

def read_integers() -> List[int]:
    integers = input()
    integers_list = integers.split(",")

    for i in range(len(integers_list)):
        integers_list[i] = int(integers_list[i])
    
    return integers_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
