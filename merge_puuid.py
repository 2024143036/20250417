import json

with open("puuid_MASTER_list.json",'r',encoding='utf-8') as f:
    data_m=json.load(f)
with open("puuid_GRANDMASTER_list.json",'r',encoding='utf-8') as f:
    data_gm=json.load(f)
with open("puuid_CHALLENGER_list.json",'r',encoding='utf-8') as f:
    data_ch=json.load(f)

puuids={
    'MASTER' : [],
    'GRANDMASTER' : [],
    'CHALLENGER' : []
}

def get_puuids_from_list(data):
    puuid_list=[]
    for player in data:
        puuid_list.append(player['puuid'])
    return puuid_list

puuids['MASTER']=get_puuids_from_list(data_m)
puuids['GRANDMASTER']=get_puuids_from_list(data_gm)
puuids['CHALLENGER']=get_puuids_from_list(data_ch)
print(len(puuids['MASTER']),len(puuids['GRANDMASTER']),len(puuids['CHALLENGER']))
with open('puuids_over_MASTER_tier.json','w',encoding='utf-8') as f:
    json.dump([puuids], f, ensure_ascii=False, indent=4)


