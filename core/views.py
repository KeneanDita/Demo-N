from django.shortcuts import render
from items.models import Item, Category
from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[:6]
    categories = Category.objects.all()
    return render(request, "core/index.html", {
        "items": items,
        "categories": categories,
    })


def contact(request):
    return render(request, "core/contact.html")

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "core/signup_success.html")
    else:
        form = SignupForm()
    return render(request, "core/signup.html", {"form": form})

