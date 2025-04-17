from http.client import responses
from wsgiref.headers import Headers

import requests
import json



API_KEY="RGAPI-aada3a13-eeee-461c-b938-ddef373a4b56"
HEADERS={"X-Riot-Token" : API_KEY}

QUEUE="RANKED_SOLO_5x5"
TIERS=["MASTER","GRANDMASTER","CHALLENGER"]
REGION="kr"

def get_puuid_from_tier(queue,tier,region,division="I"):
    url=f"https://{region}.api.riotgames.com/lol/league-exp/v4/entries/{queue}/{tier}/{division}?page=1"
    print(url)
    response=requests.get(url,headers=HEADERS)
    if response.status_code==200:
        return response.json()
    else:
        raise Exception(f"Error : {response.status_code}")

# Master의 1 페이지에 대한 puuid가 담긴 RESPONSE BODY를 읽어들인다
#data_master=get_puuid_from_tier(QUEUE,TIERS[0],REGION)
#with open("master_player_info_from_python.json",'w',encoding='utf-8') as f:
#    json.dump(data_master,f,ensure_ascii=False,indent=4)


def get_puuid_from_tier_with_pages(queue,tier,region,division='I'):
    page=1
    all_data=[]
    while True:
        url=f"https://{region}.api.riotgames.com/lol/league-exp/v4/entries/{queue}/{tier}/{division}?page={page}"
        print(url)
        response=requests.get(url,headers=HEADERS)

        if response.status_code==200:
            all_data.extend(response.json())
        else:
            raise Exception(f"Error : {response.status_code}")

        if not response.json():
            break
        page+=1
    return all_data

data=get_puuid_from_tier_with_pages(QUEUE,TIERS[1],REGION)
with open(f"puuid_{TIERS[1]}_list.json","w",encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)



