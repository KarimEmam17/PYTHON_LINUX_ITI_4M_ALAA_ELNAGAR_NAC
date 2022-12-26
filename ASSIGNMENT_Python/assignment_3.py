iti_shop_dict = { "apple":40,
   "bannaa":50 ,
   "cherry":60, }
iti_shop_dict_cost = { "apple":1,
   "bannaa":2 ,
   "cherry":5, }
iti_shop=int(input("welcome to  iti  shop please select  the moode  customer=1 User=2 press exit=0\n"))
while(iti_shop):
    if (iti_shop==1):
        customer_status_iti_shop=int(input("To show our products press=1 \nTo Buy from our products press=2  \nto print the bill press=3 \nexit press=4\n"   ))
        while(customer_status_iti_shop!=4):
            if(customer_status_iti_shop==1 ):
                print(iti_shop_dict_cost)
                customer_status_iti_shop=int(input("To show our products press=1 \nTo Buy from our products press=2  \nto print the bill press=3 \nexit press=4\n"   ))
            elif (customer_status_iti_shop==2):
                apple=int(input("how many apples u  want to buy ?"))
                bannaa=int(input("how many bannaae u  want to buy ?"))
                cherry=int(input("how many cherries u  want to buy ?"))
                iti_shop_dict["apple"]=iti_shop_dict["apple"]-apple
                iti_shop_dict["bannaa"]=iti_shop_dict["bannaa"]-bannaa
                iti_shop_dict["cherry"]=iti_shop_dict["cherry"]-cherry
                customer_status_iti_shop=int(input("To show our products press=1 \nTo Buy from our products press=2  \nto print the bill press=3 \nexit press=4\n"   ))
            elif(customer_status_iti_shop==3 ):
                bill=(iti_shop_dict_cost["apple"]*apple)+(iti_shop_dict_cost["bannaa"]*bannaa)+(iti_shop_dict_cost["cherry"]*cherry)
                print("the bill  equal = %d \n "%(bill))
                customer_status_iti_shop=int(input("To show our products press=1 \nTo Buy from our products press=2  \nto print the bill press=3 \nexit press=4\n"   ))
            elif(customer_status_iti_shop==4 ): 
                break
        iti_shop=int(input("welcome to  iti  shop please select  the moode  customer=1 User=2 press exit=0\n"))
        
    elif(iti_shop==2):
        user_status_iti_shop=int(input("To show our products and cost press=1 \nAdd new product and it'scost press=2  \nChange cost press=3 exit=4\n"   ))
        while(user_status_iti_shop!=4):
            if(user_status_iti_shop==1 ):
                    print(iti_shop_dict_cost)
                    print(iti_shop_dict)
                    user_status_iti_shop=int(input("To show our products and cost press=1 \n Add new product and it'scost press=2  \n Change cost press=3 exit=4"   ))
            elif(user_status_iti_shop==2):
                new_product=input("what  is the name of the new product ")
                num_items=int(input("how many items did  we have "))
                product_cost=int(input("what is the cost?"))
                iti_shop_dict[new_product]=num_items
                iti_shop_dict_cost[new_product]=product_cost
                user_status_iti_shop=int(input("To show our products and cost press=1 \n Add new product and it'scost press=2  \n Change cost press=3 exit=4"   ))
            elif(user_status_iti_shop==3):
                the_product=input("what  is the name of the  product ?")
                product_new_cost=int(input("what is the new cost?"))
                iti_shop_dict_cost[the_product]= product_new_cost
                user_status_iti_shop=int(input("To show our products and cost press=1 \n Add new product and it'scost press=2  \n Change cost press=3 exit=4"   ))
            elif(customer_status_iti_shop==4 ): 
                break
        iti_shop=int(input("welcome to  iti  shop please select  the moode  customer=1 User=2 press exit=0\n"))




