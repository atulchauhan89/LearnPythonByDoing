f = open("Writelist.txt","w")
list = ["lipika\n","ugain\n","sandeep\n","sanjeev"]
f.writelines(list)
print("All the lines from the list are written to the list")
f.close()