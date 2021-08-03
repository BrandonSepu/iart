from django.shortcuts import render, redirect
from .models import usercontact , newProduct, order
from .forms import contactForm, addProduct, CustomUserCreationForm, User, addOrder, moreData #, addAdress
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def index(request): #WEB INDEX

    products = newProduct.objects.all()
    data = {
        'entity' : products
    }
    return render(request, 'web/index.html', data)
@login_required
def iart_admin(request): #WEB ADMIN
    return render(request, 'web/admin.html')

def equipo(request): #EQUIPO IART
    return render(request, 'web/equipo.html')

def profile(request): #PROFILE
    return render(request, 'web/profile.html')

def terms(request): #PROFILE
    return render(request, 'web/terms.html')

def contact(request): #CONTACTO

    msnform = contactForm()
    data = {'cform' : msnform}
    
    if request.method == 'POST':
        msnform = contactForm(data = request.POST) 
        if msnform.is_valid():
            msnform.save()
        else:
            data["cform"] = msnform;
        
        print("Mensaje enviado Correctamente")
    else:
        print("No se puedo enviar el mensaje, revisa los datos")
        

    return render(request, 'web/contact.html',  data)

def trabajo(request): #TRABAJA CON NOSOTROS

    msnform = contactForm()
    data = {'cform' : msnform}
    
    if request.method == 'POST':
        msnform = contactForm(data = request.POST) 
        if msnform.is_valid():
            msnform.save()
        else:
            data["cform"] = msnform;
        
        print("Mensaje enviado Correctamente")
    else:
        print("No se puedo enviar el mensaje, revisa los datos")
        

    return render(request, 'web/trabajo.html',  data)

def contactcrud(request): #CONTACT CRUD

    contacts = usercontact.objects.all()

    data = {
        'entity' : contacts
    }

    return render(request, 'web/contactcrud.html', data)

@permission_required('core.delete_contact')
def deleteContact(request, idContact): #DELATE CONTACT

    contact = usercontact.objects.get(id=idContact)

    try:
        usercontact.delete(contact)
        print("Eliminado Correctamente")   
    except:
        print('No se puedo eliminar, revisa los datos')
        
    return redirect('contactcrud')

@permission_required('core.change_contact')
def editContact(request, idContact): #EDIT CONTACT
    econtact = usercontact.objects.get(id=idContact)
    data = {
    'cform': contactForm(instance=econtact) 
    }
    if request.method == 'POST':
        formulario_edit = contactForm(data=request.POST, instance=eproduct)
        if formulario_edit.is_valid:
            formulario_edit.save()
            print("Producto editado correctamente")
            return redirect('contactcrud')
        else:
            data["cform"] = formulario_edit;

    return render(request, 'web/contact.html', data)

def register(request): #REGISTER USER

    data = {
        'form' : CustomUserCreationForm()
    }
    formulario = CustomUserCreationForm(data=request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            reguser = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, reguser)
            print("te has registrado correctamente")
            return redirect('index')
        else:
            data['form'] = formulario
    else:
        print('error en el formulario')

    return render(request, 'registration/register.html', data)

def usercrud(request): #USER CRUD

    contacts = User.objects.all()

    data = {
        'entity' : contacts
    }

    return render(request, 'web/usercrud.html', data)

@permission_required('auth.delete_user')
def deleteUser(request, iduser): #DELATE USER
    users = User.objects.get(id=iduser)

    try:
        User.delete(users)
        print("Eliminado Correctamente")   
    except:
        print('No se puedo eliminar, revisa los datos')
        
    return redirect('usercrud')

@permission_required('auth.change_user')
def editUser(request, iduser): #EDIT USER
    euser = User.objects.get(id=iduser)
    data = {
    'form': CustomUserCreationForm(instance=euser) 
    }
    if request.method == 'POST':
        formulario_edit = CustomUserCreationForm(data=request.POST, instance=euser)
        if formulario_edit.is_valid:
            formulario_edit.save()
            print("usuario editado correctamente")
            return redirect('usercrud')
        else:
            data["form"] = formulario_edit;

    return render(request, 'registration/register.html', data)

def productcrud(request): #PRODUCT CRUD

    contacts = newProduct.objects.all()

    data = {
        'entity' : contacts
    }

    return render(request, 'product/productcrud.html', data)

@permission_required('core.add_newproduct')
def addproduct(request): #AGREGAR PRODUCTO

    product = addProduct()
    data = {'proForm' : product}
    if request.method == 'POST':
        product = addProduct(request.POST, files = request.FILES) 
        if product.is_valid():
            product.save()
            print("producto Creado Correctamente")
            return redirect('index')
        else:
            data["proForm"] = product;  
    else:
        print("No se puedo crear el producto, revisa los datos")
        
    return render(request, 'product/addproduct.html',data)

@permission_required('core.delete_newproduct')
def deleteProduct(request, idProduct): #DELATE PRODUCT
    product = newProduct.objects.get(id=idProduct)

    try:
        newProduct.delete(product)
        print("Eliminado Correctamente")   
    except:
        print('No se puedo eliminar, revisa los datos')
        
    return redirect('productcrud')

@permission_required('core.change_newproduct')
def editProduct(request, idProduct): #EDIT PRODUCT

    eproduct = newProduct.objects.get(id=idProduct)
    data = {
    'proForm': addProduct(instance=eproduct) 
    }
    if request.method == 'POST':
        formulario_edit = addProduct(data=request.POST, instance=eproduct, files = request.FILES)
        if formulario_edit.is_valid:
            formulario_edit.save()
            print("Producto editado correctamente")
            return redirect('productcrud')
        else:
            data["proForm"] = formulario_edit;

    return render(request, 'product/addproduct.html', data)

'''def adressOrder(request): #DIRECCION DEL PEDIDO

    data = {
        'formAdress' : addAdress()
    }
    formulario = addAdress(data=request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            print("te has registrado correctamente")
            return redirect('orderUser')
        else:
            data['formAdress'] = formulario
    else:
        print('error en el formulario')

    return render(request, 'order/adress.html', data)
'''
def orderUser(request): #ORDEN DE PEDIDO

    data = {
        'formOrder' : addOrder()
    }
    formulario = addOrder(data=request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            print("te has registrado correctamente")
            return redirect('index')
        else:
            data['formOrder'] = formulario
    else:
        print('error en el formulario')

    return render(request, 'order/orderuser.html', data)

def orderCrud(request):
    
    orderUser = order.objects.all()

    data = {
        'entity' : orderUser
    }

    return render(request, 'order/ordercrud.html', data)