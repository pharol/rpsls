import random
def name_to_number(name):
    if name=='rock':
        return 0
    elif name=='Spock':
        return 1
    elif name=='paper':
        return 2
    elif name=='lizard':
        return 3
    elif name=='scissors':
        return 4

def number_to_name(number):
    if number==0:
        return 'rock' 
    elif number==1:
        return 'Spock'
    elif number==2:
        return 'paper'
    elif number==3:
        return 'lizard'
    elif number==4:
        return 'scissors'
    
def rpsls(name):
    print "Player chooses",name
    p1 = name_to_number(name)
   # print p1
    p2=  random.randrange(5)
    #print p2
    print "Computer chooses",number_to_name(p2)
    result= (p2-p1) % 5
    
    if result==1 or result ==2:
        print "Computer Wins!"
    elif result==4 or result ==3:
        print "Player Wins!"
    #else:
    print
        
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")    
#print number_to_name(name_to_number('rock'))
