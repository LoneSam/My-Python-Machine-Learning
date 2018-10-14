import pandas as pd

f=open("companylist.csv","r")
lines=f.readlines()

headers=lines[0].split('",')[:-1]

print(headers)

col=[]
i=0

for h in headers:
	col.append((h,[]))

rows=lines[1:]
for r in rows:
	vals=r.split('","')
	vals[0]=vals[0].replace('"','')
	vals[7]=vals[7].replace('",\n','')
	print(vals)
	for v in vals:
		col[i][1].append(v)
		i+=1
	i=0

Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)
print(df.head(20))
f.close()