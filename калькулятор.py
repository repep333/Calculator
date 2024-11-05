import tkinter
window=tkinter.Tk()
window.title("мой калькулятор")
window.geometry("300x300")
window.configure(bg="pink")

def get_num1():
    num1=text_num1.get()
    num1=int(num1)
    return num1
    
def get_num2():
    num2=text_num2.get()
    num2=int(num2)
    return num2

def get_num(text_num):
    num=text_num.get()
    num=int(num)
    return num

def set_answer(result):
    text_ans.delete(0,"end")
    text_ans.insert(0,result)


def add():
    num1=get_num(text_num1)
    num2=get_num(text_num2)
    #print("выполняем сложение")
    #num1=text_num1.get()
    #num1=int(num1)
    #print(num1)
    #num2=text_num2.get()
    #num2=int(num2)
    #print(num2)
    result=num1+num2
    #print(result)
    #text_ans.delete(0,"end")
    #text_ans.insert(0,result)
    set_answer(result)

def sub():
    num1=get_num(text_num1)
    num2=get_num(text_num2)
    #print("выполняем вычитание")
    #num1=text_num1.get()
    #num1=int(num1)
    #print(num1)
    #num2=text_num2.get()
    #num2=int(num2)
    #print(num2)
    result=num1-num2
    #print(result)
    #text_ans.delete(0,"end")
    #text_ans.insert(0,result)
    set_answer(result)

def mult():
    num1=get_num(text_num1)
    num2=get_num(text_num2)
    #print("выполняем умножение")
    #num1=text_num1.get()
    #num1=int(num1)
    #print(num1)
    #num2=text_num2.get()
    #num2=int(num2)
    #print(num2)
    result=num1*num2
    #print(result)
    #text_ans.delete(0,"end")
    #text_ans.insert(0,result)
    set_answer(result)

def div():
    num1=get_num(text_num1)
    num2=get_num(text_num2)
    #print("выполняем деление")
    #num1=text_num1.get()
    #num1=int(num1)
    #print(num1)
    #num2=text_num2.get()
    #num2=int(num2)
    #print(num2)
    result=num1/num2
    #print(result)
    #text_ans.delete(0,"end")
    #text_ans.insert(0,result)
    set_answer(result)
button_add=tkinter.Button(window,text="+",command=add,width=7,height=2,bg="white")
button_add.place(x=95,y=110)
button_sub=tkinter.Button(window,text="-",command=sub,width=7,height=2,bg="white")
button_sub.place(x=150,y=110)
button_mult=tkinter.Button(window,text="*",command=mult,width=7,height=2,bg="white")
button_mult.place(x=95,y=150)
button_div=tkinter.Button(window,text="/",command=div,width=7,height=2,bg="white")
button_div.place(x=150,y=150)
text_num1=tkinter.Entry(window,width=20)
text_num1.place(x=95,y=40)
text_num2=tkinter.Entry(window,width=20)
text_num2.place(x=95,y=80)
text_ans=tkinter.Entry(window,width=20)
text_ans.place(x=95,y=210)
label_num1=tkinter.Label(window,text="ввидите первое число",bg="pink")
label_num1.place(x=95,y=20)
label_num2=tkinter.Label(window,text="ввидите второе число",bg="pink")
label_num2.place(x=95,y=60)
label_ans=tkinter.Label(window,text="ответ",bg="pink")
label_ans.place(x=95,y=190)
window.mainloop()
