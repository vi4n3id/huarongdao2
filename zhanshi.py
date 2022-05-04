import numpy
import matplotlib.pyplot as plt
import copy
import huarongdao.init as init0
qizis=[]
qizis_find={}
rw=[i[2] for i in init0.list123]+['000']
print(rw)
finnnnn={}
for i in rw:
    d2={}
    for j in rw:
        d1={}
        for k in rw:
            d0={}
            for h in rw:
                d11={}
                for w in rw:
                    d12={}
                    for p in rw:
                        d12[p]=[]
                    d11[w]=d12
                d0[h] = d11
            d1[k] = d0
        d2[j] = d1
    finnnnn[i] = d2

def dicapp():
    finnnnn[qipan_r[1, 0]][qipan_r[1, 2]][qipan_r[3, 1]][qipan_r[3, 3]]\
        [qipan_r[4, 2]][qipan_r[0, 1]].append(copy.copy(qipan_r))

def dicfind():
    return finnnnn[qipan_r[1, 0]][qipan_r[1, 2]][qipan_r[3, 1]][qipan_r[3, 3]][qipan_r[4, 2]][qipan_r[0, 1]]



qipan_r=numpy.array([['000' for j in range(4)]for i in range(5)])

class qizi():
    def __init__(self,color,position,name):
        self.color=color
        self.position=position
        self.name=name

def qi_init():
    for i in init0.list123:
        print(i[2])
        qizis.append(qizi(i[0], i[1], i[2]))
    for i in qizis:
        qizis_find[i.name]=i
        for j in i.position:
            qipan_r[j[0],j[1]]=i.name



def display(en):
    qipan_d = numpy.zeros([5, 4, 3])
    for i in qizis:
        for j in i.position:
            for k in range(3):
                qipan_d[j[0],j[1],k]=i.color[k]
    plt.imshow(qipan_d)
    if en == 0:
        plt.show()
    if en == 1:
        plt.pause(0.5)


def mov(nam,step):
    qi=qizis_find[nam]
    error=0
    l=[[j for j in i] for i in qi.position]
    for i in qi.position:
        i[0] += step[0]
        i[1] += step[1]
        if i[0]>4 or i[0]<0 or i[1]>3 or i[1]<0\
                or (qipan_r[i[0],i[1]] != qi.name and qipan_r[i[0],i[1]] != '000'):
            error=1
    if error == 1:
        for i in qi.position:
            i[0] -= step[0]
            i[1] -= step[1]
        return 1

    for i in l:
        qipan_r[i[0], i[1]]='000'
    for i in qi.position:
        qipan_r[i[0], i[1]]=qi.name
    return 0

def syn(r):
    global qipan_r
    for i in qizis:
        i.position=[]
    for i in range(5):
        for j in range(4):
            if r[i,j] != '000':
                qizis_find[r[i,j]].position.append([i,j])
    qipan_r = r



def deng(a,b):
    for i in range(5):
        for j in range(4):
            if a[i,j][0] != b[i,j][0]:
                return 0
    return 1

def exit(a,b):
    if len(a) == 0:
        return 0
    for i in a:
        if deng(i,b) == 1:
            return 1
    return 0



def possible():
    l=[]
    for i in range(5):
        for j in range(4):
            if qipan_r[i,j] == '000':
                if i+1 <= 4 and qipan_r[i+1,j] != '000':
                    l.append([qipan_r[i+1,j],[-1,0]])
                if i-1 >= 0 and qipan_r[i-1,j] != '000':
                    l.append([qipan_r[i-1,j],[1,0]])
                if j+1 <= 3 and qipan_r[i,j+1] != '000':
                    l.append([qipan_r[i,j+1],[0,-1]])
                if j-1 >=0 and qipan_r[i,j-1] != '000':
                    l.append([qipan_r[i,j-1],[0,1]])
    return l
qi_init()
with open('hrd.txt','r') as f:
    l=eval(f.read())
    l=[numpy.array(i) for i in l]
    for i in l:
        syn(i)
        display(1)
plt.show()