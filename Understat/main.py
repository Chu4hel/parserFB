import requests
from bs4 import BeautifulSoup
import json
#import pandas as pd
#from pandas import json_normalize
from setting import base_url, match_id
import helper as hp

#base_url = 'https://Understat.com/match/'

#match = '22336'

for match in match_id:
    url = base_url+match

    res = requests.get(url)
    soup = BeautifulSoup(res.content, features="html.parser")
    scripts = soup.find_all('script')

    strings = scripts[1].string
    strings[0:1000]

    str_start = strings.index("('")+2
    str_end = strings.index("')")
    json_data = strings[str_start:str_end]
    json_data = json_data.encode('utf8').decode('unicode_escape')

    data = json.loads(json_data)

    """dp = ['h_goals': int(data['h'][0]['h_goals']), 'a_goals': data['h'][0]['a_goals'], "h_team"=data['h'][0]['h_team'], "a_team"=data['h'][0]['a_team']]
    for command in data:
        for moments in data["{}".format(command)]:
            if moments['result']=='Goal' and moments['h_a']==command: dp["{}".format(command)]+=1"""

    hp.insertdb(where='accounts_matches',
                 data1="{},{},{},{},{}".format('date','score_home','score_away','team_home_id', 'team_away_id'),
                 data2="'{}',{},{},'{}','{}'".format(data['h'][0]['date'], data['h'][0]['h_goals'], data['h'][0]['a_goals'], data['h'][0]['h_team'], data['h'][0]['a_team']))
print("thats all")

