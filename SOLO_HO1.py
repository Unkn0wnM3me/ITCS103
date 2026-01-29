def compute_average(numbers):
 
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def compare_average_length(avg, length, word):
    
    if length > avg:
        relation = "greater than"
    elif length < avg:
        relation = "less than"
    else:
        relation = "equal to"
    print(f"The length of the word '{word}' is {relation} the average.")

def main():
    word = input("Enter a word:").strip()
    if not word:
        print("No word entered. Exiting.")
        return

    length = len(word)

    numbers = []
    for i in range(1, length + 1):
        while True:
            entry = input(f"Enter number {i}:")
            try:
                # accept integers or floats
                num = float(entry)
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    # For nicer display: show integers without .0 when possible
    def format_num(x):
        return int(x) if float(x).is_integer() else x
    display_list = [format_num(x) for x in numbers]

    avg = compute_average(numbers)

    print(display_list)
    print(f"The length of the word is {length}")
    print(f"The average of the numbers is {avg}")
    compare_average_length(avg, length, word)

if __name__ == "__main__":
    main()


#perfect na 'to
