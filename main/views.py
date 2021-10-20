from django.shortcuts import render
from django.http import HttpResponse
import datetime
from main.models import Producto
# Create your views here.

# Function Based Views.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body> Son las %s </body></html>" % now
    return HttpResponse(html)

def home_page(request):
    template_name = 'home.html'
    now = datetime.datetime.now()
    productos = Producto.objects.all()
    productos = Producto.objects.filter(cantidad_en_bodega__gte=1).order_by('-pk')
    calcetines_halloween = Producto.objects.filter(nombre='Calcetines de Halloween').first()
    calcetines_halloween.precio = 700.00
    calcetines_halloween.save()
    context = { "now": now, "productos": productos}
    return render(request, template_name=template_name, context=context)