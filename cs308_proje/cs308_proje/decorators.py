from django.shortcuts import redirect
from django.contrib import messages


class Singleton:
    def __init__(self, client):
        self.__client = client()
        self.__value = None

    def __call__(self, *args, **kwargs):
        if self.__value is None:
            self.__value = self.__client

        return self.__value

@Singleton
class logintracker:
    username = None
    Object = None

    def __init__(self):
        self.status = False
    
    def activate(self,admin_name,obj):
        self.status = True
        self.username = admin_name
        self.Object = obj

    def deactivate(self):
        self.status = False
        self.username = None
        self.Object = None

def login_check_required(func):
    def decorator(*args, **kwargs):
        hold = logintracker()
        if hold.status == False:
            return redirect("/appointment_app/loginpage")
        else:
            return func(*args, **kwargs)
    return decorator

def user_type_check(func):
    def decorator(*args, **kwargs):
        hold = logintracker()
        if hold.Object.user_type == "highschool":
            return redirect("/highschool_app/profile")
        elif hold.Object.user_type == "university":
            return redirect("/university_app/universityprofile")
        elif hold.Object.user_type == "individual":
            return redirect("/individual_app/profile")
        else:
            hold.deactivate()
            return redirect("/")
    return decorator
