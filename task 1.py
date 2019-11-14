import re
print("Юлія Артурівна \nЛабораторна робота №5 \nВаріант 13 \nСтворити список ключів і список значень, і виконати операції з ними")
keys=[]
values=[]
main_list=[]
re_answy=re.compile("\s{0,}y\s{0,}$")#comparing with tamplate func
re_answn=re.compile("\s{0,}n\s{0,}$")
inp_n=re.compile("\s{0,}[+]?\d{0,}\s{0,}$")#index,int
inp_x=re.compile("\s{0,}[-+]?[0-9]*\.?[0-9]*\s{0,}$")#float +-

def validation(text, pattern): #matches text and pattern, returns true/false
    return bool(pattern.match(text))

def ans():
    answer=input("Do you want to continue(y/n)?")
    if validation(answer, re_answy):
        keys.clear()
        main_list.clear()
        values.clear()
        average_val()
    elif validation(answer, re_answn):
        print("Bye")
    else:
        print("You entered incorrect symbol, choose y or n")
        ans()


def index():
    n=input("Enter the integer value n, that >=1:")
    if validation(n, inp_n):
        n=int(n)
        if n<1:
            print("You entered a wrong symbol. Try again.")
            del n
            n=index()
    else:
        print("You entered incorrect input. Try again.")
        del n
        n=index()
    return n

elem = 0
def val_key():
    print("Enter a key for the ", elem + 1, " element:")
    key = input()
    if key == " " or "":
        print("Incorrect value, try again.")
        val_key()
        average_val()
    else:
        keys.append(key)
    return key

def val_val():
    print("Enter a value for the ", elem + 1, " element:")
    value = input()
    if value == " " or "":
        print("Incorrect value, try again.")
        val_val()
    elif validation(value, inp_x):
        value=float(value)
        values.append(value)
    else:
        print("Incorrect value, try again.")
        val_val()
    return value

def calculating():
    na = index()
    for elem in range(na):
        key= val_key()
        value= val_val()
        main_list.append([key, value])
    print(main_list)

def average_val():
    calculating()
    elem=0
    count=0
    for element in values:
        element=float(element)
        elem+= element
        count+=1
    average=elem/count
    print(average)
    ans()

average_val()

