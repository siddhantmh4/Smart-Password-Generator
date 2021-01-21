import string
import random
if __name__ == '__main__':
    s1=string.ascii_uppercase
    s2=string.ascii_lowercase
    s3=string.punctuation
    s4=string.digits
    print("*********Welcome At Password Generator**********")
    while True:
        try:
            len=int(input("Enter the Length of Password\n"))
            break
        except:
            print("Enter Number\n")


    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #print(s)

    random.shuffle(s)
    random.shuffle(s)
    print("Your Password is\n")
    print("".join(s[0:len]))