#A solution to the well known Josephus problem
"""*Josephus Problem*

N people (numbered 1 to N) are standing in a circle. Person 1 kills Person 2 with a sword and gives it to Person 3. Person 3 kills Person 4 and gives the sword to Person 5. This process is repeated until only one person is alive.

Task:
(Medium) Given the number of people N, write a program to find the number of the person that stays alive at the end.
Hard) Show each step of the process."""


while True:
    number = int(input("Input the number of people\n"))
    n=[]
    for i in range(1,number + 1):
        n.append(i)
    
    if len(n) < 1:
        print("invalid no")
    elif len(n) ==1 or len(n) ==2:
        print(n[0])
    else:
        while len(n) >= 3:
            b=0
            a=[]
            
            while True:
                
                a.append(n[b])
                
                
                try:
                    n[b+2]
                    
                    
                except:
                    IndexError
                    a=n[b:] + a[:len(a)-1]
                    
                    
                    n=a[:]
                    a=[]
                    break
                b=b+2    
                
        print("Person number", n[0], "survives")
    

                
