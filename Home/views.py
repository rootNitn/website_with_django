from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from Home.models import Contact,video
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    #return HttpResponse("home nitin")
    

    return render(request,'index.html')    
def about(request):
    if request.user.is_anonymous:
        return redirect("/signin")
    return render(request,'about.html')    
def videos(request):
    if request.user.is_anonymous:
        return redirect("/signin")
    vid = video.objects.all()
    kk = {'task':vid}     
    return render(request,'videos.html',kk)
def signin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
            # A backend authenticated the credentials

        else:
            messages.danger(request,"your Username must be 8 characters")
            return render(request,'signin.html')
            # No backend authenticated the credentials

    return render(request,'signin.html')  
def signup(request):
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if len(fname)<2 or len(email)<5 or len(lname)<2 or len(password)>8:
            messages.error(request,"you fill worng entry")
        if password != cpassword:
            messages.error(request,"your password must be match")
            return redirect("/signup")
 
        
        user = User.objects.create_user(uname, email, password)
        user.last_name = lname
        user.first_name = fname
        user.save()
        messages.success(request,"your account Created")
        return redirect("/")
        
           
    return render(request,'signup.html') 
         
def contact(request):
    if request.user.is_anonymous:
        return redirect("/signin")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email,desc=desc,date=datetime.today())
        contact.save()
    return render(request,'contact.html')        
def logouthandle(request):
    if request.user.is_anonymous:
        return redirect("/signin")
    
    logout(request)
    messages.success(request,"your account logout")
    return redirect("/")    

def player(request,idi):
    if request.user.is_anonymous:
        return redirect("/signin")
    vid = video.objects.filter(idi=idi)[0]
    kk = {'task':vid}    
    
    return render(request,'player.html',kk) 

def chatbot(request):
    return render(request,'chatbot.html')    
