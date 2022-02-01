import airtel
import GP
import dactarbhai
import bioscopelive
import robi

print('''

  _____                   _______                 
 |  __ \                 |__   __|                
 | |__) |  _ __    ___      | |      __ _   _ __  
 |  ___/  | '__|  / _ \     | |     / _` | | '_ \ 
 | |      | |    | (_) |    | |    | (_| | | | | |
 |_|      |_|     \___/     |_|     \__,_| |_| |_|
                                                  
                                                  
The SMS boomber developed by -> Protan Halder      
Contact : https://www.facebook.com/Protan1010
Email   : protanhalder2021@gmail.com

      ''')

with open("number.txt", 'r') as f:
    numbers = f.read().split('\n')

while True:
    for n in numbers:
        
        if n[0:3] == "013" or n[0:3] == "017":
            if GP.Sent(n):
                print(f"Message Sent to {n} From GP web")
        
        if n[0:3] == "013" or n[0:3] == "017":
            GP.Sent(n)
            print(f"Message Sent to {n} From GP web" )
        
        if n[0:3] == "018":
            if robi.Sent(n):
                print(f"Message Sent to {n} From Robi Web")
        
        if n[0:3] == "016":
            if airtel.Sent(n):
                print(f"Message Sent to {n} From Airtel Web")
                
        if bioscopelive.Sent(n):
            print(f"Message Sent to {n} From Bioscope")
        if dactarbhai.Sent(n):
            print(f"Message Sent to {n} From Dactarbhai")