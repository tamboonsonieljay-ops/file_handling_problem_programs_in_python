def write_user_input():
    print("Enter lines about your life (type 'STOP' to finish):")
    lines = []

    while True:
        line = input()
        if line.upper() == "STOP":
            break
        lines.append(line)

    with open("mylife.txt", "a") as file:
        for line in lines:
            file.write(line + "\n")

    print("Your input has been saved to mylife.txt.")

write_user_input()