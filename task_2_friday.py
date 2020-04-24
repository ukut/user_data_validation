def get_details():
  first_name = input(" my first name is : ")
  last_name = input(" my last name is : ")
  email = input(" my email is : ")
  user_details = (first_name, last_name,  email)
  return user_details

#generate password from users details
    def random_password(user_details):
        characters = string.ascii_letters
        str_length = 5
        generated_pwd = ''.join(random.choice(characters) for i in range(str_length)
        password = user_details[0][:2] + user_details[1][-2:] + generated_pwd
        return password                        

     # get users details
    status = True
    container = []
    while True:
          user_details = get_details()
         # display generated password
         password = ran_password(user_details)
         print("the password is: " + str(password))

         # ask if the user will like to continue
         like_password = input(" are you satisfy with the password,if yes, enter: YES, or enter: NO, and supply your password")

        password_loop  = True
         while password_loop:
             if like_password = 'yes'
                 #add password to users details
                 user_details.append(password)
                  # add user details to the container
                 container.append(user_details)
                 break

         else:
           # enter password longer than or equal to 7
            user_pwd = input("enter password greater than or equal to 7")
            #password length loop
            pwd_length = True
              while pwd_length:
                if len(pwd_length) >= 7:
                     user_details.append(user_pwd)
             # add user details to the container
                     container.append(user_details)
                         pwd_length = False
                    #break out of the whole password loop
                    password_loop = False
               else:
                  print(" your password is less than 7")

                  user_pwd = input("enter password grater than or equal to 7: ")

# new_user
new_user = input("will you like to enter a new user, Yes or No")
if new_user == "NO":
   status = False
    for items in the container:
        print(item)
else:
    status = True


