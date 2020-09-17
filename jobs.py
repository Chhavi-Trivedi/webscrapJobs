import requests
import bs4
print("\n\n")
print(('WELCOME TO "MY INTERNSHIP FILTERED" PORTAL').center(100,"*"),"\n\n")
city=''
nature=''
selected_category=''
city_choice=0
nature_choice=0
category_choice=0
choice_dict={1:"city",2:"nature",3:"category"}
print("ENTER THE CODE OF CRITERIONS YOU WANT TO FILTER FROM THE FOLLOWINGS : ")
for key,value in choice_dict.items():
    print(key," : ",value.upper())
code_list=input("ENTER YOUR CODE(S) HERE(SEPERATED BY COMMA) : ").split(",")
for code in code_list:
    if code=='1':
        city_choice=1
    elif code=='2':
        nature_choice=1
    elif code=='3':
        category_choice=1
       

#CITY
        
 
while(city_choice==1):
 if city=='':
     
  temp=input("enter the city you want an internship at : ".upper()).replace(" ","%20")
  city=temp.lower()
 else:
  temp=input("enter the city you want an internship at : ".upper())   
  if temp in city:
    print("PLEASE ENTRY UNIQUE CITY NAME ")
  else:  
    city=city+','+temp.lower()
 choice=input("DO YOU WANT TO CHOOSE MORE CITIES(YES/NO) : ")
 if choice.lower()=="yes":
     city_choice=1
 elif choice.lower()=="no":
     city_choice=0
 else:
     print(" ENTRY IS NOT VALID ".center(100,"*"))
 

#NATURE
while(nature_choice==1):   
  nature_dict={1:"PART TIME",2:"WORK FROM HOME"}
  print("ENTER THE CODE OF YOUR PREFERENCE FROM THE FOLLOWING :")
  for key,value in nature_dict.items():
     print(str(key)+" : "+value)
  code=int(input("PLEASE ENTER YOUR CODE HERE : "))
  if code not in nature_dict.keys():
      print("PLEASE ENTER A VALID KEY".center(100,"*"))
  else:    
   nature=nature_dict.get(code).lower().replace(" ","-")
   nature_choice=0 
if nature!='':
  nature=nature+"-"

#CATEGORY

while(category_choice==1):
 with open("category.txt",'r') as fp:
    category_dict={}
    code=1
    lines=fp.readlines()
    for line in lines:
           category=line.strip("\n")
           category_dict.update({code:category})
           code+=1
    C=input("DO YOU REQUIRE LIST OF CODE WISE CATEGORY TO CHOOSE CATEGORY FROM ?(Y/N) ")
    if C.lower()=='y':
     for key,value in category_dict.items():
        print(str(key)+" : "+value)
    elif C.lower()=='n':
        pass
    else:
        print("PLEASE ENTER VALID INPUT".center(80,"*"))
        continue
    category_code=int(input("PLEASE ENTER THE CATEGORY CODE HERE : "))
    if category_code not in category_dict.keys():
        print("PLEASE ENTER VALID CATEGORY CODE".center(100,"*"))
        continue
    else:
     if selected_category=='':
        selected_category=(category_dict.get(category_code).lower()).replace(" ","%20").replace("/","%2F")
     else:
        selected_category=selected_category+","+(category_dict.get(category_code).lower()).replace(" ","%20").replace("/","%2F")      
   

    choice=input("DO YOU WANT TO CHOOSE MORE CATEGORIES(YES/NO) : ").lower()
 if choice=="yes":
     category_choice=1
 elif choice=="no":
     category_choice=0
 else:
     print("ENTRY IS NOT VALID".center(80,"*"))
if selected_category!='':
    selected_category+="-"


company=input("enter the company you want to interned at : ".upper())
count=0
for i in range(1,11):
 if(nature=='' and city=='' and selected_category==''):                                     #none
   url='https://internshala.com/internships/'+"/page-"+str(i)
 elif(nature=='' and city=='' and selected_category!=''):                                   #category
   url='https://internshala.com/internships/'+selected_category+'internship'+"/page-"+str(i)
 elif(nature=='' and city!='' and selected_category==''):                                   #city
   url='https://internshala.com/internships/'+"internship-in-"+city+"/page-"+str(i)
 elif(nature!='' and city=='' and selected_category==''):                                   #nature
   url='https://internshala.com/internships/'+nature+"jobs"+"/page-"+str(i)
 elif(nature!='' and city!='' and selected_category==''):                                   #nature+city
   url='https://internshala.com/internships/'+nature+"jobs-in-"+city+"/page-"+str(i)   

 elif(nature=='' and city!='' and selected_category!=''):                                   #city+category
  url='https://internshala.com/internships/'+selected_category+'internship-in-'+city+"/page-"+str(i)  
 elif(nature!='' and city=='' and selected_category!=''):                                   #nature+category
   url='https://internshala.com/internships/'+nature+selected_category+'jobs'+"/page-"+str(i) 
 else:                                                                                      #all
  url='https://internshala.com/internships/'+nature+selected_category+'jobs-in-'+city+"/page-"+str(i)     


 page = requests.get(url)
 soup=bs4.BeautifulSoup(page.text,'lxml')
 for i in soup.select('.link_display_like_text'):
        if company in i.text:
            count+=1

print("RESULTS".center(80,"*"))
print("There are in total ",count," internship available as per your need")
