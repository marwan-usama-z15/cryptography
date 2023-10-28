import random
global p,q
enccr=""
deecc=""

def decimalToBinary(n):
    return "{0:b}".format(int(n))
# squre and mul method
def sqANDmult(x,y,m):
    #x^y mod m
    w =decimalToBinary(y)
    # we convert the power (y) to decimal to check if it 0 or 1
    for i in range (0,len(w)):
       if i==0:
           # in the first iteration we dont need to look if its 0 or 1
           # we just see save the value of  the x to over write it as we want
          z = x
          continue
    #at any case in sqandmul method we will power the x and take the mod of it
       z=pow(z,2)%m
       if w[i]=="1":
           #in the case of that the binary power have we will multiply with the x after we take the power one (see sq and mull for details)
            z=z*x % m
    return (z)

def fermet(n):
    #we try every possible a ( 2,->p-2)
    a = 2
    for i in range (0,n-2):
       if sqANDmult(a,n-1,n)!=1:
           #if i found any a value that make the number mod not equal to 1 i will return false
           return False
       a=a+1
    return True
def gcd(awel,tany):
    #the function of gcd
    #gcd(awel,tany)
    #gcd(20,3)
    # the result of the (20%3)->2
    #thats why i save the result in (tany) variable
    #the 3 from the above i store in temp and but it in awel
    #the rest of answer
    #gcd (3,2)
    #gcd (2,1)
    #gcd (1,0)
    #tany here reached 0 so we will stop and look at awel result
    while(tany!=0):
        temp=tany
        tany =awel%tany
        awel=temp
    return awel
def eea(remi1,remi2):
    #extended ecludian algo
    # just same as the table that i explain it to u (i will send the pic to compare it)
   s0=1
   s1=0
   t0=0
   t1=1
   f=remi1
   while(True):
       temp=remi2
       q=remi1//remi2
       temp2 =s1
       s1=(s0)-(q*s1)
       s0=temp2

       remi2 = remi1 % remi2
       remi1 = temp
       if (remi2 == 0):
           break

       temp3 = t1
       t1 = (t0) - (q * t1)
       t0 = temp3
       if (t1<0):
           t1=t1%f

   return t1
def decrp(y,d,p,q,rees):

    #i will send u a video of crt method those var names are the same of the ass or lec var go check them
    yp=y%p
    yq=y%q
    dp=d%(p-1)
    dq=d%(q-1)
    xp=sqANDmult(yp,dp,p)   #pow(yp,dp)%p
    xq=sqANDmult(yq,dq,q)
    cp=eea(p,q)
    cq=eea(q,p)
    xx=((q*cp)*xp+(p*cq)*xq)%(rees)
    return xx
x=input("please Enter your input :  ")
for i in x:
    # we are choosing our p and q and do the calc. of n here and phi(n)
    while(True):
#as desciped in the sheet the p and q value should be between the  ascci value that we are taken in this loop(i)
    #ord(i)<p,q<32767(2^15-1)
       p = random.randint(ord(i), 32767)
       q = random.randint(ord(i),32767)
#if p =q we repeat again to make it unique
       if (p==q):
          continue
# if its unique     we need to check if those numbers(p,q) are likely prime by the fermat algorithm as described

       if (fermet(p) and fermet(q)):
           #if both of them are likely prime stop the random genaration and save the value of them
          break

    print("the leteer ",i,"in ascii",ord(i))
    print("p              q")
    print(p, "     ",q)


    rees=p*q
    print("N",rees)
    on=(p-1)*(q-1)
    print("o(n)",on)
    while (True):
        #as descriped e should be between 1,phi (n)-1
      e=random.randint(1, on-1)
        #if gcd(phi (n)-1,e) ==1 make sure that e has inverse see the algo if u want more details see the lec
      if (gcd(on,e)==1):
             break

    print("e",e)
    y=sqANDmult(ord(i),e,rees)
    #here the encryption ord(i)^e mod rees  == x^e mod n
    enccr+=str(y)
    print("y  for encryption ",y)
    # here the encryption y^d mod rees  == y^d mod n
    d=eea(on,e)
    print("d",d)
    print("Decryption",decrp(y, d, p, q, rees))
    ##convert back to ascci
    print("ascci after decryption ",chr(decrp(y, d, p, q, rees)))
    deecc+=chr(decrp(y, d, p, q, rees))
print("                          ")
print("                          ")
print("                          ")
print("encrypted",enccr)
print("                          ")
print("                          ")
print("                          ")
print("decryption ",deecc)


