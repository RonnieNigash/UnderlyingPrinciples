import Tkinter as tk

class PyStat(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)

		self.air_temp_label = tk.Label(parent, text = "Air Temp")
		self.air_temp_label.pack()

		self.air_temp = tk.Entry(parent, justify = tk.LEFT)
		self.air_temp.pack()
		self.air_temp.insert(0, "")

		self.bar_pres_label = tk.Label(parent, text = "Barometric Pressure")
		self.bar_pres_label.pack()

		self.bar_pres = tk.Entry(parent, justify = tk.LEFT)
		self.bar_pres.pack()
		self.bar_pres.insert(0, "")

		self.wind_speed_label = tk.Label(parent, text = "Wind Speed")
		self.wind_speed_label.pack()

		self.wind_speed = tk.Entry(parent, justify = tk.LEFT)
		self.wind_speed.pack()
		self.wind_speed.insert(0, "")

		self.calculate = tk.Button(parent, text = "Calculate!", command = calculate_values)
		self.calculate.pack()


	def calculate_values(self):
		pass
		# @TODO
		# Take values from the past XX days, (week? month?)
		# Scraped from HTML page -- new method?
		# Input values into label fields above


if __name__ == "__main__":
	root = tk.Tk()
	PyStat(root).pack(side = "top", fill = "both", expand = True)
	root.title("Statistical Analysis")
	root.mainloop()
