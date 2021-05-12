#Observer
import abc
import numpy as np
import tkinter as tk
from tkinter import Canvas
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Observer(object):
	"""Observer"""
	def __init__(self,Subject):
		self.subject = Subject

	@abc.abstractmethod
	def update():
		pass

class Summary(Observer):
	"""Summary"""
	def __init__(self,Subject):
		super().__init__(Subject)
		self.mode = 0

		#---MODE BUTTONS---#
		#1
		self.head = tk.Button(text="Head")
		self.head.config(width=8,height=2)
		self.head.config(font=("Courier", 15))
		self.head.place(x=350,y=780)		
		self.head.config(relief="groove")		
		self.head.config(command=lambda: self.setMode(0))

		#2
		self.describe = tk.Button(text="Describe")
		self.describe.config(width=8,height=2)
		self.describe.config(font=("Courier", 15))
		self.describe.place(x=480,y=780)		
		self.describe.config(relief="groove")
		self.describe.config(command=lambda: self.setMode(1))

		#---CONTENT LABEL---#
		self.SummaryLabel = tk.Label()
		self.SummaryLabel.place(x=350,y=850)
		self.SummaryLabel.config(bg="thistle2")
		self.SummaryLabel.config(relief="solid")
		self.SummaryLabel.config(width=100,height=10)

	def update(self): 		
		#Button colors
		if self.mode == 0:
			self.head.config(bg="tomato3")
			self.describe.config(bg="dim gray")
		else:
			self.head.config(bg="dim gray")
			self.describe.config(bg="tomato3")

		self.SummaryLabel.config(text=self.getSummary())

	#function to get the data from subject
	def getSummary(self):
		if self.mode == 0:	
			return self.subject.getState().head()
		else:
			return self.subject.getState().describe()

	#function to change label mode
	def setMode(self,newMode):
		if newMode == 0:
			self.mode = 0
			self.update()
		else:
			self.mode = 1
			self.update()

class Column(Observer):
	"""SurvivedSum"""
	def __init__(self, Subject):
		super().__init__(Subject)
		self.column = ""
		self.mode = 0

		#---COLUMN LIST---#
		self.columnList = tk.Listbox()

		#---CONTENT LABEL---#
		self.columnLabel = tk.Label()
		self.columnLabel.config(text="nincs oszlop kiválasztva")
		self.columnLabel.place(x=10,y=910)
		self.columnLabel.config(bg="thistle2")
		self.columnLabel.config(relief="solid")
		self.columnLabel.config(width=20,height=5)

		#---COLUMN NAME ENTRY---#
		self.entry = tk.Entry(bg="cyan3")
		self.entry.place(x=10,y=870,width=100,height=30)
		self.entry.bind('<Return>',(lambda event: self.setColumn(self.entry.get())))

		#---OK BUTTON---#
		self.button = tk.Button(text="Ok")
		self.button.config(width=3,height=1)
		self.button.config(font=("Courier", 15))
		self.button.place(x=120,y=865)		
		self.button.config(relief="groove")
		self.button.config(bg="tomato3")
		self.button.config(command=lambda: self.setColumn(self.entry.get()))

		#---MODE BUTTONS---#
		#1
		self.sum = tk.Button(text="Sum")
		self.sum.config(width=6,height=1)
		self.sum.config(font=("Courier", 15))
		self.sum.place(x=180,y=900)		
		self.sum.config(relief="groove")		
		self.sum.config(command=lambda: self.setMode(0))

		#2
		self.type = tk.Button(text="type")
		self.type.config(width=6,height=1)
		self.type.config(font=("Courier", 15))
		self.type.place(x=180,y=950)		
		self.type.config(relief="groove")
		self.type.config(command=lambda: self.setMode(1))

	def setColumn(self,column):
		self.column = column
		self.update()

	def update(self):	
		try:
			self.columnLabel.config(text=self.getColumn())
		except KeyError:
			self.columnLabel.config(text="nincs oszlop kiválasztva")
		except TypeError:
			self.columnLabel.config(text="az oszlop adatai nem megfelelőek")

		#Button colors
		if self.mode == 0:
			self.sum.config(bg="tomato3")
			self.type.config(bg="dim gray")
		else:
			self.sum.config(bg="dim gray")
			self.type.config(bg="tomato3")
		
		#---COLUMN LIST---#
		for column in self.subject.getState().columns:
			if column not in self.columnList.get(0,len(self.subject.getState().columns)):
				self.columnList.insert(tk.END,column)
		self.columnList.place(x=10,y=690)
		self.columnList.config(width=30,height=10)
		self.columnList.config(bg="thistle2")

	def setMode(self,newMode):
		if newMode == 0:
			self.mode = 0
			self.update()
		else:
			self.mode = 1
			self.update()

	def getColumn(self):
		if self.mode == 0:	
			return np.sum(self.subject.getState()[self.column])
		else:
			return self.subject.getState()[self.column].dtypes

class Diagram(Observer):
	"""docstring for Diagram"""
	def __init__(self, Subject):
		super().__init__(Subject)
		self.column1 = ""
		self.column2 = ""
		self.isCurrent = False

		#drop all na's
		self.subject = self.subject.getState().dropna()

		#---INPUT LABEL---#
		self.inputLabel = tk.Label()
		self.inputLabel.config(text="Korreláció Diagram")
		self.inputLabel.place(x=10,y=130)

		#---USER INPUTS---#
		self.firstColumnEntry = tk.Entry(bg="cyan3")
		self.firstColumnEntry.place(x=10,y=170,width=100,height=30)

		self.secondColumnEntry = tk.Entry(bg="cyan3")
		self.secondColumnEntry.place(x=120,y=170,width=100,height=30)

		#---OK BUTTON---#
		self.button = tk.Button(text="Ok")
		self.button.config(width=3,height=1)
		self.button.config(font=("Courier", 15))
		self.button.place(x=10,y=220)		
		self.button.config(relief="groove")
		self.button.config(bg="tomato3")
		self.button.config(command=lambda: self.setColumn(self.firstColumnEntry.get(),self.secondColumnEntry.get()))

	def update(self):
		#---UPDATE PLOT---#
		plot = plt.Figure(figsize=(5,4))
		canvas = Canvas()
			
		if self.column1 in self.subject.columns and self.column2 in self.subject.columns:
			ax = plot.add_subplot(111)
			chart_type = FigureCanvasTkAgg(plot)
			chart_type.get_tk_widget().place(x=10,y=280)
			new_index_subject = self.subject.set_index(self.column1).sort_values(self.column1)			
			df = new_index_subject.loc[:,self.column2]
			df.plot(kind='line', legend=True, ax=ax, xlabel = f"{self.column1}")
			ax.set_title(f"{self.column1} ~ {self.column2}")

			self.isCurrent = True
		elif self.column1 != "":
			print("hibás oszlopok vannak megadva !")
		elif self.column1 == "" and self.column2 == "":
			label = tk.Label()
			label.place(x=10,y=280)
			label.config(bg="papaya whip")
			label.config(width=71,height=27)

	def setColumn(self,column1,column2):
		self.column1 = column1
		self.column2 = column2
		self.update()

class Barplot(Observer):
	"""Barplot observer"""
	def __init__(self, Subject):
		super().__init__(Subject)
		self.column1 = ""
		self.column2 = ""
		self.isCurrent = False

		#drop all na's
		self.subject = self.subject.getState().dropna()

		#---INPUT LABEL---#
		self.inputLabel = tk.Label()
		self.inputLabel.config(text="Barplot Diagram")
		self.inputLabel.place(x=530,y=130)

		#---USER INPUTS---#
		self.firstColumnEntry = tk.Entry(bg="cyan3")
		self.firstColumnEntry.place(x=530,y=170,width=100,height=30)

		self.secondColumnEntry = tk.Entry(bg="cyan3")
		self.secondColumnEntry.place(x=650,y=170,width=100,height=30)

		#---OK BUTTON---#
		self.button = tk.Button(text="Ok")
		self.button.config(width=3,height=1)
		self.button.config(font=("Courier", 15))
		self.button.place(x=530,y=220)		
		self.button.config(relief="groove")
		self.button.config(bg="tomato3")
		self.button.config(command=lambda: self.setColumn(self.firstColumnEntry.get(),self.secondColumnEntry.get()))

	def update(self):
		#---UPDATE PLOT---#
		plot = plt.Figure(figsize=(5,4))
			
		if self.column1 in self.subject.columns and self.column2 in self.subject.columns:
			ax = plot.add_subplot(111)
			chart_type = FigureCanvasTkAgg(plot)
			chart_type.get_tk_widget().place(x=530,y=280)		
			df = self.subject.groupby(self.column1)[[self.column2]].sum()
			df.plot(kind='bar', legend=True, ax=ax)
			ax.set_title(f"")

			self.isCurrent = True
		elif self.column1 != "":
			print("hibás oszlopok vannak megadva !")
		elif self.column1 == "" and self.column2 == "":
			label = tk.Label()
			label.place(x=530,y=280)
			label.config(bg="papaya whip")
			label.config(width=71,height=27)

	def setColumn(self,column1,column2):
		self.column1 = column1
		self.column2 = column2
		self.update()

class Scatterplot(Observer):
	"""Scatterplot observer"""
	def __init__(self, Subject):
		super().__init__(Subject)
		self.column1 = ""
		self.column2 = ""
		self.isCurrent = False

		#drop all na's
		self.subject = self.subject.getState().dropna()

		#---INPUT LABEL---#
		self.inputLabel = tk.Label()
		self.inputLabel.config(text="Scatterplot Diagram")
		self.inputLabel.place(x=1050,y=130)

		#---USER INPUTS---#
		self.firstColumnEntry = tk.Entry(bg="cyan3")
		self.firstColumnEntry.place(x=1050,y=170,width=100,height=30)

		self.secondColumnEntry = tk.Entry(bg="cyan3")
		self.secondColumnEntry.place(x=1170,y=170,width=100,height=30)

		#---OK BUTTON---#
		self.button = tk.Button(text="Ok")
		self.button.config(width=3,height=1)
		self.button.config(font=("Courier", 15))
		self.button.place(x=1050,y=220)		
		self.button.config(relief="groove")
		self.button.config(bg="tomato3")
		self.button.config(command=lambda: self.setColumn(self.firstColumnEntry.get(),self.secondColumnEntry.get()))

	def update(self):
		#---UPDATE PLOT---#
		plot = plt.Figure(figsize=(5,4))
			
		if self.column1 in self.subject.columns and self.column2 in self.subject.columns:
			ax = plot.add_subplot(111)
			ax.scatter(self.subject[self.column1],self.subject[self.column2])
			scatter = FigureCanvasTkAgg(plot) 
			scatter.get_tk_widget().place(x=1050,y=280)
			ax.legend([self.column1]) 
			ax.set_xlabel(self.column1)
			ax.set_title(f'{self.column1} Vs. {self.column2}')

			self.isCurrent = True
		elif self.column1 != "":
			print("hibás oszlopok vannak megadva !")
		elif self.column1 == "" and self.column2 == "":
			label = tk.Label()
			label.place(x=1050,y=280)
			label.config(bg="papaya whip")
			label.config(width=71,height=27)

	def setColumn(self,column1,column2):
		self.column1 = column1
		self.column2 = column2
		self.update()

