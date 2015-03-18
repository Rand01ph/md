#from django import VERSION

from .models import About
from mezzanine.utils.views import render
# Create your views here.

def test(request):
    return render("Hello World, Django")


def about_detail(request, template="mezzanine_about/about_detail.html"):
    about = About.objects.all()[0]
    context = {"about": about}
    return render(request, template, context)
