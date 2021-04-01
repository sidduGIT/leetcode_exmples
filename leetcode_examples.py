# A = "apple apple"
# B =  "banana"
# lst=A.split()+B.split()
# print([w for w in lst if lst.count(w)==1])
#
# nums=[3,4,5,1,2]
# sort_nums=sorted(nums)
# for i in range(1,len(nums)):
#     if nums[i:]+nums[:i]==sort_nums:
#         print(True)
#         break
# else:
#     print(False)
#
# def rem_pali(s):
#     if not s:
#         return 0
#     if s==s[::-1]:
#         return 1
#     else:
#         return 2
#
# print(rem_pali('"ababa"'))
# print(rem_pali('"abb"'))
# print(rem_pali('"baabb"'))
# #print(rem_pali('"ababa"'))
#
# items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
# ruleKey = "color"
# ruleValue = "silver"
# cnt=0
# for i in items:
#     if ruleKey=='type':
#         if ruleValue==i[0]:
#             cnt+=1
#     if ruleKey=='color':
#         if ruleValue==i[1]:
#             cnt+=1
#     if ruleKey=='name':
#         if ruleValue==i[2]:
#             cnt+=1
# print(cnt)
#
# from collections import Counter
# def findLucky(arr):
#     if len(arr) == 1:
#         return -1
#     res = []
#     d = Counter(arr)
#     for k, v in d.items():
#         if k == v:
#             res.append(v)
#     if len(res)==0:
#         return -1
#     else:
#         return max(res)
#
# print(findLucky([2,2,2,3,3]))
# print(findLucky([2,2,3,4]))
#
# s = "a"
# t = "b"
# if sorted(t)==sorted(s):
#     print('True')
# else:
#     print('False')
#
#
# def countSubstrings(s):
#     if len(s) == 1:
#         return 1
#     cnt = 0
#     from itertools import permutations
#     for i in range(1,len(s)+1):
#         for combi in permutations(s, i):
#             print(combi)
#             if combi == combi[::-1]:
#                 cnt += 1
#     return cnt
# print(countSubstrings('aa'))
# print(countSubstrings('a'))
# print(countSubstrings('aaa'))
# print(countSubstrings('aaaa'))
#
# import itertools
# def maxSubArray(nums):
#     for i in range(1,len(nums)):
#         nums[i]=max(nums[i-1]+nums[i],nums[i])
#         print(nums)
#     return max(nums)
#
# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
#
# nums=[1,2,3,4]
# res=[1 for i in range(len(nums))]
# prod=1
#
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if i==j:
#             continue
#         else:
#             prod*=nums[i]
#             res.append(prod)
#             prod=1
# print(res)
#
# def maxProduct(nums):
#     for i in range(1,len(nums)):
#             nums[i]=max(nums[i-1]*nums[i],nums[i])
#             # print(nums)
#     return max(nums)
#
# print(maxProduct([2,3,-2,4]))
# print(maxProduct([-2,0,-1]))
# print(maxProduct([-2,3,-4]))

# n=83
# ns=str(n)
# while True:
#     if len(ns)>=2:
#         ns=int(ns[0])+int(ns[1])
#         ns=str(ns)
#     else:
#         print(ns)
#         exit()

#arr = [100,100,100]#[40,10,20,30]
# def arrayRankTransform(arr):
#     #
#     if len(arr) < 1: return None
#     newarr = sorted(arr)
#     orderdict = {newarr[0]: 1}
#     prev = newarr[0]
#     for i in newarr[1:]:
#         if i > prev:
#             orderdict.setdefault(i, orderdict[prev] + 1)
#             prev = i
#     print(orderdict)
#     return [orderdict[i] for i in arr]
#
# print(arrayRankTransform([40,10,20,30]))
# # print(arrayRankTransform([100,100,100]))
# # print(arrayRankTransform([37,12,28,9,100,56,80,5,12]))
# #
# # #Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
# # def addDigits(num):
# #     if num%9==0 and num!=0:
# #                 return 9
# #     else:
# #         return num%9
# #
# # print(addDigits(38))
# # print(addDigits(3883))
# # print(addDigits(1000))
#
# for i in range(1,6):
#     for j in range(i):
#         print(i,end=' ')
#     print('\n')
#
# for i in range(6,0,-1):
#     for j in range(i):
#         print('*',end=' ')
#     print('\n')
#
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end='  ')
#     print('\t\t')
#
# # arr=[i for i in input().split()]
# # print(arr)
#
# with open('siddu.txt','r') as fr:
#     data=fr.readlines()
#     print(data[3])
# i=0
# while(i<11):
#     print(i)
#     i+=1
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='  ')
#     print('\n')
#
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end='  ')
#     print('\n')
#
# def prime(start,stop):
#     for i in range(start,stop+1):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             yield i
# for i in prime(25,50):
#     print(i)
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print('\n')
# for i in range(5,0,-1):
#     for j in range(i):
#         print('*',end=' ')
#     print('\n')
#
# def func1(*l):
#     return l
# print(func1([1]))
# print(func1([1,2]))
# print(func1([1,2,3]))
# print(func1([1,2,3,4]))
# print(func1([1,2,3,4,5]))
# print(func1([1,2,3,4,5,6]))
#
# def func1(a,b):
#     def func2(a,b):
#         return a+b
#     outer=func2(a,b)
#     return outer+5
# print(func1(8,3))
#
# def sum1(n):
#     if n:
#         return n+sum1(n-1)
#     else:
#         return 0
# print(sum1(10))
#
# def mid(s):
#     l=len(s)
#     mid1=l//2
#     return s[mid1-1:mid1+2]
# print(mid("JhonDipPeta"))
# print(mid("JaSonAy"))
#
# s1 = "Ault"
# s2 = "Kelly"
# mid=len(s1)//2
# print(s1[0:mid]+s2+s1[mid:])
#
# s='PyNaTive'
# print(''.join([i for i in s if i.islower()]+[i for i in s if i.isupper()]))
#
# s="P@#yn26at^&i5ve"
# chars=digits=symbols=0
# for i in s:
#     if i.isdigit():
#         digits+=1
#     elif i.islower() or i.isupper():
#         chars+=1
#     else:
#         symbols+=1
# print(chars,digits,symbols)
#
# s1 = "Abc"
# s2 = "Xyz"
# res=[]
# for x,y in zip(s1,s2[::-1]):
#     res.append(x)
#     res.append(y)
# print(''.join(res))
#
# s1 = "Yn"
# s2 = "PYnative"
# print(all( 1 if i in s2 else 0 for i in s1 ))
#
# s= "Welcome to USA. usa awesome, isn't it?".lower()
# print(s.count('usa'))
#
# import re
# str1 = "English = 78 Science = 83 Math = 68 History = 65"
# digits=re.findall(r'\d+',str1)
# digits=[int(i) for i in digits]
# print(sum(digits),sum(digits)/len(digits))
#
# str1 = "English = 78 Science = 83 Math = 68 History = 65"
# dict1={}
# for i in str1:
#     if i not in dict1:
#         dict1[i]=1
#     else:
#         dict1[i]+=1
# print(dict1)
#
# str1 = "PYnative"
# revs=''
# l=len(str1)-1
# while l>=0:
#     revs+=str1[l]
#     l-=1
# print(''.join(revs))
#
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# print("Original String is:", str1)
#
# index = str1.rfind("Emma")
# print("Last occurrence of Emma starts at", index)
#
# str1 = 'Emma-is-a-data-scientist'
# print(str1.split('-'))
#
# str1 = "/*Jon is @developer & musician"
# print(''.join([i for i in str1 if i.isalpha()]))
#
# str1 = 'I am 25 years and 10 months old'
# print(''.join(re.findall(r'\d',str1)))
#
# #Given two lists create a third list by picking an odd-index element from the first list and
# # even index elements from the second.
# listOne = [3, 6, 9, 12, 15, 18, 21]
# listTwo = [4, 8, 12, 16, 20, 24, 28]
# print([v for i,v in enumerate(listOne) if i%2!=0])
# print([v for i,v in enumerate(listOne) if i%2==0])
# print([v for i,v in enumerate(listOne) if i%2!=0]+[v for i,v in enumerate(listOne) if i%2==0])
# odd=listOne[1::2]
# even=listTwo[0::2]
# list3=list()
# list3.extend(odd)
# list3.extend(even)
# print(list3)
#
# #Given a list, remove the element at index 4 and add it to the 2nd position and at the end of the list
# list1 = [54, 44, 27, 79, 91, 41]
# item=list1.pop(4)
# list1=list1[0:1]+[item]+list1[1:]+[item]
# print(list1)
#
# l=[34, 54, 67, 89, 11, 43, 94]
# item=l.pop(3)
# l.insert(1,item)
# l.append(item)
# print(l)
#
# #Given a list slice it into 3 equal chunks and reverse each chunk
# l=[11, 45, 8, 23, 14, 12, 78, 45, 89]
# chunks=[l[i:i+3] for i in range(0,len(l)-1,3)]
# print('original',chunks)
# print('reversed',[i[::-1] for i in chunks])
#
# # Iterate a given list and count the occurrence of each element and create a
# # dictionary to show the count of each element
# l=[11, 45, 8, 11, 23, 45, 23, 45, 89]
# dict1={}
# for  i in l:
#     if i not in dict1:
#         dict1[i]=1
#     else:
#         dict1[i]+=1
# print(dict1)
#
# #Given a two list of equal size create a Python set such that it shows the element from both lists in the pair
# l1=[2, 3, 4, 5, 6, 7, 8]
# l2=[4, 9, 16, 25, 36, 49, 64]
# l3=set((x,y) for x,y in zip(l1,l2))
# print(l3)
#
# #Given the following two sets find the intersection and remove those elements from the first set
#
# s1={65, 42, 78, 83, 23, 57, 29}
# s2={67, 73, 43, 48, 83, 57, 29}
# intsec=s1.intersection(s2)
# print(s1.symmetric_difference(intsec))
#
# #Given two sets, Checks if One Set is a subset or superset of another Set.
# # if the subset is found delete all elements from that set
#
# s1={27, 43, 34}
# s2={34, 93, 22, 27, 43, 53, 48}
# print(s1.issubset(s2))
# print(s1.issuperset(s2))
# if s1.issubset(s2):
#     print(s2.symmetric_difference(s1))
#
# # Iterate a given list and Check if a given element already exists in a dictionary
# # as a key’s value if not delete it from the list
#
# l= [47, 64, 69, 37, 76, 83, 95, 97]
# d={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
# dv=d.values()
# print(set(l).symmetric_difference(set(dv)))
# print([i for i in l if i in dv])
# print([i for i in l if i not in dv])
#
# #Given a dictionary get all values from the dictionary and add them to a list but don’t add duplicates
# d={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
# print(list(set(d.values())))
#
# #Remove duplicate from a list and create a tuple and find the minimum and maximum number
# l= [87, 45, 41, 65, 94, 41, 99, 94]
# tup=tuple(set(l))
# print(max(tup),min(tup))
#
# #Concatenate two lists index-wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# print([x+y for x,y in zip(list1,list2)])
#
# #Given a Python list of numbers. Turn every item of a list into its square
# l=[1, 2, 3, 4, 5, 6, 7]
# print([i**2 for i in l])
# print([i**3 for i in l])
#
# #Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# res=[]
# for i in list1:
#     for j in list2:
#         res.append(i+j)
# print(res)
#
# print([i+j for i in list1 for j in list2])
#
# #Given a two Python list. Iterate both lists simultaneously such that list1 should display item in
# # original order and list2 in reverse order
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for x,y in zip(list1,list2[::-1]):
#     print(x,y)
#
# #Add item 7000 after 6000 in the following Python List
# l= [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# l[2][2].append(700)
# print(l)
#
# #Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list
# l1= ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# l1[2][1][2].extend(["h", "i", "j"])
# print(l1)
#
# #Given a Python list, find value 20 in the list, and if it is present, replace it with 200.
# # Only update the first occurrence of a value
# l=[5, 10, 15, 20, 25, 50, 20]
# for i in range(len(l)):
#     if l[i]==20:
#         l[i]=200
#         break
# print(l)
# l=[5, 10, 15, 20, 25, 50, 20]
# index=l.index(20)
# l[index]=200
# print(l)
#
# #Given a Python list, remove all occurrence of 20 from the list
# l=[5, 20, 15, 20, 25, 50, 20]
# for i in l:
#     if i==20:
#         l.remove(20)
# print(l)
#
# print([i for i in l if i!=20])
#
# #Below are the two lists convert it into the dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# print(dict(zip(keys,values)))
#
# #Merge following two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2)
# print(dict1)
#
# #Access the value of key ‘history’ from the below dict
# d= {
#    "class":{
#       "student":{
#          "name":"Mike",
#          "marks":{
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# print(d['class']['student']['marks']['history'])
#
# #Delete set of keys from a dictionary
#
# #Add a list of elements to a given set
# s= {"Yellow", "Orange", "Black"}
# l=["Blue", "Green", "Red"]
# s.update(set(l))
# print(s)
#
# #Return a new set of identical items from a given two set
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.intersection(set2))
#
# #Returns a new set with all items from both sets by removing duplicates
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.union(set2))
#
# # Given two Python sets, update the first set with items that exist only in the first set and not in the second set
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# intsec=set1.intersection(set2)
# print({i for i in set1 if i not in intsec})
# print({i for i in set2 if i not in intsec})
#
# set1.difference_update(set2)
# print(set1)
#
# set1.difference(set2)
# print(set1)
#
# set2.difference(set1)
# print(set2)
#
# #Remove items 10, 20, 30 from the following set at once
# set1 = {10, 20, 30, 40, 50}
# print(set1.intersection({40,50}))
#
# set1 = {10, 20, 30, 40, 50}
# set1.difference_update({10, 20, 30})
# print(set1)
#
# #Return a set of all elements in either A or B, but not both
# #Update set1 by adding items from set2, except common items
#
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.symmetric_difference(set2))
#
# # Remove items from set1 that are not common to both set1 and set2
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set1.intersection_update(set2)
# print(set1)
#
# #Reverse the following tuple
# t=(10, 20, 30, 40, 50)
# print(t[::-1])
#
# #Access value 20 from the following tuple
# t= ("Orange", [10, 20, 30], (5, 15, 25))
# print(t[1][1])
# print(t[2][1])
# t[1].append(40)
# t[1].extend([50,60])
# print(t)
#
# # t[0]='mango'
# # print(t)
#
# #Create a tuple with single item 50
# t=(50,)
# print(t)
#
# t1,t2,t3=(10,20,30)
# print(t1,t2,t3)
#
# #Unpack the following tuple into 4 variables
# t1,t2,t3,t4=(10, 20, 30, 40)
# print(t1,t2,t3,t4)
#
# #Swap the following two tuples
# tuple1 = (11, 22)
# tuple2 = (99, 88)
# print(tuple1,tuple2)
# tuple1,tuple2=tuple2,tuple1
# print(tuple1,tuple2)
#
# #Copy element 44 and 55 from the following tuple into a new tuple
# t= (11, 22, 33, 44, 55, 66)
# t1=t[3:5]
# print(t1)
#
# tuple1 = (11, 22, 33, 44, 55, 66)
# tuple2 = tuple1[3:-1]
# print(tuple2)
#
# #Modify the first item (22) of a list inside a following tuple to 222
# t= (11, [22, 33], 44, 55)
# print(t)
# t[1][0]=222
# print(t)
#
# #Sort a tuple of tuples by 2nd item
# t=(('a', 23),('b', 37),('c', 11), ('d',29))
# print(sorted(t,key=lambda x:x[1]))
# from operator import itemgetter
# print(sorted(t,key=itemgetter(1)))
#
# t=[('c', 11), ('a', 23), ('d', 29), ('b', 37)]
# print(sorted(t,key=lambda x:x[0]))
# print(sorted(t,key=itemgetter(0)))
#
# #Counts the number of occurrences of item 50 from a tuple
# t=(50, 10, 60, 70, 50)
# print(t.count(50))
#
# #Check if all items in the following tuple are the same
#
# t=(45, 45, 45, 45)
# print(all(i==45 for i in t))
#
# t=(45, 45, 45, 45,46)
# print(all(i==45 for i in t))
#
# #Create a new dictionary by extracting the following keys from a below dictionary
# d= {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
#
# }
# keys = ["name", "salary"]
# d1={}
# for k in keys:
#     d1[k]=d[k]
# print(d1)
#
# print({k:d[k] for k in keys})
#
# #Delete set of keys from a dictionary
# d= {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
#
# }
# keysToRemove = ["name", "salary"]
# print({k:v for k,v in d.items() if k not in keysToRemove})
#
# print({k:d[k] for k in d.keys()-keysToRemove})
#
# #Check if a value 200 exists in a dictionary
# d= {'a': 100, 'b': 200, 'c': 300}
# if 200 in d.values():
#     print(True)
# else:
#     print(False)
#
# if 2001 in d.values():
#     print(True)
# else:
#     print(False)
#
# print(200 in d.values())
# print(2001 in d.values())
#
# #Rename key city to location in the following dictionary
# d= {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
#
# d1={}
# for k,v in d.items():
#     if k=='city':
#         d1['location']=v
#     else:
#         d1[k]=v
# print(d1)
#
# d['location']=d.pop('city')
# print(d)
#
# #Get the key of a minimum value from the following dictionar
# d= {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# print(min(d.items(),key=lambda x:x[1])[0])
# print(max(d.items(),key=lambda x:x[1])[0])
# print(min(d,key=d.get))
# print(max(d,key=d.get))
# sampleDict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# print(min(sampleDict, key=sampleDict.get))

#Change Brad’s salary to 8500 from a given Python dictionary
#
# d={
#      'emp1': {'name': 'Jhon', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 6500}
# }
# print('original',d)
# for k,v in d.items():
#     if d['emp3']['name']=='Brad':
#         d['emp3']['salary']=8500
#     # else:
#     #     d[k]=v
# print('after changing Brad''s salary to 8500',d)
#
# for k,v in d.items():
#     if d['emp2']['name']=='Emma':
#         d['emp2']['name'] ='Kate'
# print(d)
#
# Employee = {
#     'emp1': {
#         'name': 'Lisa',
#         'age': '29',
#         'Designation':'Programmer'
#             },
#          'emp2': {
#              'name': 'Steve',
#              'age': '25',
#              'Designation':'HR'
#                  }
#              }
# for k,v in Employee.items():
#     if Employee['emp2']['Designation']=='HR':
#         Employee['emp2']['Designation'] ='Engineer'
# print(Employee)
# d1={
#     'emp3':{
#         'name':'siddu',
#         'age':'42',
#         'Designation':'Python Programmer'
#             }
#     }
# # Employee['emp3']['name']='siddu'
# # Employee['emp3']['age']=41
# # Employee['emp3']['Designation']='Python programmr'
# Employee.update(d1)
# print(Employee)
#
# from collections import Counter
# def isUnique(item):
#     d=Counter(item)
#     return all(i==1 for i in d.values())
#
#
# listOne = [123, 345, 456, 23, 567]
# print("All List elemtnts are Unique ", isUnique(listOne))
#
# listTwo = [123, 345, 567, 23, 567]
# print("All List elemtnts are Unique ", isUnique(listTwo))
#
# var= "James Bond"
# print(var[2::-1])

#Ask user to give name and marks of 10 different students. Store them in dictionary.
# d={}
# for i in range(10):
#     name=input('entaer name')
#     marks=int(input('enter marks'))
#     d[name]=marks
# print(d)
#
# d={'siddu': 98, 'santu': 56, 'renuka': 86, 'atharv': 78, 'surahi': 95, 'suman': 72, 'anu': 56, 'gundya': 38, 'kritka': 49, 'basu': 35}
# #sorting on marks
# print(sorted(d.items(),key=lambda x:x[1]))
#
# #sorting on names
#
# print(sorted(d.items(),key=lambda x:x[0]))
#
# from collections import Counter
# d=Counter("MISSISSIPPI")
# print(d)
#
# s="MISSISSIPPI"
# d1={}
# for i in s:
#     if i not in d1:
#         d1[i]=1
#     else:
#         d1[i]+=1
# print(d1)
#
# # l=["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]
# # print(sorted(l,key=lambda x:x.count('bug')))
#
# data={'System ID':2019008144,'Roll No':190101306,'Sem':2,'Year':2020}
# print(dict(sorted(data.items(),key=lambda x:x[1])))
# print(dict(sorted(data.items(),key=lambda x:x[1],reverse=True)))
#
# data = {'A':2015, 'B':2002, 'C': 3900}
# print(max(data.items(),key=lambda x:x[1]))
# print(min(data.items(),key=lambda x:x[1]))
#
# for i in range(1,6):
#     for j in range(i):
#         print('*',end='')
#     print('\n')
#
# for i in range(1,6):
#     for j in range(i):
#         print(i,end='')
#     print('\n')
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
# #     print('\n')
#
# for i in range(10,1,-1):
#     for j in range(i,1,-1):
#         print('*',end='')
#     print('\n')
#
# for i in range(10,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print('\n')
#
# for i in range(1,11,1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print('\n')
#
# #write a program to print star patterns and alphabets pattern
#
# n=6
# asci_number=65
# for i in range(n):
#     for j in range(0,i+1):
#         char=chr(asci_number)
#         print(char,end=' ')
#         asci_number+=1
#     print('\n')
#
# # Given the following dictionary:
# #
# # inventory = {
# #     'gold' : 500,
# #     'pouch' : ['flint', 'twine', 'gemstone'],
# #     'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
# # }
# # Try to do the followings:
# #
# # Add a key to inventory called 'pocket'.
# # Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
# # .sort()the items in the list stored under the 'backpack' key.
# # Then .remove('dagger') from the list of items stored under the 'backpack' key.
# # Add 50 to the number stored under the 'gold' key.
# #
# # inventory = {
# #     'gold' : 500,
# #     'pouch' : ['flint', 'twine', 'gemstone'],
# #     'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
# #             }
# # inventory['pocket']=['seashell', 'strange berry','lint']
# # print(inventory)
# #
# # inventory['backpack'].sort()
# # print(inventory)
# #
# # inventory['backpack'].remove('dagger')
# # print(inventory)
# #
# # inventory['gold']+=50
# # print(inventory)
#
# #find unique elements in a matrix
#
# # mat=[[20,30,50,60,70],[70,10,20,40,80],[12,13,12,13,16]]
# # mat=[j for i in mat for j in i]
# # d={}
# # res=[]
# # for i in mat:
# #     if i not in d:
# #         d[i]=1
# #     else:
# #         d[i]+=1
# # for k,v in d.items():
# #     if v==1:
# #         res.append(k)
# # print(res)
#
# prices={
#         "banana": 4,
#         "apple": 2,
#         "orange": 1.5,
#         "pear": 3
#         }
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# for k in prices:
#     print(k)
#     print('price:',prices[k])
#     print('stock:',stock[k])
#
# total=0
# for k in prices:
#     stock_price=prices[k]*stock[k]
#     print(stock_price)
#     total+=stock_price
# print(total)
#
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
#
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
#
# groceries=['banana','orange','apple']
#
# def compute_bill(food):
#     total=0
#     for i in food:
#         total+=prices[i]*stock[i]
#     return total
#
# print('Total bill for the above groceries',compute_bill(groceries))
#
# def compute_bill1(food):
#     total=0
#     for i in food:
#         if stock[i]>0:
#             total+=prices[i]*stock[i]
#             stock[i]-=1
#     return total
#
# print('Total bill for the above groceries',compute_bill1(groceries))

# lloyd = {"name": "Lloyd","homework": [],"quizzes":[],"tests":[],}
# alice = {"name": "Alice", "homework":[],"quizzes":[],"tests":[],}
# tyler = {"name": "Tyler", "homework":[],"quizzes":[],"tests":[],}
# lloyd = {
#   "name": "Lloyd",
#   "homework": [90.0,97.0,75.0,92.0],
#   "quizzes": [88.0,40.0,94.0],
#   "tests": [75.0,90.0]
# }
# alice = {
#   "name": "Alice",
#   "homework": [100.0, 92.0, 98.0, 100.0],
#   "quizzes": [82.0, 83.0, 91.0],
#   "tests": [89.0, 97.0]
# }
# tyler = {
#   "name": "Tyler",
#   "homework": [0.0, 87.0, 75.0, 22.0],
#   "quizzes": [0.0, 75.0, 78.0],
#   "tests": [100.0, 100.0]
# }
#
# students=[lloyd,alice,tyler]
# for student in students:
#     print(student["name"])
#     print(student["homework"])
#     print(student["quizzes"])
#     print(student["tests"])
#
# def average(numbers):
#     total=float(sum(numbers)/len(numbers))
#     return total
#
# def get_average(student):
#     homework=average(student['homework'])
#     quiz = average(student['quizzes'])
#     test = average(student['tests'])
#     final = 0.1 * homework + 0.3 * quiz + 0.6 * test
#     return final
#
# def get_letter_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >=80:
#         return "B"
#     elif score >=70:
#         return "C"
#     elif score >=60:
#         return "D"
#     else:
#         return "F"
#
# print(get_letter_grade(get_average(lloyd)))
# print(get_letter_grade(get_average(alice)))
# print(get_letter_grade(get_average(tyler)))
#
# def get_class_average(students):
#     results=[]
#     for student in students:
#         results.append(get_average(student))
#     return results
#
# print(get_class_average( [lloyd, alice, tyler]))
# print(average(get_class_average( [lloyd, alice, tyler])))
#
# # Scrabble is a game where players get points by spelling words. Words are scored by adding together the point
# # values of each individual letter.Define a function scrabble_score that takes a string word as input and
# # returns the equivalent scrabble score for that word.
#
# score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
#          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
#          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
#          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
#          "x": 8, "z": 10}
# s='scrabblescore'
# total=0
# for i in s:
#     total+=score[i]
#     print(score[i])
# print(total)
#
# grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
#
# def print_grades(grades):
#     for grade in grades:
#         print(grade)
# print_grades(grades)
#
# def grades_sum(grades):
#     return sum(grades)
# print(grades_sum(grades))
#
# def grades_averge(grades):
#     return float(grades_sum(grades)/len(grades))
# print(grades_averge(grades))
#
# def grades_variance(grades):
#     average=grades_averge(grades)
#     variance=0
#     for grade in grades:
#         variance+=(average-grade)**2
#     return variance/len(grades)
#
# print(grades_variance(grades))
#
# def grades_std_deviation(variance):
#     variance=grades_variance(grades)
#     return variance**0.5
# print(grades_std_deviation(grades_variance(grades)))
#
# l=[i**2 for i in range(1,10)]
# print(list(filter(lambda x:x>=30 and x<=70,l)))
#
# garbled = list("!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI")
# msg=garbled[0::2]
# print(''.join(msg[::-1]))
#
# #Print "Z" from the nested data.
# lst = [["Hat", "Glove", "Goggle"], ["Button", "Zipper", "Hook"]]
# print(lst[1][1][0])
#
# for i in lst:
#     for j in i:
#         print(j[0])
#
# lst[1][1]='Zopper'
# print(lst)
#
# print([[j[::-1] for j in i] for i in lst ])
#
# lst = [{"orange": "orange"}, {"rose": "red"}, {"violet": "blue"}]
# print(lst[0]['orange'])
# print(lst[1]["rose"])
# print(lst[2]["violet"])
#
# for i in lst:
#     for k in i:
#         print(k,i[k])
#
# d= {"Dakar":{"weather":"sunny", "roads":"dry"}}
# print(d['Dakar']['roads'])
#
# d= {"Tokyo": {"weather":["sunny", "cloudy"], "roads":"dry"}, "Dakar": {"weather":["foggy","windy"], "roads": "sandy"}}
# print(d['Tokyo']['weather'])
# d['Tokyo']['weather'].append('rainy')
# print(d)
#
# d['Tokyo']['weather'].remove('rainy')
# print(d)
#
# d['Tokyo']['siddu']='bagewadi'
# print(d)
#
# s='siddu'
# print(s.split('d'))
#
# print([i for i in range(1,1000)])
# print(min([i for i in range(1,1000)]))
# print(max([i for i in range(1,1000)]))
# print(([i for i in range(1,1000) if i%2==0]))
# print(([i for i in range(1,1000) if i%2!=0]))

# def rebase_parser(rebase_file):
#     """
#     :param rebase_file: the rebase file to parse
#     :type rebase_file: file object
#     :return: at each call return a tuple (str enz name, str binding site)
#     :rtype: iterator
#     """
#
#     def clean_seq(seq):
#         """
#         remove each characters which are not a base
#         """
#         clean_seq = ''
#         for char in seq:
#             if char in 'ACGT':
#                 clean_seq += char
#         return clean_seq
#
#     for line in rebase_file:
#         fields = line.split()
#         # fields = fields.split()
#         name = fields[0]
#         seq = clean_seq(fields[2])
#         yield (name, seq)
#
#
# if __name__ == '__main__':
#     import sys
#     import os.path
#
#     rebase_path=r'C:\Users\surabhi_siddu\PycharmProjects\Siddu_Python\gnome.txt'
#     if not os.path.exists(rebase_path):
#         sys.exit("No such file: {}".format(rebase_path))
#
#     with open(rebase_path, 'r') as rebase_input:
#         for enz in rebase_parser(rebase_input):
#             print(enz)
#
# from collections import namedtuple
#
# Sequence =  namedtuple("Sequence", "id comment sequence")
#
# def fasta_reader(fasta_path):
#     """
#     :param fasta_path: the path to the file to parse
#     :type fasta_path: string
#     :return: a sequence
#     :rtype: Sequence instance
#     """
#     with open(fasta_path, 'r') as fasta_infile:
#         id_ = ''
#         comment = ''
#         sequence = ''
#         for line in fasta_infile:
#             if line.startswith('>'):
#                 header = line.split()
#                 id_ = header[0]
#                 comment = ' '.join(header[1:])
#             else:
#                 sequence += line.strip()
#     return Sequence(id_ , comment, sequence)
#
# path=r'C:\Users\surabhi_siddu\PycharmProjects\Siddu_Python\fasta_file.txt'
# lst=[]
# lst.append(fasta_reader(path))
# print(lst)
#
# from collections import Counter
# lst=[3,1,4,4,5,2,6,1]
# dict1=Counter(lst)
# res=[]
# k_num=2
# for k,v in dict1.items():
#     if v==k_num:
#         res.append(k)
# print(res)
#
# def my_max(arr):
#     max1=arr[0]
#     for i in arr:
#         if i>max1:
#             max1=i
#     return max1
# print(my_max([10,234,567,98,456,34,67]))
# print(my_max((457,234,68,934,23,79,54)))
# print(my_max([67.8,34.7,23.5,89.3,14.5]))
#
# #lst=[10,23,67,84,98,53,61,75]
# lst=[10,12,102,31,15]
# lst=[str(i) for i in lst]
# print([int(i) for i in sorted(lst,key=lambda x:int(x[0])+int(x[1]))])
#
# def all_codons():
#     all_codons = []
#     alphabet = 'acgt'
#     for base_1 in alphabet:
#         for base_2 in alphabet:
#             for base_3 in alphabet:
#                 codon = base_1 + base_2 + base_3
#                 all_codons.append(codon)
#     return all_codons
# print(all_codons())
#
# s='ABCD'
# res=[]
# for i in s:
#     for j in s:
#         for k in s:
#             for l in s:
#                 grp=i+j+k+l
#                 res.append(grp)
# print(res)
#
# from itertools import product
# s='ABCD'
# res=[''.join(grp) for grp in product(s,repeat=4)]
# print(res)
#
# d = {1 : 'a', 2 : 'b', 3 : 'c' , 4 : 'd'}
# print({v:k for k,v in d.items()})
#
# mat=[[1,2,3,4,5],
#      [3,4,5,8,10],
#      [3,5,7,9,11],
#      [1,3,5,7,9]
#      ]
# #print(list(set.intersection(*map(set, mat))))
# res=set(mat[0])
# for i in mat[1:]:
#     res.intersection_update(i)
# print(res)
#
# dicPC = {"HP": 11, "Acer": 7, "Lenovo": 17, "Del": 23}
# dicPhone = {"Sumsung": 22, "Iphone": 9, "Other": 13}
# dicTablet = {"Sumsung": 15, "Other": 13}
# dicPC.update(dicPhone)
# dicPC.update(dicTablet)
# print(dicPC)
#
# from collections import defaultdict
# d={}
# l=[ 2, 7, 11, 5, 3, 19, 14, 9, 1, 4]
# def divisors(n):
#     listDiv = []
#     # browsing through all integers from 1 to n
#     # and then we tst if i is a divisor of n
#     for i in range(1, n + 1):
#         if n % i == 0:
#             listDiv.append(i)
#     return listDiv
#
# for i in l:
#     d[i]=divisors(i)
# print(d)
#
# d = {'a1': [21, 17, 22, 3], 'a2': [11, 15, 8, 13], 'a3': [7, 13, 2, 11], 'a4': [22,14,7,9]}
# print({k:sorted(v) for k,v in d.items()})

# Write a Python program that allows from a given directory to create a dictionary whose keys are the names of the text files
# located in this directory and the keys are the numbers of the lines of the files.

# records=[]
# with open('a.txt','r') as fr:
#     data=fr.readlines()
#     for chunk in range(0,len(data)-1,5):
#         #print(data[chunk:chunk+5])
#         for i in chunk:
#             i=i.rstrip('\n')
#             print(i)
#
# # to open/create a new html file in the write mode
# f = open('GFG.html', 'w')
#
# # the html code which will go in the file GFG.html
# html_template = """<html>
# <head>
# <title>Title</title>
# </head>
# <body>
# <h2>Welcome To GFG</h2>
#
# <p>Default code has been loaded into the Editor.</p>
#
# </body>
# </html>
# """
#
# # writing the code into the file
# f.write(html_template)
# f.close()
#
# import os
# name_email = {'david' : 'david@gmail.com' ,  'hafid' : 'hafid@gmail.com' ,  'nathalie' : 'nathalie@gmail.com' , 'najib' : 'najib@gmail.com' }
#
# htmlContent = ''
# for key , value in name_email.items():
#     htmlContent = htmlContent + ''.format(key , value)
# htmlContent = htmlContent + "Name\t\tEmail"
# file = open("convert_dictionary.html" , 'w')
# file.write(htmlContent)
# file.close()
# os.startfile("convert_dictionary.html")
#
# from itertools import combinations
# s='BANANA'
# T='BAN'
# print(len([i for i in combinations(s,3) if ''.join(i)==T]))

# import os
# user=os.getlogin()
# print('User=',user)
# with open('My_file.txt','w') as fw:
#     fw.write('Python is a object oriented programming language')
#
# with open('My_file.txt','r') as fr:
#     data=fr.read()
#     print(data)

# Using the os and chdir modules in console mode, give the commands that
# allow you to create a file called myFile.txt on the desktop.
# import os
# #path=r'C:\Users\surabhi_siddu\PycharmProjects\Siddu_Python'
# get_dir=os.getcwd()
# print(get_dir)
# os.chdir(r'C:\Users\surabhi_siddu\PycharmProjects')
# with open('My_file.txt','w') as fw:
#     fw.write('siddu bagewadi')
# os.rename(r'C:\Users\surabhi_siddu\PycharmProjects\My_file.txt',r'C:\Users\surabhi_siddu\PycharmProjects\My_file_1.txt')

# Write a python program that allowing you to create a directory in the desktop called myDir
# Write  a Python program allowing you to create a file in the desktop named myFile.txt and write it the following lines:
# here is an example of a text file
# this file was created with python
# we can write on this file
# Write  a Python program allowing you to moving myFile.txt in the  directory  myDir.

# import os
# os.mkdir(r'C:\Users\surabhi_siddu\PycharmProjects\Siddu_Python\tmp')
# os.chdir(r'C:\Users\surabhi_siddu\PycharmProjects\Siddu_Python\tmp')
# s='''here is an example of a text file
# this file was created with python
# we can write on this file
# '''
# with open('My_file.txt','w') as fw:
#     fw.write(s)
#
# # opening file in read mode
# f = open("myfile.txt" , "r")
#
# # getting content lines
# linesContent = f.readlines()
# f.close()
#
# # changing the second line
# linesContent[1] = "sorry! The content of this line has been changed!\n"
#
# # opening file in write mode
# f = open("myfile.txt" , "w")
#
# #writing new lines content
# f.writelines(linesContent)
# f.close()
#
# Given a file called myfile.txt which contains the following lines:
#
# line 1
# line 2
# line 3
#
# write a Python program that transforms the content into the form:
#
# line 3
# this line has just been inserted via Python code
# line 2
# line 1

# with open('My_file.txt','r') as fr:
#     data=fr.readlines()[::-1]
#     # for line in data:
#     #     print(line)
#     #
#     data[2]='"Python is object oriented programming language"'
# with open('My_file.txt','r+') as fw:
#     data = fw.readlines()[::-1]
#     data[2] = '"Python is object oriented programming language"'
#     for line in data:
#         #print(line)
#         fw.write(line)
# with open('My_file.txt','r') as fr:
#     data=fr.readlines()
#     data=data[::-1]
#     data[2]='"Python is object oriented programming language"\n'
#     with open('My_file.txt', 'w') as fw:
#         for line in data:
#             fw.write(line)

# Write a program that lists all the folders in the 'C: / Windows' directory
# b) write another program which lists all the files in the 'C: / Windows'  directory.
# c) Using the getlogin() method, write a program that make the same operations for the user's Desktop directory.
#
# import os,glob
#
# for file in os.scandir('c:/windows'):
#     if file.is_dir():
#         print(file)
#
# for file in os.scandir('c:/windows'):
#     if file.is_file():
#         print(file)
#
# # importing the pathlib module
# import os
# from pathlib import Path
#
# # creating an empty list which will contain all directories in the chosen directory
# fileList = []
# directoryList = []
#
# # desktop directory
# dir = 'C:/Users/' + os.getlogin() + "/Desktop"
#
# # creating a path object from the chosen directory
# p = Path(dir)
#
# # testing if the entry is file or directory
# for entry in os.scandir(p):
#     if entry.is_file():
#         fileList.append(entry)
#     else:
#         directoryList.append(entry)
# print("File list in chosen directory :")
# for file in fileList:
#     print(file)
# print("Folder list in chosen directory :")
# for directory in directoryList:
#     print(directory)

# with open('My_file.txt','r') as fr:
#     data=fr.read()
#     fields=data.split()
#     with open('My_file.txt','w') as fw:
#         for field in fields:
#             field=field.strip()
#             fw.write(field)

#find the frequency of words in a file

# with open('My_file.txt','r') as fr:
#     data=fr.read()
#     words=data.split()
#     dict1={}
#     for word in words:
#         if word not in dict1:
#             dict1[word]=1
#         else:
#             dict1[word]+=1
# for k,v in dict1.items():
#     print(k,'\t\t',v)

# a)Write a python program that create a text file called myFile.txt and write on it the following lines:
#
# - this is the line 1
#
# - thtis is the line 2
#
# - this is the line3
#
# - this is the line4
#
# - this is the line5
#
# - this is the line6
#
# - this is the line7
#
# - this is the line8
#
# - this is the line9
#
# - this is the line10
#
# b) Write a Python program which allows you to read the first 5 lines of myFile.txt.
# c) Write a program to read the last 5 lines of myFile.txt
# d) Write a Python program which allows you to extract the content of a file from the 3rd line to the
# 7th line and save it in another file called extract_content.txt.
#
# with open('My_file.txt','w') as fw:
#     for i in range(1,11):
#         fw.write('-this is a line{}\n'.format(i))
# with open('My_file.txt','r') as fr:
#     data=fr.readlines()
#     print(data[0:5]) #print 5 lines
#     print(data[-5:]) #print last 5 lines
#     print(data[3:8]) #print 3 to 7th lines
# with open('content.txt','w') as fw:
#     for line in data[-5:]:
#         fw.write(line)
#     for line in data[0:5]:
#         fw.write(line)
#     for line in data[3:8]:
#         fw.write(line)

#Write a Python program that allows you to group in a list the words common for two text files: file1.txt and file2.txt.
# with open('file1.txt','r') as fr1:
#     with open('file2.txt', 'r') as fr2:
#         data1=fr1.readlines()
#         data2 = fr2.readlines()
#         for line in set(data1).intersection(set(data2)):
#             print(line)

# Given a non-empty integer array, find the minimum number of moves required to make all array elements equal,
# where a move is incrementing a selected element by 1 or decrementing a selected element by 1.
# def minMoves2(nums):
#     nums.sort()
#     medien = nums[len(nums) // 2]
#     diff = [x - medien for x in nums]
#     new_moves = sum([abs(d) for d in diff])
#     return new_moves
#
# print(minMoves2([3,2,3]))

#Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
# def low_high(low,high):
#     return len([i for i in range(low,high+1) if i%2!=0])
# print(low_high(3,7))
# print(low_high(8,10))
# print(low_high(800445804,979430543))

# def check(word):
#     if word.isupper():
#     #if all(1 for i in word if i.isupper()):
#         return True
#     if word.islower():
#     #elif all([1 for i in word if i.islower()]):
#         return True
#     elif word[0].isupper() and word[1:].islower():
#         return True
#     else:
#         return False
#
# print(check('USA'))
# print(check('usa'))
# print(check('Usa'))
# print(check('UaA'))
# print(check('FlaG'))

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest
# palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# from itertools import combinations_with_replacement
# def longest(word):
#     longest=''
#     if word.islower() or word.isupper():
#         for i in range(1,len(word)):
#             for comb in combinations_with_replacement(word,i):
#                 if comb==comb[::-1]:
#                     if len(comb)>len(longest):
#                         longest=comb
#     return longest
#
# print(longest("abccccdd"))
#
# def isPowerOfTwo(n):
#     for i in range(n + 1):
#         if 2 ** i == n:
#             return True
#     else:
#         return False
#
# print(isPowerOfTwo(16))
# print(isPowerOfTwo(15))
# print(isPowerOfTwo(2))
#
#
# def reverseBits(n):
#     nstr = bin(n)[2:]
#     #print(nstr)
#     return nstr[::-1]
# print(reverseBits(43261596))
# print(reverseBits(4294967293))
#
#
# def hasAlternatingBits(n):
#     nstr = bin(n)[2:]
#     return all(nstr[i]!=nstr[i+1] for i in range(len(nstr)-1))
# print(hasAlternatingBits(5))
# print(hasAlternatingBits(10))
# print(hasAlternatingBits(7))
# print(hasAlternatingBits(11))
#
# #Number of Steps to Reduce a Number to Zero
# def numberOfSteps (num):
#     step=0
#     while num>0:
#         if num%2==0:
#             num=num//2
#             step+=1
#         elif num%2!=0:
#             num=num-1
#             step += 1
#     return step
#
# print(numberOfSteps(14))
# print(numberOfSteps(8))
# print(numberOfSteps(123))
#
# nums = [1,2,3]
# res=[[]]
# for i in range(len(nums)+1):
#     for j in range(i+1,len(nums)+1):
#         sublist=nums[i:j]
#         res.append(sublist)
# print(res)

# In this Python exercise, write a Python program that will take the input from a user to move a robot around a room that
# will start from the original point of (0,0). The robot has the ability to move FORWARD, BACK, LEFT and RIGHT.
#
# The first input would be the located of the steps (forward, back, left and right). The second part of the input would be
# the numerical number of steps ( 1, 2, 3, 4, 5 and so on).
#
# # The output should compute the current position distance from the sequence of movements and the original location point.
# import math
# pos=[0,0]
#
# while True:
#     ds=input("What direction and how many steps? ")
#     if not ds:
#         break
#     path=ds.split()
#     direction=path[0].upper()
#     steps=int(path[1])
#     if direction=='FORWARD':
#         pos[0]+=steps
#     elif direction=='BACK':
#         pos[0] -= steps
#     elif direction=='RIGHT':
#         pos[1] += steps
#     elif direction=='LEFT':
#         pos[1] -= steps
#     else:
#         pass
# # print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
# from  operator import itemgetter
# user_data=[]
# print("Please enter the user data in order of first and last name, age, weight, and height separated by commas. ")
# while True:
#     data=input()
#     if not data:
#         break
#     user_data.append(tuple(data.split(',')))
# print(user_data)
#
# print('Sorting on name',sorted(user_data,key=itemgetter(0)))
# print('Sorting on age',sorted(user_data,key=itemgetter(1)))
# print('Sorting on weight',sorted(user_data,key=itemgetter(2)))
# print('Sorting on height',sorted(user_data,key=itemgetter(3)))

# from itertools import combinations
# arr=[0,-1,2,-3,1]
# for comb in combinations(arr,3):
#     if sum(comb)==0:
#         print(comb)

# def extsort(lst):
#     return sorted(lst,key=lambda x:x.split('.')[1])
#
#
# print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))
# from itertools import combinations_with_replacement
# def triplets(n):
#     lst=[i for i in range(n+1)]
#     for comb in combinations_with_replacement(lst,3):
#         #print(comb)
#         if sum(comb[:2])==comb[2]:
#             print(comb)
# print(triplets(5))

# def my_enumerate(lst):
#     for i in range(len(lst)):
#         yield (i,lst[i])
# for i in my_enumerate([20,10,40,30,60,80]):
#     print(i)
#
# def my_enumerate(lst,k):
#     for i in range(k-2,len(lst)):
#         yield (i+k,lst[i])
# for i in my_enumerate([20,10,40,30,60,80],2):
#     print(i)

# Python3 implementation of smallest
# difference triplet
#
# # Function to find maximum number
# def maximum(a, b, c):
#     return max(max(a, b), c)
#
#
# # Function to find minimum number
# def minimum(a, b, c):
#     return min(min(a, b), c)
#
#
# # Finds and prints the smallest
# # Difference Triplet
# def smallestDifferenceTriplet(arr1, arr2, arr3, n):
#     # sorting all the three arrays
#     arr1.sort()
#     arr2.sort()
#     arr3.sort()
#
#     # To store resultant three numbers
#     res_min = 0;
#     res_max = 0;
#     res_mid = 0
#
#     # pointers to arr1, arr2,
#     # arr3 respectively
#     i = 0;
#     j = 0;
#     k = 0
#
#     # Loop until one array reaches to its end
#     # Find the smallest difference.
#     diff = 2147483647
#     while (i < n and j < n and k < n):
#
#         sum = arr1[i] + arr2[j] + arr3[k]
#
#         # maximum number
#         max = maximum(arr1[i], arr2[j], arr3[k])
#
#         # Find minimum and increment its index.
#         min = minimum(arr1[i], arr2[j], arr3[k])
#         if (min == arr1[i]):
#             i += 1
#         elif (min == arr2[j]):
#             j += 1
#         else:
#             k += 1
#
#         # Comparing new difference with the
#         # previous one and updating accordingly
#         if (diff > (max - min)):
#             diff = max - min
#             res_max = max
#             res_mid = sum - (max + min)
#             res_min = min
#
#     # Print result
#     print(res_max, ",", res_mid, ",", res_min)
#
#
#
# # Driver code
# arr1 = [5, 2, 8]
# arr2 = [10, 7, 12]
# arr3 = [9, 14, 6]
# n = len(arr1)
# smallestDifferenceTriplet(arr1, arr2, arr3, n)

#Find the first duplicate/repeated character in the string.
# from collections import Counter
# s='character'
# d=Counter(s)
# print(d)
# for k,v in d.items():
#     if v>1:
#         print(k)
#         break

# from itertools import permutations
# s='ABCD'
# for i in range(1,len(s)+1):
#     for perm in permutations(s,i):
#         print(perm)
# from collections import OrderedDict
# d=OrderedDict()
# d['z']=26
# d['y']=25
# d['x']=24
# d['w']=23
# d['v']=22
# print(dict(d))

# import sys
# msg=sys.stdin.readlines()
# print(msg)

# def fibo_generate(n):
#     a=0
#     b=1
#     for i in range(n+1):
#         yield b
#         a,b=b,a+b
# print([i for i in fibo_generate(10)])
#
# s='75.7,77.7,88.9,34.6,73.5'
# temps=s.split(',')
# temps=[float(f) for f in temps]
# print('sum={},avg={}'.format(sum(temps),sum(temps)/len(temps)))

#return single occurence element from an array

# from collections import Counter
# def single(lst):
#     d=Counter(lst)
#     for k,v in d.items():
#         if v==1:
#             return k
# print(single([3,19,3,3,3,3]))
# print(single([1,2,3,21,3,1,2,3,2,1,3,1,2]))
# print(single([6, 1, 3, 3, 3, 6, 6]))

# def print_max(pos,lst):
#     min=pos
#     max=pos
#     while (min>0 & lst[min]<=lst[pos]):
#         min-=1
#     while(max<len(lst)-1 & lst[max]<=lst[pos]):
#         max-=1
#     print(str(lst[pos]) + "[" + str((min + 2)) + "," + str((max)) + "]")
#
# lst=[1, 5, 4, 3, 6]
# for i in range(len(lst)):
#     print_max(i,lst)
#
# def pyramid(n):
#     for i in range(n+1):
#         for j in range(i):
#             print('* ',end='')
#         print('\n')
#
# pyramid(8)
# pyramid(10)
# pyramid(15)
#
# def pyramid(n):
#     for i in range(1,n+1,2):
#         for j in range(i):
#             print('* ',end='')
#         print('\n')
#
# pyramid(8)
# pyramid(10)
# pyramid(15)

# import sys
#
# # Complete the staircase function below.
# def staircase(n):
#     for stairs in range(1, n + 1):
#         print(' ' * (n - stairs) + '#' * stairs)
#
# if __name__ == '__main__':
#     n = int(input())
#
#     staircase(n)

# import random
# #key='exit'
# while True:
#     print(random.randint(100000,900000))
#     key=input()
#     if key=='exit':
#         break

# get a string(word) from user, then make every possible permutation words.
# Ex)intput: tree => output : tree, rtee, rete, reet, etre, eetr, eert, eter, eret, teer, reet..

# from itertools import permutations
# s=input('enter a string')
# for combi in permutations(s,4):
#     print(''.join(combi))

# #given an int number count the number of 1s
# n=int(input())
# bin_num=bin(n)
# print('binary number is= {} Count 1s= {} '.format(bin_num,bin_num.count('1')))

# Given a char array find possible soln like :
# eg for "abc"
# ans: {a,ab,abc.b,bc,c}

# from itertools import permutations
# s='abc'
# for i in range(1,len(s)+1):
#     for combi in permutations(s,i):
#         print(''.join(combi))


# Given an integer array find the longest subarray cantaining consequitive nos.
#
# eg {4,5,34,33,32,11,10,31}
# ans is {31,32,33,34}

# lst=[4,5,34,33,32,11,10,31]
# lst=[str(i) for i in lst]
# print(sorted([i for i in lst if len(i)==2]))

# s='0b1001100101'
# swap=''
# for i in s[1:]:
#     if i=='0':
#         swap+='1'
#     elif i=='1':
#         swap+='0'
# print('0b'+swap)

# Given a list of 100 songs on your cell phone, find a way for each user to hear the songs without repeating songs,
# you need to use an algorithm that uses shuffle for songs.
from random import choice
# song='song'
# songs=[song+str(i) for i in range(1,101)]
# print(songs)

#What's the algorithm to transform the sentence "the brown fox ran fast" in "eht nworb xof nar tsaf" (reverse any word)

# def reverse(str1):
#     #words=str1.split()
#     return ' '.join([word [::-1] for word in str1.split()])
# print(reverse('eht nworb xof nar tsaf'))
# print(reverse("the brown fox ran fast"))

#rotating a list
#
# from collections import deque
# lst=[10,20,30,40,50,60]
# dq=deque(lst)
# dq.rotate(3)
# print(dq)
#
# dq.rotate(-3)
# print(dq)
#
# element=dq.pop()
# dq.appendleft(element)
# print(dq)
#
# element=dq.popleft()
# dq.append(element)
# print(dq)

#Write a function to return string when passed integer . Note : do not use tostring() in built function.

# def int_str(n):
#     # n_str=''
#     # while n>0:
#     #     rem=n%10
#     #     n_str+=str(rem)
#     #     n=n//10
#     # return n_str
#     return str(n)
# print(123)

# s='H-e-l-l-o-w'
# chars=s.split('-')
# print('-'.join(chars[::-1]))

# how to sort a list with dictionary as variables.Sort should be based on dictionary value.
#
# for example :
#
#
# a = [{'b':2},{'b':1},{'b':5}{'b':4]
# now the sort should be based on value.
#
# a=[{'b':2},{'b':1},{'b':5},{'b':4}]
# print(sorted(a,key=lambda x:x['b']))
#
# lis = [{ "name" : "Nandini", "age" : 20},
# { "name" : "Manjeet", "age" : 20 },
# { "name" : "Nikhil" , "age" : 19 }]
# print(sorted(lis,key=lambda x:x['name']))
# print(sorted(lis,key=lambda x:x['age']))
# print(sorted(lis,key=lambda x:(x['name'],x['age'])))
#
# lst=[{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
# print(sorted(lst,key=lambda x:x['name']))
# print(sorted(lst,key=lambda x:x['age']))
#
# from operator import itemgetter
# a=[{'b':2},{'b':1},{'b':5},{'b':4}]
# print(sorted(a,key=itemgetter('b')))

# given a stream of natural numbers ,
#
# and a array J contains integers in increasing orders
# operations performed J = [2,3,4]
# 1 2 3 4 5 6 7 8 9 10…………..27....100...1111
# first operation
#
# J[0] = 2 => remove every 2nd integer
#
# now the stream is
# 1 3 5 7 … 27
# J[1] = 3
# remove every 3rd
# stream is now
# 1 3 7 …
# 3rd
# given a natural number n , find if it will survive given J, or at what index it will
# die.
#
# lst=[i for i in range(1,51)]
# print(lst)
# index=[2,3,4,5,6,7,8]
#
# lst1=[i for i in range(1,51,j[0])]
# print(lst1)
#
# lst2=[i for i in range(1,51,j[1])]
# print(lst2)
#
# lst3=[i for i in range(1,51,j[2])]
# print(lst3)

# lst=[i for i in range(1,51)]
# index=[2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#
# for j in range(len(index)):
#     print([i for i in range(1,len(lst),index[j])])
# Given a file (which can be considered as a String with comma delimiter for the complexity of the question) of usernames and a value k, find top k usernames (with number of logins) who logged into the system the most.
#
# For example -
# Input:
# User (String) = user1, user4, user2, user1, user3, user1, user2, user3
# k (int) = 2
#
# Output:
# user1 (3)
# user2 (2)
# user3 (2)
#
# - Both user2 and user3 should be included since both has same number of logins

# from collections import Counter
# with open('1.txt','r') as fr:
#     data=fr.read()
#     words=data.split(',')
#     dict1=Counter(words)
#     print(dict1)
#     print(dict1.most_common(2))
#

# Sorted array of integers and key = 2.
# Return index at which this key is present in the array.
#
# in=1,2,2,2,2,2,3,4,5,6,7,8,9,10
# index=[]
# k=2
# arr=[1,2,2,6,2,9,3,4,5,2,7,8,2,10]
# for i,v in enumerate(arr):
#     if v==k:
#         index.append(i)
# print(index)

# Write a program to modify the string in following pattern,
# Change odd words to uppercase and Reverse the even words. Make sure that the spaces (multiple) between the words remains as it is.
# E.g.:
# Input : "This is a test String!!"
# Output: "THIS si A tset STRING!!"
#
# str1="This is a test String!!"
#
# new_str1=[]
# words=str1.split()
#
# for i in range(len(words)):
#     if i%2==0:
#         new_str1.append(words[i].upper())
#     else:
#         new_str1.append(words[i][::-1])
# print(' '.join(new_str1))

# There are several words in a file. Get the occurrence of every word and sort it based on the occurrence,
# if more than one word is having same occurrence than sort it alphabetically.
#
# from collections import Counter
# with open('1.txt','r') as fr:
#     data=fr.read()
#     words=data.split()
#     dict1=Counter(words)
#     print(sorted(dict1.items(),key=lambda x:x[1]))
#
# def prime(n):
#     flag=0
#     for i in range(2,n):
#         if n%i==0:
#             break
#     else:
#         flag=1
#     if flag:
#         return('prime')
#     else:
#         return('not prime')
# prime(17)
# prime(18)
# prime(19)
#
# for i in range(50,150):
#     print(i,prime(i))

#circulary equivalent of two strings

from collections import deque
#import time
# s1='juniper'
# s2='iperjun'
# i=1
# while True:
#     s2=deque(s2)
#     s2.rotate(i)
#     s2=''.join(s2)
#     print(s2,s1)
#
#     if s2==s1:
#         print('circulary eqvivalent')
#         break
#     i+=1

# def square_gen():
#     for i in range(10):
#         yield i**2
#
#
# for v in square_gen():
#     print(v)

#highest positive products of three numbers
# I recently, appeared for second phone interview with CloudEra, the interviewer asked me to
# write a function which takes in an array of integers and returns the highest positive product
# possible by multiplying 3 distinct numbers. NO SORTING is ALLOWED
#
# PS: Please write a solution in JAVA or Python. (Not interviewer request)
#
#
# example:
#
# [1, 3, 5, 2, 8, 0, -1, 3]
#
# => 8 * 5 * 3 = 120
#
# [0, -1, 3, 100, -70, -5]
#
# => -70*-50*100=350000
#
# def products(lst):
#     lst.sort()
#     return lst[-1]*lst[-2]*lst[-3]
#
# print(products([1, 3, 5, 2, 8, 0, -1, 3]))
# print(products([0, -1, 3, 100, -70, -5]))

# If in a relation there are multiple duplicate rows . Your task is to delete one duplicate row.
#
# a1 a2
# 1 3
# 1 3
# 2 4
# 3 5
# 3 5
# 3 5
# after deletion
# a1 a2
# 1 3
# 2 4
# 3 5
# 3 5
#
# 3
# Give this input: Sea!tle is a nice place. Work Hard! have Fun, make HIStory!
# display this output using any C or vb script:
# Seattle is a nice place.
# Work hard.
# Have fun.
# Make history.

# str1='Sea!tle is a nice place. Work Hard! have Fun, make HIStory!'
# str1=[i for i in str1 if i.isalpha() or i.isspace()]
# print(''.join(str1))

# Imagine we have a large string like this "ABCBAHELLOHOWRACECARAREYOUIAMAIDOINGGOOD" which contains multiple palindromes
# within it, like ABCBA, RACECAR, ARA, IAMAI etc... Now write a method which will accept this large string and return the
# largest palindrome from this string. If there are two palindromes which are of same size, it would be sufficient to
# just return any one of them.

# str1='ABCBAHELLOHOWRACECARAREYOUIAMAIDOINGGOOD'
# from itertools import combinations
# #for i in range(1,len(str1)):
# for combi in combinations(str1,15):
#     if combi==combi[::-1]:
#         print(''.join(combi))

#Given two strings remove duplicates and test it
#
# def duplicates(str1,str2):
#     return set(str1).intersection(set(str2))
#
# str1='there are two palindromes'
# str2='largest palindrome from'
# print(duplicates(str1,str2))
#
# #Remove common characters from two strings and print the common characters and test cases
# str1='there are two palindromes'
# str2='largest palindrome from'
# common=set(str1).intersection(set(str2))
# print(set(str1).symmetric_difference(common))
# print(set(str2).symmetric_difference(common))

# ###Print numbers between 45 to 4578 without repeating digits.###
# Ex: 45-ALLOWED;55(repeatng digits)(-NOT ALLOWED. Frnd tld ths 2 me.he tried diff concepts but interviewer wanted
# an OPTIMAL ONE..LETS C WHO WRITE THIS WITH SIMPLE LOGIC..

# for n in range(45,4579):
#     if len(set(str(n)))==1:
#         pass
#     else:
#         print(n)

#NEVER SKIP THIS QUESTION..ASKED IN AMAZON###
# Take THREE arrays,like arr1={1,3,5,7,9}; arr2={1,2,3,5,4,1,8,9,7};arr3={1,3,5,7,9,2,1,4,6,5,8};Now find out the
# Duplicates of First two(arr1,arr2) arrays and store it in new another array arr4(should contain only duplicates,
# no unique elements).Now compare arr3 with arr4.You should return only UNIQUE elements from both of the array.
# If found, return it, else return -1.

# a1=[1,3,5,7,9]
# a2=[1,2,3,5,4,1,8,9,7]
# a3=[1,3,5,7,9,2,1,4,6,5,8]
#
# a1_a2_common=set(a1).intersection(set(a2))
# print(a1_a2_common)
#
# print(set(a3).symmetric_difference(a1_a2_common))

# Write a method to determine if two strings are anagrams of each other.
# e.g. isAnagram(“secure”, “rescue”) → false
# e.g. isAnagram(“conifers”, “fir cones”) → true
# e.g. isAnagram(“google”, “facebook”) → false

# def anagrams(s1,s2):
#     if sorted(s1)==sorted(s2):
#         return True
#     else:
#         return False
#
# print(anagrams('secure', 'rescue'))
# print(anagrams('conifers', 'fir cones'))
# print(anagrams('google', 'facebook'))

# Given array of words, group the anagrams
# IP:{tar,rat,banana,atr}
# OP:{[tar,rat,atr],[banana]}

# def group_anagrams(words):
#     A=[''.join(sorted(word)) for word in words]
#
#     dict1={}
#     for i,v in enumerate(A):
#         dict1.setdefault(v,[]).append(i)
#
#     for index in dict1.values():
#         print([words[i] for i in index])
# words=['tar','rat','banana','atr']
# # #words=["CARS", "REPAID", "DUES", "NOSE", "SIGNED", "LANE",
# #         "PAIRED", "ARCS", "GRAB", "USED", "ONES", "BRAG",
# #         "SUED", "LEAN", "SCAR", "DESIGN"]
# group_anagrams(words)

# Given any string (for e.g. "abfdRacecaRAbAorTITabcdef" find all the palindromes and return the longest one.
# Discuss the approach before you actually go ahead and code.

# from itertools import combinations
# str1='abfdRacecaRAbAorTITabcdef'
# palindrome=[]
# for i in range(1,len(str1)):
#     for combi in combinations(str1,i):
#         if combi==combi[::-1]:
#             #print(combi)
#             palindrome.append(''.join(combi))
#
# print(palindrome,len(palindrome),max(palindrome))

# Given a sorted integer array and a number, find the start and end indexes of the number in the array.
#
# Ex1: Array = {0,0,2,3,3,3,3,4,7,7,9} and Number = 3 --> Output = {3,6}
# Ex2: Array = {0,0,2,3,3,3,3,4,7,7,9} and Number = 5 --> Output = {-1,-1}
#
# Complexity should be less than O(n)

# def index(lst,k):
#     res=[]
#     for i,v in enumerate(lst):
#         if v==k:
#             res.append(i)
#     return (res[0],res[-1])
#
# print(index([0,0,2,3,3,3,3,4,7,7,9],3))
# print(index([0,0,2,3,3,3,3,4,7,7,9],7))
# print(index([0,0,2,3,3,3,3,4,7,7,9],5))

# In a given array a = {1, 7, 3, 4, 5, 6, 2} Print the indices of all the combinations which lead to a given sum
# called target. For e.g. if the method is
# Void PrintAllSumCombos(int[] arr, int target) - and the array shown above is passed with sum target = 7,
# then the output should be:
#
# 0, 3, 6
# 0, 5
# 1
# 2, 3
# 4, 6

# from itertools import combinations
# def print_sum(lst,k):
#     indexes=[]
#     for i in range(1,len(lst)):
#         for combi in combinations(lst,i):
#             if sum(combi)==k:
#                 temp = []
#                 for e in combi:
#
#                     #print(lst.index(e))
#                     temp.append(lst.index(e))
#                 indexes.append(temp)
#     return indexes
# print(print_sum([1, 7, 3, 4, 5, 6, 2],7))

# In an array of unsorted integers (you may assume the array may contain +ve, -ve and 0s), write a function
# int returnNthMax(int[] arr, int n)
# which will return the nth Max number. For e.g. if this is given array {2, -4, 5, 6, 0, 7, -1, 10, 9} and n=1,
# it should return the max number, 10 and if n=3, it should return 3rd max number, which is: 7.

# def print_max(lst,k):
#     lst.sort()
#     return lst[-k]
#
# print(print_max([2, -4, 5, 6, 0, 7, -1, 10, 9],1))
# print(print_max([2, -4, 5, 6, 0, 7, -1, 10, 9],3))
# print(print_max([2, -4, 5, 6, 0, 7, -1, 10, 9],2))
# print(print_max([2, -4, 5, 6, 0, 7, -1, 10, 9],4))

# A large character array is there in which there are spaces in between the character like ab c d ...etc
# Write a method to search any character in the above array in O(n).
#
# from collections import Counter
#
# def get_char(lst,char):
#     chars=lst.split()
#     dict1=Counter(chars)
#     return dict1[char]
#
# lst='A l a r g e c h a r a c t e r a r r a y i s t h e r e i n w h i c h t h e r e a r e s p a c e s ' \
#     'i n b e t w e e n t h e c h a r a c t e r'
# print(get_char(lst,'r'))
# print(get_char(lst,'a'))
# print(get_char(lst,'i'))
# print(get_char(lst,'s'))

from operator import itemgetter
emp_details = {'Employee': {'Dave': {'ID': '001',
                                     'Salary': 2000,
                                     'Designation':'Python Developer'},
                            'Ava': {'ID':'002',
                                    'Salary': 2300,
                                    'Designation': 'Java Developer'},
                            'Joe': {'ID': '003',
                                    'Salary': 1843,
                                    'Designation': 'Hadoop Developer'}}}

print(emp_details['Employee']['Joe']['Designation'])
dict1={}
emp_details['Employee']['siddu']={'ID': '003',
                'Salary': 12345,
                'Designation': 'pythonsta'}
print(emp_details)

print(sorted(emp_details['Employee'].items(),key=itemgetter(0),reverse=True))

from collections import defaultdict
dd = defaultdict(list)

# Accessing a missing key creates it and initializes it
# using the default factory, i.e. list() in this example:
# dd['dogs'].append('Rufus')
# dd['dogs'].append('Kathrin')
# dd['dogs'].append('Mr Sniffles')
# print(dd)
#
# from collections import ChainMap
# dict1 = {'one': 1, 'two': 2}
# dict2 = {'three': 3, 'four': 4}
# dict3 = {'five': 5, 'six': 6}
# dict4 = {'seven': 7, 'eight': 8}
#
# chain = ChainMap(dict1, dict2,dict3,dict4)
# print(chain)
#
# print(chain['one'])
# print(chain['four'])
# print(chain['six'])
# print(chain['eight'])

# from itertools import permutations
# #s="ABBABBC"
# s='forgeeksskeegfor'
# res=[]
# for i in range(1,len(s)):
#     for combi in permutations(s,i):
#         if combi==combi[::-1]:
#             res.append(''.join(combi))
# print(res)
# print(max(res,key=len))

#get the numbers which appear in odd and even number of times

# from collections import Counter
# arr=[2,5,1,7,9,2,1,5,8,9,4,1,7,3,8,9,6,1,2,5,2,3]
# even=[]
# odd=[]
# dict1=Counter(arr)
# for k,v in dict1.items():
#     if v%2==0:
#         even.append(k)
#     elif v%2!=0:
#         odd.append(k)
# print(even,odd)
