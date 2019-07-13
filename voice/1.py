import os
os.system('python asr_json.py')
with open('/Users/liuminghao/voice/result.txt') as f:
    file = f.readlines()

num = 0
for i in file[0].split(','):
    if num == 3:
        name = i[11:-2]
        print(i[11:-2])
        break
    num=num+1

import datetime
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

try:
    api = Connection(appid='YOUR_APPID_HERE', config_file=None)
    response = api.execute('findItemsAdvanced', {'keywords': name})

    assert(response.reply.ack == 'Success')
    assert(type(response.reply.timestamp) == datetime.datetime)
    assert(type(response.reply.searchResult.item) == list)

    item = response.reply.searchResult.item[0]
    assert(type(item.listingInfo.endTime) == datetime.datetime)
    assert(type(response.dict()) == dict)

except ConnectionError as e:
    #print(e)
   # print(e.response.dict())
    with open('/Users/liuminghao/access.txt') as b:
        list1=[]
        txt = b.readline()
        while txt!="\n":
            dict2={'name':0,'price':0,'holder':0,'ID':0}
            txt = str(txt[1:])
            txt = txt.split(',')
            dict2['name']=txt[0]
            dict2['price']=txt[1]
            dict2['holder']=txt[2]
            dict2['ID']=txt[3][:-2]
            print(txt[0],txt[1],txt[2],txt[3][:-2])
            list1.append(dict2)
            txt = b.readline()
    print(list1)
            
#运行一下程序
os.system('python asr_json.py')
with open('/Users/liuminghao/voice/which.txt') as f:
    file = f.readlines()

num = 0
for i in file[0].split(','):
    if num == 3:
        name = i[11:-2]
        print(i[11:-2])
        break
    num=num+1

name='3'

for i in list1:
    if name==i['ID']:
        print(i['name'])
        break

#运行一下程序
os.system('python asr_json.py')
with open('/Users/liuminghao/voice/which.txt') as f:
    file = f.readlines()

num = 0
for i in file[0].split(','):
    if num == 3:
        name = i[11:-2]
        print(i[11:-2])
        break
    num=num+1

print('Do you want to buy',i['name'],'?')
name ='yes'

if name=='yes':
    print('Success to buy!')
else:
    print('Fail!')
        
