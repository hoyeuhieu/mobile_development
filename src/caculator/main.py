from constants import *
from tkinter import *
import math
expressions = []
index = 0

window = Tk()
window.title('My Caculator')
finish = False
buttons = [
    ['2nd', 'pi', 'e', 'C', "X"],
    ['^2', '1/x', 'abs', 'exp', 'mod'],
    ['sqrt', '(', ')', 'n!', '/'],
    ['x^y', '7', '8', '9', 'x'],
    ['10^x', '4', '5', '6', '-'],
    ['log', '1', '2', '3', '+'],
    ['ln', '+/-', '0', '.', '=']]


def transform(str, current, old, new):
    if(new == null or old == null or new == "" or old == ""):
        return str + current
    if(current == old):
        return str + new
    else:
        return str + current


def insertExpressions(ch):
    global expressions
    global index
    expressions.insert(index, ch)
    index += 1
    insert_display(ch)


def on_btn_clicked(ch):
    return lambda: on_click(ch)


def show_display():
    global expressions
    for i in range(len(expressions)):
        display.insert(i, expressions[i])

def remove_display():
    global index
    if index != 0:
        display.delete(index - 1, index)
    else:
        display.delete(0, END)
        display.insert(0, 0)


def insert_display(ch):
    global index
    global expressions
    if(index == 1):
        display.delete(0, END)
        display.insert(index, ch)
    else:
        display.insert(index, ch)
    print(expressions)


def clear_all():
    global expressions
    global index
    expressions = []
    index = 0
    display.delete(0, END)
    display.insert(0, 0)


def on_click(ch):
    global finish
    if ch == 'C':
        on_btn_clear_clicked()
    elif ch == '=':
        on_btn_equal_clicked()
    elif ch == 'X':
        clear_all()
    else:
        insertExpressions(ch)


def on_btn_clear_clicked():
    global finish
    global expressions
    global index
    if(index != 0):
        expressions.pop(index - 1)
        remove_display()
        index -= 1
    print(expressions)


def on_btn_equal_clicked():
    global finish
    global expressions

    try:
        temp = ""
        str_expressions = ""
        for i in expressions:
            str_expressions += i

        for e in default_variables:
            if(e.name in str_expressions):
                if(temp == ""):
                    temp = str_expressions.replace(e.name, e.value)
                else:
                    temp = temp.replace(e.name, e.value)
        if(temp == ""):
            if(str_expressions == ""):
                temp = "0"
            else:
                temp = str_expressions

        text = str_expressions
        label.config(text=text, justify='right')
        res = eval(temp)

    except Exception:
        res = 'ERROR'
    display.delete(0, END)
    display.insert(0, res)
    finish = True


# def on_btn_equal_clicked():
#     global finish
#     global expressions

#     try:
#         temp = ""
#         str_expressions = ""
#         temp_array = []
#         for variable in default_variables:
#             for i in expressions:
#                 i_temp = ""
#                 if(i == variable.name):
#                     i_temp = variable.value
#                 else:
#                     i_temp = i

#                 temp += i_temp
#                 temp_array.append(i)
#             str_expressions += i

#         print(temp)
#         print(temp_array)
#         text = str_expressions
#         label.config(text=text, justify='right')
#         res = eval(temp)
#     except Exception:
#         res = 'ERROR'
#     display.delete(0, END)
#     display.insert(0, res)
#     finish = True


def defind_buttons(buttons):
    row_d = 1
    for i in range(len(buttons)):
        column_d = 0
        for j in (buttons[i]):
            btn = Button(window, text=j, font=(
                'Tahoma', 20), command=on_btn_clicked(j))
            btn.grid(row=row_d + 1, column=column_d,
                     sticky='nesw', padx=5, pady=5)
            column_d += 1
        row_d += 1


display = Entry(window, font=('Tahoma', 20), width=30, justify='right')
display.grid(row=1, column=0, columnspan=5, padx=5, pady=5)
display.insert(0, 0)
label = Label(window, font=('Tahoma', 20), width=30, anchor='e', fg='gray')
label.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
defind_buttons(buttons)

window.mainloop()
