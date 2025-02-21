print("Try programiz.pro")

# exampleInput = [
#     { "name": "Steve", "age": 25 },
#     { "name": "Bob", "age": 35 },
#     { "name": "Charlie", "age": 45 },
#     { "name": "David", "age": 55 },
#     { "name": "Eve", "age": 65 },
#     { "name": "Frank", "age": 75 },
# ]
# # exampleOutput = {
# #     "0-20": [],
# #     "21-40": ["Alice", "Bob"],
# #     "41-60": ["Charlie", "David"],
# #     ">60": ["Eve", "Frank"],
# # }
# sortedList =  sorted(exampleInput, key= lambda x: x['name'])
# print("==== sortedList ",sortedList)



# # exampleOutput = {
# #     "0-20": [],
# #     "21-40": [],
# #     "41-60": [],
# #     ">60": [],
# # }
# lst_0_20 = []
# lst_21_40 = []
# lst_41_60 = []
# lst_60 = []


# for i in exampleInput:
#     if 0 <=i["age"] < 21:
#         lst_0_20.append(i['name'])
#         # exampleOutput["0-20"].append(i['name'])
#     elif 21 <= i['age'] <= 40:
#         lst_21_40.append(i['name'])
#         # exampleOutput["21-40"].append(i['name'])
#     elif 41 <= i['age'] <= 60:
#         lst_41_60.append(i['name'])
#         # exampleOutput["41-60"].append(i['name'])
#     elif 60 < i['age']:
#         lst_60.append(i['name'])
#         # exampleOutput[">60"].append(i['name'])
        
        
# exampleOutput = {
#     "0-20": sorted(lst_0_20),
#     "21-40": sorted(lst_21_40),
#     "41-60": sorted(lst_41_60),
#     ">60": sorted(lst_60),
# }
        
# print("==== exampleOutput ", exampleOutput)


lst = [4,5,6]
lst.append(7)
lst.insert(0,3)
print("====1 lst ",lst)
lst.remove(5)
print("====2 lst ",lst)
lst.pop(0)
print("====3 lst ",lst)
del lst[0]
print("====4 lst ",lst)




