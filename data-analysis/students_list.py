import pandas as pd

names = []
maths_marks = []
science_marks = []

print("Enter student details.")
print("Type STOP as name when you are done.\n")

while True:
    name = input("Enter student name: ")

    if name.lower() == "stop":
        break

    maths = int(input("Enter Maths marks: "))
    science = int(input("Enter Science marks: "))

    names.append(name)
    maths_marks.append(maths)
    science_marks.append(science)

    print("Student added.\n")

# Create DataFrame (table)
df = pd.DataFrame({
    "Name": names,
    "Maths": maths_marks,
    "Science": science_marks
})

# Total marks
df["Total"] = df["Maths"] + df["Science"]

# Sort by Total (highest first)
df = df.sort_values(by="Total", ascending=False)

# Rank
df["Rank"] = df["Total"].rank(method="dense", ascending=False).astype(int)

# Save to Excel
df.to_excel("students.xlsx", index=False)

print("\nExcel file 'students.xlsx' created successfully.")
print(df)
