def count_down_100():        
    counter = 100

    while(counter >= 0):
        print(counter)
        counter -= 1


count_down_100()

def count_up_100():
    counter = 0

    while(counter <= 100):
        print(counter)
        counter += 1


count_up_100()

def password():
    guess="easy_access"
    while(guess != "scuba"):
        guess = input("no_access ")
        

password()
        
        
