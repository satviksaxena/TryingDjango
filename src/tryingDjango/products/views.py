from django.shortcuts import render, get_object_or_404
from .forms import ProductForm,RawProductForm
from .models import Product
# Create your views here.

# Old way
# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form=ProductForm()
#
#     context={
#         'form': form,
#     }
#     return render(request, "products/item_create.html", context)

def render_initial_data(request, my_id):
    initial_data = {
        'title': "My Samsung Mobile"
    }
    obj = Product.objects.get(id=my_id)
    form= ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, "products/item_create.html", context)

def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm (request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data ) ## **  To pass as arguments
        else:
            print(my_form.errors)
    context={
        "form": my_form
    }
    return render(request, "products/item_create.html", context)

def product_detailed_view(request,my_id):
    # obj = Product.objects.get(id=my_id)
    # Better way to write above line To give 404 if object not found.
    obj = get_object_or_404(Product, id= my_id)
    context={
        'title': obj.title,
        'description': obj.description,
        'price' : obj.price,
    }
    return render(request, "products/item_details.html", context)

def product_delete_view(request, my_id):
    obj=get_object_or_404(Product, id= my_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../')
    context= {
        "object":obj
    }
    return render(request, "products/item_delete.html", context)

def product_list_view(request):
    queryset= Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/item_list.html", context)

