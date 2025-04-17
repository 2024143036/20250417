import json
import time
from http.client import responses
from time import sleep

import requests

API_KEY="RGAPI-faf291a6-3083-4df0-85bf-9708d90f4be2"

HEADERS={"X-Riot-Token" : API_KEY}

STARTTIME="1736294400"
TYPE="ranked"
COUNT=100

with open("puuids_over_MASTER_tier.json","r",encoding="utf-8") as f:
    puuid_data=json.load(f)

sample_puuid=puuid_data[0]['CHALLENGER'][0]
print(f"첫번째 CALLENGER의 puuid : {sample_puuid}")

# 특정 puuid에 대해서 최근 100개의 Match Id 리스트를 얻어오는 함수
def get_match_list_single_100(puuid):
    base_url="https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/"
    url=f"{base_url}{puuid}/ids?startTime={STARTTIME}&type={TYPE}&start=0&count={COUNT}"
    responses=requests.get(url,headers=HEADERS)
    
    if responses.status_code==200:
        match_list=responses.json()
        return match_list
    else:
        raise Exception(f"Error: {responses.status_code}")

match_list=get_match_list_single_100(sample_puuid)
print(match_list)

def get_match_list_from_puuid(puuid):
    base_url="https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/"
    match_ids=[]
    start_idx=[]

    while True:
        url=f"{base_url}{puuid}/ids?startTime={STARTTIME}&type={TYPE}&start=0&count={COUNT}"
        responses = requests.get(url, headers=HEADERS)

        if responses.status_code == 200:
            match_list = responses.json()
            if not match_list:
                print(f"수집이 종료되었습니다. 현재까지 수정한 Match Id의 수는 {len(match_ids)}입니다.")
                break
            match_ids.extend(match_list)
            start_idx+=COUNT
            elif responses.status_code==429:
                print(f"사용 한도를 초과했습니다. 10초간 대기합니다.")
                time.sleep(10)
        else:
            print(f"요청 실패 : {responses.status_code}")
            break
        time.sleep(0.1)
    return match_ids
match_ids=get_match_list_from_puuid(sample_puuid)
print(match_ids,len(match_ids))


