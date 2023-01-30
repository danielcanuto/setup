from django.contrib.auth import views

class Login(views.LoginView):
    template_name = "usuario/registration/form.html"
    

class Logout(views.LogoutView):
    next_page = "/"

   