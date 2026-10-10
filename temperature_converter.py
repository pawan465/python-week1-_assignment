def celsius_to_fahrenheit(celsius):
    # Formula to convert Celsius to Fahrenheit.
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    # Formula to convert Fahrenheit to Celsius.
    return (fahrenheit - 32) * 5 / 9


def main():
    # Step 1: Choose the conversion.
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose 1 or 2: ")

    # Step 2: Get the temperature and call the correct function.
    if choice == "1":
        celsius = float(input("Enter Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print("Fahrenheit:", result)
    elif choice == "2":
        fahrenheit = float(input("Enter Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print("Celsius:", result)
    else:
        print("Please choose 1 or 2.")


main()
