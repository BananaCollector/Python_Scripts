#Example Python math script 

def safe_division(a: float, b: float) ->float:
    if b == 0:
        raise ValueError("Do not devide by zero!")
    return a/ b

def average(values: list[float]) -> float:
    if not values:
        raise ValueError(" List cannot be empty!")
    return(sum(values)/len(values))

if __name__ == "__main__":
    ex_1 = input("Enter two numbers to divide, separated by a space: ").split()
    print(f"Your division: {safe_division(float(ex_1[0]), float(ex_1[1]))}")
    
    ex_2 = input("Enter a list of numbers separated by spaces: ").split()
    print(f"Your average: {average([float(x) for x in ex_2])}")
    