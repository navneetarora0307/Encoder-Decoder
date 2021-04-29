import numpy as np
import math

class Crypto:

    def Encryptor(self,msg):
        length=len(msg)
        n= math.sqrt(length)
        n=math.ceil(n)
        list1=[]
        for i in range(length):
            list1.append(ord(msg[i:i+1]))
        
        list2=[]
        if (length%2==0):
            for i in range(int(length/2)):
                k=2*i
                diff=list1[k]-list1[k+1]
                if (diff==0): diff=2020
                list2.append(list1[k]+list1[k+1])
                list2.append(diff)
        if (length%2==1):
            for i in range(int((length-1)/2)):
                k=2*i
                list2.append(list1[k]+list1[k+1])
                diff=list1[k]-list1[k+1]
                if (diff==0): diff=2020
                list2.append(diff)
            list2.append(list1[length-1])
        for i in range (n*n-length):
            list2.append(0)
        mat=np.array(list2)
        mat=np.reshape(mat,(n,n))
        mat2=np.random.randint(10000,size=(n,n))
        random=np.random.randint(40,size=(1,1))
        mat3=np.mod(mat2,random)
        flist=[]
        flist.append(random[0][0])
        mat4=np.matmul(mat,mat3)
        for i in range(n*n):
            flist.append((mat4.reshape(n*n,1))[i][0])
            flist.append((mat2.reshape(n*n,1))[i][0])
        return flist


    def Decryptor(self,encmsg):
        random=encmsg[0]
        n=int(math.sqrt((len(encmsg)-1)/2))
        list1=[]
        list2=[]
        for i in range(n*n):
            k=2*i+1
            list1.append(int(encmsg[k]))
        for i in range(n*n):
            k=2*i+2
            list2.append(int(encmsg[k]))
        mat=np.array(list1)
        mat=np.reshape(mat,(n,n))
        mat2=np.array(list2)
        mat2=mat2.reshape(n,n)
        mat2=np.mod(mat2,random)
        inv=np.linalg.inv(mat2)
        decmsg=np.matmul(mat,inv)
        li=[]
        decmsg=decmsg.reshape(n*n,1)
        for i in range(n*n):
            key=int(round(decmsg[i][0]))
            if (key!=0):
                li.append(key)
        li1=[]
        if (len(li)%2==0):
            for i in range(int(len(li)/2)):
                k=2*i
                if(li[k+1]==2020):
                    li[k+1]=0 
                li1.append((li[k]+li[k+1])/2)
                li1.append((li[k]-li[k+1])/2)
        else:
            for i in range(int(len(li)/2)):
                k=2*i
                if(li[k+1]==2020): 
                    li[k+1]=0
                li1.append((li[k]+li[k+1])/2)
                li1.append((li[k]-li[k+1])/2)
            li1.append(li[len(li)-1])
        output=""
        for i in range(len(li1)):
            if (int(li1[i])!=0):
                output=output+chr(int(li1[i]))
        return output

    def convertToString(self,LIST):
        StrList = [str(element) for element in LIST]
        output = ",".join(StrList)
        return output

    def ConvertToList(self,STRING):
        output = STRING.split(",")
        for i in range(0, len(output)): 
            output[i] = int(output[i]) 
        return output