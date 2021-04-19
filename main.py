import tkinter as tk
import subject
import observer

class MainApp(tk.Frame):
    def __init__(self,root):
    	tk.Frame.__init__(self, root)
    	self.root = root
    	self.root.title("VisualizationApp")
    	self.root.geometry("1000x700")
    	self.root.config(bg="papaya whip")
    	
    	self.entry = tk.Text(bg="cyan3",width=30,height=2)
    	self.entry.place(x=10,y=10)
    	self.button = tk.Button(bg="tomato3",
    		text="Ok",
    		width="15",
    		height="2",
    		relief="groove",
    		command=lambda: load(self.entry.get("1.0","end-1c")))
    	self.button.place(x=10,y=50)			

def main():
	root = tk.Tk()
	main = MainApp(root)	

	root.mainloop()

def load(file):
	try:
		dataset = subject.Dataset(file)
		summary = observer.Summary(dataset)
		columnSum = observer.ColumnSum(dataset,"Survived")
		dataset.attach(summary)
		dataset.attach(columnSum)
	except FileNotFoundError:
		print("wrong file name! try again.")

if __name__ == "__main__":
    main()