from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Add_item
from .forms import Add_item_post
#from django import handle_uploaded_file
# Create your views here.


def get_item(request):
    form = Add_item_post()
    if request.method == "POST":
        form = Add_item_post(request.POST,  request.FILES)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect('/post_items/')
        else:
            form = Add_item_post()
    return render(request, 'post_items/add_item.html', {'form':form})

def post_items(request):
    obj_list = Add_item.objects.all().order_by("-id")
    return render(request, 'post_items/post_items.html', {'obj_list': obj_list})



def edit_item(request, id):
    edit_form = get_object_or_404(Add_item, id=id)
    if request.method == "POST":
        form = Add_item_post(request.POST, request.FILES, instance = edit_form)
        if form.is_valid():
            Add_item_post.name_item = request.POST.get("name_item")
            Add_item_post.price_item = request.POST.get("price_item")
            Add_item_post.desciption_item = request.POST.get("desciption_item")
            edit_form.save()
            return HttpResponseRedirect('/post_items/')
    else:
        form = Add_item_post(instance=edit_form)
    return render(request, 'post_items/edit_item.html', {'form': form})

def delete_item(request, id):
    try:
        delete_list = Add_item.objects.get(id=id)
        delete_list.delete()
        return HttpResponseRedirect("/post_items/")
    except Add_item.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
