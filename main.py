import tkinter as tk
import subject
import observer

Page = tk.Tk()

dataset = subject.Dataset("train.csv")
summary = observer.Summary(dataset)
columnSum = observer.ColumnSum(dataset,"Survived")
dataset.attach(summary)
dataset.attach(columnSum)

Page.mainloop()