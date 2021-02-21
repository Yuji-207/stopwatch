import csv
import time
import tkinter as tk
import datetime as dt
from playsound import playsound

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        master.geometry("600x300")
        master.title("ストップウォッチ")
        master.config(bg="black")

        self.startTime=time.time()
        self.stopTime=0.0
        self.elapsedTime=0.0
        self.lap_times = []
        self.lap_number = 0
        self.lap_numbers = []
        self.scores = []
        self.playTime=False
        self.sound_path = '/Users/yuji/Documents/GitHub/stopwatch/sound/fasten_seatbelt_sign.wav'

        self.canvas = tk.Canvas(master,width=590,height=80,bg="skyblue")
        self.canvas.place(x=3,y=10)

        tk.Button(master,text="Reset",command=self.resetButtonClick,width=10).place(x=10, y=110)
        tk.Button(master,text="Start",command=self.startButtonClick,width=10).place(x=110, y=110)
        tk.Button(master,text="Stop",command=self.stopButtonClick,width=10).place(x=210, y=110)
        tk.Button(master,text="Correct",command=self.correctButtonClick,width=10, bg='blue').place(x=310, y=110)
        tk.Button(master,text="Incorrect",command=self.incorrectButtonClick,width=10, bg='red').place(x=410, y=110)
        tk.Button(master,text="Next",command=self.nextButtonClick,width=10, bg='yellow').place(x=510, y=110)

        master.after(50,self.update)

    def startButtonClick(self):
        if not self.playTime:
            self.startTime=time.time()-self.elapsedTime
            self.playTime=True
            self.csv_path = f'/Users/yuji/Documents/study_records/{dt.datetime.now()}.csv'

    def stopButtonClick(self):
        if self.playTime:
            self.stopTime=time.time()-self.startTime
            self.playTime=False

    def nextButtonClick(self):
        if self.playTime:
            self.lap_time = time.time() - self.startTime
            self.lap_times.append(self.lap_time)
            self.lap_numbers.append(self.lap_number)
            self.lap_number = 0
            lap = tk.Label(text=round(self.lap_time, 2))
            lap.pack()

    def correctButtonClick(self):
        if self.playTime:
            self.scores.append(True)
            self.lap_number += 1

    def incorrectButtonClick(self):
        if self.playTime:
            self.scores.append(False)
            self.lap_number += 1

    def resetButtonClick(self):
        with open(self.csv_path, 'w') as f:
            writer = csv.writer(f)
            writer.writerows([self.lap_times, self.lap_numbers, self.scores])
        self.startTime=time.time()
        self.stopTime=0.0
        self.elapsedTime=0.0
        self.playTime=False
        playsound(self.sound_path)

    def update(self):
        self.canvas.delete("Time")
        if self.playTime:
            self.elapsedTime=time.time()-self.startTime
            self.canvas.create_text(580,40,text=round(self.elapsedTime,1),font=("Helvetica",40,"bold"),fill="black",tag="Time",anchor="e")
        else:
            self.canvas.create_text(580,40,text=round(self.stopTime,1),font=("Helvetica",40,"bold"),fill="black",tag="Time",anchor="e")

        self.master.after(50,self.update)

def main():
    win = tk.Tk()
    #win.resizable(width=False, height=False) #ウィンドウを固定サイズに
    app = Application(master=win)
    app.mainloop()

if __name__ == "__main__":
    main()