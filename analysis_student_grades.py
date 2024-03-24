import report_find_export as rfe
import file_operations as fo
import exception_and_read as er
import advise as ad


def analysis_student_grades(name):
    """分析学生成绩"""
    data = fo.import_data('grades.txt')
    scores = rfe.find_student_report(data, 'name', name)
    unqualified_courses = []
    weak_courses = []
    strong_courses = []
    deferred_courses = []
    for score in scores:
        if score['student_info']['pass_or_not'] == '否':
            if score['student_info']['special_reasons'] == '缓考':
                deferred_courses.append((score['course_info']['course_name'], score['student_info']['score']))
            else:
                unqualified_courses.append((score['course_info']['course_name'], score['student_info']['score']))
        elif score['student_info']['score'] > 90:
            strong_courses.append((score['course_info']['course_name'], score['student_info']['score']))
        else:
            weak_courses.append((score['course_info']['course_name'], score['student_info']['score']))

    if deferred_courses:
        print("The postponed courses include：")
        for course, grade in deferred_courses:
            print("%s（成绩：%.2f）" % (course, grade))
        print('Suggestion:\n'
              'Carefully prepare for relevant subjects, apply and participate in exams on time\n')

    if unqualified_courses:
        print("Unqualified courses include：")
        for course, grade in unqualified_courses:
            print("%s（成绩：%.2f）" % (course, grade))
        print('Suggestion:\n'
              '1.Carefully analyze the reasons for the unqualified courses,\n'
              ' whether it is due to improper learning attitude, lack of interest, improper learning methods, etc.\n'
              '2.Actively communicate with teachers, seek help and solutions.\n'
              '3.Develop corresponding learning plans to strengthen the learning and understanding of these course '
              'contents.\n'
              '4.Pay attention to the evaluation standards for homework,'
              ' exams, and other aspects, strive to overcome difficulties, and improve grades.\n'
              '5.Pay attention to the timing of make-up exams and take them on time.\n')

    if weak_courses:
        print("The courses that need improvement include：")
        for course, grade in weak_courses:
            print("%s（成绩：%.2f）" % (course, grade))
        print('Suggestion:\n'
              'There is still room for improvement in these subjects, '
              'and you can improve your grades through hard work and improvement.\n '
              'For example, developing a reasonable learning plan, '
              'participating more in classroom interactions, '
              'and seeking additional learning resources for learning\n')

    if strong_courses:
        print("Advantage subjects include：")
        for course, grade in strong_courses:
            print("%s（成绩：%.2f）" % (course, grade))
        print('Suggestion:\n'
              'You have achieved certain grades in these courses,'
              ' and you can maintain the status quo '
              'while further exploring and developing your potential.\n '
              'If you are interested, '
              'you can delve into the cutting-edge knowledge '
              'and related applications in this field to broaden your knowledge.\n')
    print("If specific subject suggestions are needed, you can press 1; otherwise, press 2")
    choice = er.read_choice([1, 2])
    if choice == 1:
        print("请提出想要查询的科目（输入 'quit' 退出）")
        while True:
            course_name = input()
            if course_name == 'quit':
                break
            ad.get_advise(course_name)


if __name__ == "__main__":
    analysis_student_grades('张三')
