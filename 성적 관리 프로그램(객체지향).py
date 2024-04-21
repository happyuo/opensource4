subjects = ["영어", "C-언어", "파이썬"]

class Student:
    def __init__(self, student_id, student_name, scores):
        self.student_id = student_id
        self.student_name = student_name
        self.scores = scores
        self.total_score = sum(scores)
        self.average_score = self.total_score / len(scores)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.average_score >= 90:
            return 'A'
        elif self.average_score >= 80:
            return 'B'
        elif self.average_score >= 70:
            return 'C'
        elif self.average_score >= 60:
            return 'D'
        else:
            return 'F'

class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student.student_id == student_id:
                del self.students[i]
                break

    def search_student(self, search_key):
        for student in self.students:
            if search_key in [student.student_id, student.student_name]:
                return student
        return None

    def sort_students_by_total_score(self):
        self.students.sort(key=lambda x: x.total_score, reverse=True)

    def count_students_above_80(self):
        count = sum(1 for student in self.students if all(score >= 80 for score in student.scores))
        print("80점 이상을 받은 학생 수:", count)

    def print_results(self):
        print("\t\t\t\t\t성적관리 프로그램\t\t\t\t")
        print("==================================================================")
        print("학번\t\t이름\t\t", end="")
        for subject in subjects:
            print(subject + "\t\t", end="")
        print("총점\t\t평균\t\t학점\t\t등수")
        for idx, student in enumerate(self.students):
            print(student.student_id, student.student_name, end="\t")  # 학번과 이름 출력
            for score in student.scores:  # 과목 성적 출력
                print(score, end="\t\t")
            print(student.total_score, end="\t\t")
            print("{:.1f}".format(student.average_score), end="\t\t")
            print(student.grade, idx+1, end="\t\t\t")
            print()  # 다음 줄로 넘어감

# 메인 함수
def main():
    grade_manager = GradeManager()
    while True:
        print("\n1. 학생 추가\n2. 학생 삭제\n3. 학생 조회\n4. 성적 정렬\n5. 80점 이상 학생 수\n6. 성적 출력\n7. 종료")
        choice = input("원하는 작업을 선택하세요: ")
        if choice == '1':
            student_id = input("학번: ")
            student_name = input("이름: ")
            scores = []
            print("점수를 입력하세요:")
            for subject in subjects:
                score = int(input(subject + ": "))
                scores.append(score)
            student = Student(student_id, student_name, scores)
            grade_manager.add_student(student)
        elif choice == '2':
            student_id = input("삭제할 학생의 학번을 입력하세요: ")
            grade_manager.delete_student(student_id)
        elif choice == '3':
            search_key = input("찾을 학생의 학번 또는 이름을 입력하세요: ")
            student = grade_manager.search_student(search_key)
            if student:
                print("학번:", student.student_id)
                print("이름:", student.student_name)
                for idx, score in enumerate(student.scores):
                    print(subjects[idx] + ":", score)
            else:
                print("해당하는 학생이 없습니다.")
        elif choice == '4':
            grade_manager.sort_students_by_total_score()
        elif choice == '5':
            grade_manager.count_students_above_80()
        elif choice == '6':
            grade_manager.print_results()
        elif choice == '7':
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
