from student_grades import StudentsGrades
from sorting import random_numbers
import matplotlib.pyplot as plt


def main():
    # results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    results = StudentsGrades(random_numbers(30, 0, 100))
    student_count = results.count()

    print(f"Pocet studentov: {student_count}")
    grades = []
    for i in range(student_count):
        grade = results.get_grade(i)
        points = results.scores[i]
        grades.append(grade)
        print(f"Student {i}: {points} points -- {grade}")

    for i in range(student_count):
        points = results.scores[i]
        if points == 100:
            idx = results.get_by_index(i)
            print(f"Student {i}: {idx}")

    sorted_points = results.get_sorted()
    order = ["A", "B", "C", "D", "E", "F"]
    sorted_grades = sorted(grades, key=lambda x: order.index(x))
    print(f"Sorted zoznam: {sorted_points}")
    plt.hist(sorted_grades, bins=6, edgecolor="black", color="steelblue")
    plt.title("Histogram známek")
    plt.xlabel("Známka (F=1 ... A=6)")
    plt.ylabel("Počet studentů")
    plt.grid(axis="y", alpha=0.3)

    plt.show()


main()