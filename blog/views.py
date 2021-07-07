from django.shortcuts import redirect, render, HttpResponse
from blog.models import blog
from django.contrib import messages

# Create your views here.
def blogs(request):
    #return HttpResponse("home nitin
    allpost = blog.objects.all()
    contxt = {'allpost': allpost}

    return render(request,'blog/blogs.html',contxt)
   

    return render(request,'blog/blogs.html') 
def profile(request):
    #return HttpResponse("home nitin")
    

    return render(request,'blog/profile.html') 
def newblog(request):
    #return HttpResponse("home nitin")
    if request.method=="POST":
        title = request.POST['title']
        content = request.POST['content']
        slug = request.POST['title']
        image = request.POST['image']
        #upload_to = request.POST['upload_to']
        contact = blog(title=title, content=content,slug=slug,image=image)
        contact.save()
        messages.success(request,"New Post added")
        return redirect("/blogs/allblog.html")
    

    return render(request,'blog/newblog.html')
    
def allblog(request):
    #return HttpResponse("home nitin")
    
    allpost = blog.objects.all()
    contxt = {'allpost': allpost}
    return render(request,'blog/allblog.html',contxt)

def blogspost(request, slug):
    post = blog.objects.filter(slug=slug)[0]
    
    contxt = {'post': post}
    return render(request,'blog/display.html',contxt)
    

    #return render(request,'newblog.html')      