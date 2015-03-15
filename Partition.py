import time

count=0
def Partition(n,m,j):
	global List
	global count
	if n==0:
		#print(List)
		count+=1

	for i in range(m,0,-1):
		
		if n<i:
			continue
		List[j]=i
		
		Partition(n-i,i,j+1)
		List[j]=0

	return
	

if __name__=="__main__":
	
	start_time = time.time()
	p=int(input("enter an integer:"))
	List =[0 for i in range(0,p)]
	Partition(p,p,0)
	print(count)
	print("--- %s seconds ---" % (time.time() - start_time))
