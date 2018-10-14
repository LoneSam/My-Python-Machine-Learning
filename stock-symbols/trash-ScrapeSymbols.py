import requests
import lxml.html as lh
import pandas as pd

url='https://www.nasdaq.com/screening/companies-by-name.aspx?A&pagesize=10000000'

#Create a handle, page, to handle the contents of the website
page = requests.get(url)

#Store the contents of the website under doc
doc = lh.fromstring(page.content)

#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')

#get the number of columns on the 1st line
num_cols = tr_elements[1]

#Create empty list
col=[]
i=0

#For each row, store each first element (header) and an empty list
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    #print '%d:"%s"'%(i,name)
    col.append((name,[]))
	
#Since out first row is the header, data is stored on the second row onwards
for j in range(1,len(tr_elements)):
    #T is our j'th row
	T=tr_elements[j]
    
    #If row is not of size 10, the //tr data is not from our table 
	if len(T)!= num_cols:
		break

	#i is the index of our column
	i=1
	#Iterate through each element of the row
	for t in T.iterchildren():
		try:
			data=t.text_content()
		except Exception as e:
			print("Error Processing Line:",i+1)
			print("Error:",e)
		#Check if row is empty
		if i>0:
		#Convert any numerical value to integers
			try:
				data=int(data)
			except:
				pass
		#Append the data to the empty list of the i'th column
		col[i][1].append(data)
		#Increment i for the next column
		i+=2



Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)

f= open("guru99.txt","w+")
f.writelines(df.head())
f.close() 