# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm, AccessForm
from .models import Item, Sessions

def inventory_list(request):
    items = None
    access_form_visible = False

    if request.method == 'POST':
        access_form = AccessForm(request.POST)
        if access_form.is_valid():
            user = access_form.cleaned_data['user']
            code = access_form.cleaned_data['code']
            session = Sessions.objects.filter(user=user, user_code=code).first()

            if session:
                request.session['user_code'] = code
                items = Item.objects.filter(user_code=code)
            else:
                access_form_visible = True
    else:
        access_form = AccessForm()
        user_code = request.session.get('user_code')
        if user_code:
            items = Item.objects.filter(user_code=user_code)
        else:
            access_form_visible = True

    return render(request, 'inventory/inventory_list.html', {'access_form': access_form, 'items': items, 'access_form_visible': access_form_visible})

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
            # Get the user code from the session
            user_code = request.session.get('user_code')

            # Check if user code is available
            if user_code:
                item = form.cleaned_data['item']
                quantity = form.cleaned_data['quantity']
                Item.objects.create(item=item, quantity=quantity, user_code=user_code)
                return redirect('inventory_list')
    else:
        form = ItemForm()

    return render(request, 'inventory/add_item.html', {'form': form})