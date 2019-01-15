#classic approch
x=[4,5,12,-2,8,9]

anslist=[]
# for i in range(0,len(x)-1):
#     for j in range(i+1,len(x)):
#         if x[i]+x[j]==10:
#             anslist.append((x[i],x[j]))
# print(anslist)

# Above method takes more time complexity greater than O(n) lest than O(n*n)
# so Efficient method

hashlist=[]
#it is more like to store visited elements in list
for i in x:
    try:
        indexVal=hashlist.index(10-i)
        #checks if i subtracted from 10 value exist in anslist
    except ValueError:
        indexVal=-1
    if indexVal==-1:
        hashlist.append(i)
    else:
        anslist.append((i,10-i))
print(anslist)

