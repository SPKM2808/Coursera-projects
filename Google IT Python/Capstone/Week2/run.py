#! /usr/bin/env python3
import os
import requests
data1=[]
for i in os.listdir('/data/feedback'):
	buff={}
	f=open('/data/feedback/'+i)
	lines=f.readlines()
	buff['title']=lines[0].strip()
	buff['name']=lines[1].strip()
	buff['date']=lines[2].strip()
	buff['feedback']=lines[3].strip()
	data1.append(buff)
	f.close()
	#print(data1)
	x=requests.post('http://35.194.55.88/feedback/',json=buff)
	#print(x)

	if x.status_code==201:
		print('Success')
	else:
		print('Fail')
