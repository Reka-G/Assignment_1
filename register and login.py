import re
global email
global password
global c
c=0
def check(us1):#chceking email id present in file or not
    db = open("register.txt", "r")
    d = []
    f = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        d.append(a)
        f.append(b)
        data = dict(zip(d,f))
    if us1 not in data:
        return 1

    else:
        print("user name exist")
        print("try again")
        mail()

def p_word():#passsword validation
    def up(s):
        for i in range(len(s)):
            if s[i].isalpha():
                if s[i].isupper():
                    return 1

    def low(s):
        for i in range(len(s)):
            if s[i].isalpha():
                if s[i].islower():
                    return 1

    def digit(s):
        for i in range(len(s)):
            if s[i].isdigit():
                return 1

    def run(s):
        regex = re.compile('[@_!#$%^&*()<>?/{}~:;`\.,]')
        if (regex.search(s) == None):
            return 0
        else:
            return 1

    password = input("Enter your password")
    password2=input("confirm your password")
    lenghtpw = len(password)
    if lenghtpw > 5 and lenghtpw < 16:
        if up(password) == 1:
            if low(password) == 1:
                if run(password) == 1:
                    if digit(password) == 1:
                        if password==password2:
                            print("password created successfully")
                            return password
                        else:
                            print("password mismatch")
                            p_word()
                    else:
                        print("minimum one digit required,try again")
                        p_word()
                else:
                    print("minimum one special character required,try again")
                    p_word()
            else:
                print("minimum one lowercase required,try again")
                p_word()
        else:
            print("minimum one uppercase Required,try again")
            p_word()
    else:
        print("password must 5 to 16 lenght,try again")
        p_word()
def spw(p,u):#append mail id and password to file
    f = open("register.txt", "a")
    f.writelines(p+","+u+"\n")
    f.close()
def mail():#email validation
    email = input("Enter Email Id")
    if '@' and '.' in email:
        index1 = (email.index('@'))  # 8
        if email[index1 + 1] != '.':
            if email[0].islower():
                if email[0].isalpha():
                    if check(email)==1:
                        return email
                        print("set mail id successfully")
                        #global s_id
                        #s_id=email
                else:
                    print("Invalid Username\tTry again")
                    mail()
            else:
                print("Invalid Username\tTry again")
                mail()
        else:
            print("Invalid Username\tTry again")
            mail()
    else:
        print("Invalid Username\tTry again")
        mail()
def register():#registertaion process
    print("register")
    email1 = mail()
    password1 = p_word()
    spw(email1,password1)
    print("successfully registered")
def d(s):#chcek mail id in file
    db=open("register.txt","r")
    d=[]
    f=[]
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        d.append(a)
        f.append(b)
        data = dict(zip(d, f))
    if s not in data:
        print("username not found press 1 to register")
        r1=int(input())
        if r1==1:
            register()
    else:
        n=1
        while n<4:
            passcode=input("enter your password")
            if passcode==data[s]:
                print("login successfully")
                break
            else:
                print("try again",n)
                n+=1
        if n==4:
            print("failed 3 times press 1 to retrieve your password")
            fpw=int(input())
            if fpw==1:
                checkmail=input("enter your mail and get your password")
                if checkmail==s:
                    print("your password=",data[s])
#driver code
print("1.Register\n2.Login")
a = int(input())
if a == 1:
    register()
elif a == 2:
    print("Login")
    lin=input("Enter mail id:")
    d(lin)

