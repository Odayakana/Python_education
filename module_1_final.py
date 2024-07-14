grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list = list(students)
students_list.sort()

total_grades_dict = {}

for i in range(len(students_list)):
    grade = sum(grades[i]) / len(grades[i])
    total_grades_dict[students_list[i]] = grade

print(total_grades_dict)
