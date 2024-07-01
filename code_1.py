# making a random q generator
import random
alphabets = (('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'))
numbers= (('1','2','3','4','5','6','7','8','9'))
characters = (('!','@','#','$','%','^','&','*','(',')'))
capitals = (('A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'))

print ('hello, i will generate a q for you , type "get" to generate a q ')
print ("type 'help' to know how this works" )

input1 = input()
if input1 == "get":
     print('generating')
     print('alomst there....')

     while True:
            print('how many charecters long do u want the password to be , type  a number between 4 to 100')
            length = int(input())
            if 4<= length <= 100:
                break
            else :
                 print('please enter a valid input')
        
 
     q = ''
     for _ in range (length):
         category = random.choice(['alphabets','numbers','characters','capitals'])
         if category == 'alphabets':
                        q += random.choice(alphabets)
         elif category == 'number':
                        q += random.choice(numbers)
         elif category == 'capitals':
                        q += random.choice(capitals)
         else:
                        q += random.choice(characters)

print ('your password:',q)
        
                      
            
            
        
            


