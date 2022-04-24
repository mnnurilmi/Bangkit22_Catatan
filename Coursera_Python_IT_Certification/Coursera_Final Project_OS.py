import re
import operator
#import pandas as pd
import csv

f = open("C:/Users/Muhammad Nur Ilmi/OneDrive/Dokumen/Bangkit/Bangkit2022/Catatan/syslog.log",'r')
per_user={}
error={}
x=0

for l in f:
  a = re.search(r"ticky: INFO ([\w.*]*).*\((\w.*)\)",l.strip())
  if a!= None:
    if a.group(2) not in per_user.keys():
      per_user[a.group(2)] = {'INFO':1,'ERROR':0}
    else:
      per_user[a.group(2)]['INFO']+=1

  b = re.search(r"ticky: ERROR ([\w.*].*) \((\w.*)\)",l.strip())
  if b!= None:
    if b.group(1) not in error.keys():
      error[b.group(1)] = 1
    else:
      error[b.group(1)]+=1
    
    if b.group(2) not in per_user.keys():
      per_user[b.group(2)] = {'INFO':0,'ERROR':1}
    else:
      per_user[b.group(2)]['ERROR']+=1
      per_user[b.group(2)]['INFO']+=1
print(error)
print(per_user)

print()


sorted_error = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
sorted_error_list=[]
for x in sorted_error:
  a = []
  sorted_error_list.append([x[0],x[1]])
with open('error_message.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['Error','Count'])
    writer.writerows(sorted_error_list)
# df = pd.read_csv('error_message.csv')
# print(df.to_string()) 

sorted_per_user = sorted(per_user.items())
sorted_per_user_list = []
for x in sorted_per_user:
  a = []
  sorted_per_user_list.append([x[0],x[1]["INFO"],x[1]["ERROR"]])
print(sorted_per_user_list)
with open('user_statistics.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['Username', 'INFO', 'ERROR'])
    writer.writerows(sorted_per_user_list)
# df = pd.read_csv('user_statistics.csv')
# print(df.to_string()) 