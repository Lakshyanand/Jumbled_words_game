import random

def choose():
    words=["rainbow bow","brownie","umbrella","dog","communication"]
    word=random.choice(words)
    return word

def jumbled(wordd):
    jumbled=" ".join(random.sample(wordd,len(wordd)))
    return jumbled

def thanks(p1,p2,pp1,pp2):
    print(p1," your score is: ",pp1)
    print(p2," your score is: ",pp2)
    print("thanks for playing")
    print("have a nice day!")

def play():
    p1=input("player 1 name ")
    p2=input("player 2 name ")
    pp1=0
    pp2=0
    turn=0
    
    while(1):
        picked_word=choose()
        
        qn=jumbled(picked_word)
        print(qn)
        
        if turn%2==0:
            ans=input("player 1 your answer ")
            
            if ans==picked_word:
                pp1=pp1+1
                print("Correct answer")
                print("your score: ",pp1)
            else:
                print("better luck next time,coorect ans: ",picked_word)
            turn=turn+1
                
            c=int(input("press 1 to continue and 0 to exit "))
            if c==0:
                thanks(p1,p2,pp1,pp2)
                break
            
                
        else:
            ans=input("player 2 your answer ")
            
            if ans==picked_word:
                pp2=pp2+1
                print("Correct answer")
                print("your score: ",pp2)
            else:
                print("better luck next time,correct ans: ",picked_word)
            turn=turn+1
                
            c=int(input("press 1 to continue and 0 to exit "))
            if c==0:
                thanks(p1,p2,pp1,pp2)
                break
                

play()
            
                  
            
            