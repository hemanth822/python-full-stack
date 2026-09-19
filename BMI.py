
try :
    count = int(input('Enter the iteration count: '))
    while count>0:
        username = input('Enter your name: ')
        weight= float(input('Enter your weight in kgs: '))
        height = float(input('Enter your height in meters: '))
        if height < 0.20 or weight < 2:
            print('Invalid height and weight')
        else:
            bmi=weight/(height**2)
            print(bmi)
            if bmi < 18.5 :
                print('Underweight')
            elif 18.5 < bmi < 24.9 :
                print('Normal weight')
            elif 25 <  bmi < 29.9 :
                print('over weight')
            else:
                print('Obesity')
        count-=1
except ValueError:
    print("Enter valid numeric values ")

    
        

                    
