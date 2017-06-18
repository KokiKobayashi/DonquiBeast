#!/usr/bin/env/bin/python3
# coding: utf-8
 
# モジュールインポート
import json
import urllib3

def get():
    # 天気取得のURL設定
    # cityに地域コードを設定
    city = "080010"
    # 取得URLを生成
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=%s' % city
    http = urllib3.PoolManager()
 
    try:
        # 天気データ取得
        # 最初に指定URLのデータ取得
        ### response = urllib.urlopen(url)
        response = http.request('GET', url)
        # jsonデータ取得
        ### weather = json.loads(response.read())
        weather = json.loads(response.data.decode('utf-8'))
 
        # 取得したデータを表示
        # titleとforecastsの最初の要素のtelopを表示
        print (weather['title'] + " : " + weather['forecasts'][0]['telop'])
        
 
    finally:
        response.close()
        return (weather['forecasts'][0]['telop'])
    
