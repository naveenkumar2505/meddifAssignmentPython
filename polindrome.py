def isPolindrome(charec):
    charec=charec.lower()
    rcharec=charec[::-1]
    if charec==rcharec:
        return True
    else:
        return False

word=input("Enter thr word: ")
flag=isPolindrome(word)
if flag==True:
    print("Ploindrome")
else:
    print("Not A Ploindrome")
