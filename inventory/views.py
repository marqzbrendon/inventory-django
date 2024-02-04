from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm
from .models import Item

def inventory_list(request):
    items = Item.objects.all()
    return render(request, 'inventory/inventory_list.html', {'items': items})

def increase_quantity(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.quantity += 1
    item.save()
    return redirect('inventory_list')

def decrease_quantity(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if item.quantity > 0:
        item.quantity -= 1
        item.save()
    return redirect('inventory_list')

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return redirect('inventory_list')

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            Item.objects.create(name=name, quantity=quantity)
            return redirect('inventory_list')
    else:
        form = ItemForm()

    return render(request, 'inventory/add_item.html', {'form': form})

