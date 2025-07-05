from django.shortcuts import render, get_object_or_404
from .models import Item

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item.pk)[:4]
    
    return render(request, 'items/detail.html', {'item': item, 'related_items': related_items})