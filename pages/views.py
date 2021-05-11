from django.shortcuts import render
from django.template.loader import get_template
from django.conf import settings
from django.http import HttpResponse
# Create your views here.
#HOME_PAGE_MSG = settings.HOME_PAGE_MSG
HOME_PAGE_MSG = getattr(settings, "HOME_PAGE_MSG", "Missing Message")
BASIC_INFO_MSG = getattr(settings, "BASIC_INFO_MSG", "Missing Message")

#def home_view(request):
#    return HttpResponse(f"<h1>{HOME_PAGE_MSG}, {BASIC_INFO_MSG}, 875 Manomen Ave. St. Paul</h1>")

def home_page(request):
   #doc = "<h1>{title}</h1>".format(title=title)
   #django_rendered_doc = "<h1>{{title}}</h1>".format(title=mytitle)
#    context = {"title":HOME_PAGE_MSG, "info": BASIC_INFO_MSG}
#    if request.user.is_authenticated:
    context = {"title":HOME_PAGE_MSG, "info": BASIC_INFO_MSG, 'my_list':["Holy Days 2021","May 13", "Nov 01", "Dec 08", "Dec 25"]}
    return render(request, "home.html", context)
def contact_page(request):
    return render(request, "contact.html", {"title":HOME_PAGE_MSG, "info":"Contact Us"})
def about_page(request):
    return render(request, "about.html", {"title":HOME_PAGE_MSG, "info": BASIC_INFO_MSG})
def example_page(request):
    context         = {"title":"Example"}
    template_name   = "hello.html"
    template_obj    = get_template(template_name)
    rendered_item   = template_obj.render(context)
    return HttpResponse(rendered_item)
