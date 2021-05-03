import tkinter as tk
import subject
import observer

class MainApp(tk.Frame):
    def __init__(self,root):
    	tk.Frame.__init__(self, root)
    	self.root = root
    	self.root.title("VisualizationApp")
    	self.root.geometry("1500x1200")
    	self.root.config(bg="papaya whip")
    	
    	self.entry = tk.Entry(bg="cyan3")
    	self.entry.place(x=10,y=10,width=200,height=30)
    	self.button = tk.Button(bg="tomato3",
    		text="Ok",
    		width="15",
    		height="2",
    		relief="groove",
    		command=lambda: load(self.entry.get()))
    	self.button.place(x=10,y=50)	
    	self.entry.bind('<Return>',lambda event: load(self.entry.get()))


def main():
	root = tk.Tk()
	main = MainApp(root)	

	root.mainloop()

def load(file):
	try:
		dataset = subject.Dataset(file)
		summary = observer.Summary(dataset)
		columnSum = observer.Column(dataset)
		diagram = observer.Diagram(dataset)

		dataset.attach(summary)
		dataset.attach(columnSum)
		dataset.attach(diagram)
	except FileNotFoundError:
		print("wrong file name! try again.")

if __name__ == "__main__":
    main()