# # # # # for i in range (1,6):

# # # # #  print(i)


# # # # # for i in range (9,4,-2):
# # # # #   print(i)


# # # # for i in range (-1,-10,-4):
# # # #     print(i)

# # # z=True
# # # name="beautiful"
# # # for i in name:
# # #     if z:
# # #         print(i)

# # # a="beautiful"
# # # for i in range(5):
# # #   print(a[i])

# # name="sanjay"
# # for i in range(4):
# #   print(name[i])

# # for i in range(1,6):
# #   print(i)

# # list=["sanjay","developer","it"]
# # for i in list:
# #   print(f"im my self{i}")
# #   print(f" i want to become {i}")

# # fruits=["apple","banana","grapes","kiwi","mosambi"]
# # for i in fruits:
# #   print(f" i like {i}")

# # tuple=(1,2,3,4,5,6,7,8,9,10)
# # for i in tuple:
# #   print(i*5)

# # user={
# #   "name": "sanjay",
# #   "age": 21,
# #   "city": "suryapet"
# # }
# # for values in user.values():
# #   print(values)

# # fruits_details={
# #   "name":"banana",
# #   "color":"yellow",
# #   "use": "health",
# #   "proce" :70,
# #   "location": "suryapet"
# #   }
# # for key in fruits_details:
# #   print(key)
# # for values in fruits_details.values():
# #   print(values)
# # for key,values in fruits_details.items():
# #   print(f"{key}: {values}")

# # color={"yellow","blue","grey","green"}
# # for i in color:
# #     print(i)

# # for i in range(2000):
# #     print("i hate you ")
# #     print("forever")
# #     print("andever")
# #     print("endever")

# # for i in range(1,10,2):
# #     print(i)
# # fruits=["apple","banana","grapes","kiwi","mosambi"]
# # for index,value in enumerate(fruits):
# #   print(f" {index}: {value}")
# for i in range(5):
#     if i==4:
#         break
#     print(i)
# else:
#     print("your for loop is completed")

  
# for i in range(1,4):
#     for j in range(1,4):
#         print(f"{i}x{j}={i*j}")
#     print("------")

# cubes=[]
# for x in range(10):
#    cubes.append(x**3)

# print(cubes)

numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=[]
for i in numbers:
    if i%2==0:
     even_numbers.append(i)
print(even_numbers)

names=["sanjay","prabhas","radheshyam"]
capital_names=[]
for i in names:
   capital_names.append(i.capitalize())
print(capital_names)

numbers = [4, 7, 2, 1, 1, 5]
found = False

for num in numbers:
    if num > 8:
        print(f"Found a number greater than 8: {num}")
        found = True
        break
        
if not found:
    print("No number greater than 8 found")


numbers=[1,2,3,4,5]
total=0
for i in numbers:
   total=total+i
print(f"sum:{total}")