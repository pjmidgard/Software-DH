from time import time
cvf=0
import os
import binascii
namez = input("program new: c to new old: e ")
#@Author Jurijus pacalovas
class compression:
    def cryptograpy_compression(self):
                

        
            
    
                self.name = "Written: Jurijus pacalovas"
                if namez=="e":
                    name = input("What is name of file? ")
                    namea="file.WhiteHall"
                    namem=""
                    namema="?"
                   
                    blockw=5
                    blockw1=4
                    T=100001
                    assxw=0
                    name_cut=""
                    name_cut=len(".bin")
                    nameas=name
                    
                    name_long=len(nameas)
                    nameSS=name[name_long-name_cut:]
                    if nameSS!=".bin":
                        x3=0.0
                        return print(x3)
                        
                    nameas=name[:name_long-name_cut]
                    
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

                    block=2
                    block2=0

                    x=0
                    x1=0
                    x2=0
                    x = time()

            
                    
                    with open(nameas, "w") as f4:
                            f4.write(s)
                   
                    with open(name, "rb") as binary_file:

           
                  
                        # Read the whole file at once
                        
                        data = binary_file.read()

                        s=str(data)
                        
            
                  
                        lenf1=len(data)
                        lenf5=len(data)
                        
            
                  
                        
                        if lenf1>(2**256)-1:
                            print("This file is too big");
                            raise SystemExit

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
                                block3=0
                                while block3<lenf2:
                                    	e4=sda2[block3:block3+4+T]
                                    	shake_reverse=0
                                    	e6=e4
                                    	
                                    	d2=int(e6,2)
                                    	d3=d2
                                    	e4=e4[2+T:4+T]+e4[0:2+T]
                                    	
             
		                                            
		                                     
                                                                      	
                                        		
                                        	
                                    	long_size=len(e4)
                                    	C="0"+str(long_size)+"b"
                                    	e3=e4
                                    	#print(e3)
    
                                    	
                                    	sda3+=e3
                                    	block3+=4+T
                                  
                                block3=0
                                sda3="" 
                                if assxw==0:
                                
                                    Water=100000
                                    Core=102400
                                
                                while block3<lenf2:

                                    	e4=sda2[block3:block3+102400]

                                    	shake_reverse=0

                                    	e6=e4

                                    	

                                    	d2=int(e6,2)

                                    	d3=d2

                                    	

                                    	if len(e4)==Core:

	                                    	

		                                  

		                                    

		                                    	

		                                            

		                                            if d2>=((2**(Core*8))-(2**Water)):

		                                            	d2=d2-(2**(Water*8))

		                                            d2=d2+(2**Core)

		                                            

		                                            

		                                     

                                                                      	

                                        		

                                        	

                                    	long_size=len(e4)

                                    	C="0"+str(long_size)+"b"

                                    	e3=format(d2,C)

                                    	#print(e3)

    

                                    	

                                    	sda3+=e3

                                    	block3+=102400
                                    	
                                    	Water=-1
                                    	Core=-1
                                    	if Water==1 and Core==2401:
                                    	    Water=100000
                                    	    Core=102400
                                    	    
                                  
                                   
                               
                               
                            

                                    	
                                    	
                                    	
                                    	
                                    	
                               
                                       
                               
                                
                                                     		 
                                sda2=sda3
                                n = int(sda3, 2)
                                qqwslenf=len(sda3)
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
                                T=T-1
                                sda3=""
                                if assxw==100000:
                                         assx=10
                                         if assx==10:
                                             f2.write(jl)
                                             x2 = time()
                                             x3=x2-x
                                             return print(x3)
                

                           
    
            
    def cryptograpy_unpack(self):                       
                    if namez=="c":
                        name = input("What is name of file? ")
                        namea="file.WhiteHall"
                        namem=""
                        namema="?"
                        block2=0
                        T=1
              

                        assxw=0
                        blockw=5
                        blockw1=4
                        nameas=name
                        
                        nac=len(nameas)

                        long=len(name)
                   
                        name_cut=len(".bin")
                    
                        nameas=name+".bin" 
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

                        sscvf=0
                        
                        qqqqwzl=0

                        block=0

                        x=0
                        x1=0
                        x2=0
                        x = time()
                       
                        with open(nameas, "w") as f4:
                                f4.write(s)
                        
                        with open(name, "rb") as binary_file:
                            # Read the whole file at once
                            
                            data = binary_file.read()
                        
                            s=str(data)
                            lenf1=len(data)
                            lenf5=len(data)
                            
                            if lenf1>(2**32)-1:
                                print("This file is too big");
                                raise SystemExit
                            
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
                                        sda2=sda
                                        lenf3=len(sda2)
                                    lenf2=len(sda2)  
                                    block3=0
                                    sda3=""
                                    if assxw==0:
                                        Water=1
                                        Core=2401

                                    
                                    while block3<lenf2:
                                    	e4=sda2[block3:block3+102400]
                                    	shake_reverse=0
                                    	e6=e4
                                    	
                                    	d2=int(e6,2)
                                    	d3=d2
                                    	
                                    	if len(e4)==Core:
	                                    	
		                                  
		                                    
		                                    	
		                                            d2=d2-(2**Water)
		                                            if d2<=-1:
		                                            	d2=d2+(2**(Core*8))
		                                     
                                                                      	
                                        		
                                        	
                                    	long_size=len(e4)
                                    	C="0"+str(long_size)+"b"
                                    	e3=format(d2,C)
                                    	#print(e3)
    
                                    	
                                    	sda3+=e3
                                    	block3+=102400
                                    	Water=+1
                                    	Core=+1
                                    	if Water==100000 and Core==102400:
                                    	    Water=1
                                    	    Core=2401
                                    	    
                                  
                                    	#print(e4)
                                    sda2=sda3
                                    sda3=""
                                    block3=0
                                    	
                                    while block3<lenf2:

                                    	e4=sda2[block3:block3+4+T]

                                    	shake_reverse=0

                                    	e6=e4

                                    	

                                    	d2=int(e6,2)

                                    	d3=d2

                                    	

                                    	e4=e4[2+T:4+T]+e4[0:2+T]

	                                    	

		                                  

		                                    


		                                     

                                                                      	

                                        		

                                        	

                                    	long_size=len(e4)

                                    	C="0"+str(long_size)+"b"

                                    	e3=e4

                                    	#print(e3)

    

                                    	

                                    	sda3+=e3

                                    	block3+=4+T
                                     
                                    	
                                       	
	                                     	
	                                    
                                    	


                                    	

                                              
                                                         	
                                    sda2=sda3 
                                    n = int(sda3, 2)
                                    
                                    qqwslenf=len(sda3)
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
                                    T=T+1
                                    sda3=""
                                    if assxw==100000:
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