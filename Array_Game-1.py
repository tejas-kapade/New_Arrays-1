arr = []
#created by Tejas Kapade 
#18 Dec 2020 / 10:48pm
#Powered By Andro Coder
#this code demonstrate the adding items in array list

print("Create array list !!")
print("Only numbers are acceptable \nEntered numbers are added in arrays! \n")
cm = True
while(True):
    try:
    	add=int(input("Add items in array, or type 0 to end list___"))
    	if(add == 0):
    		cm= False
    	else:
    		arr.append(add)
    	if(cm == False):
    		print("\nYour Array list , containig ",len(arr)," items is \n\n      ",arr)
    		break
    except:
    	print("invalid syntax, Try again__")
