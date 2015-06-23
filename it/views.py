from django.shortcuts                                 import render, render_to_response, get_object_or_404, redirect
from django.utils                                     import timezone
from django.template                                  import RequestContext
from .models                                          import Itmanual
from .forms                                           import PostForm
    
def all_posts(request):
    context = RequestContext(request)
    # context_dict = {"post_title" :  }
    posts = Itmanual.objects.filter()
    # return render(request, 'it/post_list.html', {'posts': posts})
    return render(request, 'it/post_list.html', {'posts': posts})
def language(request, language):
    posts = Itmanual.objects.filter(language=language)
    return render(request, 'it/post_list.html', {'posts': posts})
def topic(request, topic):
    posts = Itmanual.objects.filter(topic=topic)
    return render(request, 'it/post_list.html', {'posts': posts})
def item(request, language, topic):
    posts = Itmanual.objects.filter(language=language, topic=topic)
    return render(request, 'it/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Itmanual, pk=pk)
    return render(request, 'it/post_detail.html', {'post': post})
def post_new(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, 'it/post_edit.html', {'form': form})
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('it.views.post_detail', pk=post.pk)
        else:
            return render(request, 'it/post_edit.html', {'form': form})
    else:
        return render(request, 'it/debug.html', {})

def post_edit(request, pk):
    post = get_object_or_404(Itmanual, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('it.views.post_detail', pk=post.pk)
        else:
            return render(request, 'it/post_edit.html', {'form': form})
    elif request.method == "GET":
        form = PostForm()
        return render(request, 'it/post_edit.html', {'form': form})
    else:
        return render(request, 'it/debug.html', {})



