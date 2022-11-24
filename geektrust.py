from sys import argv
def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines(
    for line in lines:
        #split the line into commands
        command=line.split(' ')
        for i in range(len(command)):
        	command[i]=''.join(command[i].split())
        #for adding items in basket
        if(command[0] in add):
        	basket.setdefault(command[1],0)
        	temp=basket[command[1]]+int(command[2])
        	if(temp>maxQuantity[Listeditems[command[1]]['Category']]):
        		#tag print(str(basket)+command[1]+command[2])
        		print('ERROR_QUANTITY_EXCEEDED')
        	else:
        		basket[command[1]]+=int(command[2])
        		print('ITEM_ADDED')
        #calculating and printing the result
        elif(command[0] in prints):
        	total=0
        	discount=0
        	output = ''
        	for item in basket:
        		discount=discount+((Listeditems[item]['Discount']*Listeditems[item]['Price'])*basket[item])
        		total=total+(Listeditems[item]['Price']*basket[item])
        	if(total>=1000):
        		total=total-discount
        	else:
        		discount=0
        	if(total>=3000):
        		total=total-(total*0.05)
        	print('TOTAL_DISCOUNT '+str("%.2f"%discount))
        	total=total+(total*0.1)
        	print('TOTAL_AMOUNT_TO_PAY '+str("%.2f"%total))
        	print() #just for legibility
        	basket.clear()
        #irrelevant input
        else:
        	print('Command not understood')
        #process the input command and get the output
if __name__ == "__main__":
    main()
