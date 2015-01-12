import Tkinter as tk
import tkFont
import time

def plus(num, team):
    scores[team]['score'].set(num + scores[team]['score'].get())
    #scores[team]['score2'].set(scores[team]['score'].get())
def minus(num, team):
    scores[team]['score'].set(max(0,scores[team]['score'].get() - num))
    #scores[team]['score2'].set(scores[team]['score'].get())
def kg(num, team):
    scores[team]['kyonggo'] += 1
    if scores[team]['kyonggo'] % 2 == 0:
        if team == 'red':
            plus(1,'blue')
        elif team == 'blue':
            plus(1,'red')
def key_pressed(event):
    global state
    event = event.char
    team = 'red'
    num = 0
    function = plus
    if event == 'r' and state == False:
        global timer
        timer = [1, 0]
        timeText.configure(text='1:00')
        timeText2.configure(text='1:00')
    elif event in ['1','2','3','4']:
        num = int(event)
    elif event in ['7','8','9','0']:
        if event == '0':
            num = 4
        else:
            num = int(event) - 6
        team = 'blue'
    elif event in ['q','p']:
        function = kg
        if event == 'p':
            team = 'blue'
    elif event in ['a','l']:
        function = minus
        num = 1
        if event == 'l':
            team = 'blue'
    else:
        return
    function(num, team)
def space(event):
    global state, timer
    if state == False and (timer[0] != 0 or  timer[1] != 0):
        state = True
    elif state == False and timer[0]==0 and timer[1]==0:
        timer = [1,0]
        state = True
    else:
        state = False

def esc_key(event):
    root.destroy()
def update_timeText():
    global state
    if state:
        global timer
        if timer[0] == 1:
            timer[1] = 60
            timer[0] = 0
        # Every time this function is called,
        # we will increment 1 centisecond (1/100 of a second)
        timer[1] -= 1

        # Every 60 seconds is equal to 1 min
        if (timer[1] == 00):
            timer[0] = 0
            timer[1] = 0
            state = False
        # We create our time string here
        timeString = pattern.format(timer[0], timer[1])
        # Update the timeText Label box with the current time
        timeText.configure(text=timeString)
        timeText2.configure(text=timeString)
        # Call the update_timeText() function after 1 centisecond
    root.after(1000, update_timeText) 


root=tk.Tk()
root.wm_title('Sparring')
scores = {'red':{'kyonggo':0},'blue':{'kyonggo':0}}
state = False
timer = [1, 0]
pattern = '{0:01d}:{1:02d}'
timeText = tk.Label(root, text="1:00", bg='black', fg="white", font=tkFont.Font(size=150))
timeText.pack(fill=tk.X)

pad=0
root.geometry("{0}x{1}+0+0".format(
root.winfo_screenwidth()-pad, root.winfo_screenheight()-pad))

for i in ['red','blue']:
    scores[i]['score'] = tk.IntVar()
    scores[i]['score'].set(0)
    tk.Label(root, textvariable = scores[i]['score'], bg=i, fg="white", font=tkFont.Font(size=755),width=2, height=20).pack(side=tk.LEFT)
root.bind('<space>', space)
root.bind('<Escape>', esc_key)
root.bind('<Key>', key_pressed)
update_timeText()

win2 = tk.Toplevel()
win2.wm_title('Sparring 2')
timeText2 = tk.Label(win2, text="1:00", bg='black', fg="white", font=tkFont.Font(size=450))
timeText2.pack(fill=tk.X)
win2.geometry("{0}x{1}+0+0".format(1600, 1000-60))

for i in ['blue','red']:
    tk.Label(win2, textvariable = scores[i]['score'], bg=i, fg="white", font=tkFont.Font(size=450),width=3, height=20).pack(side=tk.LEFT)
win2.bind('<space>', space)
win2.bind('<Escape>', esc_key)
win2.bind('<Key>', key_pressed)
root.mainloop()
##############################################
