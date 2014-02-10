# -*- coding:utf-8 -*-


from azure.storage import *
import datetime
import re
import urllib2
import math
import time

table_service = TableService(account_name='asthmacure', account_key='zryh9UWR1w2SCl386sAIT4RfHfmhBgYD6eUFDpUBjiiLfCab6kOT6rTtJnQOC3h4RLZzMTDz5+bgw4HN2sG57w==')




class Temperature(object):
    def toCelcius(self, deg_f):
        return (deg_f-32)*5/9

#minute=minute+1
city='kolkata'
url = "http://api.openweathermap.org/data/2.5/weather?q=kolkata&mode=xml&units=metric"
source=urllib2.urlopen(url)
tomorrow=str(datetime.date.today()+datetime.timedelta(days=1))
htmltext=source.read()
print("<------------------------WEATHER REPORT: "+city.upper()+" for "+tomorrow+" ------------>")

# search for pattern using regular expressions (.+?)
#if(htmltext.find(adate)!=-1):
direction='<direction value="(.+?)" code="(.+?)" name="(.+?)"/>'
wind='<speed value="(.+?)" name="(.+?)"/>'
temp='<temperature value="(.+?)" min="(.+?)" max="(.+?)" unit="(.+?)"/>'
humidity='<humidity value="(.+?)" unit="%"/>'
condition='<weather number="(.+?)" value="(.+?)" icon="(.+?)"/>'
pattern_direction=re.compile(direction)
pattern_wind=re.compile(wind)
pattern_temp=re.compile(temp)
pattern_humidity=re.compile(humidity)
pattern_cond=re.compile(condition)



# match pattern with htmltext
weather_windspeed=re.findall(pattern_wind,htmltext)
weather_winddirection=re.findall(pattern_direction,htmltext)
weather_temp=re.findall(pattern_temp,htmltext)
weather_cond=re.findall(pattern_cond,htmltext)
weather_humid=re.findall(pattern_humidity,htmltext)



#print "Overall Weather status: ",weather_cond[0][1]
RowKey=datetime.datetime.now().strftime("%d%m%Y%H%M")
temperature = weather_temp[0][0]
#print "Minimum Temperature: ",weather_temp[0][1]
#print "Maximum Temperature: ",weather_temp[0][2]
print "Wind Direction: ",weather_windspeed[0][0]           
    

def checkduplicate():
    tasks = table_service.query_entities('WeatherFetch', "PartitionKey eq 'data'")
    flag=0
    
    for task in tasks:
        if(task.RowKey==RowKey):
            flag=1
        elif(task.temperature==temperature):
            flag=1

    if(flag==1):
        return True
    else:
        return False
        
    






if(not checkduplicate()):
    fetched_data = {'PartitionKey': 'data', 'RowKey': RowKey, 'temperature' : temperature,'min_temperature' : weather_temp[0][1], 'humidity' : weather_humid[0],'windspeed':weather_windspeed[0][0],'winddirection':weather_winddirection[0][1] ,'condition':weather_cond[0][1]}
    table_service.insert_entity('WeatherFetch', fetched_data)
else:
    print 'Fuck off'


