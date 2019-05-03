from werkzeug.security import generate_password_hash, check_password_hash


def enPassWord(password):  # 将明密码转化为hash码
    return generate_password_hash(password)  # 返回转换的hash码


def checkPassWord(enpassword, password):  # 第一参数是从数据查询出来的hash值，第二参数是需要检验的密码
    return check_password_hash(enpassword, password)  # 如果匹配返回true
