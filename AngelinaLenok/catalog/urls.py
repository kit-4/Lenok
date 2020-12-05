from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('works', views.works, name='works'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('color', views.color, name='color'),
    path('graphics', views.graphics, name='graphics'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('update_item', views.updateItem, name="update_item"),
    path('process_order', views.processOrder, name="process_order"),
    path('store', views.store, name="store"),
    path('item/<str:pk>', views.item, name="item"),
]

# redirecting root to store app
urlpatterns += [
        path('', RedirectView.as_view(url='works', permanent=True)),
]
