from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
# Create your views here.
def register(request):
    if request.method == 'POST':
        print('enter')
        username = request.POST['username']
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        email = request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']
        user = User.objects.create_user(username=username,email=email,first_name=first_name,password=password1,last_name=last_name)
        user.save()
        print('user created')
        return redirect('/')
    else:
        return render(request,'register.html')
def login(request):
    pass
