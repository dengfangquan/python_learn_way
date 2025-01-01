import requests
import json

import tkinter as tk
t=tk.Tk()
t.title("翻译器")
t.geometry('400x400')
l=tk.Label(t,text = '请输入中文或者英文')
e=tk.Entry(t)
l1 = tk.Label(t)
def tran():
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'cookie': 'BIDUPSID=6325C24B8E1F27555FC32F05EA1779BA; PSTM=1704785529; BAIDUID=51FDE6421A933FFCC8EECE54B13320DE:FG=1; BAIDUID_BFESS=51FDE6421A933FFCC8EECE54B13320DE:FG=1; ZFY=7pUaUjsjB1JwsGy8kdkraOEc:B4i36v6kzyOLr9IPVEA:C; BDRCVFR[E6DhbwomKun]=9xWipS8B-FspA7EnHc1QhPEUf; H_PS_PSSID=60272_61027_61217_60853_61352_61391_61504_61527_61361_61610_61633; delPer=0; PSINO=3; BA_HECTOR=ag01048kal0h0h008l0k8lah1unh4n1jn6og71u; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; ab_sr=1.0.1_N2U2OTA1ZWI4ZTg4OGZmNzY0ZDIzMzMxMGRmNzVhMjU0NmFlODk0ZjUwZDQwOWFlNWViZmQ1YmQ5NDY1ZjUyNjg1YWViMDJiZjA4ZDQ2ZGY5MGRhMmI3N2M0YTI5ZDQ2NzYwZDhiZmRiOWRmOGRiZDc4YzI3MTkxYTYzOTBjZDE4MmI2MjdiMTgxY2FhNTViMGM0NWQ3YjQwZmMwMmRhNTU0MmQxNzAyYWQ5MDk2ZDVkMDM1MWU5M2NmNzE3YjcwYWYyOTczMjk5MmQ0N2FkYzQyOGIwOWMwYzBmMzBkMmM=; RT="z=1&dm=baidu.com&si=c5dec215-15ae-4134-916b-11ecda71bf52&ss=m5bwclvr&sl=5&tt=4o4&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=jn46"',
        }
    data = {
        'kw': e.get()
    }
    resualt = ["没有对应结果"]
    response = requests.post(url='https://fanyi.baidu.com/sug', headers=head, data=data)
    text_res = json.loads(response.text)
    english_ci =text_res['data']
    #print(english_ci)

    if english_ci != []:
        resualt = english_ci[0]['v'].split(';')
        l1.config(text = resualt[0])
    else:
        l1.config(text=resualt[0])
b=tk.Button(t,text = "翻译",command=tran)
l.place(x=135,y=10)
e.place(x=120,y=50)
b.place(x=175,y=90)
l1.place(x=1,y=125)
t.mainloop()
