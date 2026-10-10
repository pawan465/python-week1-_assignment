def check_even_odd(number):
    # A number is even when the remainder after dividing by 2 is 0.
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")


def check_prime(number):
    # Numbers smaller than 2 are not prime.
    if number < 2:
        print("The number is not prime.")
        return

    # Try dividing by each number from 2 up to number - 1.
    divisor = 2
    while divisor < number:
        if number % divisor == 0:
            print("The number is not prime.")
            return
        divisor = divisor + 1

    print("The number is prime.")


def main():
    # Step 1: Enter a whole number.
    number = int(input("Enter a whole number: "))

    # Step 2: Call both checking functions.
    check_even_odd(number)
    check_prime(number)


main()
