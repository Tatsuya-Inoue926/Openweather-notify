import json
import requests
from pprint import pprint

TOKEN = "TOKEN-KEY"

#APIのURL
api_url ="https://notify-api.line.me/api/notify"

weather_url ="http://api.openweathermap.org/data/2.5/weather?q=Nara,JP&appid=4bf036962ce63110047e4608532b982d&lang=ja&units=metric"

jsondata = requests.get(weather_url).json()

name = jsondata["name"]
weather = jsondata["weather"][0]["description"]
temp = jsondata["main"]["temp"]
t_max = jsondata["main"]["temp_max"]
t_min = jsondata["main"]["temp_min"]

send_contents = "今日の" + name + "の天気は" + weather + "です。\n" + "気温は" + str(temp) + "度。最高気温は" + str(t_max) + "度で最低気温は" + str(t_min) + "度です。"
TOKEN_dic = {"Authorization": "Bearer" + " " + TOKEN }
send_dic = {"message": send_contents }

requests.post(api_url, headers = TOKEN_dic, data = send_dic)
