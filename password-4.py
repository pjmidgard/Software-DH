from time import time
import os
import binascii
self="'"

name_input = input("for password for encrypt file encryption  or description insert password from file ")
#@Author Jurijus pacalovas
class password_class:

    def password1(self):
                def strToBinary(s):
                    bin_conv = []
                 
                    for c in s:
                         
                        # convert each char to
                        # ASCII value
                        ascii_val = ord(c)
                         
                        # Convert ASCII value to binary
                        binary_val = bin(ascii_val)
                        bin_conv.append(binary_val[2:])
                     
                        return (' '.join(bin_conv))    
                
                self.name = "Author: Jurijus Pacalovas"

                print(self.name)

                if name_input!="encryption " and name_input!="description":
                    print("Your enter incorrect letter")
                
                if name_input=="encryption ":


                    
                   
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                   
                    long_block=100
                        
                 
                    
                
                    Portal=2
                    Times_2=0
                    blockw=5
                    blockw1=4
                    name_after=name
                    nac=len(name_after)

                    long=len(name)
                   
                    Times_compression=1
                    
                    name_cut=len(".bin")
                    
                    name_after=name+".bin"
                    name_bofore=len(name_after)
                    F=0
                    
                    
                    	 
                    nac=len(name_after)
                    
                    countra_times=0
                    compression_to_file=2
                    compression_to_file1=0
                    s=""
                    
                 
                    size_data3=""
                    size_data2=""

                    sscompression_to_file=0
                    
                    qTimesl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(name_after, "w") as f4:
                            f4.write(s)
                    with open(name_after, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                        
                
                        size_after2=len(data)
                        #print(size_after2)  
                        
                        if len(data)==0 or len(data)>2**40:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                            
                      
                         

                  
                        s=str(data)
                        
                        
                        long1=len(data)
                          
                    
                            
  
                            
                        long5=len(data)
                        
                        Times_3=0
                        Times=0
                       
                        while Times_3<10:
                       
                            Times_41=0
                            Times_5=0

                            compression_to_file=compression_to_file+1
                            
                            countra_times=countra_times+1

                            with open(name_after, "ab") as f2:
                                if countra_times==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    long=len(size_data)
                                    long1=len(data)
                                
                                    xc=(long1*8)-long
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countra_times==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    binary_to_data=len(size_data2)
                                    binary_to_data=(binary_to_data/8)*2
                                    binary_to_data=str(binary_to_data)
                                    binary_to_data="%0"+binary_to_data+"x"
                             
                                    binary_to_data_2=binascii.unhexlify(binary_to_data % n)
                                    long_len=len(binary_to_data_2)
                                    
                                    data=binary_to_data_2
                                    Times=Times+1
                                   
                                    if countra_times==1:

                                        long5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    long=len(size_data)

                                    long1=len(data)
                                
                                    xc=(long1*8)-long
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    long3=len(size_data2)
                                long2=len(size_data2)

                                
                                    
                                
                                size_data3=size_data2

                                import getpass
                                
                                password=getpass.getpass()
                                

                            # Python3 program for the above approach
                             
                            # Function to convert Decimal to Hex
                                def convertToHex(num):
                                 
                                    temp = ""
                                    while (num != 0):
                                        rem = num % 16
                                        c = 0
                                         
                                        if (rem < 10):
                                            c = rem + 48
                                        else:
                                            c = rem + 87
                                             
                                        temp += chr(c)
                                        num = num // 16
                                 
                                    return temp
                                 
                                # Function to encrypt the string
                                def encryptString(S, N):
                                 
                                    ans = ""
                                    i = 0
                                 
                                    # Iterate the characters
                                    # of the string
                                    while (i<N): #changed from for i in range(N)
                                        ch = S[i]
                                        count = 0
                                 
                                        # Iterate until S[i] is equal to ch
                                        while (i < N and S[i] == ch):
                                 
                                            # Update count and i
                                            count += 1
                                            i += 1
                                 
                                        # Decrement i by 1
                                        #i -= 1 # not required
                                 
                                        # Convert count to hexadecimal
                                        # representation
                                        hex = convertToHex(count)
                                 
                                        # Append the character
                                        ans += ch
                                 
                                        # Append the characters frequency
                                        # in hexadecimal representation
                                        ans += hex
                                 
                                    # Reverse the obtained answer
                                    ans = ans[::-1]
                                     
                                    # Return required answer
                                    return ans
                                 
                                # Driver Code
                                if __name__ == '__main__':
                                     
                                    # Given Input
                                    S = password
                                    N = len(S)
                                 
                                    # Function Call
                                    s=encryptString(S, N)
                                
                                password=strToBinary(s)
 
# This code is contributed by mohit kumar  
                                #print(password)
                                N=int(password,2)
                                
                                long=len(password)
                                long_N=str(long)
                                
                                long_count="0"+long_N+"b"
                               
                                
                                N=format(N,long_count)
                          
                                    

                                password=N
                                
                                size_data12=password

                                size_data12="1"+size_data12
                            
                                long=len(size_data12)
                                        
                                add_bits118=""
                                count_bits=8-long%8
                                z=0
                                    
                                if count_bits!=8:
                                    while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                                    
                                                                    
                                size_data12=add_bits118+size_data12
                                
                                
                                    
                                size_data11=size_data12 
                                  
                                size_data11=size_data11+size_data3
             
                                                                                
                                n = int(size_data11, 2)
                                
                                binary_to_data=len(size_data11)
                                binary_to_data=(binary_to_data/8)*2
                                binary_to_data=str(binary_to_data)
                                binary_to_data="%0"+binary_to_data+"x"
                             
                                binary_to_data_2=binascii.unhexlify(binary_to_data % n)
                                
                                import paq
                                binary_to_data_2= paq.compress(binary_to_data_2)
                                
                                
                                    
                                size_after=len(binary_to_data_2)

                                size_after=len(binary_to_data_2)
                                
                                   
                                Times=Times+1
                               
                              
                            
                                Times_2=Times_2+1
                                if Times_2==1:
                                    Times_3=10
                                    if Times_3==10:

                                        f2.write(binary_to_data_2)
                                        x2 = time()
                                        x3=x2-x
                                        return print(x3)

    def password2(self):

                 def strToBinary(s):
                    bin_conv = []
                 
                    for c in s:
                         
                        # convert each char to
                        # ASCII value
                        ascii_val = ord(c)
                         
                        # Convert ASCII value to binary
                        binary_val = bin(ascii_val)
                        bin_conv.append(binary_val[2:])
                     
                        return (' '.join(bin_conv))   
                                         
                 if name_input=="description":
                    
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                    Portal=2
            
               
             
                    Deep=0
                 
                    Times_2=0
                    blockw=5
                    blockw1=4
                    name_after=name
                    nac=len(name_after)
                    name_cut=""
                    name_cut=len(".bin")
                    name_after=name
                    
                    name_long=len(name_after)
                    nameSS=name[name_long-name_cut:]
                    if nameSS!=".bin":
                        x3=0.0
                        return print(x3)
                        
                    name_after=name[:name_long-name_cut]
                    nac=len(name_after)
                    
                  
                    
                    long=len(name_after)

                    nac=len(name_after)
                   
                    countra_times=0
                    compression_to_file=2
                    compression_to_file1=0
                    s=""
                    
                 
                    size_data3=""
                    size_data2=""

                    sscompression_to_file=0
                    
                    qTimesl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(name_after, "w") as f4:
                            f4.write(s)
                    with open(name_after, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        
                        data = binary_file.read()
                        import paq
                        data= paq.decompress(data)

                        

                    
                        if len(data)==0:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                     	

                        s=str(data)
                       
                        long1=len(data)
                        long5=len(data)
                        
                        Times_3=0
                        Times=0
                       
                        while Times_3<10:
                       
                            Times_41=0
                            a1=0

                            compression_to_file=compression_to_file+1
                            
                            countra_times=countra_times+1

                            with open(name_after, "ab") as f2:
                                if countra_times==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    long=len(size_data)
                                    long1=len(data)
                                
                                    xc=(long1*8)-long
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countra_times==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    binary_to_data=len(size_data2)
                                    binary_to_data=(binary_to_data/8)*2
                                    binary_to_data=str(binary_to_data)
                                    binary_to_data="%0"+binary_to_data+"x"
                             
                                    binary_to_data_2=binascii.unhexlify(binary_to_data % n)
                                    long_len=len(binary_to_data_2)
                                    
                                    data=binary_to_data_2
                                    Times=Times+1
                                   
                                    if countra_times==1:

                                        long5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    long=len(size_data)

                                    long1=len(data)
                                
                                    xc=(long1*8)-long
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    long3=len(size_data2)
                                long2=len(size_data2)  
                                x4=1
                                if x4==1:

                                    

                                    size_data3=size_data2
                                    
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
                                    
                                    import getpass

                                    password=getpass.getpass()
                                    
                                                
                                                                    

                                    
                                         
                                 
                                # This code is contributed by mohit kumar 
                                    
                                    # Python3 program for the above approach
                                     
                                    # Function to convert Decimal to Hex
                                    def convertToHex(num):
                                     
                                        temp = ""
                                        while (num != 0):
                                            rem = num % 16#rem mean stage
                                            c = 0
                                             
                                            if (rem < 10):
                                                c = rem + 48
                                            else:
                                                c = rem + 87
                                                 
                                            temp += chr(c)
                                            num = num // 16
                                     
                                        return temp
                                     
                                    # Function to encrypt the string
                                    def encryptString(S, N):
                                     
                                        ans = ""
                                        i = 0
                                     
                                        # Iterate the characters
                                        # of the string
                                        while (i<N): #changed from for i in range(N)
                                            ch = S[i]
                                            count = 0
                                     
                                            # Iterate until S[i] is equal to ch
                                            while (i < N and S[i] == ch):
                                     
                                                # Update count and i
                                                count += 1
                                                i += 1
                                     
                                            # Decrement i by 1
                                            #i -= 1 # not required
                                     
                                            # Convert count to hexadecimal
                                            # representation
                                            hex = convertToHex(count)
                                     
                                            # Append the character
                                            ans += ch
                                     
                                            # Append the characters frequency
                                            # in hexadecimal representation
                                            ans += hex
                                     
                                        # Reverse the obtained answer
                                        ans = ans[::-1]
                                         
                                        # Return required answer
                                        return ans
                                     
                                    # Driver Code
                                    if __name__ == '__main__':
                                         
                                        # Given Input
                                        S = password
                                        N = len(S)
                                     
                                        # Function Call
                                        s=encryptString(S, N)                                       
                                    password=strToBinary(s)
                                    long=len(password)
                                    long_eight=long
                                    long_N=str(long)
                                    long_count="0"+long_N+"b"
                                
                                    N=int(password,2)
                                    N=format(N,long_count)

                                    password=N
                                    password1=size_data3[:long_eight] 
                                    
                                    if  password==password1:
                                        size_data3=size_data3[long_eight:]
                                        
                                        long_file=len(size_data3)
                                        divide=long_file%8
                                        if divide==0:
                                            print("Password it's right!")
                                        else:
                                            print("Password it's incorrect!")
                                            raise SystemExit
                                            
                                    else:
                                        print("Password it's incorrect!")
                                        raise SystemExit
                                        
                                    n = int(size_data3, 2)
                                    
                                    
                                    binary_to_data=len(size_data3)
                                    binary_to_data=(binary_to_data/8)*2
                                    binary_to_data=str(binary_to_data)
                                    binary_to_data="%0"+binary_to_data+"x"
                             
                                    binary_to_data_2=binascii.unhexlify(binary_to_data % n)
                                  
                                    long_len=len(binary_to_data_2) 
                                  
                                   

                                    Times=Times+1
                                    
                                 
                                    
                            
                                    Times_2=Times_2+1
                                    if Times_2==1:
                                        Times_3=10
                                        if Times_3==10:
                                        	
                                            f2.write(binary_to_data_2)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)  
                  
self=""                                
d=password_class()
    
xw=d.password1()
print(xw)

xw1=d.password2()
print(xw1)