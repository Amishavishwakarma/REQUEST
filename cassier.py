import os
import pprint
import json
import requests
#This is the first request to call the Api courses.
file_exist=os.path.exists("pro1.json")
print(file_exist)
if file_exist==True:
    with open("pro.json","r") as file1:
        cources_data=json.load(file1)
    with open("pro1.json","r") as file2:
        exercise_data=json.load(file2)

elif file_exist==False:
    r=requests.get("https://saral.navgurukul.org/api/courses")
    cources_data = r.json()
    req=requests.get("https://saral.navgurukul.org/api/courses/"+topic_id+"/exercises")
    exercise_data=req.json()



for i in range(0,len(cources_data["availableCourses"])):
    print(0+i,cources_data["availableCourses"][i]['name'])
select_data_cources=int(input("enter the topic you want to do"))
print(select_data_cources,cources_data["availableCourses"][select_data_cources]['name'])
topic_name=cources_data["availableCourses"][select_data_cources]['name']
topic_id=cources_data['availableCourses'][select_data_cources]['id']


length_of_exercise=len(exercise_data['data'])
for j in exercise_data:
    for k in range(0,length_of_exercise):
        print("    ",k,exercise_data[j][k]['name'])

select_data_exercise=int(input("enter the parent child topic you want to learn"))
print(exercise_data['data'][select_data_exercise]['name'])
length_of_childexercise=len(exercise_data['data'][select_data_exercise]["childExercises"])
#this is for child exercise
for l in range(0,length_of_childexercise):
        print("    ",l,exercise_data['data'][select_data_exercise]["childExercises"][l]['name'])  
    
