import textwrap
import binascii
pc1 = [56, 48, 40, 32, 24, 16,  8,
		  0, 57, 49, 41, 33, 25, 17,
		  9,  1, 58, 50, 42, 34, 26,
		 18, 10,  2, 59, 51, 43, 35,
		 62, 54, 46, 38, 30, 22, 14,
		  6, 61, 53, 45, 37, 29, 21,
		 13,  5, 60, 52, 44, 36, 28,
		 20, 12,  4, 27, 19, 11,  3
	]
pc2 = [13, 16, 10, 23,  0,  4,
		 2, 27, 14,  5, 20,  9,
		22, 18, 11,  3, 25,  7,
		15,  6, 26, 19, 12,  1,
		40, 51, 30, 36, 46, 54,
		29, 39, 50, 44, 32, 47,
		43, 48, 38, 55, 33, 52,
		45, 41, 49, 35, 28, 31]

ip = [57, 49, 41, 33, 25, 17, 9,  1,
		59, 51, 43, 35, 27, 19, 11, 3,
		61, 53, 45, 37, 29, 21, 13, 5,
		63, 55, 47, 39, 31, 23, 15, 7,
		56, 48, 40, 32, 24, 16, 8,  0,
		58, 50, 42, 34, 26, 18, 10, 2,
		60, 52, 44, 36, 28, 20, 12, 4,
		62, 54, 46, 38, 30, 22, 14, 6
	]
expansion_table = [
		31,  0,  1,  2,  3,  4,
		 3,  4,  5,  6,  7,  8,
		 7,  8,  9, 10, 11, 12,
		11, 12, 13, 14, 15, 16,
		15, 16, 17, 18, 19, 20,
		19, 20, 21, 22, 23, 24,
		23, 24, 25, 26, 27, 28,
		27, 28, 29, 30, 31,  0
	]

S1=      [  [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
		 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
		 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
		 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

S2=     [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5,10 ],
		 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
		 [ 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2,15],
		 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

S3=	[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
		[ 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
		[ 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
		[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]]

S4=     [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
		[ 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
		[ 10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
		[ 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

S5=	[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
		 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
		[ 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
		 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

S6=	[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
		[ 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
		[ 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
		 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

S7=	[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
		[ 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
		 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
		 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

S8=	[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
		[ 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
		[ 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
		[ 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
p_sbox= [
		15, 6, 19, 20, 28, 11,
		27, 16, 0, 14, 22, 25,
		4, 17, 30, 9, 1, 7,
		23,13, 31, 26, 2, 8,
		18, 12, 29, 5, 21, 10,
		3, 24
	]

fp = [
		39,  7, 47, 15, 55, 23, 63, 31,
		38,  6, 46, 14, 54, 22, 62, 30,
		37,  5, 45, 13, 53, 21, 61, 29,
		36,  4, 44, 12, 52, 20, 60, 28,
		35,  3, 43, 11, 51, 19, 59, 27,
		34,  2, 42, 10, 50, 18, 58, 26,
		33,  1, 41,  9, 49, 17, 57, 25,
		32,  0, 40,  8, 48, 16, 56, 24
	]
sboxs=[S1,S2,S3,S4,S5,S6,S7,S8]

final_plain_txt=""
res =""
res2=""

def change_to_be_hex(s):
    return int(s,base=16)
def toBinary(a):
    return ''.join(format(ord(i), '08b') for i in a)

def sbox(stable,i,ans):
        return stable[int(ans[i][0] +ans[i][5], 2)][int(ans[i][1:5], 2)]
def permutation(size,old,pt):
    z=""
    for i in range(0, size):
        z += old[pt[i] ]
    return z
plaintext=str(input("Please Enter your plain text : "))
def enc(final_plain_txt,kv):
  c=1
  print("L 0 ->", final_plain_txt[:64 // 2])
  print("R 0 ->", final_plain_txt[64 // 2:])
  for i in range (1,17):

    k=kv
    print("K",i,"--->","after PC-2",k[i-1])
    print("     ")
    lpl=final_plain_txt[:64//2]
    rpl=final_plain_txt[64//2:]
    expan=permutation(48,rpl,expansion_table)
    print("expantion :",expan)
    ans=""
    ans2 = ""
    ans3 = ""
    for j in range(0,48):

      ans+=str(int( k[i-1][j])^int(expan[j]))
    print("XOR with round key :",ans)

    ans = textwrap.wrap(ans, 6)
    for i in range(8):
        ans2+=format(sbox(sboxs[i],i,ans),"04b")
    print("Sboxs result :", ans2)
    ans2=permutation(32,ans2,p_sbox)
    print("Result after permutation :", ans2)
    for j in range(0,32):
      ans3+=str(int( lpl[j])^int(ans2[j]))
    lpl=rpl
    rpl=ans3
    final_plain_txt =  lpl +rpl
    print("l",c, "->", lpl)
    print("R",c, "->", rpl)
    c+=1
    print("     ")


  return permutation(64,rpl+lpl,fp)






def ksh():

     z=permutation(56,key,pc1)
     print("key after PC-1",z)
     finalk = []
     print ("C 0 ->",z[ :56//2])
     print("D 0 ->", z[56//2: ])
     for i in range (1,17):

        l=z[:56//2]
        r=z[56//2:]

        if (i==1or i== 2 or i== 9 or  i==16 ):
           l =l[1 :  ] + l[0 : 1]
           r = r[1:  ] + r[0: 1]

        else :
              l = l[2:] + l[0: 2]
              r = r[2:] + r[0: 2]

        z=l+r
        print("C",i,"->",l)
        print("D",i,"->",r)

        finalk.append( permutation(48, z, pc2))

     return finalk



##take the input key from the user
while(True):
    key = str(input("Please Enter your key "))

    if(len(key)==8):
        break
    print("Error")
key=toBinary(key)
print("Key in bits ",key)

def de_k():
    finalk=[]
    z=permutation(56,key,pc1)




    for i in range (1,17):
        l=z[:56//2]
        r=z[56//2:]
        if (i==1):
           finalk.append(permutation(48, z, pc2))
           print("C", i, "->", l)
           print("D", i, "->", r)

           continue

        elif (i== 2 or i== 9 or  i==16 ):
               l=l[len(l)-1:  ]+l[0: len(l)-1]
               r = r[len(l) - 1: ] + r[0: len(l) - 1]


        else :
            l = l[len(l) - 2:  ] + l[0: len(l) - 2]
            r = r[len(l) - 2:  ] + r[0: len(l) - 2]


        z=l+r
        print("C", i, "->", l)
        print("D", i, "->", r)

        finalk.append(permutation(48, z, pc2))

    return finalk

def dec(final_plain_txt,kv):
  final_plain_txt=permutation(64, final_plain_txt, ip)
  c=1
  print("L 0 ->", final_plain_txt[64 // 2:])
  print("R 0 ->", final_plain_txt[:64 // 2])
  for i in range (1,17):

    k=kv
    print("K",i,"--->","after PC-2",k[i-1])
    print("     ")
    rpl =final_plain_txt[:64//2]
    lpl=final_plain_txt[64//2:]
    expan=permutation(48,lpl,expansion_table)
    print("expantion :",expan)
    ans=""
    ans2 = ""
    ans3 = ""
    for j in range(0,48):

      ans+=str(int( k[i-1][j])^int(expan[j]))
    print("XOR with round key :",ans)

    ans = textwrap.wrap(ans, 6)
    for i in range(8):
        ans2+=format(sbox(sboxs[i],i,ans),"04b")
    print("Sboxs result :", ans2)
    ans2=permutation(32,ans2,p_sbox)
    print("Result after permutation :", ans2)
    for j in range(0,32):
      ans3+=str(int( rpl[j])^int(ans2[j]))
    rpl=lpl
    lpl=ans3
    final_plain_txt =  rpl+lpl

    print("l",c, "->", lpl)
    print("R",c, "->", rpl)
    c+=1
    print("     ")

  return permutation(64, lpl+rpl, fp)
if len(plaintext)>8:
    last=""
    final_plain_txt = [plaintext[i:i+8] for i in range(0, len(plaintext), 8)]
    zzz=len(final_plain_txt)-1
    while (len(final_plain_txt[zzz])<8):
            final_plain_txt[zzz]=f'{"@"}{final_plain_txt[zzz]}'
    print("Plain text ",final_plain_txt)

    for i in range(0,zzz+1)  :
         n=""
         final_plain_txt[i] = toBinary(final_plain_txt[i])
         last+= final_plain_txt[i]
         final_plain_txt[i] = permutation(64, final_plain_txt[i], ip)
         print("Plain text in bits after initial permutation at index",i ,final_plain_txt[i])
         n=enc(final_plain_txt[i],ksh())
         res+=n
         res2+=dec(n,de_k())
    print("Plain text in bits",last)



else:
     while (len(plaintext)<8):
         plaintext=f'{"@"}{plaintext}'
     print("Plain text ", plaintext)
     final_plain_txt+=toBinary(plaintext)
     print("Plain text in bits", final_plain_txt)
     final_plain_txt = permutation(64, final_plain_txt, ip)
     print("Plain text in bits after initial permutation", final_plain_txt)
     res=enc(final_plain_txt,ksh())
     res2=dec(res,de_k())

print("                     ")
print("Cipher text :",res)
print("                     ")
print("decrypted text in bits :",res2)
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
print("                     ")
print("The Plain Text")
print(text_from_bits(res2))
## decryption key method

##print the decryption


