print("==List Programming==")
list1=[10,20,30,40,20,51]
a=list1 + [60]
b=list1.count(20)
c=list1.pop()
d=list1*2
e=list1.index(40)
print(a)
print(b)
print(c)
print(d)
print(e)

print("==Tuple Operations==")
tup1=(1,2,3,4,5,2)
print(tup1.index(4))
print(tup1.count(2))
print(len(tup1))
print(tup1*2)

print("==Dictionary Operations==")
dict1 = {"name":"Mohammad",
         "amount":"$2,000,000",
          "Bank":"JPMorgan Chase"}
print(len(dict1))
print(dict1['amount'])
print(dict1['Bank'])
dict1["asset_type"] = ["Fine Art & Bullion"]
print(dict1["asset_type"])
print(dict1.keys())
print(dict1.values())