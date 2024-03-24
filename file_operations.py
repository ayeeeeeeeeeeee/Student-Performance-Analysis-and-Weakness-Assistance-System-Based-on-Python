import json


def import_data(filename):
    """导入成绩数据"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    return data


def export_data(filename, data):
    """导出成绩数据"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    export_data('1.txt', ["This is the data"])
    grades_data = import_data('1.txt')
    print(grades_data)


