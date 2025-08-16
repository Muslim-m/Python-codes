from source.Students import Student

def formatFile():
    file = open("file.txt", "r")
    file2 = open("file2.csv", "w")

    studentlist = []

    # iterate over each line in file
    for line in file.readlines():
        line = line.strip()  # remove \n
        if not line:
            continue

        parts = line.split()   # split by spaces
        # parts = ['9202974', 'Jin', 'M', '092']

        id = parts[0]
        name = parts[1]
        gender = parts[2]
        grade = parts[3]

        studentlist.append(Student(id, name, gender, grade))

    # write CSV header
    file2.write("ID,Name,Gender,Grade\n")
    for s in studentlist:
        file2.write(f"{s.id},{s.name},{s.gender},{s.grade}\n")

    file.close()
    file2.close()

formatFile()