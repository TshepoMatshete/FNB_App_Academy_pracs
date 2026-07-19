
#Grade classifier logic

def calculate_grade_status(name, subj1, subj2, subj3):

    average = (subj1 + subj2 + subj3) / 3

    letter_grade = ""

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

    pass_status = "Pass" if average >= 50 else "Fail"
    
    student_result = {
        "name": name,
        "average": average,
        "letter_grade": letter_grade,
        "pass_status": pass_status,
    }
    return student_result


students = [
    {"name": "Ntando", "maths": 85, "english": 78, "science": 92},
    {"name": "Tshepo", "maths": 67, "english": 72, "science": 70},
    {"name": "Tsholofelo", "maths": 90, "english": 88, "science": 95},
    {"name": "Daniel", "maths": 45, "english": 55, "science": 60},
    {"name": "Thabo", "maths": 75, "english": 80, "science": 85}]

students_results = []
for student in students:
    name = student["name"]
    subj1 = student["maths"]
    subj2 = student["english"]
    subj3 = student["science"]

    result = calculate_grade_status(name, subj1, subj2, subj3)
    students_results.append(result)


print("=" * 60)
print(f"{'Student':<20} {'Average':<10} {'Grade':<10} {'Status':<10}")
print("=" * 60)
student_ave_sum = 0.0
highest_mark = 0.0
lowest_mark = 0.0

for result in students_results:
    student_ave_sum += result['average']
    if result['average'] > highest_mark:
        highest_mark = result['average']
    if result['average'] < lowest_mark or lowest_mark == 0.0:
        lowest_mark = result['average']
        
    print(
        f"{result['name']:<20} "
        f"{result['average']:<10.2f} "
        f"{result['letter_grade']:<10} "
        f"{result['pass_status']:<10}"
    )

class_average = student_ave_sum / len(students_results) if students_results else 0

print("=" * 60)

print(f"{'Class Average:':<20} {class_average:<10.2f}")
print(f"{'Highest Mark:':<20} {highest_mark:<10.2f}")
print(f"{'Lowest Mark:':<20} {lowest_mark:<10.2f}")

print("=" * 60)

print("You can search for a student by name. Type 'exit' to quit." )

while True:
    search_name = input("Enter student name to search: ").strip()
    if search_name.lower() == 'exit':
        break

    found_student = next((result for result in students_results if result['name'].lower() == search_name.lower()), None)

    if found_student:
        print(
            f"Found: {found_student['name']} - "
            f"Average: {found_student['average']:.2f}, "
            f"Grade: {found_student['letter_grade']}, "
            f"Status: {found_student['pass_status']}"
        )
    else:
        print(f"No student found with the name '{search_name}'.")