from time import time
cvf=0
import os
import binascii
self="'"

namez = input("for compress c or extract e? ")
#@Author Jurijus pacalovas
class compression:

    def cryptograpy_compression(self):

                
                
                self.name = "Author: Jurijus Pacalovas"

                print(self.name)

                if namez!="c" and namez!="e":
                    print("Your enter incorrect letter")
                
                if namez=="c":


                    
                   
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                   
                    long_block=100
                    times=0
                        
                    namea="file.W"
                    namem=""
                    namema="?"
                    Portal=2
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)

                    long=len(name)
                   

                    

                    
                    
                   
                    
                    Deep_long=240
                    Deep_long_All=Deep_long*16
                    block_size_long=16
                    Times_compression=1
                    
                    name_cut=len(".bin")
                    
                    nameas=name+".bin"
                    name_bofore=len(nameas)
                    F=0
                    
                    
                    	 
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

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
                        #import paq
                        #data=paq.compress(data)
                        data1=data
                        size_after2=len(data)
                        #print(size_after2)
                        if len(data)==0:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                            
                      
                         

                  
                        s=str(data)
                        
                        Limit_size_of_file=0
                        File_size_Divide=0
                        lenf1=len(data)
                        Divide=lenf1%2
                        File_size_Divide=0
                        
                        
                        if Divide==0:
                            Limit_size_of_file=0
                            File_size_Divide=0
                        elif Divide!=0:
                            Limit_size_of_file=0
                            File_size_Divide=1    
                    
                            
  
                            
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
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)

                                
                                    
                              
                                size_datat=size_data2
                                size_data3=size_data2
                                size_after3=len(size_datat)
                                #print(size_after3)
                                block=0
                             
                              



# Initialize variables in reverse order
                                size_data5 = size_datat
                                n = 5
                                a = 20  # Replace '42' with the desired numeric value for 'a'
                                blocks=-1
                                divisible_numbers = [1, 3, 7, 4, 5, 3, 7, 6, 8, 9, 5, 8, 7, 3, 2, 8, 6, 5, 6, 5, 4, 5, 5, 1, 3, 7, 4, 5, 3, 7, 6, 8, 9, 5, 8, 7, 3, 2, 8, 6, 5, 6, 5, 4, 5, 5, 1, 3, 7, 4, 5, 3, 7, 6, 8, 9, 5, 8, 7, 3, 2, 8, 6, 5, 6, 5, 4, 5, 5, 1, 3, 7, 4, 5, 3, 7, 6, 8, 9, 5, 8, 7, 3, 2, 8, 6, 5, 6, 5, 4, 5, 5, 1, 3, 7, 4, 5, 3, 7]



                                while block < size_after3:
                                    long_divide = size_datat[block:block + 8]
                                    long_divide1 = long_divide
                                    n += 2
                                    a-=5
                                    if any(blocks % num == 0 for num in divisible_numbers):
                                        if blocks==5:
                                           if n == 5:
                                                n = a
                                
                                    times = 0
                                    while times != 5 + n:
                                        long_divide_int = int(long_divide1, 2)
                                
                                        if long_divide_int % 2 == 0:
                                            long_divide_int = long_divide_int // 2
                                            c = "0" + str(7) + "b"
                                            div = format(long_divide_int, c)
                                            div = "1" + div
                                        elif long_divide_int % 2 == 1:
                                            long_divide_int = long_divide_int // 2
                                            c = "0" + str(7) + "b"
                                            div = format(long_divide_int, c)
                                            div = "0" + div
                                
                                        long_divide1 = div
                                        #print(len(long_divide1))
                                        div = ""
                                        times += 1
                                    
                                    block += 8
                                    size_data5 += long_divide1
                                


                                
                                
                                
              
                                                                        #print(size_data5)
                                                                    
                                                                    
                                                                                                 
                                w=1                              
                                if w==1:
                                            assxw=assxw+1
                                            


                                     
                                       
                                                                   
                                size_data11=size_data5
                                #print(size_data11)
                                
                                        
                                n = int(size_data11, 2)
                                    
                                qqwslenf=len(size_data11)
                                qqwslenf=(qqwslenf/8)*2
                                qqwslenf=str(qqwslenf)
                                qqwslenf="%0"+qqwslenf+"x"
                                 
                                jl=binascii.unhexlify(qqwslenf % n)
                                        
                                        
                                data2=jl
                                
                                size_after=len(jl)
    
                                        
                                     
                                        #print(size_after)
    
                                        
                                            
                                    
                                   
                                   
                                size_after=len(jl)                                                               
                                size_after=len(jl)
                                qqqwz=qqqwz+1
                                szxzzza=""
                                szxzs=""
                                
                                        
                                if assxw==1:
                                     assx=10
                                     if assx==10:
    
                                                f2.write(jl)
                                                x2 = time()
                                                x3=x2-x
                                                return print(x3)

    def cryptograpy_unpack(self):                      
                 if namez=="e":
                    
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                    Portal=2
                    namea="file.W"
                    namem=""
                    namema="?"
                    Deep=0
                 
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
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
                    
                  
                    
                    long=len(nameas)

                    
                    
                    
                    
                    Deep_long=240
                    Deep_long_All=Deep_long*16
                    block_size_long=16
                    Times_compression=1
                    	
                    
                    
                    nac=len(nameas)
                   
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

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
                        
                        data3 = binary_file.read()

                        data=data3

                    
                    

                        
                        
                        

                        if len(data)==0:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                     	

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
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)  
                                x4=1
                                if x4==1:

                                    

                                    size_data3=size_data2

                                    Limit=0
                                    File_size_divide=0
                                    File_size_dividel=1

                                    

                                    

                                    
                                size_data_chunk=size_data2
                                size_data3=size_data2
                                size_after3=len(size_data_chunk)
                                #print(size_after3)
                                block=size_after3
                                size_data5=""
                              


                                #```python


                                block = 0
                                while block < len(size_data_chunk):
                                    size_data_chunk_chunk = size_data_chunk[block:block + 8]
                                
                                    # Reverse inner loop
                                    times = 5 + n
                                    while times != 0:
                                        size_data_chunk_int = int(size_data_chunk_chunk, 2)
                                
                                        if size_data_chunk_int % 2 == 0:
                                            size_data_chunk_int = size_data_chunk_int * 2 + 1
                                        elif size_data_chunk_int % 2 == 1:
                                            size_data_chunk_int = size_data_chunk_int * 2
                                
                                        size_data_chunk_chunk = format(size_data_chunk_int, '08b')
                                        times -= 1
                                
                                    size_data5 += size_data_chunk_chunk
                                    block += 8
    
    # Resulting reversed size_after3
    
                                        
                                  # Reconstruct reversed dareversed_size_data = size_data_chunk + reversed_size_data
                                                                        #print(size_data5)
                                                                    
                                                                    
                                                                                                 
                                w=1                              
                                if w==1:
                                            assxw=assxw+1
                                            


                                     
                                       
                                                                   
                                size_data11=size_data5
                                #print(size_data11)
                                
                                        
                                n = int(size_data11, 2)
                                    
                                qqwslenf=len(size_data11)
                                qqwslenf=(qqwslenf/8)*2
                                qqwslenf=str(qqwslenf)
                                qqwslenf="%0"+qqwslenf+"x"
                                 
                                jl=binascii.unhexlify(qqwslenf % n)
                                        
                                        
                                data2=jl
                              
                                        
                                size_after=len(jl)
    
                                        
                                     
                                        #print(size_after)
    
                                        
                                            
                                    
                                   
                                   
                                size_after=len(jl)                                                               
                                size_after=len(jl)
                                qqqwz=qqqwz+1
                                szxzzza=""
                                szxzs=""
                                
                                        
                                if assxw==1:
                                     assx=10
                                     if assx==10:
    
                                                f2.write(jl)
                                                x2 = time()
                                                x3=x2-x
                                                return print(x3)

  
                  
self=""                                
d=compression()
    
xw=d.cryptograpy_compression()
print(xw)

xw1=d.cryptograpy_unpack()
print(xw1)