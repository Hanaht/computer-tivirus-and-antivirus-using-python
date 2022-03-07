def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
xt=open('file.txt','r')
text=xt.readline()
s = 4
f = open("file.txt", "w")
f.write(encrypt(text,s))
