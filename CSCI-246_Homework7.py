import math
import pyperclip as pc

def extendedEuclideanAlgorithm(A,B):
    
    a = A
    b = B
    s = 1
    t = 0
    u = 0
    v = 1

    aList = ["a"]
    bList = ["b"]
    rList = ["r"]
    qList = ["q"]
    sList = ["s"]
    tList = ["t"]
    uList = ["u"]
    vList = ["v"]
    newuList = ["newu"]
    newvList = ["newv"]
    saPlustbList = ["sa + tb"]

    table = []

    newuList.append(" ")
    newvList.append(" ")
    rList.append(" ")
    qList.append(" ")
    
    while(b != 0):
        
        aList.append(str(a))
        bList.append(str(b))
        sList.append(str(s))
        tList.append(str(t))
        uList.append(str(u))
        vList.append(str(v))
        saPlustbList.append(str((s*a)+(t*b)))
        
        
        r = a % b
        q = math.floor(a / b)

        rList.append(str(r))
        qList.append(str(q))

        a = b
        b = r

        uTemp = s - u * q
        vTemp = t - v * q

        s = u
        t = v

        u = uTemp
        v = vTemp

        newuList.append(str(uTemp))
        newvList.append(str(vTemp))

    aList.append(str(a))
    bList.append(str(b))
    sList.append(str(s))
    tList.append(str(t))
    uList.append(str(u))
    vList.append(str(v))
    saPlustbList.append(str(s*A+t*B))

    return A,a,s

    

    

def inverseModulo(A,B,s):
       
    e = s

    while(e < 0):

        e = s + B

    return e

def GenerateKeyExponents(p,q):

    A = 2
    B = (p-1)*(q-1)
    a = A

    
    
    while(a != 1):

        
        if(a != 1):
            
            A += 1
            A,a,s = extendedEuclideanAlgorithm(A,B)
            
        if(a == 1):
            d = inverseModulo(A,B,s)
            print("e = " + str(A),"d = " + str(d))
            return A, d


    
    
     
    

def RSAEncrypt(message,e,pq):
    
    cipher = []
    
    for i in range(len(message)):
        C = ((ord(message[i])-32)**e) % (pq)
        C = chr(C)
        cipher.append(C)

    return(cipher)
    

def RSADecrypt(cipher,d,pq):
    
    decryptMessage = []
    
    for j in range(len(cipher)):
        M = (ord(cipher[j])**d) % (pq)
        M = chr(M+32)
        decryptMessage.append(M)

    return(decryptMessage)

def PrintMessage(message):
    for i in range(len(message)):
        print(message[i], end="")
    print()
    print("----------------------------------------------------------")
    

def main():

    check = False
    argument = 0

    print("please enter a p value")

    p = int(input())

    print("please enter a q value")

    q = int(input())

    A = 3
            
    e,d = GenerateKeyExponents(p,q)

    pq = p*q
    
    while check == False:
        
        try:

            print("enter the number to make selection >>>>MAKE SURE MESSAGE YOU WANT TO DECRPTE OR INCRPTE IS IN CLIPBOARD<<<<")
            print("1. create a ciper")
            print("2. decrpt message")
            print("0. exit")

            argument = int(input())
            print(argument)

            message = pc.paste()

            
            if(argument == 0):
                check = True
            if(argument == 1):
                print("encrpting::::" + message)
                cipher = RSAEncrypt(message,e,pq)
                print("encrption complete::::", end = "")
                PrintMessage(cipher)
            if(argument == 2):
                print("decrpting::::" + message)
                decryptMessage = RSADecrypt(message,d,pq)
                print("decrption complete::::", end = "")
                PrintMessage(decryptMessage)

            print()

        except:
            print("error")

main()












    
