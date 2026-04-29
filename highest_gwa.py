highest_names = []
highest_gwa = float('inf')

with open("top_students_gwa.txt", "r") as file:
    for line in file:
        names, gwa = line.strip().split(",")
        gwa = float(gwa)

        if gwa < highest_gwa: 
            highest_gwa = gwa
            highest_names = [names]

        elif gwa == highest_gwa:
            highest_names.append(names)

print(f"Top GWA: {highest_gwa}")
print("Top student(s):")

for student in highest_names:
    print(student)