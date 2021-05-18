
# products/views.py
from django.views.generic import ListView #new
from .models import Product #new

class Home(ListView): # new
    model = Product
    context_object_name = "all_courses_list"
    template_name = "courses/base.html"