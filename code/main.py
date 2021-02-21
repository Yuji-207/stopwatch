import tkinter as tk
import time

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        master.geometry("500x500")
        master.title("ストップウォッチ")
        master.config(bg="black")

        self.startTime=time.time()
        self.stopTime=0.0
        self.elapsedTime=0.0
        self.lap1_times = []
        self.lap2_times = []
        self.playTime=False

        self.canvas = tk.Canvas(master,width=490,height=80,bg="skyblue")
        self.canvas.place(x=3,y=10)

        tk.Button(master,text="Reset",command=self.resetButtonClick,width=10).place(x=10, y=110)
        tk.Button(master,text="Start",command=self.startButtonClick,width=10).place(x=110, y=110)
        tk.Button(master,text="Stop",command=self.stopButtonClick,width=10).place(x=210, y=110)
        tk.Button(master,text="Lap 1",command=self.lap1ButtonClick,width=10).place(x=310, y=110)
        tk.Button(master,text="Lap 2",command=self.lap2ButtonClick,width=10).place(x=410, y=110)

        master.after(50,self.update)

    def startButtonClick(self):
        if not self.playTime:
            self.startTime=time.time()-self.elapsedTime
            self.playTime=True

    def stopButtonClick(self):
        if self.playTime:
            self.stopTime=time.time()-self.startTime
            self.playTime=False

    def lap1ButtonClick(self):
        if self.playTime:
            self.lap1_time = time.time() - self.startTime
            self.lap1_times.append(self.lap1_time)
            lap1 = tk.Label(text=u'test')
            lap1.pack()

    def lap1ButtonClick(self):
        if self.playTime:
            self.lap1_time = time.time() - self.startTime
            self.lap1_times.append(self.lap1_time)
            lap1 = tk.Label(text=u'test')
            lap1.pack()

    def resetButtonClick(self):
        self.startTime=time.time()
        self.stopTime=0.0
        self.elapsedTime=0.0
        self.playTime=False

    def update(self):
        self.canvas.delete("Time")
        if self.playTime:
            self.elapsedTime=time.time()-self.startTime
            self.canvas.create_text(480,40,text=round(self.elapsedTime,1),font=("Helvetica",40,"bold"),fill="black",tag="Time",anchor="e")
        else:
            self.canvas.create_text(480,40,text=round(self.stopTime,1),font=("Helvetica",40,"bold"),fill="black",tag="Time",anchor="e")

        self.master.after(50,self.update)

def main():
    win = tk.Tk()
    #win.resizable(width=False, height=False) #ウィンドウを固定サイズに
    app = Application(master=win)   
    app.mainloop()

if __name__ == "__main__":
    main()