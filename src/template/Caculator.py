from tkinter import *
import math
window = Tk()
window.title('My Caculator')

finish = False

# Ham onclick
def on_btn_clicked(ch):
    return lambda: on_click(ch)

def on_click(ch):
    global finish
    if ch == 'C' or ch == 'del':
        on_btn_clear_clicked()
    elif ch == '=':
        on_btn_equal_clicked()
    elif ch == '%':
        on_btn_percent_clicked()
    elif ch == "n!":
        on_btn_factorial_clicked()
    elif ch == 'π':
        on_btn_pi_clicked()
    elif ch == 'e':
        on_btn_e_clicked()
    elif ch == 'x\u00B2':
        on_btn_x_2_clicked()
    elif ch == '1⁄x':
        on_btn_1x_clicked()
    elif ch == 'mod':
        on_btn_mod_clicked()
    elif ch == 'sqrt':
        on_btn_sqrt_clicked()
    elif ch == '|x|':
        on_btn_abs_clicked()
    elif ch == '10\u02e3':
        on_btn_pow_x_clicked()
    elif ch == 'log':
        on_btn_log_clicked()
    elif ch == 'ln':
        on_btn_ln_clicked()
    elif ch == '+/-':
        on_btn_doidau_clicked()
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

# Ham clear
def on_btn_clear_clicked():
    global finish
    if finish:
        display.delete(0, END)
        display.insert(0, 0)
    else:
        display.delete(len(display.get()) - 1)

# Ham nhan
def on_btn_equal_clicked():
    global finish
    try:
        text = display.get()
        true_number_sentance = text.replace('^', '**')
        res = eval(true_number_sentance)
    except Exception:
        res = 'ERROR'
    display.delete(0, END)
    display.insert(0, res)
    finish = True

# ham chia
def on_btn_percent_clicked():
    global finish
    res = float(display.get()) / 100
    display.delete(0, END)
    display.insert(0, res)
    finish = True

# Giai thua
def on_btn_factorial_clicked():
    global finish
    gt = 1
    n = int(display.get())
    for i in range(1, n + 1):
        gt = gt * i
    display.delete(0, END)
    display.insert(0, gt)
    finish = True

# pi
def on_btn_pi_clicked():
    global finish
    res = float(display.get()) * math.pi
    display.delete(0, END)
    display.insert(0, res)
    finish = True

# e
def on_btn_e_clicked():
    global finish
    if display.get() == '':
        res = math.e
    else:
        res = float(display.get()) * math.e
    display.delete(0, END)
    display.insert(0, res)
    finish = True

# x2
def on_btn_x_2_clicked():
    global finish
    res = math.pow(int(display.get()), 2)
    display.delete(0, END)
    display.insert(0, res)
    finish = True

# 1/x
def on_btn_1x_clicked():
    global finish
    res = 1 / float(display.get())
    display.delete(0, END)
    display.insert(0, res)
    finish = True

# mod
def on_btn_mod_clicked():
    global finish

# sqrt
def on_btn_sqrt_clicked():
    global finish
    res = math.sqrt(int(display.get()))
    display.delete(0, END)
    display.insert(0, res)
    finish = True

# Gia tri tuyet doi abs
def on_btn_abs_clicked():
    global finish
    res = math.fabs(float(display.get()))
    display.delete(0, END)
    display.insert(0, res)
    finish = True

# 10 ^ x
def on_btn_pow_x_clicked():
    global finish
    if display.get() == '':
        res = math.pow(10, 0)
    else:
        res = math.pow(10, float(display.get()))
    display.delete(0, END)
    display.insert(0, res)
    finish = True

# log
def on_btn_log_clicked():
    global finish
    res = math.log(float(display.get()), 10)
    display.delete(0, END)
    display.insert(0, res)
    finish = True

# ln
def on_btn_ln_clicked():
    global finish
    res = math.log(float(display.get()))
    display.delete(0, END)
    display.insert(0, res)
    finish = True

# doi dau
def on_btn_doidau_clicked():
    global finish
    if float(display.get()) < 0:
        res = math.fabs(float(display.get()))
    else:
        res = 0 - float(display.get())
    display.delete(0, END)
    display.insert(0, res)
    finish = True


# Giao dien
# Display
display = Entry(window, font=('Tahoma', 20), width=30, justify='right')
display.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
# hang 1
b1 = '2\u207f\u1d48'
b2 = 'π'
b3 = 'e'
b4 = 'C'
b5 = 'del'
# hang 2
b6 = 'x\u00B2'
b7 = '1⁄x'
b8 = '|x|'
b9 = 'exp'
b10 = 'mod'
# hang 3
b11 = 'sqrt'
b12 = '('
b13 = ')'
b14 = 'n!'
b15 = '/'
# hang 4
b16 = 'x\u02b8'
b17 = '7'
b18 = '8'
b19 = '9'
b20 = '*'
# hang 5
b21 = '10\u02e3'
b22 = '4'
b23 = '5'
b24 = '6'
b25 = '-'
# hang 6
b26 = 'log'
b27 = '1'
b28 = '2'
b29 = '3'
b30 = '+'
# hang 7
b31 = 'ln'
b32 = '+/-'
b33 = '0'
b34 = '.'
b35 = '='
buttons = [[b1, b2, b3, b4, b5], [b6, b7, b8, b9, b10], [b11, b12, b13, b14, b15], [b16, b17, b18, b19, b20], [b21, b22, b23, b24, b25], [b26, b27, b28, b29, b30], [b31, b32, b33, b34, b35]]
for i in range(len(buttons)):
    line = buttons[i]
    for j in range(len(line)):
        ch = line[j]
        btn = Button(window, text=ch, font=('Tahoma', 20), command=on_btn_clicked(ch))
        btn.grid(row=i + 1, column=j, sticky='nesw', padx=5, pady=5)


window.mainloop()