import os  

from time import time

import binascii

import math

import os.path

enter_name_of_file = input("c: compess to metadata e: extract? ")

#@Author Jurijus pacalovas



class compression:

    def cryptograpy_compression(self):

                

                self.name = "Created: Jurijus pacalovas Please, pay 1000 000"

                if enter_name_of_file=="c":

                    corridors=0

                    corridors_2=7

                    name = input("What is name of file? ")
                    
                    if os.path.exists(name):
                        print('Path is exists!')
                    else:
                        print('Path is not exists!')
                        raise SystemExit


                    name_new="file.Secret"

                    name_2=""

                    name_2_clear="?"
                    count_H=0



                    e5=0

                    e1=""

                    e6=0

                    e7=255
                    count_N_N=0


                    INFO3=""

                    INFO4=""

                    INFO5=""



                   

                 

                    reverse_bin=0

                    block_2=5

                    block_21=4

                    name_1=name

                    name_of_file=len(name_1)

                    name_1=name+".bin"

                    

                    name_of_file=len(name_1)

                    

                    count_numbers=0

                    counts_1=2

                    counts_11=0

                    s=""

                    e2=0

                    e3=2

                    e4=""

                    c=2
                    N=0
                    X=2
                    count_N=0

                    select_words=2

                    elements_words=0

                 

                    INFO3=""

                    INFO_OR_DATA_TO_BINARY=""



                    size_of_size_cosscounts_1=0

                    

                    binary_to_data=0



                    block=1

                    r=""
                    Er="0"



                    x=0

                    x1=0

                    x2=0

                    x = time()



                    with open(name_1, "w") as f4:

                            f4.write(s)

                    with open(name_1, "a") as f3:

                            f3.write(s)

                    with open(name, "rb") as binary_file:




                       # Read the whole file at once

                        data = binary_file.read()

                        s=str(data)

                       

                        long1=len(data)

                        long5=len(data)
                        long5_before=len(data)

                        

                        times_numbers_reapits=0

                        binary_to_data_1=0

                        

                       

                        while times_numbers_reapits<10:

                       

                            aas1=0

                            a1=0



                            counts_1=counts_1+1

                            

                            count_numbers=count_numbers+1



                            with open(name_1, "ab") as f2:

                                if count_numbers==1:

                                    INFO=bin(int(binascii.hexlify(data),16))[2:]

                                    long=len(INFO)

                                    long1=len(data)

                                

                                    times_7=(long1*8)-long

                                    z=0

                                    if times_7!=0:

                                        while z<times_7:

                                            INFO="0"+INFO

                                            z=z+1

                                            

                                    INFO=INFO+INFO_OR_DATA_TO_BINARY



                                    if count_numbers==1:

                                        INFO_OR_DATA_TO_BINARY=INFO

                            

                                    n = int(INFO_OR_DATA_TO_BINARY, 2)

                                

                                    binary_data=len(INFO_OR_DATA_TO_BINARY)

                                    binary_data=(binary_data/8)*2

                                    binary_data=str(binary_data)

                                    binary_data="%0"+binary_data+"x"

                             

                                    jl=binascii.unhexlify(binary_data % n)

                                    binary_to_data_2=len(jl)

                                    

                                    data=jl

                                    binary_to_data_1=binary_to_data_1+1

                                   

                                    if count_numbers==1:



                                        long5=len(data)



                                    INFO=bin(int(binascii.hexlify(data),16))[2:]

                                    long=len(INFO)



                                    long1=len(data)

                                

                                    times_7=(long1*8)-long

                                    z=0

                                    if times_7!=0:

                                        while z<times_7:

                                            INFO="0"+INFO

                                            z=z+1



                                    INFO_OR_DATA_TO_BINARY=INFO



                                    long3=len(INFO_OR_DATA_TO_BINARY)

                                long2=len(INFO_OR_DATA_TO_BINARY)
                                block=0
                                X=2
                                INFO_OR_DATA_TO_BINARY1=""
                                while block<long2:
                                
                                    INFO=INFO_OR_DATA_TO_BINARY[block:block+33]
                                    W=0
                                    from decimal import Decimal

                                    if len(INFO)==33:
                                    
                                        N=int(INFO,2)
                                        #print(N)
                                        N=Decimal(N/X)
                                        
                                        
                                    
                                    
                                            
                                        #print(N
                                        if N>=2**32:
                                            Er="1"
                                            
                                        
                                            
                                        number = N
                                            
                                        import struct
                                            
    
                                        # pack the float as a binary string
                                        s = struct.pack('!f', number) 
    
                                        # convert each byte to binary and join them
                                        b = ''.join(format(c, '08b') for c in s)
                                        Number=((2**33)-1)/2
                                        #print(Number)
                                        s = struct.pack('!f', Number)
                                        b2= ''.join(format(c, '08b') for c in s)
                                        #print(b2)
                                        if b==b2:
                                                        Er="1"
                                                        #print("wrong format of file!") 
                                        Number=(2**33)
                                        #print(Number)
                                        s = struct.pack('!f', Number)
                                        b2= ''.join(format(c, '08b') for c in s)
                                        #print(b2)
                                        if b==b2:
                                                        Er="1"                                                                
                                        
                                        #print(b)
                                        if b[0:1]!="0":
                                            Er="1"
                                            #print(Er)
                                            
                                                 
                                            
                                            
                                                
                                    if len(INFO)==33:
                                        INFO_OR_DATA_TO_BINARY1+=b
                                    else:
                                        INFO_OR_DATA_TO_BINARY1+=INFO
                                        #print(INFO)
                                            
                                    block+=33                                   


                               

                                
                                

                                

                                count_N+=1
                               # print(count_N)
                                if len(INFO)>0:
                                    
                                    last_block=len(INFO_OR_DATA_TO_BINARY1)
                                    INFO_OR_DATA_TO_BINARY1=INFO_OR_DATA_TO_BINARY1[:last_block-len(INFO)]
                                    INFO_OR_DATA_TO_BINARY1+=INFO
                                    
                                if Er=="0":
                                    INFO_OR_DATA_TO_BINARY=INFO_OR_DATA_TO_BINARY1
                                #print(len(INFO_OR_DATA_TO_BINARY1))
                                
                                

                                if len(INFO_OR_DATA_TO_BINARY)<=256 or count_N==(2**24)-1 or Er=="1":
                                        if Er=="1":
                                            count_N-=1
                                        
                                        
                                        
                                        long_N=format(count_N,"024b")
                                    
                                        long5_before_1=format(long5_before,"032b")
                                        
                                        
                                        INFO_OR_DATA_TO_BINARY="1"+INFO_OR_DATA_TO_BINARY
                                    
                                    
                           
                                        long1_After3=len(INFO_OR_DATA_TO_BINARY)
                                           
                                        add_bits118=""
                                        count_bits=8-long1_After3%8
                                        z=0
                                        
                                        if count_bits!=8:
                                                    while z<count_bits:
                                                        add_bits118="0"+add_bits118
                                                        z=z+1
                                                                        
                                                                        
                                        INFO_OR_DATA_TO_BINARY=long5_before_1+long_N+add_bits118+INFO_OR_DATA_TO_BINARY
                                        count_H+=1
                                        #print(count_H)
                                
                                        count_N=0
                                                                      
                                
                                        #print(len(INFO_OR_DATA_TO_BINARY))
                                            
               

                                        n = int(INFO_OR_DATA_TO_BINARY, 2)

                                            

                                        binary_data=len(INFO_OR_DATA_TO_BINARY)

                                        binary_data=(binary_data/8)*2

                                        binary_data=str(binary_data)

                                        binary_data="%0"+binary_data+"x"

                                         

                                        jl=binascii.unhexlify(binary_data % n)

                                        binary_to_data_2=len(jl)

                                        data=jl

                                        binary_to_data_1=binary_to_data_1+1

                                        binary_to_data_3=""

                                        size_x=""

                                        

                                        reverse_bin=reverse_bin+1

                                        if reverse_bin==1:

                                                times_numbers_reapits=10

                                                if times_numbers_reapits==10:

                                                      

                                                    f2.write(jl)

                                                    x2 = time()

                                                    x3=x2-x

                                                    return print(x3)

                                            

                                        

                                      

                                            

                                    


#############################################################################
    def cryptograpy_unpack(self):                                 

                 if enter_name_of_file=="e":

                    corridors=0

                    corridors_2=7

                    name=input("What is name of file? ")

                    if os.path.exists(name):
                        print('Path is exists!')
                    else:
                        print('Path is not exists!')
                        raise SystemExit

                    name_new="file.Secret"

                    name_2=""

                    name_2_clear="?"

                    e1=""
                    count_H=0



                    e5=0

                    e6=0

                    e7=255
                    count_N_N=0



                    INFO3=""

                    INFO4=""

                    INFO5=""

                    INFO8=""



                 

                    reverse_bin=0

                    block_2=5

                    block_21=4

                    name_1=name

                    name_of_file=len(name_1)

                    name_1=name[:name_of_file-4]

                    name_of_file=len(name_1)

                    

                    count_numbers=0

                    counts_1=2

                    counts_11=0

                    s=""

                    e2=0

                    e3=2

                    e4=""

                    c=2

                    select_words=2

                    elements_words=0

                    cr=0

                 

                    INFO3=""

                    INFO_OR_DATA_TO_BINARY=""



                    size_of_size_cosscounts_1=0

                    

                    binary_to_data=0
                    Times_count=0



                    block=1

                    counts_11=0



                    x=0

                    x1=0

                    x2=0

                    x = time()



                    with open(name_1, "w") as f4:

                            f4.write(s)

                    with open(name_1, "a") as f3:

                            f3.write(s)

                    with open(name, "rb") as binary_file:


                        # Read the whole file at once

                        data = binary_file.read()

                        s=str(data)

                       

                        long1=len(data)

                        long5=len(data)

                        

                        times_numbers_reapits=0

                        binary_to_data_1=0

                        

                       

                        while times_numbers_reapits<10:

                       

                            aas1=0

                            a1=0



                            counts_1=counts_1+1

                            

                            count_numbers=count_numbers+1



                            with open(name_1, "ab") as f2:

                                if count_numbers==1:

                                    INFO=bin(int(binascii.hexlify(data),16))[2:]

                                    long=len(INFO)

                                    long1=len(data)

                                

                                    times_7=(long1*8)-long

                                    z=0

                                    if times_7!=0:

                                        while z<times_7:

                                            INFO="0"+INFO

                                            z=z+1

                                            

                                    INFO=INFO+INFO_OR_DATA_TO_BINARY



                                    if count_numbers==1:

                                        INFO_OR_DATA_TO_BINARY=INFO

                            

                                    n = int(INFO_OR_DATA_TO_BINARY, 2)

                                

                                    binary_data=len(INFO_OR_DATA_TO_BINARY)

                                    binary_data=(binary_data/8)*2

                                    binary_data=str(binary_data)

                                    binary_data="%0"+binary_data+"x"

                             

                                    jl=binascii.unhexlify(binary_data % n)

                                    binary_to_data_2=len(jl)

                                    

                                    data=jl

                                    binary_to_data_1=binary_to_data_1+1

                                   

                                    if count_numbers==1:



                                        long5=len(data)



                                    INFO=bin(int(binascii.hexlify(data),16))[2:]

                                    long=len(INFO)



                                    long1=len(data)

                                

                                    times_7=(long1*8)-long

                                    z=0

                                    if times_7!=0:

                                        while z<times_7:

                                            INFO="0"+INFO

                                            z=z+1



                                    INFO_OR_DATA_TO_BINARY=INFO



                                long3=len(INFO_OR_DATA_TO_BINARY)
                                


                                
                                N5_size=int(INFO_OR_DATA_TO_BINARY[:32],2)
                                INFO_OR_DATA_TO_BINARY=INFO_OR_DATA_TO_BINARY[32:]
                                N3=int(INFO_OR_DATA_TO_BINARY[:24],2)
                                INFO_OR_DATA_TO_BINARY=INFO_OR_DATA_TO_BINARY[24:]
                                F=INFO_OR_DATA_TO_BINARY
                                #print(N3)


                                if N3==0:
                                        INFO_OR_DATA_TO_BINARY=F
                                        W=1
                            
                                    
                                    #print(N3)


                                if N3!=0:

                                    size_data3=INFO_OR_DATA_TO_BINARY    
                                    if size_data3[0:9]=="000000001":
                                        size_data3=size_data3[9:]
                                    elif size_data3[0:8]=="00000001":
                                        size_data3=size_data3[8:]
                                    elif size_data3[0:7]=="0000001":
                                        size_data3=size_data3[7:]
                                    elif size_data3[0:6]=="000001":
                                        size_data3=size_data3[6:]
                                    elif size_data3[0:5]=="00001":
                                        size_data3=size_data3[5:]
                                    elif size_data3[0:4]=="0001":
                                        size_data3=size_data3[4:]
                                    elif size_data3[0:3]=="001":
                                        size_data3=size_data3[3:]
                                    elif size_data3[0:2]=="01":
                                        size_data3=size_data3[2:]
                                    elif size_data3[0:1]=="1":
                                        size_data3=size_data3[1:]
        
                                    INFO_OR_DATA_TO_BINARY=size_data3     
                                    W=0
                                    count_N_N=0
                                    while W!=1:
                                        long2=len(INFO_OR_DATA_TO_BINARY)
                                        block=0
                                        X=2
                                        b2=""
                                        INFO_OR_DATA_TO_BINARY1=""
                                        while block<long2:
                                            
                                            INFO=INFO_OR_DATA_TO_BINARY[block:block+32]
                                            INFO5=INFO_OR_DATA_TO_BINARY[block:block+32]
                                            INFO2=INFO_OR_DATA_TO_BINARY[block:block+33]
                                            #print(INFO)
                                        
                                            if len(INFO)==32:
                                                from decimal import Decimal

                                                Varitions=0
                                                Find=2**32     
                                                Find1=-1
                                                                   
                                                while Varitions!=1:
                                                    Find1+=1
                                                    INFO=format(Find1,"032b")
                                                    #print(INFO)
                                                     

                                              
                                                
                                                    N=int(INFO,2)
                                                    #print(Find)
                                                    N=Decimal(N/2)
                                                    
                                                    
                                                
                                                   
                                                        
                                                    #print(N)
                                                    
                                                        
                                                    number = N
                                                        
                                                    import struct
                                                        

                                                    # pack the float as a binary string
                                                    s = struct.pack('!f', number) 

                                                    # convert each byte to binary and join them
                                                    b = ''.join(format(c, '08b') for c in s)#0-7
                                                    b2=format(Find1,"033b")
                                   
                                                        
                                                        
                                                            
                                                    if INFO5==b or Find1==2**33:
                                                          
                                                          Varitions=1
                                                          block+=32
                                                          
                                            else:
                                                b2=INFO2
                                                block+=33
                                         
                                                                                        
                                            INFO_OR_DATA_TO_BINARY1+=b2        
                                                                                    


                                       

                                        
                                        

                                        #print(INFO_OR_DATA_TO_BINARY1)

                                        count_N_N+=1
                                        
                                        if len(INFO)>0:

                                            last_block=len(INFO_OR_DATA_TO_BINARY1)
                                            INFO_OR_DATA_TO_BINARY1=INFO_OR_DATA_TO_BINARY1[:last_block-len(INFO)]
                                            INFO_OR_DATA_TO_BINARY1+=INFO
                                            INFO_OR_DATA_TO_BINARY=INFO_OR_DATA_TO_BINARY1
                                        if N3==0:
                                            INFO_OR_DATA_TO_BINARY=F
                                            count_N_N=0
                                        #print(count_N_N)
     
     
                                      
                                        
                                        #print(len(INFO_OR_DATA_TO_BINARY1))
                                        
                                        

                                        if count_N_N==N3:
                                            W=1
                                            
                                            
                                    
                                if W==1:                                        
                                        
                                        
                                        
                                    
                                    
                                    
                           
                                        long1_After3=len(INFO_OR_DATA_TO_BINARY)
                                           
                                        add_bits118=""
                                        count_bits=8-long1_After3%8
                                        z=0
                                        
                                        if count_bits!=8:
                                                    while z<count_bits:
                                                        add_bits118="0"+add_bits118
                                                        z=z+1
                                                                        
                                                                        
                                        INFO_OR_DATA_TO_BINARY=INFO_OR_DATA_TO_BINARY
                                        long1_After3=len(INFO_OR_DATA_TO_BINARY)
                                           
                                        add_bits118=""
                                        count_bits=8-long1_After3%8
                                        z=0
                                        
                                        if count_bits!=8:
                                                    while z<count_bits:
                                                        add_bits118="0"+add_bits118
                                                        z=z+1
                                                                        
                                                                        
                                        INFO_OR_DATA_TO_BINARY=add_bits118+INFO_OR_DATA_TO_BINARY


                                        size_after=len(INFO_OR_DATA_TO_BINARY)
                                        


                                        INFO_OR_DATA_TO_BINARY=INFO_OR_DATA_TO_BINARY[size_after-N5_size*8:size_after]
                                        
                                                  

                                    

                                    

                                      







                                  

                                        

                                        n = int(INFO_OR_DATA_TO_BINARY, 2)

                                        

                                        binary_data=len(INFO_OR_DATA_TO_BINARY)

                                        binary_data=(binary_data/8)*2

                                        binary_data=str(binary_data)

                                        binary_data="%0"+binary_data+"x"

                                     

                                        jl=binascii.unhexlify(binary_data % n)

                                        binary_to_data_2=len(jl)

                                        data=jl

                                        binary_to_data_1=binary_to_data_1+1

                                        binary_to_data_3=""

                                        size_x=""

                                    

                                        reverse_bin=reverse_bin+1

                                        if reverse_bin==1:

                                                times_numbers_reapits=10

                                                if times_numbers_reapits==10:

                                                  

                                                    f2.write(jl)

                                                    x2 = time()

                                                    x3=x2-x

                                                    return print(x3)
                     



                                

               



d=compression()



xw=d.cryptograpy_compression()

print(xw)



xw1=d.cryptograpy_unpack()

print(xw1)
