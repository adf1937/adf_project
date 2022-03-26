from tkinter import *


class BMI(Frame):
    'Body Mass Index app'

    def __init__(self, parent=None):
        'constructor'
        Frame.__init__(self, parent)
        self.grid()
        BMI.make_widgets(self)

    def make_widgets(self):
        'defines BMI widgets'
        Label(self, text='Enter your height: ').grid(row=0, column=0)
        self.htEnt = Entry(self)
        self.htEnt.grid(row=0, column=1)
        Label(self, text='Enter your weight: ').grid(row=1, column=0)
        self.wtEnt = Entry(self)
        self.wtEnt.grid(row=1, column=1)
        Button(self, text='Compute BMI', command=self.compute).grid(
            row=2, column=0, columnspan=2)

    def compute(self):
        'the handler for button "Compute BMI"'
        try:
            hgt = eval(self.htEnt.get())
            wgt = eval(self.wtEnt.get())
            res = wgt*703/hgt**2
            showinfo(title='Result', message='Your BMI is {}'.format(res))
        except:
            showinfo(title='Ooops!', message='Invalid number!')
        self.wtEnt.delete(0, END)
        self.htEnt.delete(0, END)


root = Tk()
BMI(root)

root.mainloop()
