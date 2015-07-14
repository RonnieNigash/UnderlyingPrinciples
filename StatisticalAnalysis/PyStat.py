import Tkinter as tk

class PyStat(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)

		self.airTempLabel = tk.Label(parent, text = "Air Temp")
		self.airTempLabel.pack()

		self.airTemp = tk.Entry(parent, justify = tk.LEFT)
		self.airTemp.pack()
		self.airTemp.insert(0, "")

		self.barPresLabel = tk.Label(parent, text = "Barometric Pressure")
		self.barPresLabel.pack()

		self.barPres = tk.Entry(parent, justify = tk.LEFT)
		self.barPres.pack()
		self.barPres.insert(0, "")

		self.windSpeedLabel = tk.Label(parent, text = "Wind Speed")
		self.windSpeedLabel.pack()
		
		self.windSpeed = tk.Entry(parent, justify = tk.LEFT)
		self.windSpeed.pack()
		self.windSpeed.insert(0, "")

		self.calculate = tk.Button(parent, text = "Calculate!")
		self.calculate.pack()

if __name__ == "__main__":
	root = tk.Tk()
	PyStat(root).pack(side = "top", fill = "both", expand = True)
	root.title("Statistical Analysis")
	root.mainloop()
