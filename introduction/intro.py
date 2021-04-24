 import os
# import pprint
# import json
# import requests
# #This is the first request to call the Api courses.
# r=requests.get("https://saral.navgurukul.org/api/courses")
# data = r.json()
# #This is for making Json file 
# with open("pro.json","w") as f:
#     js=json.dump(data,f,indent=4)

# #This is For items of of the exercise
# # with open("pro.json","r") as file1:
# #     lod=json.load(file1)
# for i in range(0,66):
#     print(i+1,data["availableCourses"][i]['name'])
# user=int(input("enter the topic you want to do"))
# print(user,data["availableCourses"][user]['name'])
# topic_name=data["availableCourses"][user]['name']
# topic_id=data['availableCourses'][user]['id']

# print(user,data["availableCourses"][user]['id'])
# req=requests.get("https://saral.navgurukul.org/api/courses/"+topic_id+"/exercises")
# data1=req.json()
# with open("pro1.json","w") as f1:
#     s1=json.dump(data1,f1,indent=4)


# # with open("pro1.json","r") as file2:
# #     lod1=json.load(file2)
# length=len(data1['data'])
# for j in data1:
#     for k in range(0,length):
#         print("    ",k,data1[j][k]['name'])
# user1=int(input("enter the parent child topic you want to learn"))
# print(data1['data'][user1]['name'])
# length1=len(data1['data'][user1]["childExercises"])
# for l in range(0,length1):
#     print("    ",l,data1['data'][user1]["childExercises"][l]['name'])
#     # print("-----","slug=",dic['data'][user1]["childExercises"][l]['slug'])
# user3=int(input('enter the topic for that you wnat to find the slug'))
# slug_cont=data1['data'][user1]["childExercises"][user3]['slug']
# print(slug_cont)
# # pprint.pprint(dic['data'][1]["childExercises"][1]['name'])
    

# req=requests.get("https://saral.navgurukul.org/api/courses/"+topic_id+"/exercise/getBySlug?slug="+slug_cont)
# data3=req.json()
# print(req)

# with open("pro2.json","w") as f2:
#     js2=json.dump(data3,f2,indent=4)

# with open("pro2.json","r") as file4:
#     lod4=json.load(file4)
#     pprint.pprint(lod4)
#     pprint.pprint(lod4['content'])

   
















# #its a main code for navigation
# import os
# import pprint
# import json
# import requests
# #This is the first request to call the Api courses.
# r=requests.get("https://saral.navgurukul.org/api/courses")
# cources_data = r.json()
# #This is for making Json file 
# with open("pro.json","w") as f:
#     js=json.dump(cources_data,f,indent=4)

# #This is For items of of the exercise


# for i in range(0,len(cources_data["availableCourses"])):
#     print(0+i,cources_data["availableCourses"][i]['name'])
# select_data_cources=int(input("enter the topic you want to do"))
# print(select_data_cources,cources_data["availableCourses"][select_data_cources]['name'])
# topic_name=cources_data["availableCourses"][select_data_cources]['name']
# topic_id=cources_data['availableCourses'][select_data_cources]['id']

# print(select_data_cources,cources_data["availableCourses"][select_data_cources]['id'])
# req=requests.get("https://saral.navgurukul.org/api/courses/"+topic_id+"/exercises")
# exercise_data=req.json()
# with open("pro1.json","w") as f1:
#     s1=json.dump(exercise_data,f1,indent=4)

# length_of_exercise=len(exercise_data['data'])
# for j in exercise_data:
#     for k in range(0,length_of_exercise):
#         print("    ",k,exercise_data[j][k]['name'])
# ask=input("....enter the nevigation..for previous exercise press(p)...for next exercise press(n)")
# if ask=="p":
#     #this is for the cources
#     for i in range(0,len(cources_data["availableCourses"])):
#         print(0+i,cources_data["availableCourses"][i]['name'])
#     select_data_cources=int(input("enter the topic you want to do"))
#     print(select_data_cources,cources_data["availableCourses"][select_data_cources]['name'])

#     #This is for parents topic
#     for j in exercise_data:
#         for k in range(0,length_of_exercise):
#             print("    ",k,exercise_data[j][k]['name'])
        
#         select_data_exercise=int(input("enter the parent child topic you want to learn"))
#         print(exercise_data['data'][select_data_exercise]['name'])
#         # dic=lod1
#         length_of_childexercise=len(exercise_data['data'][select_data_exercise]["childExercises"])

#     #this is for child exercise
#         for l in range(0,length_of_childexercise):
#             print("    ",l,exercise_data['data'][select_data_exercise]["childExercises"][l]['name'])   
            
# elif ask=="n":
#     #This is for parents topic
#     select_data_exercise=int(input("enter the parent child topic you want to learn"))
#     print(exercise_data['data'][select_data_exercise]['name'])
#     # dic=lod1
#     length_of_childexercise=len(exercise_data['data'][select_data_exercise]["childExercises"])
#     for l in range(0,length_of_childexercise):
#          print("    ",l,exercise_data['data'][select_data_exercise]["childExercises"][l]['name'])
#     ask1=input("....enter the nevigation..for previous exercise press(p)...for next exercise press(n)")
#     if ask1=="p":
#         for j in exercise_data: 
#             for k in range(0,length_of_exercise):
#                 print("    ",k,exercise_data[j][k]['name'])

#         select_data_exercise=int(input("enter the parent child topic you want to learn"))
#         print(exercise_data['data'][select_data_exercise]['name'])
#         # dic=lod1
#         length_of_childexercise=len(exercise_data['data'][select_data_exercise]["childExercises"])
#         for l in range(0,l):
#              print("    ",l,exercise_data['data'][select_data_exercise]["childExercises"][l]['name'])   
#     elif ask1=="n":
#         print("sorry there is no next topic after it but you can acess the content")   

    
# select_child_content=int(input("enter the topic for the content "))
# slug_cont=exercise_data['data'][select_data_exercise]["childExercises"][select_child_content]['slug']
# req=requests.get("https://saral.navgurukul.org/api/courses/"+topic_id+"/exercise/getBySlug?slug="+slug_cont)
# length_of_childexercise=len(exercise_data['data'][select_data_exercise]["childExercises"])
# slag_call=req.json()
# select=0
# print(req)
# # print(slug_cont)
# with open("pro2.json","w") as f2:
#     js2=json.dump(slag_call,f2,indent=4)
# pprint.pprint(slag_call['content'])

# m=0
# while m<length_of_childexercise-1:
            
#     ask3=input("****enter the nevigation..for the content....for previous exercise press(p)...for next exercise press(n)") 
#     if select_child_content==0 and ask3=="p":
#         print("stop")
#         break


#     elif ask3=="p":
#         select_child_content=select_child_content-1
        
#     elif ask3=="n":
#         select_child_content=select_child_content+1

#     select_child_content=select_child_content-1
#     slug_cont=exercise_data['data'][select_data_exercise]["childExercises"][select_child_content]['slug']
#     req=requests.get("https://saral.navgurukul.org/api/courses/"+topic_id+"/exercise/getBySlug?slug="+slug_cont)
#     slag_call=req.json()
#     print(req)
#     # print(slug_cont)
#     with open("pro2.json","w") as f2:
#         js2=json.dump(slag_call,f2,indent=4)
#     pprint.pprint(slag_call['content'])


#     m=m+1







#for file existing 


# import os
# import pprint
# import json
# import requests
# #This is the first request to call the Api courses.
# file_exist=os.path.exists("pro1.json")
# print(file_exist)
# if file_exist==True:
#     with open("pro.json","r") as file1:
#         cources_data=json.load(file1)
#         for i in range(0,len(cources_data["availableCourses"])):
#             print(0+i,cources_data["availableCourses"][i]['name'])
#         select_data_cources=int(input("enter the topic you want to do"))
#         print(select_data_cources,cources_data["availableCourses"][select_data_cources]['name'])
#         topic_name=cources_data["availableCourses"][select_data_cources]['name']
#         topic_id=cources_data['availableCourses'][select_data_cources]['id']

#     if os.path.exists("pro1.json")==True:
#         with open("pro1.json","r") as file2:
#             exercise_data=json.load(file2)
#             length_of_exercise=len(exercise_data['data'])
#             for j in exercise_data:
#                 for k in range(0,length_of_exercise):
#                     print("    ",k,exercise_data[j][k]['name'])

#             select_data_exercise=int(input("enter the parent child topic you want to learn"))
#             print(exercise_data['data'][select_data_exercise]['name'])
#             length_of_childexercise=len(exercise_data['data'][select_data_exercise]["childExercises"])

#             #this is for child exercise
#             for l in range(0,length_of_childexercise):
#                 print("    ",l,exercise_data['data'][select_data_exercise]["childExercises"][l]['name'])   
    
#     elif os.path.exists("pro1.json")==False:
#         req=requests.get("https://saral.navgurukul.org/api/courses/"+topic_id+"/exercises")
#         exercise_data=req.json()
#         length_of_exercise=len(exercise_data['data'])
#         for j in exercise_data:
#             for k in range(0,length_of_exercise):
#                 print("    ",k,exercise_data[j][k]['name'])

        # select_data_exercise=int(input("enter the parent child topic you want to learn"))
        # print(exercise_data['data'][select_data_exercise]['name'])
        # length_of_childexercise=len(exercise_data['data'][select_data_exercise]["childExercises"])

        # #this is for child exercise
        # for l in range(0,length_of_childexercise):
        #     print("    ",l,exercise_data['data'][select_data_exercise]["childExercises"][l]['name'])  
    




# elif file_exist==False:
#     r=requests.get("https://saral.navgurukul.org/api/courses")
#     cources_data = r.json()
    
#     for i in range(0,len(cources_data["availableCourses"])):
#         print(0+i,cources_data["availableCourses"][i]['name'])
#     select_data_cources=int(input("enter the topic you want to do"))
#     print(select_data_cources,cources_data["availableCourses"][select_data_cources]['name'])
#     topic_name=cources_data["availableCourses"][select_data_cources]['name']
#     topic_id=cources_data['availableCourses'][select_data_cources]['id']
#     print(select_data_cources,cources_data["availableCourses"][select_data_cources]['id'])

    # if os.path.exists("pro1.json")==True:
    #     with open("pro1.json","r") as file2:
    #         exercise_data=json.load(file2)
#             length_of_exercise=len(exercise_data['data'])
#             for j in exercise_data:
#                 for k in range(0,length_of_exercise):
#                     print("    ",k,exercise_data[j][k]['name'])

#         select_data_exercise=int(input("enter the parent child topic you want to learn"))
#         print(exercise_data['data'][select_data_exercise]['name'])
#         length_of_childexercise=len(exercise_data['data'][select_data_exercise]["childExercises"])

#         #this is for child exercise
#         for l in range(0,length_of_childexercise):
#             print("    ",l,exercise_data['data'][select_data_exercise]["childExercises"][l]['name'])  
    

    # elif os.path.exists("pro1.json")==False:
        # req=requests.get("https://saral.navgurukul.org/api/courses/"+topic_id+"/exercises")
        # exercise_data=req.json()
        # length_of_exercise=len(exercise_data['data'])
        # for j in exercise_data:
        #     for k in range(0,length_of_exercise):
        #         print("    ",k,exercise_data[j][k]['name'])

#         select_data_exercise=int(input("enter the parent child topic you want to learn"))
#         print(exercise_data['data'][select_data_exercise]['name'])
#         length_of_childexercise=len(exercise_data['data'][user1]["childExercises"])

#         #this is for child exercise
#         for l in range(0,length_of_childexercise):
#             print("   








    


# if cousses.jsom == true:
#     read
#     data = s
# else:
#     api = call
#     data = StopAsyncIteration
# loop on data


# if parent.sj
# else
