from django.shortcuts import render
from django.views import generic
from catalog.models import *
from django.http import JsonResponse
import json
import datetime
from django.core.mail import send_mail
from .forms import Message
from django.utils.translation import gettext as _
# Create your views here.

def works(request):
    items = Picture.objects.filter(is_in_works=True)

    try:
        deviceId = request.COOKIES['deviceId']
        customer, created = Customer.objects.get_or_create(deviceId=deviceId)
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        cart_num_of_items = order.orderitem_set.count()
    except:
        cart_num_of_items = 0

    context = {
            'items':items,
            'number':cart_num_of_items,
            }
    print(cart_num_of_items)

    return render(request, 'catalog/works.html', context)

def store(request):
    try:
        deviceId = request.COOKIES['deviceId']
        customer, created = Customer.objects.get_or_create(deviceId=deviceId)
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        cart_num_of_items = order.orderitem_set.count()
    except:
        cart_num_of_items = 0

    context = {
            'number':cart_num_of_items,
            }
    return render(request, 'catalog/store.html', context)

def color(request):
    items = Picture.objects.filter(is_in_color=True)
    print(items)

    try:
        deviceId = request.COOKIES['deviceId']
        customer, created = Customer.objects.get_or_create(deviceId=deviceId)
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        cart_num_of_items = order.orderitem_set.count()
    except:
        cart_num_of_items = 0

    context = {
            'items':items,
            'number':cart_num_of_items,
            }

    return render(request, 'catalog/color.html', context)

def graphics(request):
    items = Picture.objects.filter(is_in_graphics=True)

    try:
        deviceId = request.COOKIES['deviceId']
        customer, created = Customer.objects.get_or_create(deviceId=deviceId)
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        cart_num_of_items = order.orderitem_set.count()
    except:
        cart_num_of_items = 0

    context = {
            'items':items,
            'number':cart_num_of_items,
            }

    return render(request, 'catalog/graphics.html', context)

def cart(request):

    try:
        deviceId = request.COOKIES['deviceId']
        customer, created = Customer.objects.get_or_create(deviceId=deviceId)
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        cart_num_of_items = order.orderitem_set.count()
        items = order.orderitem_set.all()
        total = order.get_total()
    except:
        cart_num_of_items = 0
        items = []
        total = 0
        cart_num_of_items = 0

    context = {
            'items': items,
            'total': total,
            'number':cart_num_of_items,
            }
    return render(request, 'catalog/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                complete=False)
        items = order.orderitem_set.all()
        total = order.get_total()
        cart_num_of_items = order.orderitem_set.count()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {
            'items':items,
            'order':order,
            'number':cart_num_of_items,
            'total':total,
            }
    return render(request, 'catalog/checkout.html', context)

def contacts(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Message(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # send a mail via sendinblue
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            send_mail("Lenok: message from " + name, message, email, ["kit4nikit4@gmail.com", "lenok.ph@gmail.com"])
    # if a GET (or any other method) we'll create a blank form
    else:
        form = Message()

    return render(request, 'catalog/contacts.html', {'form': form})

def about(request):
    context={}
    return render(request, 'catalog/about.html', context)
def picture(request, pk):
    pictures = Picture.objects.all()

def item(request, pk):
    picture = Picture.objects.get(picture_id=pk)
    try:
        deviceId = request.COOKIES['deviceId']
        customer, created = Customer.objects.get_or_create(deviceId=deviceId)
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        cart_num_of_items = order.orderitem_set.count()
    except:
        cart_num_of_items = 0

    context = {
            'picture':picture,
            'number':cart_num_of_items,
            }

    return render(request, 'catalog/item.html', context)

def updateItem(request):
    data = json.loads(request.body)
    pictureId = data['pictureId']
    action = data['action']

    print('Action: ', action)
    print('PictureId: ', pictureId)


    deviceId = request.COOKIES['deviceId']
    print('DeviceId = ', deviceId)

    customer, created = Customer.objects.get_or_create(deviceId=deviceId)
    order, created = Order.objects.get_or_create(customer=customer,
            complete=False)
    picture = Picture.objects.get(picture_id=pictureId)
    orderItem, created = OrderItem.objects.get_or_create(order=order,
            picture=picture)

    if action == 'add':
        if orderItem.quantity >= picture.quantity:
            print("Not enauth items to add")
        else:
            orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    items = order.orderitem_set.all()
    total = order.get_total()
    cart_num_of_items = order.orderitem_set.count()
    context = {
            'total':total,
            'action': action,
            'id': pictureId,
            'number': cart_num_of_items,
            }

    return JsonResponse(context, safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    print('Data:', request.body)
    return JsonResponse('Payment complete', safe=False)

