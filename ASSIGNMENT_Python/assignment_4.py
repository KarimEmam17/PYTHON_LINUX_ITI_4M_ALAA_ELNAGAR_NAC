import os
def  get_data_base():    
    The_File=open("Data_base_Pola_iti_shop.txt","r+")
    get_data_base.small_sold_item=int(The_File.readline().split(" ")[-1])
    get_data_base.meduim_sold_item=int(The_File.readline().split(" ")[-1])
    get_data_base.large_sold_item=int(The_File.readline().split(" ")[-1])
    get_data_base.small_cost_item=int(The_File.readline().split(" ")[-1])
    get_data_base.meduim_cost_item=int(The_File.readline().split(" ")[-1])
    get_data_base.large_cost_item=int(The_File.readline().split(" ")[-1])
    get_data_base.total_sold_item=int(The_File.readline().split(" ")[-1])
    The_File.close()

def listed_data_base():
    The_File = open("Data_base_Pola_iti_shop.txt","r")
    listed_data_base.data_list = list(map(lambda x: x.split(" "), The_File.readlines())) 
    The_File.close()

def  assign_data_base():
    The_File = open("Data_base_Pola_iti_shop.txt","w")
    The_File.write(str("".join(" ".join(x) for x in listed_data_base.data_list)))
    The_File.close()

get_data_base()
listed_data_base()
pola_iti_shop_dict = { "small":40,
   "medium":50 ,
   "large":60, }

pola_iti_shop_dict_cost = { "small":2,
   "medium":3 ,
   "large":5,
   "total":0, }
pola_iti_shop_dict["small"]=get_data_base.small_sold_item
pola_iti_shop_dict["medium"]=get_data_base.meduim_sold_item
pola_iti_shop_dict["large"]=get_data_base.large_sold_item
pola_iti_shop_dict_cost["small"]=get_data_base.small_cost_item
pola_iti_shop_dict_cost["medium"]=get_data_base.meduim_cost_item
pola_iti_shop_dict_cost["large"]=get_data_base.large_cost_item
pola_iti_shop_dict_cost["total"]=get_data_base.total_sold_item
#for x in range(7,15,2):
#    pola_iti_shop_dict[listed_data_base.data_list[x][0]]=int(listed_data_base.data_list[x][-1])
#    pola_iti_shop_dict_cost[listed_data_base.data_list[x+1][0]]=int(listed_data_base.data_list[x+1][-1])
pola_iti_shop=int(input("welcome to iti shop please select the mode \ncustomer=1\nUser=2\nexit=0\n"))
while(pola_iti_shop):
    if (pola_iti_shop==1):
        customer_status_iti_shop=int(input("To show our products press=1 \nTo Buy from our products press=2  \nto print the bill press=3 \nexit press=4\n"   ))
        while(customer_status_iti_shop!=4):
            if(customer_status_iti_shop==1 ):
                print(pola_iti_shop_dict_cost)
                customer_status_iti_shop=int(input("To show our products press=1 \nTo Buy from our products press=2  \nto print the bill press=3 \nexit press=4\n"   ))
            elif (customer_status_iti_shop==2):
                small=int(input("how many  small caps u  want to buy ?"))
                medium=int(input("how many medium caps u  want to buy ?"))
                large=int(input("how many large caps u  want to buy ?"))
                pola_iti_shop_dict["small"]=pola_iti_shop_dict["small"]-small
                pola_iti_shop_dict["medium"]=pola_iti_shop_dict["medium"]-medium
                pola_iti_shop_dict["large"]=pola_iti_shop_dict[ "large"]-large
                customer_status_iti_shop=int(input("To show our products press=1 \nTo Buy from our products press=2  \nto print the bill press=3 \nexit press=4\n"   ))
            elif(customer_status_iti_shop==3 ):
                bill=(pola_iti_shop_dict_cost["small"]*small)+(pola_iti_shop_dict_cost["medium"]*medium)+(pola_iti_shop_dict_cost["large"]*large)
                pola_iti_shop_dict_cost["total"]=pola_iti_shop_dict_cost["total"]+bill
                print("the bill  equal = %d \n "%(bill))
                customer_status_iti_shop=int(input("To show our products press=1 \nTo Buy from our products press=2  \nto print the bill press=3 \nexit press=4\n"   ))
            elif(customer_status_iti_shop==4 ): 
                listed_data_base.data_list[0][-1]=pola_iti_shop_dict["small"] 
                listed_data_base.data_list[1][-1]=pola_iti_shop_dict["medium"] 
                listed_data_base.data_list[2][-1]=pola_iti_shop_dict["large"] 
                listed_data_base.data_list[3][-1]=pola_iti_shop_dict_cost["small"] 
                listed_data_base.data_list[4][-1]=pola_iti_shop_dict_cost["medium"]  
                listed_data_base.data_list[5][-1]=pola_iti_shop_dict_cost["large"]    
                listed_data_base.data_list[6][-1]=pola_iti_shop_dict_cost["total"] 
                #for x in range(7,15,2):
                #    listed_data_base.data_list[x][-1]=str(pola_iti_shop_dict[listed_data_base.data_list[x][0]])+"\n"
                #   listed_data_base.data_list[x][1]=":"
                #    listed_data_base.data_list[x+1][-1]=str(pola_iti_shop_dict_cost[listed_data_base.data_list[x+1][0]])+"\n"
                #    listed_data_base.data_list[x+1][1]=":" 
                assign_data_base()             
                break
        pola_iti_shop=int(input("welcome to  iti  shop please select  the moode  customer=1 User=2 press exit=0\n"))
        
    elif(pola_iti_shop==2):
        user_status_iti_shop=int(input("To show our products and cost press=1 \nAdd new product and it's cost press=2  \nChange cost press=3 exit=4\n"   ))
        while(user_status_iti_shop!=4):
            if(user_status_iti_shop==1 ):
                    print(pola_iti_shop_dict_cost)
                    print(pola_iti_shop_dict)
                    user_status_iti_shop=int(input("To show our products and cost press=1 \n Add new product and it's cost press=2  \n Change cost press=3 exit=4"   ))
            elif(user_status_iti_shop==2):
                new_product=input("what  is the name of the new size? ")
                num_items=int(input("how many items did  we have? "))
                product_cost=int(input("what is the cost?"))
                pola_iti_shop_dict[new_product]=num_items
                pola_iti_shop_dict_cost[new_product]=product_cost
                #x=7
                #listed_data_base.data_list[x][0]=new_product
                #listed_data_base.data_list[x][1]=":"
                #listed_data_base.data_list[x][1]=str(num_items)
                #listed_data_base.data_list[x+1][0]=new_product
                #listed_data_base.data_list[x+1][1]=":"
                #listed_data_base.data_list[x+1][1]=str(product_cost)
                #x=x+2
                user_status_iti_shop=int(input("To show our products and cost press=1 \n Add new product and it'scost press=2  \n Change cost press=3 exit=4"   ))
            elif(user_status_iti_shop==3):
                the_product=input("what  is the name of the  product ?")
                product_new_cost=int(input("what is the new cost?"))
                pola_iti_shop_dict_cost[the_product]= product_new_cost
                #listed_data_base.data_list[x+1][0]=the_product
                #listed_data_base.data_list[x+1][1]=":"
                #listed_data_base.data_list[x+1][1]=str(product_new_cost)          
                user_status_iti_shop=int(input("To show our products and cost press=1 \n Add new product and it'scost press=2  \n Change cost press=3 exit=4"   ))
            elif(customer_status_iti_shop==4 ): 
                listed_data_base.data_list[0][-1]=pola_iti_shop_dict["small"] 
                listed_data_base.data_list[1][-1]=pola_iti_shop_dict["medium"] 
                listed_data_base.data_list[2][-1]=pola_iti_shop_dict["large"] 
                listed_data_base.data_list[3][-1]=pola_iti_shop_dict_cost["small"] 
                listed_data_base.data_list[4][-1]=pola_iti_shop_dict_cost["medium"]  
                listed_data_base.data_list[5][-1]=pola_iti_shop_dict_cost["large"]    
                listed_data_base.data_list[6][-1]=pola_iti_shop_dict_cost["total"] 
                #for x in range(7,15,2):
                #    listed_data_base.data_list[x][-1]=str(pola_iti_shop_dict[listed_data_base.data_list[x][0]])+"\n"
                #   listed_data_base.data_list[x][1]=":"
                #    listed_data_base.data_list[x+1][-1]=str(pola_iti_shop_dict_cost[listed_data_base.data_list[x+1][0]])+"\n"
                #    listed_data_base.data_list[x+1][1]=":" 
                assign_data_base()
                break
        pola_iti_shop=int(input("welcome to   pola iti  shop please select  the moode  customer=1 User=2 press exit=0\n"))