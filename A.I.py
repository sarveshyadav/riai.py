import math as m
import datetime
import time
print('Hey!! user, My name is M.A.I.T and I am A.I. designed by my Boss.')
user_name = str(input('\nWhat Should I call you:\t'))
print('\nHye!',user_name,' Nice to meet you.')
print('\nToday Date and Time is:' ,datetime.datetime.now())
print('\nWhat Can I do for you\n\nHere are some keywords::-> Enter serial No. only.\n\n1.Add\n2.Sub\n3.Multi\n4.Division\n5.Area\n6.Trigonometry\n7.Square root\n8.Cube root\n9.Log')
user_task = str(input('\nEnter Your Task: '))
if user_task == '1':
    number_add = int(input('How many Number you wanna Add: '))
    total_num_add = 0
    print('Enter Your Numbers ')
    for i in range(1, number_add + 1):
        numberadd = float(input('Number'+str(i)+': '))
        assert numberadd>=0 and numberadd<=999999999
        total_num_add += numberadd
        print(total_num_add)
elif user_task == '2':
    print('Enter Your Number')
    numsub_a = int(input('Number 1: '))
    numsub_b = int(input('Number 2: '))
    sub = numsub_a- numsub_b
    print('The answer is:',sub)
elif user_task == '3':
    nummulti_a = float(input('Number 1: '))
    nummulti_b = float(input('Number 2: '))
    multi = nummulti_a*nummulti_b
    print('The answer is: ',multi)
elif user_task == '4':
    numdivi_a=float(input('Number 1: '))
    numdivi_b=float(input('Number 2: '))
    divi = numdivi_a/numdivi_b
    print('The answer is: ',divi)
     # AREA OF Shape START #
elif user_task=='5':
    print('\nArea of triangle(tri), Rectangle(rect), Square(sq)')
    area1 = str(input('\nEnter your shape: '))
    if area1 == 'tri':
      s1 = float(input('\nFirst Side: '))
      s2 = float(input('\nSecond Side '))
      s3 = float(input('\nThird Side '))
      a = ((s1+s2+s3)/2)
      b = (a*(a-s1)*(a-s2)*(a-s3))
      z = math.pow(b,(1/2))
      print ('\nArea of Δ: ',z,'sq unit')
    elif area1 == 'rect':
          side_rect_l = float(input('\nEnter Length: '))
          side_rect_b = float(input('\nEnter breadth: '))
          area_rect =  side_rect_l* side_rect_b
          print('\nArea of rectangle is: ',area_rect,'sq unit')
    elif area1 == 'sq':
          side_sq = float(input('\nEnter Side: '))
          area_sq =  side_sq**2
          print('\nArea of square is: ',area_sq,'sq unit')
     # AREA OF Shape END #
elif user_task == '6':
    angle = int(input('Enter Angle: '))
    assert angle>=0 and angle<=360
    trigonometric = str(input('Enter sin or cos or tan: '))
    if trigonometric =='sin':
        sin = m.sin(angle)
        print('The value of sin',angle, '= ',sin)
    elif trigonometric =='cos':
        cos = m.cos(angle)
        print('The value of cos',angle, '= ',cos)
    elif trigonometric =='tan':
        tan = m.tan(angle)
        print('The value of tan',angle, '= ',tan) 
elif user_task == '7':
    sqr_a = float(input('Enter Number: '))
    sq_ra = (sqr_a**(1/2))
    print('Square root of ',sqr_a,'is: ',sq_ra)
elif user_task == '8':
    cbr_a = float(input('Enter Number: '))
    cb_ra = (cbr_a**(1/3))
    print('Cube root of ',cbr_a,'is: ',cb_ra)
elif user_task == '9':
    log_val = float(input('Enter Number: '))
    log = m.log(log_val)
    print('The value of log(',log_val,') is: ',log)
elif user_task == '10':
    print('Welcome in my Game zone.',user_name,)
    print('Computer number = x, you will have to find x. Can You do?')
    import random
computer_guess = random.randint(1,100)
user_input = ''
while user_input != computer_guess:
      user_input = int(input('Guess the number: '))
      if user_input > computer_guess:
           print('High! Guess Again')
      elif user_input < computer_guess:
           print('Low! Guess Again')
      else:
           print('Yeah You got it.')       
print('\nEnd of Program!! Goodbye! See you again',user_name,'Bye-~~-Bye')

                    
                    
                    
                    
                    
                    
                    
                    
                    
