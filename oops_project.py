class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Press
                           1 to signup 
                           2 to signin 
                           3 to write a post 
                           4 to message a friend 
                           5 to exit """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
    def signup(self):
        email = input("enter your email here ")
        pwd = input("enter your password ")
        self.username = email
        self.password = pwd
        print("signed up successfully ")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("press signup first ")
        else:
            uname = input("enter username ")
            pwd = input("enter your password ")
            if self.username == uname and self.password == pwd:
                print("signed in successfully ")
                self.loggedin = True
            else:
                print("invalid credentials ")
        print("\n")
        self.menu()

obj = chatbook()