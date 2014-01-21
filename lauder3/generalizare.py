from matplotlib import pyplot
import math
import random
class pct:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def __mul__(self,n):
        P=pct(self.x*n,self.y*n)
        return P
    def __div__(self,n):
        P=pct(float(self.x)/n,float(self.y)/n)
        return P
    def __add__(self,other):
        S=pct(0,0)
        S.x=self.x+other.x
        S.y=self.y+other.y
        return S
class segm:
    def __init__(self,P,Q):
        self.A=pct(P.x,P.y)
        self.B=pct(Q.x,Q.y)
    def frag(self,k,n,start=0,end=0):
        P=pct(0,0)
        t=k*1.0/n
        P=self.A*t+self.B*(1-t)
        return P
class cerc:
    def __init__(self,P,a):
        self.O=pct(P.x,P.y)
        self.r=a
    #def frag(self,k,n,t=0):
    #    u=t+2*k*math.pi/n
    #    P=pct(self.r*math.cos(u),self.r*math.sin(u))
    #    P=P+self.O
    #    return P
    def frag(self,k,n,start=0,end=0):
        if end==0:
            u=start +2*k*math.pi/n
        else:
            if start<end:
                u=start+(end-start)*k/n
            else:
                u=start+(2*math.pi+end-start)*k/n
        P=pct(self.r*math.cos(u),self.r*math.sin(u))
        P=P+self.O
        return P   
#class arc:
#    def __init__(self,P,Q,t):
#        self.A=pct(P.x,P.y)
#        self.B=pct(Q.x,Q.y)
#        self.u=t
#    def frag(self,k,n):
#        #determin raza? AB=2*r*cos u, r=AB/(2*cos u)
#        #determin unghiul de start si centrul:
#        #A.x=O.x+r cos u, B.x=O.x+r
#    

def frag(x,k,n,start,end):
    return x.frag(k,n,start,end)
    

def linkshape(d1,d2,n,start1=0,end1=0,start2=0,end2=0,dir=0):
    x=[]
    y=[]
    for k in range(0,n+1):
        P=frag(d1,k,n,start1,end1)
        if dir==0:
            Q=frag(d2,n-k,n,start2,end2)
        else:
            Q=frag(d2,k,n,start2,end2) 
        if k%2==0:
            x+=[P.x,Q.x]
            y+=[P.y,Q.y]
        else:
            x+=[Q.x,P.x]
            y+=[Q.y,P.y]
    pyplot.plot(x,y)


O=pct(0,0)
O1=pct(-1,-1)
C=cerc(O,1)
C1=cerc(O1,math.sqrt(5))
#linkshape(C,C1,100,0,0,0,0,1)
linkshape(C,C1,120,0,math.pi/2,math.pi/6,math.pi/3,0)
pyplot.show()       