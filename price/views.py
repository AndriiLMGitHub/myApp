from django.shortcuts import render

# Create your views here.
def price(request):
    price = {
        'name': ['Andrii', 'Ivan', 'Aleksandr', 'Mark', 'Bob'],
        'count': [23 , 32 , 12 , 9 , 10],
        'price_per': [12, 13, 14, 15, 16],
        'summ': [0,0,0,0,0]
    }
    return render(request, 'price/price.html', price)
