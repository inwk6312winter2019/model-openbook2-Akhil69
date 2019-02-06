file = open("Street_Centrelines.csv","r")
def list_tuple():
	for line in file:
		line=line.split(',')
		res=(line[2],line[4],line[6],line[7])
		print(res)
list_tuple()

'''Here getting the result as a dictonary
 were key as maintainence and values no.of streets.'''

def maintain_hist(): 
	hist_type = dict()
	for line in file:
		line=line.split(',')
		res=(line[12])
		if res not in hist_type:
			hist_type[res]=1
		else:
			hist_type[res]+=1
	print(hist_type)
maintain_hist()

#Unique owners list

def owners():
	lst=[]
	for line in file:
		line=line.split(',')
		res=line[11]
		if res not in lst:
			lst.append(res)
	print(lst)

owners()

# street list and classes

def Street():
	ls_street=[]
	for line in file:
		line=line.split(',')
		res=line[10]
		if res not in ls_street:
			ls_street.append(res)
	print(ls_street)
	
Street()
