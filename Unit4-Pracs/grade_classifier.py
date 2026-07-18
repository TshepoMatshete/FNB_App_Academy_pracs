name = input("Please enter your name: ")
subj1 = float(input("Please enter your mark for subject 1: "))
subj2 = float(input("Please enter your mark for subject 2: "))
subj3 = float(input("Please enter your mark for subject 3: "))

average = (subj1 + subj2 + subj3) / 3

letter_grade = ""
flag = []

if average >= 80:
    letter_grade = "A"
elif average >= 70:
    letter_grade = "B"
elif average >= 60:
    letter_grade = "C"
elif average >= 50:
    letter_grade = "D"
else:
    letter_grade = "F"

if subj1 < 40 :
    flag.append("Subject 1")
elif subj2 < 40 :
    flag.append("Subject 2")
elif subj3 < 40 :
    flag.append("Subject 3")  

pass_status = "Pass" if average >= 50 else "Fail"


print(f"Hello {name}, here is your report card:")
print(f"Average Mark: {average:.2f}")
print(f"Letter Grade: {letter_grade}")
print(f"Pass Status: {pass_status}")
if flag:
    print(" Subjects below need Intervention:")
    for subject in flag:
        print(f" - {subject}")