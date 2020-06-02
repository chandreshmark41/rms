from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def StudentRegister(request):
    return render(request,'StudentRegister.html')

    #if request.method == 'POST':
        #first_name = request.POST['first_name']
       # last_name = request.POST['last_name']
       # username = request.POST['username']
        #year = request.POST['year']
        #branch = request.POST['branch']
        #email = request.POST['email']
        #phone = request.POST['phone']
        #password1 = request.POST['password1']
        #password2 = request.POST['password2']
        #if password1 == password2:
            #if User.objects.filter(userid == userid).exits():
                #messages.info(request, 'Userid is taken')
                #return redirect('StudentRegister')
            #elif User.objects.filter(email == email).exits():
                #messages.info(request, 'Email is taken')
                #return redirect('StudentRegister')
            #elif User.objects.filter(phone == phone).exist():
                #messages.info(request, 'phone number is taken')
                #return redirect('StudentRegister')
            #else:
            #user = User.objects.create_user(first_name=first_name, last_name=last_name, password=password1, username=username)
            #user.save();

def AdminRegister(request):
    return render(request, 'AdminRegister.html')
