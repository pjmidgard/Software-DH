import os  

from time import time

import binascii

import math

import os.path

enter_name_of_file = input("New computer code: c and old computer code: e: ")

#@Author Jurijus pacalovas



class compression:

    def cryptograpy_compression(self):

                

                self.name = "Created: Jurijus pacalovas Price Portal 1000 000 000 Euro cost Date: 26/07/2021 17:11 Deep 14.5 ERA"

                if enter_name_of_file=="c":

                    corridors=0

                    corridors_2=7

                    name = input("What is name of file? ")

                    name_new="file.Secret"

                    name_2=""

                    name_2_clear="?"



                    e5=0

                    e1=""

                    e6=0

                    e7=255



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

                    select_words=2

                    elements_words=0

                 

                    INFO3=""

                    INFO_OR_DATA_TO_BINARY=""



                    size_of_size_cosscounts_1=0

                    

                    binary_to_data=0



                    block=1

                    r=""



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

                                long2=len(INFO_OR_DATA_TO_BINARY)

                                c=1



                               

                                block=0



                                while block<long2:

                                                   e4=INFO_OR_DATA_TO_BINARY[block:block+9]

                                                   if e4=="000000000":

                                                       e4="011100101"

                                                       INFO4+=e4

                                                   elif e4=="011100101":

                                                       e4="000000000"

                                                       INFO4+=e4

                                                       

                                                   else:

                                                       INFO4+=e4

                                                       

                                                       

                                        

                                                   block+=9  

                                INFO_OR_DATA_TO_BINARY=INFO4

                                INFO4=""                              

                                if c==1:



                                    block=0



                                    while block<long2:



                           

                                    



                                        e4=INFO_OR_DATA_TO_BINARY[block:block+8]

                            

                                       

                                            

                                            

                                         

                                        e1=e4

                                        

                                                                               





                                        

                                        remaider=counts_11%block_2+block//16+block

                                        

                                        



                                        r1=(block//8)+(block//block_2)

                                        r2=(block//8)+block+(block//8)

                                        r3=block%3+(block//8)

                                        r4=block%4+(block//block_2)



                                        if remaider==0 and r1==0 or remaider==0 and r2==block_2 or remaider==0 and r3==0 or remaider==0 and r4==0:

                                            e1=e4[4:8]+e4[2:4]+e4[0:2]



                                        if remaider==0 and r1==block_2 or remaider==0 and r2==block_2 or remaider==0 and r3==block_2 or remaider==0 and r4==block_2:

                                            e1=e4[4:8]+e4[0:4] 

                                            

                                        if remaider==0:

                                            e1=e4[4:8]+e4[2:4]+e4[0:2]

                                            

                                              

                                        if remaider==1:

                                            e1=e4[4:8]+e4[0:4]                                          

                                        

                                                             

                                        

                                        e5=int(e1,2)

                                        if e5==e6:



                                            

                                            INFO3=format(e7,"08b")

                                        elif e5==e7:

                                           

                                            INFO3=format(e6,"08b")

                                       



                                        else:

                                            

                                            INFO3=format(e5,"08b")

                                        INFO4+=INFO3

                                        

                                        block_2+=1

                                        if block_2==15:

                                            block_2==1

                                            

                                        block+=8                                    

                                    

                                    e6+=3

                                    e7-=3

                                    if e6>=255:

                                        e6=0

                                    if e7<=0:

                                        e7=255

                                    counts_11=counts_11+1

                                    INFO_OR_DATA_TO_BINARY=INFO4

                                    block_2=5

                                    INFO4=""

                                    



                                    

            

                                   

                                    

                                    

                                    if counts_11==23:

                                                    

                                    

                                    

                                      







                                  

                                        

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

                                        

                                        

                                      

                                            

                                    



    def cryptograpy_unpack(self):                                 

                 if enter_name_of_file=="e":

                    corridors=0

                    corridors_2=7

                    name=input("What is name of file? ")

                    name_new="file.Secret"

                    name_2=""

                    name_2_clear="?"

                    e1=""



                    e5=0

                    e6=0

                    e7=255



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

                                long2=len(INFO_OR_DATA_TO_BINARY)

                                c=1



                                if c==1:



                                    block=0



                                    while block<long2:



                           

                                    



                                        e4=INFO_OR_DATA_TO_BINARY[block:block+8]

                                        

                                        e61=""

                                        e61=e4[0:4]

                                        

                                        

    

                            

                                        

                                        e1=e4

                                        remaider=counts_11%block_2+block//16+block

                                        

                                        

                                        

                                

                                        



                                        r1=(block//8)+(block//block_2)

                                        r2=(block//8)+block+(block//8)

                                        r3=block%3+(block//8)

                                        r4=block%4+(block//block_2)





                                        if remaider==0 and r1==0 or remaider==0 and r2==block_2 or remaider==0 and r3==0 or remaider==0 and r4==0:

                                            e1=e4[4:8]+e4[2:4]+e4[0:2]



                                        if remaider==0 and r1==block_2 or remaider==0 and r2==block_2 or remaider==0 and r3==block_2 or remaider==0 and r4==block_2:

                                            e1=e4[4:8]+e4[0:4] 

                                            

                                        if remaider==0:

                                            e1=e4[4:8]+e4[2:4]+e4[0:2]

                                            

                                              

                                        if remaider==1:

                                            e1=e4[4:8]+e4[0:4]                                          

                                        

                                                             

                                        

                                        e5=int(e1,2)

                                        if e5==e6:



                                            

                                            INFO3=format(e7,"08b")

                                        elif e5==e7:

                                           

                                            INFO3=format(e6,"08b")



                                        else:

                                            

                                            INFO3=format(e5,"08b")

                                        INFO4+=INFO3

                                        

                                        block_2+=1

                                        if block_2==15:

                                            block_2==1

                                            

                                        block+=8                                    

                                    

                                    e6+=3

                                    e7-=3

                                    if e6>=255:

                                        e6=0

                                    if e7<=0:

                                        e7=255

                                    counts_11=counts_11+1

                                    INFO_OR_DATA_TO_BINARY=INFO4

                                    block_2=5

                                    INFO4=""

                                    

                                    block=0

                                 

                                    while block<long2:

                                                   e4=INFO_OR_DATA_TO_BINARY[block:block+9]

                                                   if e4=="000000000":

                                                       e4="011100101"

                                                       INFO4+=e4

                                                   elif e4=="011100101":

                                                       e4="000000000"

                                                       INFO4+=e4

                                                       

                                                   else:

                                                       INFO4+=e4

                                                       

                                                       

                                        

                                                   block+=9  

                                    INFO_OR_DATA_TO_BINARY=INFO4

                                    INFO4=""                                     

                                 

                                    if counts_11==23:

                                                   

                                        

                                        

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
