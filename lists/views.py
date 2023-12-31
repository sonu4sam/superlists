from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
    if request.method == 'POST':
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect('view_list', list_id=list_.id)

    return render(request, 'home.html')

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('view_list', list_id=list_.id) 

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('view_list', list_id=list_.id)

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'list': list_, 'items': items})