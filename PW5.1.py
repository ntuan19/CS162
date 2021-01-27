class Forum():
    def __init__(self,email,user,role,is_login = False):
        userbase = []
        self.email = email
        self.user = user
        self.role = role
        self.is_login = False
    def login(self,email):
        if self.email in userbase:
            print("Login succeed")
        else:
            print("Fail to authenticate")
class Student(Forum):
    def __init__(self, name, role,email):
        super._init_(name,role)
        self.answer_poll = False
        self.speak_in_class = False
    def answer_poll(self)
    def speak_in_class(self)
    def raise_hands(self)
class Teacher(Student):
    def __init__(self,name,role= teacher):
        self.assign_student = False
        self.break_out_class = False
    def assign_student()
    def break_out_class()


Question 2. 
