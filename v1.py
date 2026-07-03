try:

 loop = 1
 hist = "no data found"
 expense = 0
 
 while(loop == 1):
 
  print("1. today data\n")
  print("2. yesterday exp\n")
  print("3. total expenditure\n")
  
  choice = int(input("enter your choice\n"))
  
  if(choice == 1):
  
   trans = int(input("enter no of transactions:\n"))

   if(trans>0):

    exp = {}

    for i in range(trans):
    
     entry = 1
    
     while(entry == 1):
    
      spent = input("enter item name\n").strip()
      data = spent.lower()
      money = int(input("enter money spent on it\n"))

      if(money>0):
     
       entry = 0

       if data in exp:
    
        exp[data] += money 
    
       else: 
   
        exp[data] = money 

      else:

       print("spending cant be negative or zero\n") 

    maxspend = 0
    mostspend = []
    total = 0
    
    for mat,value in exp.items():
     
     print(mat,"--> \n",value)
     total += value
     
     if (value>maxspend):

      maxspend = value
      mostspend = [mat] 

     elif(value == maxspend):

      mostspend.append(mat) 

    print("highest spend on:\n")
    
    hist = total
    expense += total
    
    for high in mostspend:

     print(high,"of",maxspend,"\n")

   else:

    print("there should be atleast one transaction\n")
    
  elif(choice == 2):
   
   print(hist)
   
  elif(choice == 3):
  
   loop = 0
   
   print("total expenditue from start\n",expense)
   
   print("want to continue?\n")
   
   print("1. yes\n")
   print("2. no\n")
   
   cont_choice = int(input("enter choice\n"))
   
   if(cont_choice == 1):
   
    loop = 1
    
   elif(cont_choice == 2):
   
    print("1. reset\n")
    print("2. end\n")
    
    final_choic = int(input("enter choice\n"))
    
    if(final_choic == 1):
    
     loop = 1
     hist = ["no data found"]
     expense = 0
     
    elif(final_choic == 2):
    
     loop = 0
     print("bye, thank for visit\n")
    
    else:
     
     print("enter correct choice\n")
     
     
   else:
   
    print("enter correct choice\n")

  else:
   
   print("enter correct choice\n")
   
except Exception as e:

 print("error occur\n",e)

