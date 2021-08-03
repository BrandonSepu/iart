from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('terms/', views.terms, name= 'terms'),#CONTACT 
    path('contact/', views.contact, name= 'contact'),#CONTACT 
    path('trabajo/', views.trabajo, name= 'trabajo'),#TRABAJO 
    path('contactcrud/', views.contactcrud, name= 'contactcrud'), #CONTACT CRUD
    path('deleteContact/<idContact>', views.deleteContact, name= 'deleteContact'), #CC
    path('editContact/<idContact>', views.editContact, name= 'editContact'), #CC
    path('iart_admin', views.iart_admin, name= 'iart_admin'),
    path('register/', views.register, name= 'register'), #REGISTER
    path('login/', views.login, name= 'login'), #LOGIN
    path('equipo/', views.equipo, name= 'equipo'), #EQUIPO IART
    path('profile/', views.profile, name= 'profile'), #PROFILE
    path('usercrud/', views.usercrud, name= 'usercrud'), #USER CRUD
    path('deleteUser/<iduser>', views.deleteUser, name= 'deleteUser'), #UC
    path('editUser/<iduser>', views.editUser, name= 'editUser'), #UC
    path('productcrud/', views.productcrud, name= 'productcrud'),#PRODUCT CRUD
    path('deleteProduct/<idProduct>', views.deleteProduct, name= 'deleteProduct'), #PC
    path('editProduct/<idProduct>', views.editProduct, name= 'editProduct'), #PC
    path('addproduct/', views.addproduct, name= 'addproduct'), #PC
    path('orderUser/', views.orderUser, name= 'orderUser'), #ORDEN DE PEDIDO
    path('orderCrud/', views.orderCrud, name= 'orderCrud'), #ORDEN DE PEDIDO
    #path('adress/', views.adressOrder, name= 'adressOrder'), #DIRECCION DEL PEDIDO
]
