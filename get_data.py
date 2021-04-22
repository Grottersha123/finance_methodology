import asyncio
import json

import grequests

query = '001X4354'
query = '001К1433|001К1692'
# query = '001U2684|001U4673|001U9290|001U9443|001U9541|001U9593|001U9760|001U9868|001U9910|001X0311|001X0576|001X0632|001X0643|001X0686|001X0918|001X1203|001X1275|001X1348|001X1354|001X1380|001X1681|001X1754|001X1915|001X2035|001X2072|001X2078|001X2159|001X2679|001X2741|001X2772|001X2780|001X2819|001X3038|001X3061|001X3069|001X3121|001X3843|001X3901|001X3912|001X3978|001X4146|001X4453|001X4500|001X4535|001X4723|001X5037|001X5044|001X5056|001X5058|001X5176|001X5244|001X5341|001X5481|001X5483|001X5620|001X5646|001X5685|001X5790|001X5863|001X5876|001X5911|001X6017|001X6019|001X6395|001X6511|001X6512|001X6793|001X7089|001X7200|001X7217|001X7283|001X7306|001X7332|001X7902|001X8695|001X8982|001X9426|001У0016|001У0254|001У0378|001У0837|001У1765|001У2059|001У2109|001У3374|001У3826|001У4817|001У4818|001У6103|001У7564|001У7786|001У9213|001У9387|001У9728|001Ц0440|001Ц1478|001Ц2475|001Ц6374|001Ч3397|001Щ0225|001Щ0829|001Щ4386|001Щ4527|001Щ4748|001Щ7674|001Щ8596|001Э2453'
# query = '001U2608|001U5572|001U7671|001U8212|001U8622|001U8899|001U9286|001U9311|001U9481|001U9587|001U9594|001X0007|001X0172|001X0273|001X0275|001X0966|001X1075|001X1193|001X1228|001X1365|001X1707|001X1903|001X2105|001X2286|001X2295|001X2418|001X2634|001X2728|001X2915|001X2956|001X3512|001X3532|001X3815|001X3987|001X4140|001X4141|001X4144|001X4283|001X4326|001X4329|001X4330|001X4354|001X4368|001X4456|001X4480|001X5029|001X5225|001X5312|001X5470|001X5712|001X5767|001X5835|001X5913|001X6047|001X6773|001X7213|001X7254|001X7265|001X7276|001X7279|001X7295|001X7307|001X7311|001X7690|001X8509|001X8653|001X8976|001X9085|001X9086|001X9149|001X9714|001X9827|001X9835|001В0655|001Г3469|001Г8840|001Ж4600|001У0836|001У1506|001У2479|001У3061|001У3164|001У3169|001У6441|001Ц2338|001Ц5961|001Ц6369|001Ч2390|001Ш0019|001Ш2914|001Ш5881|001Ш8866|001Ш9896|001Щ0884|001Щ4148|001Щ4468|001Щ4533|001Щ4575|001Щ4960|001Щ7526|001X4015|001X4018|001X6897|001X7312|001X9826|001Ч1271'

dict_orgs = {o : {"01012021": {}, "01012020": {}} for o in query.split('|')}
print(dict_orgs)
oovo = {
    'url': 'http://cntrl.iacmon.ru/oleg/rkfmoovo',
    'param': [ 'pkp_1', 'pkp_2', 'pkp_3', 'pkp_4', 'pkp_5', 'pfu_1', 'pfu_2', 'pfu_3', 'pfu_4', 'pfu_5', 'pfu_6', 'sp_1',
              'sp_1a', 'sp_2', 'sp_2a', 'sp_3', 'sp_4', 'sp_5', 'last']
}
no = {
    'url': 'http://cntrl.iacmon.ru/oleg/rkfmno',
    'param': ['pkp_1', 'pkp_2', 'pkp_3', 'pfu_1', 'pfu_2', 'pfu_3', 'pfu_5', 'pfu_6', 'pfu_7', 'sp_1', 'sp_2', 'sp_3', 'sp_4', 'sp_5', 'sp_6', 'sp_7', 'dp_1', 'dp_2']
}
#  url = 'http://cntrl.iacmon.ru/oleg/rkfmno'
def async_get_data(org='', query='', url=oovo['url']):


    # for r in grequests.imap(rs, size=16)
    #     print(r[0].status_code, r[0].url)
    res = grequests.post(url, data={"org": org, "query": query})
    # Do our list of things to do via async
    res = grequests.map([res])
    for cont in res:
        print(cont)
        data_js = json.loads(cont.content)
        data_key = data_js.keys()
        for d in data_key:
            print(d)
            ids_exitst = []
            if data_js[d]:
                for p in data_js[d]:
                    if p:
                        # if p.get('year'):
                        #     # if p['year'] == '2019':
                        #     #     dict_orgs[p['codesub']]["01012020"][d] = p['total']
                        #     if p['year'] == '2020':
                        #         dict_orgs[p['codesub']]["01012021"][d] = p['total']
                        if not p.get('period'):
                            dict_orgs[p['codesub']]["01012021"][d] = p['total']
                        else:
                            dict_orgs[p['codesub']]["01012020"][d] = p['total']
                        ids_exitst.append(p['codesub'])
            print(ids_exitst)
            print(dict_orgs)
            for id_ in org.split('|'):
                if id_ not in ids_exitst:
                    print(id_)
                    dict_orgs[id_]["01012021"][d] = 0
                    print(d,'sdf', dict_orgs[id_]["01012020"])
                    dict_orgs[id_]["01012020"][d] = 0


    #
    #     if isinstance(data_js, int):
    #         data_js = json.loads(data_js)
    #     for p in data_js['post']:
    #         params = {"post": p, "report_type": data_js["report_type"][0]["check"], "org": args['org']}
    #         rs.append(grequests.post(r'http://cntrl.iacmon.ru/oleg/pass', data=params))
    # res = grequests.map(rs)
    # res_response = [data_format(data) for data in res]

async def get_peramets_all(lst,org='001X3239|001X8880', url=''):
    for d in lst:
        print(d)
        async_get_data(org=org, query=d, url=url)
# 'pkp_1','pkp_2', 'pkp_3',




def get_data_from_api(lst=['pfu_1', 'pfu_2', 'pfu_3', 'pfu_4', 'pfu_5'], org='', url=''):
    print(query)
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(get_peramets_all(lst=lst, org=org, url=url))
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    import json
    with open('data.json', 'w') as f:
        json.dump(dict_orgs, f)

a = get_data_from_api(lst=oovo['param'], org=query, url=oovo['url'])
print(a)