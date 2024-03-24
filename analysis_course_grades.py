import statistics
import file_operations as fo


def analysis_course_grades(school_year_term, course_name):
    """成绩统计：某一门课的成绩进行统计分析，输出其平均分、最高分、最低分和中位数。"""
    data = fo.import_data('grades.txt')
    scores = []
    for grades in data:
        if grades['semester'] == school_year_term:
            for course in grades['courses']:
                if course['course_info']['course_name'] == course_name:
                    for student in course['student_info']:
                        scores.append(student['score'])
                    break
            break
    if len(scores) > 0:
        average_grade = sum(scores) / len(scores)
        max_grade = max(scores)
        min_grade = min(scores)
        median_grade = statistics.median(scores)
        print("Analysis for course '%s %s':" % (school_year_term, course_name))
        print("Average grade: %.2f" % average_grade)
        print("Max grade: %s" % max_grade)
        print("Min grade: %s" % min_grade)
        print("Median grade: %s" % median_grade)
    else:
        print("No grades found for '%s %s':" % (school_year_term, course_name))


if __name__ == "__main__":
    analysis_course_grades("2022-2023学年,第1学期", "信息安全导论")
    analysis_course_grades("2022-2023学年,第2学期", "信息安全导论")
