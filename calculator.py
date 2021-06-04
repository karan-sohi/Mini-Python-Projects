def get_input(first_num):
    print("+\n-\n*\n/\n")
    operation = input("Pick an operation: ")
    second_num = int(input("What's the next number?: "))
    
    if operation == '+':
        result = first_num + second_num
    elif operation == '-':
        result = first_num - second_num
    elif operation == '*':
        result = first_num * second_num
    else:
        result = first_num / second_num
    
    print(f"{first_num} {operation} {second_num} = {result}")
    return result


def main():
    first_num = int(input("What's the first number?: "))
    result = get_input(first_num)

    continue_same = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    while continue_same == "y":
        get_input(result)
        continue_same = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")


main()