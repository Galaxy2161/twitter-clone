from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from.models import Post
from.forms import PostForm


# Create your views here.
# POST method -> when you send data to the backend
# GET method -> when you fetch data from backend to frontend

def index(request):
    # if the methos id POST
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES) 
        # if the form is valid
        if form.is_valid():
            # yes, save
            form.save() 
            # redirect to home
            return HttpResponseRedirect('/')
        else: 
            # if form is not valid
            return HttpResponseRedirect(form.errors.as_json()) 
        

    posts = Post.objects.all().order_by('-created_at')[:20] 
    form = PostForm()
    return render(request, 'index.html', {'posts':posts}) 


def delete(request , post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def like_count(request,post_id):
    post=Post.objects.get(id=post_id)
    post.likes+=1
    post.save()
    return HttpResponseRedirect("/")

def edit(request,post_id):
    if request.method=='GET':
        post=Post.objects.get(id=post_id)
        return render(request,'edit.html',{'post':post})
    
    if request.method=='POST':
        post=Post.objects.get(id=post_id)
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return  HttpResponseRedirect(form.errors.as_json())