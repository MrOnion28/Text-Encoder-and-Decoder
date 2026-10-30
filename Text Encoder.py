import math
from collections import deque
text = input("Please enter text to encode(numbers, case and foreign characters will be ignored): ")
decodetext = input("Please enter text to decode(numbers, case and foreign characters will be ignored): ")
plaintext = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ciphertext = []
morse_cipher = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
text = text.lower().split(" ")
for x in range(len(text)):
    if not text[x].isalpha:
        for letter in text[x]:
            word = ""
            if letter.isalpha:
                word+=letter
        text[x] = word
print("E: encode")
print("D: decode")
eod  = input("Would you like to encode or decode a text? (Please enter an E or a D)")
def encrypt_caesar(offset):
    for x in range(offset,26):
        ciphertext.append(plaintext[x])
    for x in range(0,offset):
        ciphertext.append(plaintext[x])
    for x in range(0,len(text)):
        coded_word = ""
        for letter in text[x]:
             if letter.isalpha():
                index = plaintext.index(letter.lower())
                cipherletter = ciphertext[index]
                coded_word+=cipherletter
        text[x]=coded_word

def encrypt_substitution(key):
    key = key.lower()
    if all(item in key for item in plaintext) and len(key) == 26:
        print(key)
        for letter in key:
            ciphertext.append(letter)
        for x in range(0,len(text)):
            coded_word = ""
            for letter in text[x]:
                if letter.isalpha():
                    index = plaintext.index(letter.lower())
                    cipherletter = ciphertext[index]
                    coded_word+=cipherletter
            text[x]=coded_word

def encrypt_morse():
    for x in range(0,len(text)):
        coded_word = ""
        for letter in text[x]:
            if letter.isalpha():
                index = plaintext.index(letter.lower())
                cipherletter = morse_cipher[index]
                coded_word+=cipherletter
            text[x]=coded_word


def encrypt_affine(a,b):
    for x in range(26):
        ciphertext.append(plaintext[x])
    for x in range(0,len(text)):
        coded_word = ""
        for letter in text[x]:
            if letter.isalpha():
                index = plaintext.index(letter.lower())
                pos = a*index + b
                while pos >= 26:
                    pos -= 26
                cipherletter = ciphertext[pos]
                coded_word+=cipherletter
            text[x]=coded_word
                
def encrypt_vigenere(keyword):
    keyword = keyword.lower()
    keyletter = 0
    for x in range(0,len(text)):
        coded_word = ""
        for letter in text[x]:
            if letter.isalpha():
                index = int(plaintext.index(letter.lower()))+int(plaintext.index(keyword[keyletter].lower()))
                while index >= 26:
                    index -= 26
                cipherletter = plaintext[index]
                coded_word+=cipherletter
                keyletter+=1
                if keyletter >= len(keyword):
                    keyletter = 0   
            text[x]=coded_word

def encrypt_cl_row_transposition(key):
    col = len(str(key))
    str_text = ''.join(text)
    print(str_text)
    row = math.ceil((len(str_text)/col))
    cur_row=[]
    for x in range(len(str_text)):
        cur_row += str_text[x]
        if len(cur_row) >= col:
            ciphertext.append(cur_row)
            cur_row = []
    if len(cur_row) >= 1:
        nml = col - len(cur_row)
        mls = ""
        for x in range(26-nml,26):
            mls += plaintext[x]
        cur_row+=mls
        ciphertext.append(cur_row)
    #for row in ciphertext:
        #for elem in row:
            #print(elem, end=' ')
        #print()
    new_text = "" 
    for x in range(1,len(str(key))+1):
        i = str(key).find(str(x))
        for y in range(0,len(ciphertext)):
            new_text += "".join(ciphertext[y][i])
    print(new_text)

def encrypt_hill(keyword):
    keyword = keyword.lower()
    key = []
    sub=[]
    if len(keyword) != 9:
        nml = 9 - len(keyword)
        mls = ""
        for x in range(26-nml,26):
            keyword += plaintext[x]
    for letter in keyword:
        sub.append(letter)
        if len(sub) >= 3:
            key.append(sub)
            sub = []
    for x in range(3):
        for y in range(3):
            i = plaintext.index(key[x][y])
            key[x][y] = i
    #for row in key:
        #for elem in row:
            #print(elem, end=' ')
        #print()
    str_text = ''.join(text)
    length = len(str_text)    
    if len(str_text) % 3 == 1:
        str_text += "yz"
    elif len(str_text) % 3 == 2:
        str_text += "z"
    print(str_text)
    lte = ""
    el = ""
    new_text = ""
    index = 0
    for x in range(0,len(str_text),3):
        #print("new")
        index = 0
        lte = list(str(str_text[x:x+3]))
        index = (plaintext.index(lte[0])*key[0][0])+(plaintext.index(lte[1])*key[0][1])+(plaintext.index(lte[2])*key[0][2])
        while index >= 26:
            index -= 26
        el += plaintext[index]
        #print(el)
        #print(el,plaintext[index],index)
        index = 0
        index = (plaintext.index(lte[0])*key[1][0])+(plaintext.index(lte[1])*key[1][1])+(plaintext.index(lte[2])*key[1][2])
        while index >= 26:
            index -= 26
        el += plaintext[index]
        #print(el,plaintext[index],index)
        index = 0
        index = (plaintext.index(lte[0])*key[2][0])+(plaintext.index(lte[1])*key[2][1])+(plaintext.index(lte[2])*key[2][2])
        while index >= 26:
            index -= 26
        el += plaintext[index]
    print(length)
    if length % 3 == 1:
        new_text = el[0:len(el)-2]
    elif length % 3 == 2:
        new_text = el[0:len(el)-1]
    else:
        new_text = el
    print(new_text)

  #------------------------------------------------------------  

def decrypt_caesar(offset):
    offset = 26 - offset
    for x in range(offset,26):
        ciphertext.append(plaintext[x])
    for x in range(0,offset):
        ciphertext.append(plaintext[x])
    for x in range(0,len(text)):
        coded_word = ""
        for letter in text[x]:
            if letter.isalpha():
                index = plaintext.index(letter.lower())
                cipherletter = ciphertext[index]
                coded_word+=cipherletter
        text[x]=coded_word

def decrypt_substitution(key):
    key = key.lower()
    for letter in decodetext:
        if letter in key:
            x = key.index(letter)
            newtext.append(plaintext[x])

def decrypt_morse():
    global decodetext
    decodetext = decodetext.split(" ")
    for part in decodetext:
        y = morse_cipher.index(part)
        newtext.append(plaintext[y])

def decrypt_affine(a,b):
    global decodetext
    decodetext = decodetext.lower()
    for letter in decodetext:
        if letter in plaintext:
            lnumber = plaintext.index(letter)
            toneg1 = 27/a
            newnumber = (toneg1*(lnumber-b))%26
            newnumber = int(newnumber)
            z = plaintext[newnumber]
            newtext.append(z)
    
def decrypt_vigenere(keyword):
    d = deque(plaintext)
    for x, letter in zip(range(len(decodetext)), decodetext):
        index = x%len(keyword)
        d.rotate(index)
        ciphindex = d.index()


#-------------------------------------------------------------
if eod.upper() == "D":
    print("1: Caesar Cipher")
    print("2: Substitution Cipher")
    print("3: Morse Code")
    print("4: Affine Cipher")
    print("5: Vigenere Cipher")
    print("6: Hill Cipher")
    print("7: Columnar Transposition")
    decryption_type = input("Enter the decryption type(1,2,3,4,5 or 6):")

    if decryption_type == "1":
        offset = int(input("Type the offset value"))
        decrypt_caesar(offset)
        print(text)

    elif decryption_type == "2":
        key = input("Enter the key for the cipher")
        newtext =[]
        decrypt_substitution(key)
        print(newtext)

    elif decryption_type == "3":
        newtext = []
        decrypt_morse()
        print(newtext)

    elif decryption_type == "4":
        a = int(input("Please enter the value for a"))
        b = int(input("Please enter the value for b"))
        newtext = []
        decrypt_affine(a,b)
        print(newtext)
#---------------------------------------------------------

if eod.upper() == "E":
    print("1:Caeser Cipher")
    print("2: Substitution Cipher")
    print("3: Morse Code")
    print("4: Affine Cipher")
    print("5: Vigenere Cipher")
    print("6: Hill Cipher")
    print("7: Columnar transposition")
    encryption_type = input("Enter the encyption type(1,2,3,4,5 or 6): ")
        



    if encryption_type == "1":
        offset = int(input("Please enter the offset value:"))
        encrypt_caesar(offset)
        print(text)
    elif encryption_type == "2":
        key = input("Please enter the key to encrypt it:")
        encrypt_substitution(key)
        print(text)
    elif encryption_type == "3":
        encrypt_morse()
        print(text)
    elif encryption_type == "4":
        a = int(input("Please enter the slope of your encryption:"))
        b = int(input("Please enter the intercept of your encryption:"))
        encrypt_affine(a,b)
        print(text)
    elif encryption_type == "5":
        keyword = input("Please enter the keyword to encrypt it:")
        encrypt_vigenere(keyword)
        print(text)
    elif encryption_type == "6":
        keyword = input("Please enter the keyword to encrypt it:")
        encrypt_hill(keyword)

    elif encryption_type == "7":
        key = input("Please the enter the key to encrypt the text:")
        encrypt_cl_row_transposition(key)
elif eod == "D":
    print()
else:
    print("try again(restart the code)")         
        


