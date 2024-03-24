import file_operations as fo

if __name__ == "__main__":
    tmpDict = {}
    teaPwd = input("Please input the teacher password:")
    tmpDict["teacher"] = teaPwd
    n = int(input("Please input the number of students:"))
    for i in range(n):
        tmpid = input("Please input the id of student"+str(i+1)+":")
        tmpwd = input("Please input the pwd of student"+str(i+1)+":")
        tmpDict[tmpid] = tmpwd
    fo.export_data('pwd.txt', tmpDict)
    print("Succeed.")
