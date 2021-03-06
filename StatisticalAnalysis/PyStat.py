import Tkinter as tk
from bs4 import BeautifulSoup
import requests
import time
from datetime import date
import re
import numpy as np


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

		self.calculate = tk.Button(parent, text = "Calculate!", command = self.calculate_values)
		self.calculate.pack()


	def calculate_values(self):
		data = self.scrape_data()
		air_temp_list, bar_pres_list, wind_speed_list = ([] for i in range(3)) # Make three empty lists
		for i in data:
			temp_list = i.split('\t') # Split each data piece by tab characters
			air_temp_list.append(temp_list[1])
			bar_pres_list.append(temp_list[2])
			wind_speed_list.append(temp_list[-1].split('<')[0])


		# Convert our strings to floats to apply mean and median operations
		air_temp_list = map(float, air_temp_list)
		bar_pres_list = map(float, bar_pres_list)
		wind_speed_list = map(float, wind_speed_list)

		self.air_temp.insert(0, np.mean(air_temp_list))
		self.bar_pres.insert(0, np.mean(bar_pres_list))
		self.wind_speed.insert(0, np.mean(wind_speed_list))
		#print air_temp_list
		#print bar_pres_list
		#print wind_speed_list
		# @TODO
		# Take values from the past XX days, (week? month?)
		# Scraped from HTML page -- new method?
		# Input values into label fields above

	def scrape_data(self):
#		data_dictionary = {} # Implement Keys of dates and Values of information later
		data_list = []

		page = requests.get("http://lpo.dt.navy.mil/data/DM/Environmental_Data_Deep_Moor_2015.txt")
		data = page.text
		soup = BeautifulSoup(data) # our dates (from page) are of the form YYYY_MM_DD

		today = date.today().isoformat() # of the form YYYY-MM-DD
		today = today.replace("-", "_") # of the form YYYY_MM_DD which matches data set
		print today
		soup_list = str(soup).splitlines()
		for row in soup_list:
			match_found = re.match(today, row)
			if match_found:
				data_list.append(row)
		#return data_dictionary;
		return data_list

if __name__ == "__main__":
	root = tk.Tk()
	PyStat(root).pack(side = "top", fill = "both", expand = True)
	root.title("Statistical Analysis")
	root.mainloop()
