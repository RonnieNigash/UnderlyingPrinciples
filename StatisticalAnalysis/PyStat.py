import Tkinter as tk



class Main(tk.Frame):
	pass


class PyStat(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.main = Main(self)	

		self.label1 = tk.Label(parent, text = "Air Temp")
		self.label1.pack()
		
		self.label2 = tk.Label(parent, text = "Barometric Pressure")
		self.label2.pack()

		self.label3 = tk.Label(parent, text = "Wind Speed")
		self.label3.pack()

		self.main.pack(side = "right", fill = "both", expand = True)

if __name__ == "__main__":
	root = tk.Tk()
	PyStat(root).pack(side = "top", fill = "both", expand = True)
	root.mainloop()
