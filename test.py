import re
from subprocess import PIPE,Popen
 
 
p1=Popen(["dmesg"], stdout=PIPE)
out,error=p1.communicate()
list_out=out.decode('ascii').split('\n')
d = {}
 
for i in list_out:
	match=re.findall(r'\S+\s+(\S+)\:\s+(\S+)\s+\S+\s+\S+\s+\S+\s+(\S+)', i)
    	if match:
		proc,flag,drive=match[0]
	else:
		continue
	if proc in d:
     		pass
 	else:
		d[proc]={flag :1, 'disk' : [drive]}

	if flag in d[proc]:
		d[proc][flag]+=1
	else:
		d[proc][flag]=1
	if drive not in d[proc]['disk']:
		d[proc]['disk'].append(drive)

print(d)

for i in d:
	#print(i)
	details = d[i]
	print(i)
	#for items in sorted(details.items(), key = lambda x: x[0], reverse=False):
	for detail in sorted(details):
		#print("{0}\t{1}".format(items[0], items[1]), end='')
		print("{0}\t{1}".format(detail, details[detail]))
	#raise SystemExit
	print("====================\n")
