x = ""
poly_eq = input("please write your polynomial equation: ")
bin_text = str(input("please write your binary plain text: "))
print("Binary text length =",len(bin_text))
load = ""
FFnum = int(poly_eq[2])

for i in range(3, len(poly_eq)):
    if (poly_eq[i] == '^'):
        load += poly_eq[i + 1]
    elif (poly_eq[i] == '1'):
        load += '0'
    elif (poly_eq[i] == 'x' and (i == len(poly_eq) - 1 or poly_eq[i + 1] == '+')):
        load += '1'

coff = [0] * FFnum
for i in range(0, len(load)):
    coff[int(load[i])] = 1
print("The feedback coefficients : ")
for i in range(0, FFnum):
    x += 'c' + str(i)
    x += " "
print(x)
print('  '.join(map(str, coff)))


initialbits = []


while True:
    initialbits = [str(initialbits) for initialbits in input("Enter the initial vector with spaces: ").split()]
    if (len(initialbits) == FFnum):
        break
    else:
        print("error try it again")

header = "clk "
for i in range(FFnum - 1, -1, -1):
    header += 'FF' + str(i)
    header += "      "

print(header)
print("0   ", '        '.join(initialbits))
k = []

k.append(int(initialbits[FFnum - 1]))

for index in range(0, len(bin_text) - 1):

    reverse = initialbits[::-1]
    xor_result = int(reverse[int(load[0])])
    for i in range(1, len(load)):
        xor_result = xor_result ^ int(reverse[int(load[i])])
    for i in range(FFnum - 1, 0, -1):
        initialbits[i] = initialbits[i - 1]
    initialbits[0] = str(xor_result)
    k.append(int(initialbits[FFnum - 1]))
    if (index < 9 ):
        print(str(index + 1) + "   ", '        '.join(initialbits))
    else:
        print(str(index + 1) + "  ", '        '.join(initialbits))

print("key =",''.join(map(str, k)))
ciphertext = ""
for i in range(len(bin_text)):
    ciphertext += str(k[i] ^ int(bin_text[i]))

print("ciphertext=",ciphertext)