import json
import asyncio
import grequests


# query = '001X3239|001X8880'
query = '001X4354|001Щ8596'
dict_orgs = {o : {"01012021": {}, "01012020": {}} for o in query.split('|')}
print(dict_orgs)
#  url = 'http://cntrl.iacmon.ru/oleg/rkfmno'
def async_get_data(org='', query='', url='http://cntrl.iacmon.ru/oleg/rkfmoovo'):


    # for r in grequests.imap(rs, size=16)
    #     print(r[0].status_code, r[0].url)
    res = grequests.post(url, data={"org": org, "query": query})
    # Do our list of things to do via async
    res = grequests.map([res])
    for i in res:
        print(i.content)
        data_js = json.loads(i.content)
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
                            dict_orgs[p['codesub']]["01012020"] = p['total']
                        ids_exitst.append(p['codesub'])
            for id_ in org.split('|'):
                if id_ not in ids_exitst:
                    print(id_)
                    dict_orgs[id_]["01012021"][d] = 0
                    dict_orgs[id_]["01012020"][d] = 0


    #
    #     if isinstance(data_js, int):
    #         data_js = json.loads(data_js)
    #     for p in data_js['post']:
    #         params = {"post": p, "report_type": data_js["report_type"][0]["check"], "org": args['org']}
    #         rs.append(grequests.post(r'http://cntrl.iacmon.ru/oleg/pass', data=params))
    # res = grequests.map(rs)
    # res_response = [data_format(data) for data in res]

async def get_peramets_all(lst,org='001X3239|001X8880'):
    for d in lst:
        print(d)
        async_get_data(org=org, query=d)
# 'pkp_1','pkp_2', 'pkp_3',




def get_data_from_api(lst=['pfu_1', 'pfu_2', 'pfu_3', 'pfu_4', 'pfu_5'], org=''):
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(get_peramets_all(lst=lst, org=org))
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    import json
    with open('data.json', 'w') as f:
        json.dump(dict_orgs, f)

a = get_data_from_api(lst=['pkp_1', 'pkp_2', 'pkp_3', 'pfu_1', 'pfu_2', 'pfu_3', 'pfu_4', 'pfu_5', 'pfu_6', 'sp_1', 'sp_1a', 'sp_2', 'sp_2a','sp_3', 'sp_4', 'sp_5'], org=query)
print(a)