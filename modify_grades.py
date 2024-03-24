import file_operations as fo
import report_find_export as rfe
import exception_and_read as er


def display_tips(info):
    """显示提示信息菜单“”“
    ”“”其中info是一个字典，key为提示信息序号，value为具体提示信息"""
    tips = ''
    for key, value in info.items():
        tips += str(key) + '.' + value + ' '
        if key % 5 == 0 or key == len(info):
            print(tips)
            tips = ''
    return


def modify_grades():
    """修改信息:1.学年学期信息 2.某个课程的信息 3.某个学生的信息"""
    data = fo.import_data('grades.txt')

    print("What information do you want to modify?")
    print("1. Academic year and semester information")
    print("2. Course information")
    print("3. Student information")
    category_choice = er.read_choice([1, 2, 3])

    semester = input("Please enter the academic year and semester:")
    semester_index = -1
    for i, grades in enumerate(data):
        if grades['semester'] == semester:
            semester_index = i
    if semester_index == -1:
        print("This academic year and semester does not exist!")
        return
    if category_choice == 1:
        number = 1
    else:
        number = er.read_int_number("Please enter the number of courses you want to modify:")

    course_key = {1: 'course_name', 2: 'course_number', 3: 'course_category', 4: 'course_type', 5: 'credit',
                  6: 'class_hour', 7: 'test_date', 8: 'grade_type', 9: 'exam_type', 10: 'teaching_unit'}
    student_key = {1: 'name', 2: 'id', 3: 'score', 4: 'major', 5: 'gpa',
                   6: 'retake', 7: 'pass_or_not', 8: 'special_reasons'}

    course_number = 0
    while course_number != number:
        if category_choice == 1:
            new_semester = input("Please enter new academic year and semester information:")
            data[semester_index]['semester'] = new_semester
            break
        else:
            course_number += 1
            course_string = input("Please enter the course name or number of course %d:" % course_number)
            print("Please enter the category:1. Course Name 2. Course Number")
            choice = er.read_choice([1, 2])
            course_category = course_key[choice]
            course = rfe.find_course_report(data, semester, course_category, course_string)
            if not course:
                print("This course does not exist!")
            else:
                if category_choice == 2:
                    category_num = er.read_int_number("Please enter the number of categories you want to modify:")
                    category_number = 0
                    show_tips = True
                    while category_number != category_num:
                        category_number += 1
                        print("Please enter the category%d you want to modify:" % category_number)
                        if show_tips:
                            display_tips(course_key)
                            show_tips = False
                        choice = er.read_choice(course_key.keys())
                        category = course_key[choice]
                        string = input("Please enter the updated information:")
                        for course_info in course["course_info"]:
                            if course_info == category:
                                course["course_info"][course_info] = string
                                break
                else:
                    student_num = er.read_int_number("Please enter the number of students you want to modify:")
                    student_number = 0
                    while student_number != student_num:
                        student_number += 1
                        student_string = input("Please enter the student name or student ID of student "
                                               "%d:" % student_number)
                        print("Please enter the category:1. Student name 2. Student ID")
                        choice = er.read_choice([1, 2])
                        student_category = student_key[choice]
                        find = False
                        show_tips = True
                        for student in course["student_info"]:
                            if student[student_category] == student_string:
                                category_num = er.read_int_number(
                                    "Please enter the number of categories you want to modify:")
                                category_number = 0
                                while category_number != category_num:
                                    category_number += 1
                                    print("Please enter the category%d you want to modify:" % category_number)
                                    if show_tips:
                                        display_tips(student_key)
                                        show_tips = False
                                    choice = er.read_choice(student_key.keys())
                                    category = student_key[choice]
                                    string = input("Please enter the updated information:")
                                    student[category] = string
                                    find = True
                                break
                        if not find:
                            print("This student doesn't have grades!")

    fo.export_data('grades.txt', data)
    print("Relevant information has been modified.")


if __name__ == "__main__":
    modify_grades()

