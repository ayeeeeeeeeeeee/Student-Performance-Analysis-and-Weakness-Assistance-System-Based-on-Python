import xlwings as xw
import file_operations as fo


def student_report_export(category, string):
    """输入学生姓名或学号，返回该生所有课程的名字和成绩。"""
    gradesDict = {}
    data = fo.import_data('grades.txt')
    for grades in data:
        for course in grades['courses']:
            for student in course['student_info']:
                if student[category] == string:
                    gradesDict[grades['semester']+course['course_info']
                               ['course_name']] = student['score']
                    break
    if not gradesDict:
        print("This student doesn't have grades!")
    else:
        return gradesDict


def print_in_xlsx(category, string):
    """用来把成绩打印在excel并生成柱形图"""
    app = xw.App(visible=True, add_book=False)
    workbook = app.books.add()
    data = student_report_export(category, string)

    sheet1 = workbook.sheets["sheet1"]

    sheet1.range('A1').value = "课程名"
    sheet1.range('B1').value = "成绩"

    indTmp = 2

    for i in data:
        sheet1.range('A'+str(indTmp)).value = i
        sheet1.range('B'+str(indTmp)).value = data[i]
        indTmp += 1

    chart = sheet1.charts.add(left=200, top=0, width=384, height=216)
    chart.set_source_data(sheet1['A1'].expand())
    chart.chart_type = 'column_clustered'

    workbook.save(string+'.xlsx')
    workbook.close()
    app.quit()


if __name__ == "__main__":
    print_in_xlsx('name', '张三')
