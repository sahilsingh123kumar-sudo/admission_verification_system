# project on admission verfication system 


print("admission verification system")
registration_number=int(input("enter your registration number:"))
if registration_number==2026:
    stream=input("enter your stream (commerce/arts/science):").lower()
    marks=int(input("enter your marks:"))

    if stream == "commerce":
        if marks>=75:
            password=int(input("enter your password:"))
            if password==1234:
                print("admission granted🎉")
            else:
                print("wrong password❌")
        else:
            print("marks are  low for commerce. better luck for the next time")
    elif stream== "science":
        if marks >= 80:
            password=int(input("enter your password:"))
            if password==1234:
                print("admission granted🎉")
            else:
                print("wrong password❌")
        else:
            print("marks are  low better for science. luck next time")
    else:
        if marks>=65:
            password=int(input("enter your password:"))
            if password==1234:
                print("admission succesful🎉")
            else:
                print("wrong password❌")
        else:
            print("marks are low for arts. better luck next time")

else:
    print("wrong registration number❌❌❌")                    

         
               

            

 


