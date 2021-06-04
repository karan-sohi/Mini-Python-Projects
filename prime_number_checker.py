def prime_checker(number):
    for i in range(2, 101):
        if number % i == 0 and i != number:
            x = False 
            break
        else:
            x = True

    if x == True:
        print("It's a prime number")
    else:
        print("It's not a prime number")



n = int(input("Check this number: "))
prime_checker(number=n)