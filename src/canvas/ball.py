from tkinter import *
window = Tk()
window.title('bouncing ball')
dx = 5
dy = 5
game_over = 0
score = 0
canvas = Canvas(window, width=640, height=480,
                bg="white")
canvas.pack()

ball = canvas.create_oval(10, 10, 30, 30, fill='red', outline='red')
rect = canvas.create_rectangle(250, 400, 400, 412, fill='blue', outline='blue')
text = canvas.create_text(320, 240, fill='red',
                          font='Times 50 bold', text='Game Over!')
end_score = canvas.create_text(320, 290, fill='black',
                               font='Times 20 bold', text='Score: ' + str(score))
lb_score = canvas.create_text(
    50, 20, fill='green', font='Times 15 bold', text='Score : ' + str(score))
canvas.itemconfigure(text, state='hidden')
canvas.itemconfigure(end_score, state='hidden')


def move_left(evt):
    global game_over
    if game_over == 1:
        return
    c = canvas.coords(rect)
    if c[0] > 10:
        canvas.move(rect, -20, 0)


def move_right(evt):
    global game_over
    if game_over == 1:
        return
    c = canvas.coords(rect)
    if c[2] < 630:
        canvas.move(rect, 20, 0)


def restart(evt):
    global game_over
    global score
    canvas.coords(ball, 10, 10, 30, 30)
    canvas.coords(rect, 250, 400, 400, 412)
    canvas.itemconfigure(text, state='hidden')
    canvas.itemconfigure(lb_score, state='normal')
    canvas.itemconfigure(end_score, state='hidden')
    game_over = 0
    score = 0
    move_ball()


canvas.bind_all('<KeyPress-Left>', move_left)
canvas.bind_all('<KeyPress-Right>', move_right)
canvas.bind_all('<Button-1>', restart)


def move_ball():
    x1, y1, x2, y2 = canvas.coords(ball)
    xp1, yp1, xp2, yp2 = canvas.coords(rect)
    global dx
    global dy
    global game_over
    global score
    if y1 <= 0:
        dy = 5
    elif y2 >= 480:
        game_over = 1
        canvas.itemconfigure(text, state='normal')
        canvas.itemconfigure(end_score, state='normal')
        canvas.itemconfigure(end_score, text="Score : " + str(score))
        canvas.itemconfigure(lb_score, text="Score : 0")
        canvas.itemconfigure(lb_score, state='hidden')
    elif x1 <= 0:
        dx = 5
    elif x2 >= 640:
        dx = -5
    elif yp1 <= y2 <= yp2 and (xp1 <= x1 <= xp2 or xp1 <= x2 <= xp2):
        score += 1
        canvas.itemconfigure(lb_score, text="Score : " + str(score))
        dy = -5
    canvas.move(ball, dx, dy)
    if game_over == 0:
        window.after(30, move_ball)


move_ball()
window.mainloop()
