import file_operations as fo
import exception_and_read as er


class Student:
    def __init__(self, name, id, score, major, gpa, retake, pass_or_not, special_reasons):
        self.name = name
        self.id = id
        self.score = score
        self.major = major
        self.gpa = gpa
        self.retake = retake
        self.pass_or_not = pass_or_not
        self.special_reasons = special_reasons

    def to_dict(self):
        return {
            'name': self.name,
            'id': self.id,
            'score': self.score,
            'major': self.major,
            'gpa': self.gpa,
            'retake': self.retake,
            'pass_or_not': self.pass_or_not,
            'special_reasons': self.special_reasons
        }


class Course:
    def __init__(self, course_name, course_number, course_category, course_type, credit, class_hour, test_date,
                 grade_type, exam_type, teaching_unit):
        self.course_name = course_name
        self.course_number = course_number
        self.course_category = course_category
        self.course_type = course_type
        self.credit = credit
        self.class_hour = class_hour
        self.test_date = test_date
        self.grade_type = grade_type
        self.exam_type = exam_type
        self.teaching_unit = teaching_unit

    def to_dict(self):
        return {
            'course_name': self.course_name,
            'course_number': self.course_number,
            'course_category': self.course_category,
            'course_type': self.course_type,
            'credit': self.credit,
            'class_hour': self.class_hour,
            'test_date': self.test_date,
            'grade_type': self.grade_type,
            'exam_type': self.exam_type,
            'teaching_unit': self.teaching_unit
        }


class Grade:
    def __init__(self, semester, courses):
        self.semester = semester
        self.courses = courses

    def to_dict(self):
        return {
            'semester': self.semester,
            'courses': self.courses
        }


class Courses:
    def __init__(self, course_info, student_info):
        self.course_info = course_info
        self.student_info = student_info

    def to_dict(self):
        return {
            'course_info': self.course_info,
            'student_info': self.student_info
        }


def enter_student_grades(user):
    """教师：录入学生成绩，其他用户：返回无权限.已经录入过的课程无需填入课程相关信息，只需填学生信息即可"""
    if user != 'teacher':
        print('You do not have the relevant permissions')
        return
    grades_data = fo.import_data('grades.txt')
    school_year_term = input("Please enter the academic year and semester:")
    semester_index = -1
    if grades_data:
        for i, grades in enumerate(grades_data):
            if grades['semester'] == school_year_term:
                semester_index = i
                break
    if semester_index == -1:
        grade = Grade(school_year_term, [])
        semester_index = len(grades_data)
        grades_data.append(grade.to_dict())
    subject_number = er.read_int_number("Please input the number of subjects:")
    for i in range(subject_number):
        print("course%d" % (i+1))
        course_name = input("Please enter the course name:")
        course_index = -1
        if semester_index != -1:
            for j, grades in enumerate(grades_data[semester_index]['courses']):
                if grades['course_info']['course_name'] == course_name:
                    course_index = j
                    break
        if course_index == -1:
            course_number = input("Please enter the course number:")
            course_category = input("Please enter the course category: ")
            course_type = input("Please enter the course type: ")
            credit = er.read_int_number("Please enter the credit: ")
            class_hour = er.read_int_number("Please enter the class hour: ")
            test_date = input("Please enter the test date: ")
            grade_type = input("Please enter the grade type: ")
            exam_type = input("Please enter the exam type: ")
            teaching_unit = input("Please enter the teaching unit: ")
            course = Course(course_name, course_number, course_category, course_type, credit, class_hour, test_date,
                            grade_type, exam_type, teaching_unit)
            courses = Courses(course.to_dict(), [])
            course_index = len(grades_data[semester_index]['courses'])
            grades_data[semester_index]['courses'].append(courses.to_dict())
        grade_number = er.read_int_number("Please input the number of grades in this subject:")
        for j in range(grade_number):
            print("grade%d" % (j + 1))
            student_name = input("Please enter the student's name:")
            student_id = input("Please enter the student's ID:")
            score = er.read_float_number("Please enter the total score:")
            major = input("Is it a major course? : ")
            gpa = er.read_float_number("Please enter the GPA: ")
            retake = input("Is it a retake? : ")
            pass_or_not = input("Did the student pass? : ")
            special_reasons = input("If there are any special reasons, please enter them: ")
            student = Student(student_name, student_id, score, major, gpa, retake, pass_or_not, special_reasons)
            grades_data[semester_index]['courses'][course_index]['student_info'].append(student.to_dict())
    fo.export_data('grades.txt', grades_data)
    print("Student grades information has been saved.")
    return


if __name__ == "__main__":
    print("When the user is a teacher:")
    enter_student_grades('teacher')
    print("\nWhen the user is not a teacher:")
    enter_student_grades('student')
