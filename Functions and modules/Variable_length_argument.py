def college(name,*information):                       #information is a variable length argument
    print("Name of student :",name)
    print("Informations of student :")
    for i in information :
        print(i)

college("Shubham","From Lucknow","Roll No: 12345")        #two argument are passed as variable length argument