def write_user_input():
    lines = []

    print("Enter 5 lines about your life:")

    for i in range(5):
        line = input(f"Line {i+1}: ")
        lines.append(line)

    with open("mylife.txt", "w") as file:
        for line in lines:
            file.write(line + "\n")

    print("Your input has been saved to mylife.txt.")

write_user_input()