

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        points = self.get_by_index(index)
        if 90 <= points <= 100:
            return "A"
        elif 80 <= points < 90:
            return "B"
        elif 70 <= points < 80:
            return "C"
        elif 60 <= points < 70:
            return "D"
        elif 50 <= points < 60:
            return "E"
        else:
            return "F"

    def find(self, score):
        positions = []
        for i in range(self.count()):
            if self.scores[i] == score:
                positions.append(i)
        return positions

    def get_sorted(self):
        sorted_scores = self.scores.copy()
        n = len(sorted_scores)
        for i in range(n):
            swapped = False
            for j in range(0, n - 1 - i):
                if sorted_scores[j] > sorted_scores[j + 1]:
                    sorted_scores[j], sorted_scores[j + 1] = sorted_scores[j + 1], sorted_scores[j]
                    swapped = True

            if not swapped:
                break
        return sorted_scores


grades = StudentsGrades([95, 82, 74, 61, 58, 30])

print(grades.find(74))
print(grades.get_sorted())