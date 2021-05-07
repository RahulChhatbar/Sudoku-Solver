from tkinter import *
import tkinter.font as font
import tkinter.messagebox
import copy
import webbrowser
import tkinter as tk

root = tk.Tk()  

root.iconbitmap('icon.ico')  

root.title('Sudoku Solver')

root.config(bg='black', cursor='sizing')

ques=[]

global_val = ''


def sudo_clearsc(ques, solve):
    global global_val
    for i in ques:
        for j in i:
            j['value'].config(state='normal')
            j['value'].delete(0, END)
    blacker(ques)
    solve.config(state='normal')
    ques[0][0]['value'].focus()
    global_val = False


def linker(event):
    webbrowser.open_new_tab('https://github.com/RahulChhatbar')


def validate(P):
    if len(P) == 0:
        return True
    elif len(P) == 1 and P.isdecimal() and 0 < int(P) < 10:
        return True
    else:
        return False


def blacker(ques):
    for i in range(9):
        for j in range(9):
            ques[i][j]['fg'] = 'black'
            ques[i][j]['value'].config(fg='black')



def rowCheck(ques,i):
    val = False
    for j in range(8):
        if ques[i][j]['value'].get():
            for k in range(j+1,9):
                if (ques[i][j]['value'].get() == ques[i][k]['value'].get()):
                    ques[i][j]['fg'] = 'red'
                    ques[i][j]['value'].config(fg='red')
                    ques[i][k]['fg'] = 'red'
                    ques[i][k]['value'].config(fg='red')
                    val = True
    if val:
        return False
    else:
        return True



def columnCheck(ques,j):
    val = False
    for i in range(8):
        if ques[i][j]['value'].get():
            for k in range(i+1,9):
                if (ques[i][j]['value'].get() == ques[k][j]['value'].get()):
                    ques[i][j]['fg'] = 'red'
                    ques[i][j]['value'].config(fg='red')
                    ques[k][j]['fg'] = 'red'
                    ques[k][j]['value'].config(fg='red')
                    val = True
    if val:
        return False
    else:
        return True



def boxCheck(ques, a):
    val = False
    quo = ((a//3)*3)
    rem = ((a%3)*3)
    for i in range(quo,quo+3):
        for j in range(rem,rem+3):
            if i==quo+2 and j==rem+2:
                continue
            if ques[i][j]['value'].get(): 
                for k in range(i, quo+3):
                    for l in range(rem, rem+3):
                        if k==i and l==j:
                            continue
                        if (ques[i][j]['value'].get() == ques[k][l]['value'].get()):
                            ques[i][j]['fg'] = 'red'
                            ques[i][j]['value'].config(fg='red')
                            ques[k][l]['fg'] = 'red'
                            ques[k][l]['value'].config(fg='red')
                            val = True
    if val:
        return False
    else:
        return True



def sudo_validate(ques):
    blacker(ques)
    global global_val
    rowval = True
    colval = True
    boxval = True
    for i in range(9):
        rowval = rowval and rowCheck(ques, i)
        colval = colval and columnCheck(ques, i)
        boxval = boxval and boxCheck(ques, i)
    if rowval and colval and boxval:
        print('True')
        Correct()
        global_val = True
    else:
        print('False')
        Error()
        global_val =  False



def Error():
    tkinter.messagebox.showinfo("Error!",  "Some of the values entered are wrong.")

def Correct():
    tkinter.messagebox.showinfo("Great Job!", "All the values entered are correct.")


def find(dc):
    for i in range(9):
        for j in range(9):
            if not dc[i][j]:
                return i, j
    return None, None


def row_validator(dc, k, i, j):
    val = False
    for x in range(9):
        if x == j:
            continue
        if k == dc[i][x]:
            val = True
    if val:
        return False
    else:
        return True


def column_validator(dc, k, i, j):
    val = False
    for y in range(9):
        if y == i:
            continue
        if k == dc[y][j]:
            val = True
    if val:
        return False
    else:
        return True


def box_validator(dc, k, i, j):
    val = False
    a = ((i//3)*3)
    b = ((j//3)*3)
    for x in range(a, a+3):
        for y in range(b, b+3):
            if x == i and y == j:
                continue
            if k == dc[x][y]:
                val = True
    if val:
        return False
    else:
        return True


def checker(dc, k, i, j):
    check1 = row_validator(dc, k, i, j)
    if check1:
        check2 = column_validator(dc, k, i, j)
        if check2:
            check3 = box_validator(dc, k, i, j)
            if check3:
                return True
            else: return False
        else: return False
    else: return False


def solution(dc):
    i, j = find(dc)
    if i == None and j == None:
        return True
    for k in range(1,10):
        flag = checker(dc, k, i, j)
        if flag:
            dc[i][j] = k
            if solution(dc):
                return True
            else:
                continue
    dc[i][j]=0
    return False


def ques_copy(ques):
    new_matrix = []
    for i in range(9):
        col = []
        for j in range(9):
            if ques[i][j]['value'].get():
                col.append(int(ques[i][j]['value'].get()))
            else:
                col.append(0)
        new_matrix.append(col)
    return new_matrix


def sudo_solve(ques, solve):
    if global_val:
        new_ques = ques_copy(ques)
        dc = copy.deepcopy(new_ques)
        if solution(dc):
            for i in range(9):
                for j in range(9):
                    if not new_ques[i][j]:
                        ques[i][j]['value'].insert(0, dc[i][j])
                        ques[i][j]['value'].config(disabledforeground='#00624A')
                    else:
                        ques[i][j]['value'].config(disabledforeground='black')
                    ques[i][j]['value'].config(state='disabled')
                    ques[i][j]['value'].config(bg=color(i, j))
                    ques[i][j]['bg'] = 'color(i, j)'
            solve.config(state="disabled")


def color(i, j):
    if i in range(0,3) or i in range (6,9):
        if j in range(0,3) or j in range(6,9):
            return '#fff'
        else:
            return '#B2BABB'
    else:
        if j in range(0,3) or j in range(6,9):
            return '#B2BABB'
        else:
            return '#fff'


vcmd = (root.register(validate), '%P')


boldFont = font.Font(family = 'Comic Sans MS', size = 9, weight = 'bold')


main_txt0 = Label(root, bd=5, text=' 1. Enter the values known ',bg='white',fg='blue', font=boldFont, relief='ridge')
main_txt0.grid(row = 0, column=0, columnspan = 9, padx=5, sticky='W', pady=5)
main_txt1 = Label(root, bd=5, text=' 2. First click on "Validate" to check if your input is correct ',bg='white',fg='blue', font=boldFont, relief='ridge')
main_txt1.grid(row = 1, column=0, columnspan = 9, padx=5, sticky='W', pady=2)
main_txt2 = Label(root, bd=5, text=' 3. If input is correct, then click on "Solve" ',bg='white',fg='blue', font=boldFont, relief='ridge')
main_txt2.grid(row = 2,column=0, columnspan = 9, padx=5, sticky='W', pady=5)
main_txt3 = Label(root, text='Made by: Rahul Chhatbar', font=boldFont, fg='red', cursor='hand2')
main_txt3.grid(row=0, column=0, columnspan=9, sticky='E', padx=5, pady=5)
main_txt3.bind("<ButtonRelease-1>", linker)


for i in range(9):
    col=[]
    for j in range(9):
        col.append({'value': Entry(root, name=str(i)+str(j), justify='center', bd=3, bg=color(i,j), width=3,text='', font = ("Comic Sans MS",15),
                            validate='key', validatecommand=vcmd, disabledbackground=color(i,j)), 
                        'bg': color(i,j),
                        'fg': 'black'})
        col[j]['value'].grid(row=i+3, column=j, ipady=6, padx=1, pady=1)
    ques.append(col)


boldFont1 = font.Font(family = 'Comic Sans MS', size = 10, weight = 'bold', underline=1)


solve = Button(bd=10, text='Solve', width=10, font = boldFont1, bg='blue', command=lambda:sudo_solve(ques, solve), fg='white')
solve.grid(column=6,row=12, columnspan=3, pady=3)


sudo_validator = Button(bd=10, text='Validate', width=10, font = boldFont1, command=lambda:sudo_validate(ques), bg='orange')
sudo_validator.grid(column=3,row=12, columnspan=3, pady=3)


clear = Button(bd=10, text='Reset', width=10, font=boldFont1, command=lambda:sudo_clearsc(ques, solve), bg='red', fg='white')
clear.grid(column=0,row=12, columnspan=3, pady=3)



root.update()
print(root.winfo_height())
print(root.winfo_width())

root.mainloop()