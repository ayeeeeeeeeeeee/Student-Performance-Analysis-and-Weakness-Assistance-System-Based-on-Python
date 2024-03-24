import file_operations as fo


class Score:
    def __init__(self, semester, course_info, student_info):
        self.semester = semester
        self.course_info = course_info
        self.student_info = student_info

    def to_dict(self):
        return {
            'semester': self.semester,
            'course_info': self.course_info,
            'student_info': self.student_info
        }


def find_student_report(data, category, string):
    """输入学生姓名或学号，返回该生所有课程的成绩列表。"""
    scores = []
    for grades in data:
        for course in grades['courses']:
            for student in course['student_info']:
                if student[category] == string:
                    score = Score(grades['semester'],
                                  course['course_info'], student)
                    scores.append(score.to_dict())
                    break
    return scores


def student_report_export(data, category, string):
    """输入学生姓名或学号，导出该生所有课程的成绩列表。"""
    scores = find_student_report(data, category, string)
    if not scores:
        print("This student doesn't have grades!")
    else:
        filename = scores[0]['student_info']['id'] + \
            scores[0]['student_info']['name'] + '.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            keys_line = ('课程名 课程号 课程类别 课程性质 学分 学时 考试日期 成绩类型 考试类型 开课单位 '
                         '总成绩 是否主修 GPA 重修重考 是否及格 特殊原因\n')
            f.write(keys_line)
            for course in scores:
                values_line = course["semester"] + ' '
                for course_info in course["course_info"]:
                    values_line += str(course["course_info"][course_info]) + ' '
                for student_info in course["student_info"]:
                    if student_info != 'name' and student_info != 'id':
                        values_line += str(course["student_info"][student_info]) + ' '
                values_line += '\n'
                f.write(values_line)


def find_course_report(data, semester, category, string):
    """输入学期，课程名或编号，返回该课程的信息和该科目所有学生成绩。"""
    for grades in data:
        if grades["semester"] == semester:
            for course in grades['courses']:
                if course["course_info"][category] == string:
                    score = Score(semester, course["course_info"], course["student_info"])
                    return score.to_dict()
    return []


def course_report_export(data, semester, category, string):
    """输入学期，课程名或编号，导出该课程的信息和该科目所有学生成绩。"""
    course = find_course_report(data, semester, category, string)
    if not course:
        print("This course does not exist!")
    else:
        filename = course['course_info']['course_name'] + '.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            keys_line = '学年学期 课程名 课程号 课程类别 课程性质 学分 学时 考试日期 成绩类型 考试类型 开课单位\n'
            f.write(keys_line)
            values_line = semester + ' '
            for course_info in course["course_info"]:
                values_line += str(course["course_info"][course_info]) + ' '
            values_line += '\n'
            f.write(values_line)
            keys_line = '姓名 学号 总成绩 是否主修 GPA 重修重考 是否及格 特殊原因\n'
            f.write(keys_line)
            for student_info in course["student_info"]:
                values_line = ''
                for info in student_info:
                    values_line += str(student_info[info]) + ' '
                values_line += '\n'
                f.write(values_line)
    return


if __name__ == "__main__":
    filedata = fo.import_data('grades.txt')
    student_report_export(filedata, 'name', '张三')
    course_report_export(filedata, "2022-2023学年,第1学期", 'course_name', "信息安全导论")
