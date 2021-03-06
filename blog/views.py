# from django.db.models.query import QuerySet
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
from .forms import BlogPostModelForm
from .models import BlogPost

def blog_post_list_view(request):
    qs = BlogPost.objects.all()  #instead of .all, you could use filter(title__icontains='hello')
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

@staff_member_required
#@login_required
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
#        form.save() # obj = BlogPost.objects.create(**form.cleaned_data)
        form = BlogPostModelForm()
    template_name = 'form.html'
    context = {'form': form}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug): # this is a retrieve view
    obj = get_object_or_404(BlogPost, slug=slug)      # query -> database
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

def blog_post_update_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)      # query -> database
    template_name = 'blog/update.html'
    context = {"object": obj, 'form': None}
    return render(request, template_name, context)

def blog_post_delete_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)      # query -> database
    template_name = 'blog/delete.html'
    context = {"object": obj}
    return render(request, template_name, context)
