import file_operations as fo
import json


def add_advise(course_name):
    """为课程添加建议，如果原有建议则先输出原来的建议，然后将读入的建议加在原建议后面"""
    try:
        with open('advise.txt', 'r', encoding='utf-8') as f:
            advises = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        advises = {}
    advise_list = []
    if course_name in advises:
        print("%s原有建议为：" % course_name)
        for advise in advises[course_name]:
            print(advise)
    print("Please input learning suggestions for %s (Enter quit to exit):" % course_name)
    while True:
        advise = input()
        if advise == 'quit':
            break
        advise_list.append(advise)
    if course_name in advises:
        advises[course_name] += advise_list
    else:
        advises[course_name] = advise_list
    fo.export_data('advise.txt', advises)
    print("The relevant suggestions have been saved.\n")


def get_advise(course_name):
    """获取某门课的建议，如果老师没有录入就展示通用建议"""
    advises = fo.import_data('advise.txt')
    if course_name in advises:
        print("%s老师建议：" % course_name)
        for advise in advises[course_name]:
            print(advise)
    else:
        print("The teacher of course %s did not provide corresponding suggestions" % course_name)
        print("Perhaps the following suggestions can help you")
        print("1.制定合理的学习计划：合理规划时间，制定目标，每天保持学习时间和学习内容的规律性。\n"
              "2.改进学习方法：探索适合自己的学习方法，例如学习笔记的制作、课堂笔记的整理、教材阅读与理解等。"
              "3.多角度学习：通过多种途径获取知识，例如参加课外培训、参加讲座、阅读相关书籍、使用互联网资源等。\n"
              "4.积极参与课堂互动：积极提问、回答问题，与老师和同学进行交流沟通，加深对知识的理解。\n"
              "5.做好课后作业：认真对待每一次的课后作业，注重细节，注意错误的纠正。\n"
              "6.多做题、做模拟试卷：通过多做题、做模拟试卷检验自己的掌握程度，并及时总结错题和不懂的知识点。\n"
              "7.寻求他人帮助：与老师、同学或家长沟通，寻求他们的帮助和指导，共同探讨问题，找出解决的方法。\n"
              "8.积极参加相关测评：及时了解自己的学习成果，总结自己的不足，发现问题并及时改进。\n")
    return


if __name__ == "__main__":
    add_advise('信息安全导论')
    get_advise('信息安全导论')
    get_advise('aaaa')
