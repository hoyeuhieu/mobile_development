from tkinter import *
window = Tk()
window.title('My Caculator')
buttons = [['2nd', 'Pi', 'e', 'C', "X"], ['x^2', '1/x', '|x|', 'exp', 'mod'], ['abs', '(',')', 'n!', '/'], ['x^y', '7', '8', '9', 'x'], ['10^x', '4', '5', '6', '-'], ['log', '1', '2', '3', '+'], ['ln', '+/-', '0', '.', '=']]
finish = False
def on_btn_clicked(ch):
    return lambda: on_click(ch)
def on_click(ch):
    global finish
    if ch == 'C':
        on_btn_clear_clicked()
    elif ch == '=':
        on_btn_equal_clicked()
    elif ch == '%':
        on_btn_percent_clicked()
    else:
        res = display.get()
        if (len(display.get()) == 1 and display.get() == '0' and not ch in '+-*/^') or \
                (not display.get() == 'ERROR' and finish == 1 and ch not in '+-*/^') or display.get() == 'ERROR':
            display.delete(0, END)
        if res == 'ERROR':
            if ch not in '+-*/^':
                display.insert(len(display.get()), ch)
                finish = False
            else:
                display.insert(len(display.get()), '0')
        else:
            display.insert(len(display.get()), ch)
            finish = False
def on_btn_clear_clicked():
    global finish
    if finish:
        display.delete(0, END)
        display.insert(0, 0)
    else:
        display.delete(len(display.get()) - 1)
def on_btn_equal_clicked():
    global finish
    try:
        text = display.get()
        print(text)
        label.config(text = text, justify= 'right')
        true_number_sentance = text.replace('^', '**')
        res = eval(true_number_sentance)
    except Exception:
        res = 'ERROR'
    display.delete(0, END)
    display.insert(0, res)
    finish = True
def on_btn_percent_clicked():
    global finish
    res = float(display.get()) / 100
    display.delete(0, END)
    display.insert(0, res)
    finish = True
def defind_buttons(buttons):
    row_d = 1
    for i in range(len(buttons)):
        column_d = 0
        for j in (buttons[i]):
            btn = Button(window, text = j, font = ('Tahoma', 20), command = on_btn_clicked(j))
            btn.grid(row=row_d + 1, column=column_d, sticky = 'nesw', padx = 5, pady = 5)
            column_d += 1
        row_d += 1


display = Entry(window, font = ('Tahoma', 20), width = 30, justify = 'right')
display.grid(row = 1, column = 0, columnspan=5, padx = 5, pady = 5)
label = Label(window, font = ('Tahoma', 20), width = 30, anchor='e', fg='gray')
label.grid(row = 0, column = 0, columnspan=5, padx = 5, pady = 5)
defind_buttons(buttons)

window.mainloop()