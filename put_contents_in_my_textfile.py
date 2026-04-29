def write_to_file():
    lines = [
        "I started learning Python.",
        "I practiced file handling.",
        "I improved my programming skills.",
        "I will continue to grow as a future developer."
    ]

    with open("mylife.txt", "w") as file:
        for line in lines:
            file.write(line + "\n")

write_to_file()