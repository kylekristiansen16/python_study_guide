
""" 
improving the student's skills in parsing XML documents;
using known methods of the Element object;

Have you seen the weather forecast for the coming week? It’ll be an extremely sunny and warm week. 
Familiarize yourself with the data in the forecast.xml file and then complete the following tasks:

Create a class named TemperatureConverter and its convert_celsius_to_fahrenheit method. The 
convert_celsius_to_fahrenheit method should convert the temperature from Celsius to Fahrenheit. 
Use the following formula:

F = 9/5 * C + 32.

Create a class named ForecastXmlParser and its parse method responsible for reading data from forecast.xml. 
Use the TemperatureConverter class to convert the temperature from Celsius to Fahrenheit (rounded to one 
decimal place). The parse method should print the following results:

Monday: 28 Celsius, 82.4 Fahrenheit
Tuesday: 27 Celsius, 80.6 Fahrenheit
Wednesday: 28 Celsius, 82.4 Fahrenheit
Thursday: 29 Celsius, 84.2 Fahrenheit
Friday: 29 Celsius, 84.2 Fahrenheit
Saturday: 32 Celsius, 89.6 Fahrenheit
Sunday: 33 Celsius, 91.4 Fahrenheit
"""
import xml.etree.ElementTree as ET


class TemperatureConverter():
    def __init__(self) -> None:
        pass
    def convert_celsius_to_fahrenheit(self, celsius):
        return round(9/5 * celsius + 32, 1)
    
class ForecastXmlParser():
    def __init__(self) -> None:
        self.converter = TemperatureConverter()
        self.tree = ET.parse('/Users/kylekristiansen/cherreco/python/05_file_processing/02_xml/forecast.xml')  # similar to the sqllight class - connect to file
        self.root = self.tree.getroot()  # initialize root element for parsing in other methods
        
    def parse(self):
        for item in self.root.iter("item"):
            day = item.find("day").text
            temp = item.find("temperature_in_celsius").text
            print(f"{day}: {temp} Celsius, {self.converter.convert_celsius_to_fahrenheit(int(temp))} Fahrenheit")
            
parser = ForecastXmlParser()
parser.parse()