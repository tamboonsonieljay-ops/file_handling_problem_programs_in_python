file = open("numbers.txt", "r")

with open ("even_numbers.txt", "w") as file_even, open("odd_numbers.txt", "w") as file_odd:


    for num in file:
        if num % 2 == 0:
            file_even.write
        else:
            file_odd.write

print(num)