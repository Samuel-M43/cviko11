from student_grades import StudentsGrades
from sorting import random_numbers
#


def main():
    # results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    results = StudentsGrades(random_numbers(30, 0, 100))
    student_count = results.count()

    print(f"Pocet studentov: {student_count}")

    for i in range(student_count):
        grade = results.get_grade(i)
        points = results.scores[i]
        print(f"Student {i}: {points} points -- {grade}")

    for i in range(student_count):
        points = results.scores[i]
        if points == 100:
            idx = results.get_by_index(i)
            print(f"Student {i}: {idx}")

    sorted_points = results.get_sorted()
    print(f"Sorted zoznam: {sorted_points}")


main()