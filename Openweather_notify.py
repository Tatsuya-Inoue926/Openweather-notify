import json
import requests
from pprint import pprint

TOKEN = "TOKEN-KEY"

#APIのURL
api_url ="https://notify-api.line.me/api/notify"

weather_url ="" #任意のURL

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
