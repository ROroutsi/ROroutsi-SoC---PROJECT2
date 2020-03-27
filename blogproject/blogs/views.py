from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import blog
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import comment
from users.forms import CommentForm
from django.http import HttpResponseRedirect

@login_required
def home(request):
	context = {
		'blogs' : blog.objects.all() 
	}
	return render(request, 'blogs/home.html', context)

@login_required
def slug(request, id, slug):
	instance = blog.objects.get(blogSlug=slug)
	comments = comment.objects.filter(commentBlog=id)
	
	if request.method == 'POST':
		commentform = CommentForm(request.POST)
		if commentform.is_valid():
			commentcontent = request.POST.get('comment_content')
			commentobjects = comment.objects.create(commentAuthor=request.user, commentBlog = instance, commentContent = commentcontent)
			commentobjects.save()
			messages.success(request, 'Your comment has been added!')	
			return HttpResponseRedirect(request.path_info)
	else:
		commentform = CommentForm()

	is_liked = False	
	if instance.blogLikes.filter(id=request.user.id).exists():
		is_liked = True
			
	context = {
		'instance' : instance,
		'comments' : comments,
		'commentform' : commentform,
		'totalLikes': instance.totalLikes(),
		'is_liked': is_liked
	}
	return render(request, 'blogs/slug.html', context)	

def likes(request):
	like = get_object_or_404(blog, id=request.POST.get('blog_id'))
	is_liked = False
	if like.blogLikes.filter(id=request.user.id).exists():
		like.blogLikes.remove(request.user)
		is_liked = False
	else:	
		like.blogLikes.add(request.user)
		is_liked = True

	return HttpResponseRedirect(like.get_absolute_url())