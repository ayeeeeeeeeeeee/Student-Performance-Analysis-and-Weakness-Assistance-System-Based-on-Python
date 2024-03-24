import file_operations as fo
import exception_and_read as er


def delete_grades():
    """删除成绩：
    1.删除某学年某学期所有内容
    2.删除某个课程所有内容
    3.某个课程中的某学生的全部信息
    4.某个学生所有信息
"""
    data = fo.import_data('grades.txt')

    print("What information do you want to delete?")
    print("1. All content for a academic year and semester information")
    print("2. All content of a certain course")
    print("3. All information about a student in a certain course")
    print("4. All information of a certain student")
    delete_choice = er.read_choice([1, 2, 3, 4])
    fo.export_data('grades.txt', data)

    course_key = {1: 'course_name', 2: 'course_number'}
    student_key = {1: 'name', 2: 'id'}

    if delete_choice != 4:
        semester = input("Please enter the academic year and semester:")
        semester_index = -1
        courses_data = None
        for index, semesters in enumerate(data):
            if semesters['semester'] == semester:
                semester_index = index
                courses_data = data[index]['courses']
                break
        if semester_index == -1:
            print("This academic year and semester does not exist!")
            return

        if delete_choice == 1:
            del data[semester_index]
            print("Relevant information has been deleted.")
        else:
            course_num = er.read_int_number("Please enter the number of courses you want to delete:")
            course_number = 0
            while course_number != course_num:
                course_number += 1
                course_string = input("Please enter the course name or number of course %d:" % course_number)
                print("Please enter the category:1. Course Name 2. Course Number")
                choice = er.read_choice([1, 2])
                course_category = course_key[choice]
                course_index = -1
                course_data = None
                for index, course in enumerate(courses_data):
                    if course["course_info"][course_category] == course_string:
                        course_index = index
                        course_data = course
                        break
                if course_index == -1:
                    print("This course does not exist!")
                else:
                    if delete_choice == 2:
                        del data[semester_index]['courses'][course_index]
                        print("Relevant information has been deleted.")
                    elif delete_choice == 3:
                        student_num = er.read_int_number("Please enter the number of students you want to delete:")
                        student_number = 0
                        while student_number != student_num:
                            student_number += 1
                            student_string = input("Please enter the student name or student ID of student "
                                                   "%d:" % student_number)
                            print("Please enter the category:1. Student name 2. Student ID")
                            choice = er.read_choice([1, 2])
                            student_category = student_key[choice]
                            find = False
                            for index, student in enumerate(course_data['student_info']):
                                if student[student_category] == student_string:
                                    del data[semester_index]['courses'][course_index]['student_info'][index]
                                    find = True
                                    break
                            if not find:
                                print("This student doesn't have this grade!")
    else:
        student_num = er.read_int_number("Please enter the number of students you want to delete:")
        student_number = 0
        while student_number != student_num:
            student_number += 1
            student_string = input("Please enter the student name or student ID of student "
                                   "%d:" % student_number)
            print("Please enter the category:1. Student name 2. Student ID")
            choice = er.read_choice([1, 2])
            student_category = student_key[choice]
            find = False
            for semester_index, grades in enumerate(data):
                for course_index, course in enumerate(grades['courses']):
                    for student_index, student in enumerate(course['student_info']):
                        if student[student_category] == student_string:
                            del data[semester_index]['courses'][course_index]['student_info'][student_index]
                            find = True
                            break
            if find:
                print("Relevant information has been deleted.")
            else:
                print("This student doesn't have grade!")

    fo.export_data('grades.txt', data)
    return


if __name__ == "__main__":
    delete_grades()
