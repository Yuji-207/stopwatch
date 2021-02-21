import time
import tkinter as tk


def __init__(self,master):
    super().__init__(master)
    self.pack()

    master.geometry('300x150')
    master.title('Stop Watch')
    master.config(bg='black')

    self.start_time = time.time()
    self.stop_time = 0.0
    self.display_time = 0.0
    self.play = False

    self.canvas = tk.Canvas(master, width=490, height=80, bg='skyblue')
    self.canvas.place(x=3, y=10)

    tk.Button(master, text='Reset', command=self.resetButtonClick, width=10).place(x=10, y=110)
    tk.Button(master, text='Start', command=self.startButtonClick, width=10).place(x=110, y=110)
    tk.Button(master, text='Stop', command=self.stopButtonClick, width=10).place(x=210, y=110)
    tk.Button(master, text='Lap 1', command=self.lap1ButtonClick, width=10).place(x=310, y=110)
    tk.Button(master, text='Lap 2', command=self.lap2ButtonClick, width=10).place(x=410, y=110)
    
    master.after(50, self.update)

def startButtonClick(self):
    if not self.play:
        self.start_time = time.time()
        self.play = True

def stopButtonClick(self):
    if self.play:
        self.stop_time = time.time() - self.start_time + self.stop_time
        self.play = False

def lap1ButtonClick(self):
    if self.play:
        self.lap1_time = time.time() - self.start_time + self.stop_time
        self.lap1_times.append(self.lap1_time)
        label1 = tk.Label(text=u'test')
        label1.pack()

def lap2ButtonClick(self):
    if self.play:
        self.lap2_time = time.time() - self.start_time + self.stop_time
        self.lap2_times.append(self.lap2_time)

def resetButtonClick(self):
    self.start_time = time.time()
    self.stop_time = 0.0
    self.display_time = 0.0
    self.play = False

def update(self):
    self.canvas.delete('Time')
    if self.play:
        self.display_time = time.time() - self.start_time + self.stop_time
        self.canvas.create_text(480, 40, text=round(self.display_time, 1), font=('Helvetica', 40, 'bold'), fill='black', tag='Time', anchor='e')
    else:
        self.canvas.create_text(480, 40, text=round(self.stop_time, 1), font=('Helvetica', 40, 'bold'), fill='black', tag='Time', anchor='e')

    self.master.after(50, self.update)

def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()