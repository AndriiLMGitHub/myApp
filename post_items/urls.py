from django.urls import path, re_path
from django.views.generic import ListView, DetailView
from . import views
from .models import Add_item
from .forms import Add_item_post


urlpatterns = [
    #path('', ListView.as_view(queryset = Add_item_post.objects.all() ,
    #template_name = "goods/goods.html" )),
    path('', views.post_items, name='post_items'),
    path('get_item', views.get_item, name='get_item'),
    re_path(r'^view/(?P<pk>\d+)$', DetailView.as_view(model = Add_item, template_name = "post_items/view_item.html")),
    path('edit_item/<int:id>', views.edit_item, name = "edit_item"),
    path('delete_item/<int:id>/', views.delete_item, name="delete_item"),
]
