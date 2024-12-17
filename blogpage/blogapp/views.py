from django.shortcuts import render, get_object_or_404, redirect
from .models import AddPost
from .forms import AddPostForm 
 # Correct form import

# Create your views here.
def index(request):
    add = AddPost.objects.all()  # Fetch all posts
    return render(request, 'index.html', {'add': add})  # Pass add to the template

def about(request):
    return render(request, 'about.html')

def recentpost(request):
    return render(request, 'recentpost.html')

def addpost(request):
    if request.method == 'POST':
        head = request.POST.get('head')
        description = request.POST.get('description')
        images = request.FILES.get('images')

        if head and description and images:  # Check for all fields
            AddPost.objects.create(head=head, description=description, images=images)
            return redirect('index')  # Redirect to the index page

        msg = 'Please fill out all fields, including an image.'
        return render(request, 'addpost.html', {'msg': msg})
   
    return render(request, 'addpost.html', {'msg': ''})

def article_detail(request, article_id):
    article = get_object_or_404(AddPost, id=article_id)
    return render(request, 'article_detail.html', {'article': article})

def article_update(request, article_id):
    article = get_object_or_404(AddPost, id=article_id)
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = AddPostForm(instance=article)

    return render(request, 'article_update.html', {'form': form, 'article': article})

def article_delete(request, article_id):
    article = get_object_or_404(AddPost, id=article_id)
    
    if request.method == 'POST':
        article.delete()
        return redirect('index')
    
    return render(request, 'article_delete.html', {'article': article})
