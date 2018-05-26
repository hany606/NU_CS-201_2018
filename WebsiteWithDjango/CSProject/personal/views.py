from django.shortcuts import render, redirect
from django.contrib import admin
from django.contrib.auth import authenticate, login 
def my_view(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/loggedin')
    else:
        if password=='' or username=='':
            return render(request, 'personal/login.html', {})
        else:
            return render(request, 'personal/login.html',{})

# Create your views here.
log={}
def index (request): 
    if request.GET.get('message') and request.GET.get('key') and request.GET.get('mode'):
       mode=request.GET.get('mode')
       message= request.GET.get('message')
       key=int(request.GET.get('key'))  
       cypheredMessage=''
       if key<1 or key >26:
           message='Please enter a valid Key'
           key=''
       else:
           
           if mode=='Decipher':
               key=-key             
           for symbol in message:
                if symbol.isalpha():
                    num = ord(symbol)       
                    num += key       
                    if symbol.isupper():           
                        if num > ord('Z'):
                            num -= 26
                        elif num < ord('A'):
                            num += 26 
                    elif symbol.islower():                  
                        if num > ord('z'):
                            num -= 26     
                        elif num < ord('a'):
                            num += 26 
                    cypheredMessage+=chr(num)
                else:
                    cypheredMessage+=symbol
                log[message]=cypheredMessage
       return render(request, 'personal/home.html',{'message':message,'key':key,'cypheredMessage':cypheredMessage,'log':log, 'mode':mode})
    else:
        message='Please fill all fields'
        key=''
        return render(request, 'personal/home.html',{'message':message,'key':key,'log':log})
       