import sys

import chart
import login
import enter_grades as eg
import analysis_course_grades as acg
import report_find_export as rfe
import file_operations as fo
import modify_grades as mg
import delete_grades as dg
import collect_feedback as feedback
import analysis_student_grades as asg
import advise as ad


class Marks:  # all the things in
    def enter_student_grades(self):
        eg.enter_student_grades('teacher')

    def analysis_course_grades(self):
        school_year_term = input("Please enter the term name:")
        course_name = input("Please enter the course name:")
        acg.analysis_course_grades(school_year_term, course_name)

    def analysis_student_grades(self):
        name = input("Please enter your name:")
        asg.analysis_student_grades(name)

    def student_report_export(self, data):
        string = input("Please enter the student name or student ID:")
        category = input("Please enter the category(\'name\'or\'id\'):")
        rfe.student_report_export(data, category, string)

    def course_report_export(self, data):
        semester = input("Please enter the semester:")
        string = input("Please enter the course name or number:")
        category = input("Please enter the category(\'course_name\'or\'course_number\'):")
        rfe.course_report_export(data, semester, category, string)

    def add_advise(self):
        course_name = input("Please enter the course name:")
        ad.add_advise(course_name)

    def get_advise(self):
        course_name = input("Please enter the course name:")
        ad.get_advise(course_name)

    def teacher_print_in_xlsx(self):
        category = input("Please enter the category(\'name\'or\'id\'):")
        str = input("Please enter the str:")
        chart.print_in_xlsx(category, str)

    def print_in_xlsx(self, str):
        chart.print_in_xlsx("id", str)


class NumberInvalidError(Exception):  # the exception class
    def __init__(self, data):
        Exception.__init__(self, data)
        self.data = data

    def __str__(self):
        return self.data+"is a invalid number.Please input again."


def input_ac(tstr):
    try:
        ac = int(input(tstr))
        return ac
    except ValueError:
        print("Invalid choice,please enter again.")
        return input_ac(tstr)


studentTip = ("Enter 0 to exit,1 to get grades report,2 to print grades in xlsx,3 to see analyse grades,"
              "4 to get course advise 5 to provide feedback on the program 6 to logout:")
teacherTip = ("Enter 0 to exit,1 to see analyse grades,"
              "2 to get grades report,"
              "3 to print grades in xlsx,"
              "4 to enter grades,"
              "5 to modify grades,"
              "6 to delete grades, "
              "7 to write course advise "
              "8 to provide feedback on the program"
              "9 to logout:")


def student_login(aID):
    ac = input_ac(studentTip)
    data = fo.import_data('grades.txt')
    while ac != 0:
        try:
            if ac == 0:
                break
            elif ac == 1:
                m.student_report_export(aID)
            elif ac == 2:
                m.print_in_xlsx(aID)
            elif ac == 3:
                m.analysis_student_grades()
            elif ac == 4:
                m.get_advise()
            elif ac == 5:
                feedback.export_feedback('student')
            elif ac == 6:
                print("Logout succeed.")
                ac, aID = login.login_access()
                if ac == -1:
                    return
                elif aID != "teacher":
                    student_login(aID)
                elif aID == "teacher":
                    teacher_login()
            else:
                raise NumberInvalidError(str(ac))
        except NumberInvalidError or ValueError:
            print("Invalid choice,please enter again.")
        finally:
            ac = input_ac(studentTip)


def teacher_login():
    ac = input_ac(teacherTip)
    data = fo.import_data('grades.txt')
    while ac != 0:
        try:
            if ac == 0:
                break
            elif ac == 1:
                m.analysis_course_grades()
            elif ac == 2:
                m.course_report_export(data)
            elif ac == 3:
                m.teacher_print_in_xlsx()
            elif ac == 4:
                m.enter_student_grades()
            elif ac == 5:
                mg.modify_grades()
            elif ac == 6:
                dg.delete_grades()
            elif ac == 7:
                m.add_advise()
            elif ac == 8:
                feedback.export_feedback('teacher')
            elif ac == 9:
                print("Logout succeed.")
                ac, aID = login.login_access()
                if ac == -1:
                    return
                elif aID != "teacher":
                    student_login(aID)
                elif aID == "teacher":
                    teacher_login()
            else:
                raise NumberInvalidError(str(ac))
        except NumberInvalidError:
            print("Invalid choice,please enter again.")
        finally:
            ac = input_ac(teacherTip)


if __name__ == "__main__":
    m = Marks()
    ac, aID = login.login_access()
    if ac == 1 and aID != "teacher":  # 学生
        student_login(aID)
    elif ac == 1 and aID == "teacher":  # 老师
        teacher_login()
    print("Thanks for using.Goodbye.")
