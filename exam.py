from math import exp




def sig(x):

    return 1/(1+exp(-x))
    
def d_sig(x): #The derivative of sig. I've written this fact in the exam: page 9 line 4

    return sig(x)*(1-sig(x))
    
x1=1.2
x2=3.2
x3=0.5

w1=0.5
w2=0.3
w3=0.25
w4=0.3
w5=0.6
w6=0.15

#I defined those in page 8 in the exam.
o3=x1*w1
o4=sig(x2*w2+x3*w3)

#Saif Alef

o1=sig(w4*o3)
o2=w5*o3*w6*o4

#Saif Beit- I will write the formulas in the EXACT same manner as the exam
#Page 8 in the exam:

dw1=x1*o4*w5*w6
dw2=w5*o3*w6*d_sig(x2*w2+x3*w3)*x2
dw3=w5*o3*w6*d_sig(x2*w2+x3*w3)*x3
dw4=0
dw5=o3*w6*o4
dw6=w5*o3*o4



dw1=2*(1-o2)*dw1
dw2=2*(1-o2)*dw2
dw3=2*(1-o2)*dw3
dw4=2*(1-o2)*dw4
dw5=2*(1-o2)*dw5
dw6=2*(1-o2)*dw6


grad=[dw1,dw2,dw3,dw4,dw5,dw6]
i=0
for dw in grad:
    i+=1
    print('dw'+str(i)+'='+str(dw))

    
#Saif Dalet-Page 10
print('1-'+str(w5*w6*x1*o4)+'*w1')
