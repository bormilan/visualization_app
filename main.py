import tkinter as tk
import subject
import observer

class MainApp(tk.Frame):
    def __init__(self,root):
    	self.root = root
    	self.root.title("VisualizationApp")
    	self.root.geometry("1000x700")
    	self.button = tk.Button(text="Ok")
    	self.button.place(x=100,y=100)

def main():
	root = tk.Tk()
	main = MainApp(root)	

	dataset = subject.Dataset("train.csv")
	summary = observer.Summary(dataset)
	columnSum = observer.ColumnSum(dataset,"Survived")
	dataset.attach(summary)
	dataset.attach(columnSum)

	root.mainloop()

if __name__ == "__main__":
    main()