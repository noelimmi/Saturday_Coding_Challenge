# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 20:16:55 2019

@author: IMMI
"""
class Chocofinder:
    def __init__(self,cookie,row,col):
        self.cookie=cookie
        self.row=row
        self.col=col
        self.rans=[]
    def depthfirstsearch(self,i,j):
        if cookie[i][j]==0:
            return
        cookie[i][j] = 0
        self.rans.append([i,j])
        if i!=0:
            self.depthfirstsearch(i-1,j)
        if i!=row-1:
            self.depthfirstsearch(i+1,j)
        if j!=0:
            self.depthfirstsearch(i,j-1)
        if j!=col-1:
            self.depthfirstsearch(i,j+1)
    def countchoco(self):
        count = 0
        for i in range(self.row): 
            for j in range(self.col):
                #If a element in a 2d matrix is not visted and its value is one
                if self.cookie[i][j]==1:
                    self.depthfirstsearch(i,j)
                    self.rans.append(None)
                    count+=1
        seq=self.rans
        print("There are "+str(count)+" chocolate Chips in the cookie")
        return seq
        
    def splitz(self,seq):    
        group = []    
        for num in seq:
            if num != None:
                group.append(num)
            elif group:
                yield group
                group = []
if __name__ == "__main__":
     row,col= [int(x) for x in input("Enter the dimension for cookie ").split(" ")]
     cookie=[]
     print("enter "+str(col)+" values seperated by space")
     temp_row=row
     for i in range(row):
         while(temp_row!=0):
             m=list(map(int,input().split()))
             if(len(m)!=col):
                 print("Wrong Input")
             else:
                 temp_row-=1
                 cookie.append(m)
     obj1=Chocofinder(cookie,row,col)
     rans=obj1.countchoco()
     ans=list(obj1.splitz(rans))
     print("These are the path of each chocolate Chips are as follow")
     print(ans)
     print("--------------------------------")
     print([len(x) for x in ans])