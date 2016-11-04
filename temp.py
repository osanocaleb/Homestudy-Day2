#This application gives the temperature of a given location
#call the function with the city name as an argument
#it must be executed from the commandline using an interpreter
import requests

def City_temp(city):
	if type(city) == str:
		b = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=1c84997bbd99db105f632758fd942d90') #this will accept the city name and search using it
		json_1 = b.json()
		temp_k = float(json_1["main"]["temp"]) #retrieves the temperature information in Kelvin
		temp_c = temp_k - 273.15
		sky = json_1["weather"][0]["description"]
		print("The temperature of ", city,"in degrees Celcius is", int(temp_c))
		print("the sky conditions in", city, "are", sky)
	else:
		print("please provide the city name as a string fomatted as 'nairobi' ")