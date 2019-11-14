import re
print("Надь Юлія Артурівна \nЛабораторна робота №5 \nВаріант 13 \n Виконати операцію з множинами\n")
re_answy=re.compile("\s{0,}y\s{0,}$")#comparing with tamplate func
re_answn=re.compile("\s{0,}n\s{0,}$")
def validation(text, pattern): #matches text and pattern, returns true/false
    return bool(pattern.match(text))
def ans():
    answer=input("Do you want to continue(y/n)?")
    if validation(answer, re_answy):
        main_func()
    elif validation(answer, re_answn):
        print("Bye")
    else:
        print("You entered incorrect symbol, choose y or n")
        ans()
def main_func():
    A={1,2,'ee','ww','c','d'}
    B = {2,'a','b','tt',1,3}
    K=A.symmetric_difference(B)
    L=A.difference(B)
    F=K.intersection(L)
    print(F)
    ans()

main_func()