def collect_feedback():
    """收集用户意见"""
    feedback_list = []
    print("请提出您的意见（输入 'quit' 退出）：")
    while True:
        feedback = input()
        if feedback == 'quit':
            break
        feedback_list.append(feedback)
    return feedback_list


def export_feedback(user):
    """将用户意见导入文件"""
    feedback = collect_feedback()
    filename = 'feedback_'+user+'.txt'
    with open(filename, 'a', encoding='utf-8') as f:
        for string in feedback:
            f.write(string + '\n')
    print("意见已保存！")


if __name__ == "__main__":
    export_feedback('test')
