from django.shortcuts import redirect, render, HttpResponse
from blog.models import blog

# Create your views here.
def blogs(request):
    #return HttpResponse("home nitin
    allpost = blog.objects.all()
    contxt = {'allpost': allpost}

    return render(request,'blog/blogs.html', contxt) 
def profile(request):
    #return HttpResponse("home nitin")
    

    return render(request,'blog/profile.html') 
def newblog(request):
    #return HttpResponse("home nitin")
    

    return render(request,'blog/newblog.html')
    
def allblog(request):
    #return HttpResponse("home nitin")
    

    return render(request,'blog/allblog.html')

def blogspost(request, slug):
    return HttpResponse(f"home nitin: {slug}")
    

    #return render(request,'newblog.html')      