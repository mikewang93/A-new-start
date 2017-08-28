import hashlib

def cal(password):
    string = hashlib.md5()
    string.update(password)
    st = string.hexdigest()

    db={
        'Mike':cal('Mike'),#123456
        'Leo':cal('Leo')#1234
        }

def login(user,password):
    pwd = hashlib.md5()
    pwd.update(str(password))
    pwdd = pwd.hexdigest()
    try:
        if db[str(user)] == pwdd:
            print "Login successfully"
        else:
            print "Something Wrong"

    except KeyError:
        print "usr or pwd wrong"

if __name__ == '__main__':
    login('Mike',123456)
