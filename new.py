def custom():
    testInfile=input("Enter file name : ")
    now=0
    file=open(testInfile,'r')
    for line in file:
        words=line.split()
        now=now+len(words)
    print("number of words : ")
    print(now)
custom()