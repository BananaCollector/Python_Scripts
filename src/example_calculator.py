#Example Python math script 
from __future__ import annotations

def safe_division(a: float, b: float) ->float:
    if b == 0:
        raise ValueError("Do not devide by zero!")
    return a/ b

def average(values: list[float]) -> float:
    if not values:
        raise ValueError("List cannot be empty!")
    return(sum(values)/len(values))

if __name__ == "__main__":
    ex_1 = input("Enter two numbers to divide, separated by a space (or 'd' for default): ").split()
    
    if ex_1[0] == "d":
        print(f"Your division for 4 / 10: {safe_division(4, 10)}")
    else:
        print(f"Your division: {safe_division(float(ex_1[0]), float(ex_1[1]))}")
    
    ex_2 = input("Enter a list of numbers separated by spaces (or 'd' for default): ").split()

    if not ex_2:
            print(f"Your average: {average([])}")
    else:
        if ex_2[0] == 'd':
            print(f"Your average for [10, 5, 7, 4]: {average([10, 5, 7, 4])}")
        else:
            print(f"Your average: {average([float(x) for x in ex_2])}")
    