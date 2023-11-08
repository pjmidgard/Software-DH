import os
import binascii
from time import time
#@Author Jurijus Pacalovas 

namez = input("Compress: c Extract: e Check file: check ")

class Compression:



    def compress_file(self):
        if namez=="c":
        
            corridors = 0
            cor = 7
            namea = "file.Secret"
            namem = ""
            namema = "?"
            e5 = 0
            e1 = ""
            e6 = 0
            e7 = 255
            sda3 = ""
            sda4 = ""
            sda5 = ""
            assxw = 0
            blockw = 5
            blockw1 = 4
            input_file = input("What is name of file? ")
        
            nameas = input_file
            nac = len(nameas)
            nameas = input_file + ".bin"
            nac = len(nameas)
            countraz = 0
            cvf = 2
            cvf1 = 0
            s = ""
            e2 = 0
            e3 = 2
            e4 = ""
            c = 2
            sw = 2
            elw = 0
            sda3 = ""
            sda2 = ""
            sscvf = 0
            qqqqwzl = 0
            block = 1
            r = ""
            x = 0
            x1 = 0
            x2 = 0
            x = time()
            with open(nameas, "w") as f4:

                            f4.write(s)

            with open(nameas, "a") as f3:

                            f3.write(s)
    
            with open(input_file, "rb") as binary_file:
                data = binary_file.read()
                s = str(data)
                lenf1 = len(data)
                lenf5 = len(data)
                assx = 0
                qqqwz = 0
    
                while assx < 10:
                    cvf = cvf + 1
                    countraz = countraz + 1
                    with open(nameas, "ab") as f2:
                        if countraz == 1:
                            sda = bin(int(binascii.hexlify(data), 16))[2:]
                            lenf = len(sda)
                            lenf1 = len(data)
                            xc = (lenf1 * 8) - lenf
                            z = 0
                            if xc != 0:
                                while z < xc:
                                    sda = "0" + sda
                                    z = z + 1
                            sda = sda + sda2
                            if countraz == 1:
                                sda2 = sda
                            
    
                       
                        c=1
                        if c == 1:
                            X=0
                            
                            block = 0
                            lenf2=len(sda2)
    
                            while block < lenf2:
                                e4 = sda2[block:block + 4]
                                
                                
                                if e4=="0000" and X==0:
                                    e4="000"
                                    sda4+=e4
                                    block+=4

                                elif e4[:3]=="111" and X==0:
                                     e4="0000"
                                     sda4+=e4
                                     block+=3
                                
                                elif e4!="1110" and e4!="1111" or X!=0:
                                    if X!=0:
                                        e6=int(e4[:3],2)
    
                                        e6+=1
                                        e4 = format(e6, "03b")
                                        sda4+=e4
                                        block+=3
                                    else:
                                       sda4+=e4
                                       block+=4

                                
                                    
                                X+=1
                                if X==1:
                                    X=0
                            sda10 = ""
                            sda2 = sda4
                            sda4=""
                            cvf1 += 1

                           
                            if len(sda2)==7000 or cvf1==255:
                                long_1 = len(sda2)
                                add_bits = ""
                                count_bits = 8 - long_1 % 8
                                z = 0
                                if count_bits != 0:
                                    while z < count_bits:
                                        add_bits = "0" + add_bits
                                        z = z + 1
                                e4 = format(cvf1, "08b")
                                sda2 = e4 + add_bits + sda2
                                n = int(sda2, 2)
                                qqwslenf = len(sda2)
                                qqwslenf = (qqwslenf / 8) * 2
                                qqwslenf = str(qqwslenf)
                                qqwslenf = "%0" + qqwslenf + "x"
                                jl = binascii.unhexlify(qqwslenf % n)
                                sssssw = len(jl)
                                data = jl
                                qqqwz = qqqwz + 1
                                szxzzza = ""
                                szxzs = ""
                                assxw = assxw + 1
                                if assxw == 1:
                                    assx = 10
                                    if assx == 10:
                                        f2.write(jl)
                                        x2 = time()
                                        x3 = x2 - x
                                        return print(x3)

    def extract_and_reverse_compression(self):
        if namez == "e":
            

            corridors = 0
            cor = 7
            namea = "file.Secret"
            namem = ""
            namema = "?"
            e5 = 0
            e1 = ""
            e6 = 0
            e7 = 255
            sda3 = ""
            sda4 = ""
            sda5 = ""
            assxw = 0
            blockw = 5
            blockw1 = 4
            input_file = input("What is name of file? ")
        
            nameas = input_file
            nac = len(nameas)
            nameas = input_file
            nameas=nameas[:nac-4]
            nac = len(nameas)
            countraz = 0
            cvf = 2
            cvf1 = 0
            s = ""
            e2 = 0
            e3 = 2
            e4 = ""
            c = 2
            sw = 2
            elw = 0
            sda3 = ""
            sda2 = ""
            sscvf = 0
            qqqqwzl = 0
            block = 1
            r = ""
            x = 0
            x1 = 0
            x2 = 0
            x = time()
            with open(nameas, "w") as f4:

                            f4.write(s)

            with open(nameas, "a") as f3:

                            f3.write(s)
    
            with open(input_file, "rb") as binary_file:
                data = binary_file.read()
                s = str(data)
                lenf1 = len(data)
                lenf5 = len(data)
                assx = 0
                qqqwz = 0
    
                sda2 = bin(int(binascii.hexlify(data), 16))[2:]
                c=1
                                
                if c==1:
                                    assxw=0
                                    blockw = 5
                                    sda4 = ""
                                    block = 0
                                    e8 = 0
                                    ch1 = ""
                                    ch = 0
                                    r1 = ""
                                    r2 = ""
            
                                    r3 = 0
                                    r4 = ""
                                    e9 = "1"
                                  
            
                                    e9 = 0
                                    r5 = ""
                                    e10 = ""
                                    s = ""
                                    sda10 = ""
                                    sda11 = ""
                                    start = 1
                                    E5=""
                                    size_data3=sda2
                                    #print(sda2)
                                    c=1
                                    if c==1:
         
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
                                    sda2=size_data3
                                    lenf2=len(sda2)
                                    #print(lenf2)
                                    block=0
                                    while block < lenf2:
                                        e4 = sda2[block + 4:block + 7]
                                        e5 = sda2[block:block + 8]
                                        E6 = sda2[block:block + 7]
                                        ch1 = sda2[block + 1:block + 3]
                                        r1 = sda2[block:block + 1]
                                        r2 = sda2[block + 7:block + 8]
                                        r4 = sda2[block + 6:block + 7]
                                        r5 = sda2[block + 1:block + 2]
                                        E5=sda2[block+8:block + 17]
                                        e8 += 1
                                        if len(e5) == 8:
                                            e1 = int(e4, 2)
                                            e9 = int(r5, 2)
                                        ch = int(ch1, 2)
                                        r3 = int(r1, 2)
                                        sda5 = ""
                                        sda6 = ""
                                        sda7 = ""
                                        sda9 = ""
                                        
                                        
                                        if r3 == e8 and e9 == e8 or len(E6) == 7 and start == 1:
                                        
                                           if len(E5)==9 and E5[0:1]=="1"  and len(E6) == 7 or len(E5)==1 and E5[0:1]=="1" :
                                               
                                               e1 = format(e8, "01b")
                                               
                                               sda3 = e1 +"0"+e1 + e5[2:7]+E5[1:]
                                               start=0
                                               
                                               sda4 += sda3
                                               block += 7+9
                                           
                                           elif len(E5)==9 and E5[0:1]=="0"  and len(e5) == 8 or len(E5)==1 and E5[0:1]=="0":
                                              
                                               sda3 = e5+E5[1:]
                                               #print(len(sda3))
                                               sda4 += sda3
                                               block += 8+9
                                               start=1
                                           else:
                                                sda4+=e5
                                                block += 8
                                                start=1
                                        else:
                                            sda4+=e5
                                            block += 8
                                            start=1
                                           
                                        if e8 == 1:
                                            e8 = 0
                                        
                                   
                                    sda10 = ""
                                    sda2 = sda4
                                
                                    cvf1 += 1
                                    if cvf1 == 1:
                                        long_1 = len(sda2)
                                        add_bits = ""
                                        count_bits = 8 - long_1 % 8
                                        z = 0
                                        if count_bits != 0:
                                            while z < count_bits:
                                                add_bits = "0" + add_bits
                                                z = z + 1
                                        sda2 = add_bits + sda2
                                        n = int(sda2, 2)
                                        qqwslenf = len(sda2)
                                        qqwslenf = (qqwslenf / 8) * 2
                                        qqwslenf = str(qqwslenf)
                                        qqwslenf = "%0" + qqwslenf + "x"
                                        jl = binascii.unhexlify(qqwslenf % n)
                                        sssssw = len(jl)
                                        data = jl
                                        
                                        szxzzza = ""
                                        szxzs = ""
                                        assxw = assxw + 1
                                        if assxw == 1:
                                            assx = 10
                                            if assx == 10:
                                                with open(nameas, "ab") as f2:
                                                    f2.write(jl)
                                                    x2 = time()
                                                    x3 = x2 - x
                                                    return print(x3)
                                
                            

d=Compression()



xw=d.compress_file()

print(xw)



xw1=d.extract_and_reverse_compression()

print(xw1)