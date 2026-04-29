highest_name = ""
highest_gwa = float('inf')

with open("top_students_gwa.txt", "r") as file:
    for line in file:
        name, gwa = line.strip().split(",")
        gwa = float(gwa)

        if gwa < highest_gwa: 
            highest_gwa = gwa
            highest_name = name