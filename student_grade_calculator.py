def calculate_average(mark1, mark2, mark3):
    # Add the marks and divide by the number of subjects.
    return (mark1 + mark2 + mark3) / 3


def get_grade(average):
    # Choose a grade based on the average mark.
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def main():
    # Step 1: Enter marks for three subjects.
    mark1 = float(input("Enter mark for subject 1: "))
    mark2 = float(input("Enter mark for subject 2: "))
    mark3 = float(input("Enter mark for subject 3: "))

    # Step 2: Call the functions and display the answers.
    average = calculate_average(mark1, mark2, mark3)
    grade = get_grade(average)
    print("Average:", average)
    print("Grade:", grade)


main()
