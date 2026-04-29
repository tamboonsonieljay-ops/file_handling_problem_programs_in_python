with open("numbers.txt", "r") as file:
    file_numbers = file.read()

file_numbers = [int() for num in file_numbers]

with open ("even_numbers.txt", "w") as file_even, open("odd_numbers.txt", "w") as file_odd:


    for num in file_numbers:
        if num % 2 == 0:
            file_even.write(str(num))
        else:
            file_odd.write(str(num))

print("The number.txt file have been sorted into even_numbers.txt and odd_numbers.txt files.")