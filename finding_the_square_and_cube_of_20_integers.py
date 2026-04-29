def process_integers():
    with open("integers.txt", "r") as file:
        numbers = [int(line.strip()) for line in file]

    with open("double.txt", "w") as double_file, open("triple.txt", "w") as triple_file:
        for num in numbers:
            if num % 2 == 0:
                double_file.write(str(num ** 2) + "\n")
            else:
                triple_file.write(str(num ** 3) + "\n")

    print("Processing complete. Files double.txt and triple.txt created.")

process_integers()