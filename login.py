import getpass
import file_operations as fo


def login_access():
    """用于身份登录，使用了密码隐藏。\n
    返回1和id：登录成功，-1：错密3次登录失败"""
    pwdict = fo.import_data("pwd.txt")

    idTmp = input("Please enter your id:")
    idExist = False
    while (not idExist):
        for i in pwdict:
            if (i == idTmp):
                idExist = True
                pwdTmp = getpass.getpass(
                    "Please enter your identity password:")
                break
        if (not idExist):
            idTmp = input("Id doesn't exist.Please enter again:")

    failTime = 3
    while (failTime > 0):
        if (pwdTmp == pwdict[idTmp]):
            print("Welcome,"+idTmp+".")
            return 1, idTmp
        elif (failTime > 0):
            print("Wrong password, "+str(failTime)+" chance last.")
            failTime -= 1
            pwdTmp = getpass.getpass("Please enter your identity password:")
    print("Wrong password, login failed.")
    return -1, -1


if __name__ == "__main__":
    print(login_access())
