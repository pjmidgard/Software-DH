import os  
from time import time
import binascii
import math
import os.path
namez = input("program: c and old program: e: ")
#@Author Jurijus pacalovas

class compression:
    def cryptograpy_compression(self):
                
                self.name = "Created: Jurijus pacalovas Price Portal 1000 000 000 Euro cost Date: 26/07/2021 17:11 Deep 14.5 ERA"
                if namez=="c":
                    corridors=0
                    cor=7
                    name = input("What is name of file? ")
                    namea="file.Secret"
                    namem=""
                    namema="?"

                    e5=0
                    e1=""
                    e6=0
                    e7=255

                    sda3=""
                    sda4=""
                    sda5=""

                   
                 
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
                    nameas=name+".bin"
                    
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                 
                    sda3=""
                    sda2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1
                    r=""

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                        
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if countraz==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)
                                c=1

                               
             
                                if c==1:

                                    block=0

                                    while block<lenf2:

                           
                                    

                                        e4=sda2[block:block+8]
                            
                                       
                                            
                                            
                                         
                                        e1=e4
                                        remaider=cvf1%blockw+block//16+block

                                        r1=(block//8)+(block//blockw)
                                        r2=(block//8)+block+(block//8)
                                        r3=block%3+(block//8)
                                        r4=block%4+(block//blockw)

                                        if remaider==0 and r1==0 or remaider==0 and r2==blockw or remaider==0 and r3==0 or remaider==0 and r4==0:
                                            e1=e4[4:8]+e4[2:4]+e4[0:2]

                                        if remaider==0 and r1==blockw or remaider==0 and r2==blockw or remaider==0 and r3==blockw or remaider==0 and r4==blockw:
                                            e1=e4[4:8]+e4[0:4] 
                                            
                                        if remaider==0:
                                            e1=e4[4:8]+e4[2:4]+e4[0:2]
                                            
                                              
                                        if remaider==1:
                                            e1=e4[4:8]+e4[0:4]                                          
                                        
                                                             
                                        
                                        e5=int(e1,2)
                                        if e5==e6:

                                            
                                            sda3=format(e7,"08b")
                                        elif e5==e7:
                                           
                                            sda3=format(e6,"08b")
                                       

                                        else:
                                            
                                            sda3=format(e5,"08b")
                                        sda4+=sda3
                                        
                                        blockw+=1
                                        if blockw==15:
                                            blockw==1
                                            
                                        block+=8                                    
                                    
                                    e6+=3
                                    e7-=3
                                    if e6>=255:
                                        e6=0
                                    if e7<=0:
                                        e7=255
                                    cvf1=cvf1+1
                                    sda2=sda4
                                    blockw=5
                                    sda4=""
                                    

                                    
            
                                   
                                    
                                    
                                    if cvf1==23:
                                                    
                                    
                                    
                                      



                                  
                                        
                                        n = int(sda2, 2)
                                        
                                        qqwslenf=len(sda2)
                                        qqwslenf=(qqwslenf/8)*2
                                        qqwslenf=str(qqwslenf)
                                        qqwslenf="%0"+qqwslenf+"x"
                                     
                                        jl=binascii.unhexlify(qqwslenf % n)
                                        sssssw=len(jl)
                                        data=jl
                                        qqqwz=qqqwz+1
                                        szxzzza=""
                                        szxzs=""
                                    
                                        assxw=assxw+1
                                        if assxw==1:
                                                assx=10
                                                if assx==10:
                                                  
                                                    f2.write(jl)
                                                    x2 = time()
                                                    x3=x2-x
                                                    return print(x3)
                                        
                                        
                                      
                                            
                                    

    def cryptograpy_unpack(self):                                 
                 if namez=="e":
                    corridors=0
                    cor=7
                    name=input("What is name of file? ")
                    namea="file.Secret"
                    namem=""
                    namema="?"
                    e1=""

                    e5=0
                    e6=0
                    e7=255

                    sda3=""
                    sda4=""
                    sda5=""
                    sda8=""

                 
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
                    nameas=name[:nac-4]
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                    cr=0
                 
                    sda3=""
                    sda2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1
                    cvf1=0

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                        # Read the whole file at once
                        data = binary_file.read()
                        s=str(data)
                        
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if countraz==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)
                                c=1

                                if c==1:

                                    block=0

                                    while block<lenf2:

                           
                                    

                                        e4=sda2[block:block+8]
                                        
                                        e61=""
                                        e61=e4[0:4]
                                        
                                        
    
                            
                                        
                                        e1=e4
                                        remaider=cvf1%blockw+block//16+block

                                        r1=(block//8)+(block//blockw)
                                        r2=(block//8)+block+(block//8)
                                        r3=block%3+(block//8)
                                        r4=block%4+(block//blockw)

                                        if remaider==0 and r1==0 or remaider==0 and r2==blockw or remaider==0 and r3==0 or remaider==0 and r4==0:
                                            e1=e4[4:8]+e4[2:4]+e4[0:2]

                                        if remaider==0 and r1==blockw or remaider==0 and r2==blockw or remaider==0 and r3==blockw or remaider==0 and r4==blockw:
                                            e1=e4[4:8]+e4[0:4] 
                                            
                                        if remaider==0:
                                            e1=e4[4:8]+e4[2:4]+e4[0:2]
                                            
                                              
                                        if remaider==1:
                                            e1=e4[4:8]+e4[0:4]                                          
                                        
                                                             
                                        
                                        e5=int(e1,2)
                                        if e5==e6:

                                            
                                            sda3=format(e7,"08b")
                                        elif e5==e7:
                                           
                                            sda3=format(e6,"08b")

                                        else:
                                            
                                            sda3=format(e5,"08b")
                                        sda4+=sda3
                                        
                                        blockw+=1
                                        if blockw==15:
                                            blockw==1
                                            
                                        block+=8                                    
                                    
                                    e6+=3
                                    e7-=3
                                    if e6>=255:
                                        e6=0
                                    if e7<=0:
                                        e7=255
                                    cvf1=cvf1+1
                                    sda2=sda4
                                    blockw=5
                                    sda4=""
                                    
                                 
                                    if cvf1==23:
                                                   
                                        
                                        
                                        n = int(sda2, 2)
                                        
                                        qqwslenf=len(sda2)
                                        qqwslenf=(qqwslenf/8)*2
                                        qqwslenf=str(qqwslenf)
                                        qqwslenf="%0"+qqwslenf+"x"
                                     
                                        jl=binascii.unhexlify(qqwslenf % n)
                                        sssssw=len(jl)
                                        data=jl
                                        qqqwz=qqqwz+1
                                        szxzzza=""
                                        szxzs=""
                                    
                                        assxw=assxw+1
                                        if assxw==1:
                                                assx=10
                                                if assx==10:
                                                
                                                    f2.write(jl)
                                                    x2 = time()
                                                    x3=x2-x
                                                    return print(x3)
                     

                                
               

d=compression()

xw=d.cryptograpy_compression()
print(xw)

xw1=d.cryptograpy_unpack()
print(xw1)
