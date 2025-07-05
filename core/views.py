from django.shortcuts import render
from items.models import Item, Category

def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[:6]
    categories = Category.objects.all()
    return render(request, "core/index.html", {
        "items": items,
        "categories": categories,
    })


def contact(request):
    return render(request, "core/contact.html")


# Create your views here.
