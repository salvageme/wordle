import os
import random



def three():
    f=open("Words/3 letter words.txt",'r')
    x=f.readlines()
    n=random.randint(0,len(x))
    w=x[n]
    w=w.lower()
    f.close()
    w=list(w)
    w.pop()

    s=' _ _ _'
    c=[]
    n=[]
    logo()
    print("Guess the Word! (don't use capital letters)")
    print("")
    print(s)

    for i in range(5):
        if '_' not in s:
            continue
        s=' _ _ _'
        print("")
        a=input()
        if len(a)!=3:
            print('Invalid input')
            continue

        a=list(a)
        for j in range(len(w)):
            if w[j]==a[j]:
                s1=list(s)
                s1[j*2+1]=a[j]
                s2=''
                for k in s1:
                    s2+=k
                s=s2
            
            if a[j] in w and a[j] not in c:
                c.append(a[j])
                
            if a[j] not in w and a[j] not in n:
                n.append(a[j])
        
        print('')
        print('Word contains: ',c)
        print('Word does not contain: ',n)
        print(s)
    
    else:
        if '_' in s:
            os.system('cls')
            print("You lose!")
            word=''
            for i in w:
                word+=i
            print("the word was: ",word)
            print('')
        else:
            os.system('cls')
            print("You Win!")
            print('')

    input('Press Enter to continue')



def four():
    f=open("Words/4 letter words.txt",'r')
    x=f.readlines()
    n=random.randint(0,len(x))
    w=x[n]
    w=w.lower()
    f.close()
    w=list(w)
    w.pop()

    s=' _ _ _ _'
    c=[]
    n=[]
    logo()
    print("Guess the Word! (don't use capital letters)")
    print("")
    print(s)

    for i in range(5):
        if '_' not in s:
            continue
        s=' _ _ _ _'
        print("")
        a=input()
        if len(a)!=4:
            print('Invalid input')
            continue

        a=list(a)
        for j in range(len(w)):
            if w[j]==a[j]:
                s1=list(s)
                s1[j*2+1]=a[j]
                s2=''
                for k in s1:
                    s2+=k
                s=s2

            if a[j] in w and a[j] not in c:
                c.append(a[j])
                
            if a[j] not in w and a[j] not in n:
                n.append(a[j])
        
        print('')
        print('Word contains: ',c)
        print('Word does not contain: ',n)
        print(s)
    
    else:
        if '_' in s:
            os.system('cls')
            print("You lose!")
            word=''
            for i in w:
                word+=i
            print("the word was: ",word)
            print('')
        else:
            os.system('cls')
            print("You Win!")
            print('')

    input('Press Enter to continue')



def five():
    f=open("Words/5 letter words.txt",'r')
    x=f.readlines()
    n=random.randint(0,len(x))
    w=x[n]
    w=w.lower()
    f.close()
    w=list(w)
    w.pop()

    s=' _ _ _ _ _'
    c=[]
    n=[]
    logo()
    print("Guess the Word! (don't use capital letters)")
    print("")
    print(s)

    for i in range(5):
        if '_' not in s:
            continue
        s=' _ _ _ _ _'
        print("")
        a=input()
        if len(a)!=5:
            print('Invalid input')
            continue

        a=list(a)
        for j in range(len(w)):
            if w[j]==a[j]:
                s1=list(s)
                s1[j*2+1]=a[j]
                s2=''
                for k in s1:
                    s2+=k
                s=s2

            if a[j] in w and a[j] not in c:
                c.append(a[j])
                
            if a[j] not in w and a[j] not in n:
                n.append(a[j])

        print('')
        print('Word contains: ',c)
        print('Word does not contain: ',n)
        print(s)
    
    else:
        if '_' in s:
            os.system('cls')
            print("You lose!")
            word=''
            for i in w:
                word+=i
            print("the word was: ",word)
            print('')
        else:
            os.system('cls')
            print("You Win!")
            print('')

    input('Press Enter to continue')



def six():
    f=open("Words/6 letter words.txt",'r')
    x=f.readlines()
    n=random.randint(0,len(x))
    w=x[n]
    w=w.lower()
    f.close()
    w=list(w)
    w.pop()

    s=' _ _ _ _ _ _'
    c=[]
    n=[]
    logo()
    print("Guess the Word! (don't use capital letters)")
    print("")
    print(s)

    for i in range(5):
        if '_' not in s:
            continue
        s=' _ _ _ _ _ _'
        print("")
        a=input()
        if len(a)!=6:
            print('Invalid input')
            continue

        a=list(a)
        for j in range(len(w)):
            if w[j]==a[j]:
                s1=list(s)
                s1[j*2+1]=a[j]
                s2=''
                for k in s1:
                    s2+=k
                s=s2

            if a[j] in w and a[j] not in c:
                c.append(a[j])
                
            if a[j] not in w and a[j] not in n:
                n.append(a[j])

        print('')
        print('Word contains: ',c)
        print('Word does not contain: ',n)
        print(s)
    
    else:
        if '_' in s:
            os.system('cls')
            print("You lose!")
            word=''
            for i in w:
                word+=i
            print("the word was: ",word)
            print('')
        else:
            os.system('cls')
            print("You Win!")
            print('')

    input('Press Enter to continue')



def seven():
    f=open("Words/7 letter words.txt",'r')
    x=f.readlines()
    n=random.randint(0,len(x))
    w=x[n]
    w=w.lower()
    f.close()
    w=list(w)
    w.pop()

    s=' _ _ _ _ _ _ _'
    c=[]
    n=[]
    logo()
    print("Guess the Word! (don't use capital letters)")
    print("")
    print(s)

    for i in range(5):
        if '_' not in s:
            continue
        s=' _ _ _ _ _ _ _'
        print("")
        a=input()
        if len(a)!=7:
            print('Invalid input')
            continue

        a=list(a)
        for j in range(len(w)):
            if w[j]==a[j]:
                s1=list(s)
                s1[j*2+1]=a[j]
                s2=''
                for k in s1:
                    s2+=k
                s=s2

            if a[j] in w and a[j] not in c:
                c.append(a[j])
                
            if a[j] not in w and a[j] not in n:
                n.append(a[j])

        print('')
        print('Word contains: ',c)
        print('Word does not contain: ',n)
        print(s)
    
    else:
        if '_' in s:
            os.system('cls')
            print("You lose!")
            word=''
            for i in w:
                word+=i
            print("the word was: ",word)
            print('')
        else:
            os.system('cls')
            print("You Win!")
            print('')

    input('Press Enter to continue')



def eight():
    f=open("Words/8 letter words.txt",'r')
    x=f.readlines()
    n=random.randint(0,len(x))
    w=x[n]
    w=w.lower()
    f.close()
    w=list(w)
    w.pop()

    s=' _ _ _ _ _ _ _ _'
    c=[]
    n=[]
    logo()
    print("Guess the Word! (don't use capital letters)")
    print("")
    print(s)

    for i in range(5):
        if '_' not in s:
            continue
        s=' _ _ _ _ _ _ _ _'
        print("")
        a=input()
        if len(a)!=8:
            print('Invalid input')
            continue

        a=list(a)
        for j in range(len(w)):
            if w[j]==a[j]:
                s1=list(s)
                s1[j*2+1]=a[j]
                s2=''
                for k in s1:
                    s2+=k
                s=s2

            if a[j] in w and a[j] not in c:
                c.append(a[j])
                
            if a[j] not in w and a[j] not in n:
                n.append(a[j])

        print('')
        print('Word contains: ',c)
        print('Word does not contain: ',n)
        print(s)
    
    else:
        if '_' in s:
            os.system('cls')
            print("You lose!")
            word=''
            for i in w:
                word+=i
            print("the word was: ",word)
            print('')
        else:
            os.system('cls')
            print("You Win!")
            print('')

    input('Press Enter to continue')



def logo():
    print('''     ____      ____   ___   _______     ______   _____     ________  
    |_  _|    |_  _|.'   `.|_   __ \   |_   _ `.|_   _|   |_   __  | 
      \ \  /\  / / /  .-.  \ | |__) |    | | `. \ | |       | |_ \_| 
       \ \/  \/ /  | |   | | |  __ /     | |  | | | |   _   |  _| _  
        \  /\  /   \  `-'  /_| |  \ \_  _| |_.' /_| |__/ | _| |__/ | 
         \/  \/     `.___.'|____| |___||______.'|________||________| 
    ''')



while True:
    os.system('cls')
    logo()
    print("Welcone!")
    print('')
    print('Choose the length of words.')
    print('(3/4/5/6/7/8)')
    print('')
    print('Type "EXIT" it quit game.')
    ans=input()



    if ans=='3':
        os.system('cls')
        three()

    elif ans=='4':
        os.system('cls')
        four()

    elif ans=='5':
        os.system('cls')
        five()

    elif ans=='6':
        os.system('cls')
        six()

    elif ans=='7':
        os.system('cls')
        seven()

    elif ans=='8':
        os.system('cls')
        eight()

    elif ans=='EXIT' or ans=='exit' or ans=='Exit':
        os.system('cls')
        [print("Exiting...")]
        break

    else:
        os.system('cls')
        print('Invalid option!')
        print()
        input("Press Enter to continue")