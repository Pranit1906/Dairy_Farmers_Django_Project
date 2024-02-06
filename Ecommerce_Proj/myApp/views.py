from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from django.urls import reverse
import razorpay
from django.db.models import Q 
from django.views import View
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from .models import Product,Customer,Cart,Payment,Order,Wishlist
from .forms import RegisterationForm,CustomerForm, CustomPassChangeForm, CustomPassResetForm,CustomeSetNewPassword
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

def Base(request):
    cart = Cart.objects.filter(user=request.user)
    count = cart.count()
    wishlist = Wishlist.objects.filter(user= request.user)
    wish_count = wishlist.count()
    orders = Order.objects.filter(user=request.user)
    order_count = orders.count() 
    # return HttpResponse('<h1 align="center">Welcome to Home Page<h1>')
    return render(request, 'base.html',locals())

def Home(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        count = cart.count()
        wishlist = Wishlist.objects.filter(user= request.user)
        wish_count = wishlist.count()
        orders = Order.objects.filter(user=request.user)
        order_count = orders.count() 
        return render(request, 'home.html',locals())
    else:
        return HttpResponseRedirect('/login/')

def About(request):
    cart = Cart.objects.filter(user=request.user)
    count = cart.count()
    wishlist = Wishlist.objects.filter(user= request.user)
    wish_count = wishlist.count()
    orders = Order.objects.filter(user=request.user)
    order_count = orders.count() 
    return render(request, 'about.html',locals())

def Contact(request):
    cart = Cart.objects.filter(user=request.user)
    count = cart.count()
    wishlist = Wishlist.objects.filter(user= request.user)
    wish_count = wishlist.count()
    orders = Order.objects.filter(user=request.user)
    order_count = orders.count() 
    return render(request, 'contact.html',locals())

def Search(request):
    cart = Cart.objects.filter(user=request.user)
    count = cart.count()
    wishlist = Wishlist.objects.filter(user= request.user)
    wish_count = wishlist.count()
    orders = Order.objects.filter(user=request.user)
    order_count = orders.count() 
    search = request.GET.get('search')
    product = Product.objects.filter(title__icontains = search)
    print('query:', product)
    if search == '':
        return HttpResponseRedirect('/home/')
    else:
        return render(request, 'search.html', locals())

def Logout(request):

    logout(request)
    return HttpResponseRedirect('/home/')


class RegistrationView(View):
    def get(self,request):
        form = RegisterationForm()
        return render(request,'user_register.html',locals())
    
    def post(self,request):
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! User Registered SuccessFully!!!')
            return HttpResponseRedirect('/login/')
        else:
            messages.warning(request, 'Invalid Input Data!! Please Try Again')
        return render(request, 'user_register.html',locals())    

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        try:
            username = request.POST.get('uname')
            password = request.POST.get('pass')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Congratulations! User Login SuccessFully!!!')
                return HttpResponseRedirect('/home/')
            else:
                messages.warning(request, 'Login Failed!! Please Try Again..!!')
        except Exception as E:
            messages.warning(request, f'An Error Occured :{str(E)}')
        return render(request, 'login.html', locals())

class UserPasswordChangeView(View):
    def get(self, request):
        cart = Cart.objects.filter(user=request.user)
        count = cart.count()
        wishlist = Wishlist.objects.filter(user= request.user)
        wish_count = wishlist.count()
        orders = Order.objects.filter(user=request.user)
        order_count = orders.count() 
        form = CustomPassChangeForm(request.user)
        return render(request, 'password_change.html',locals())

    def post(self, request):
        cart = Cart.objects.filter(user=request.user)
        count = cart.count()
        wishlist = Wishlist.objects.filter(user= request.user)
        wish_count = wishlist.count()
        orders = Order.objects.filter(user=request.user)
        order_count = orders.count() 
        form = CustomPassChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Changed SuccessFully!!!')
            return HttpResponseRedirect('/login/')
        else:
            messages.warning(request, 'Something Went wrong in changing Password!!')
        return render(request, 'password_change.html',locals())
    

class UserPassResetView(PasswordResetView):
    form_class = CustomPassResetForm
    template_name = 'password_reset.html'
    success_url = '/password_reset_done/'

class UserPassResetDone(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class UserPassResetConfirm(PasswordResetConfirmView):
    form_class = CustomeSetNewPassword
    template_name = 'password_reset_confirm.html'
    success_url = '/password_reset_complete/'   

class UserPasRestComplete(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

class ProfileCreateView(View):
    def get(self, request):
        cart = Cart.objects.filter(user=request.user)
        count = cart.count()
        wishlist = Wishlist.objects.filter(user= request.user)
        wish_count = wishlist.count()
        orders = Order.objects.filter(user=request.user)
        order_count = orders.count() 
        form = CustomerForm()
        return render(request, 'profile_create.html', locals())

    def post(self, request):
        try:
            cart = Cart.objects.filter(user=request.user)
            count = cart.count()
            wishlist = Wishlist.objects.filter(user= request.user)
            wish_count = wishlist.count()
            orders = Order.objects.filter(user=request.user)
            order_count = orders.count()
            form = CustomerForm(request.POST)
            if form.is_valid():
                user = request.user
                name = form.cleaned_data['name']
                locality = form.cleaned_data['locality']
                city = form.cleaned_data['city']
                mobile = form.cleaned_data['mobile']
                state = form.cleaned_data['state']
                pincode = form.cleaned_data['pincode']
                print("user=",user, "name=",name, "locality=",locality,
                       "city=", city, "mobile=",mobile, "state=",state, "pincode=",pincode)
                cust = Customer(user=user, name=name, locality=locality, city=city,
                         mobile=mobile, state=state, pincode=pincode)
                print("Cust:",cust)
                cust.save()
                messages.success(request,'User Profile Created SuccessFully!!!')
            else:
                messages.warning(request, 'Something went wrong in Profile Creation!!!')
        except Exception as E:
            messages.warning(request,f'An Error Occured :{str(E)}')
        return render(request, 'profile_create.html', locals())
        
def ProfileDisplay(request):
    cart = Cart.objects.filter(user=request.user)
    count = cart.count()
    wishlist = Wishlist.objects.filter(user= request.user)
    wish_count = wishlist.count()
    orders = Order.objects.filter(user=request.user)
    order_count = orders.count()
    profile = Customer.objects.filter(user = request.user)
    return render(request, 'profile_view.html',locals())


class ProfileUpdateView(View):
    def get(self,request, id):
        cart = Cart.objects.filter(user=request.user)
        count = cart.count()
        wishlist = Wishlist.objects.filter(user= request.user)
        wish_count = wishlist.count()
        orders = Order.objects.filter(user=request.user)
        order_count = orders.count()
        profile = Customer.objects.get(pk=id)
        form = CustomerForm(instance=profile)
        return render(request, 'profile_update.html',locals())

    def post(self, request,id):
        cart = Cart.objects.filter(user=request.user)
        count = cart.count()
        wishlist = Wishlist.objects.filter(user= request.user)
        wish_count = wishlist.count()
        orders = Order.objects.filter(user=request.user)
        order_count = orders.count()
        profile = Customer.objects.get(pk=id)
        form = CustomerForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'User Profile Updated SuccessFully!!')
            return HttpResponseRedirect('/profile_view/')
        else :
            messages.warning(request,'Something went wrong in Updation!!')
        return render(request, 'profile_update.html',locals())
    

class ProfileDeleteView(View):
    def get(self, request, id):
        cart = Cart.objects.filter(user=request.user)
        count = cart.count()
        wishlist = Wishlist.objects.filter(user= request.user)
        wish_count = wishlist.count()
        orders = Order.objects.filter(user=request.user)
        order_count = orders.count()
        customer = Customer.objects.get(pk=id)
        return render(request, 'profile_delete.html', locals())

    def post(self, request, id):
        customer = Customer.objects.get(pk=id)
        customer.delete()
        messages.success(request,'User Profile Deleted SuccessFully!!')
        return HttpResponseRedirect('/profile_view/')
    


class View_Prod(View):
    def get(self,request):
        cart = Cart.objects.filter(user=request.user)
        count = cart.count()
        wishlist = Wishlist.objects.filter(user= request.user)
        wish_count = wishlist.count()
        orders = Order.objects.filter(user=request.user)
        order_count = orders.count()
        product = Product.objects.all()
        return render(request, 'view_prod.html', locals())


class View_Prod_title(View):
    def get(self,request,val):
        cart = Cart.objects.filter(user=request.user)
        count = cart.count()
        wishlist = Wishlist.objects.filter(user= request.user)
        wish_count = wishlist.count()
        orders = Order.objects.filter(user=request.user)
        order_count = orders.count()
        if val == 'all':
            product = Product.objects.all()
        else:
            product = Product.objects.filter(category = val)
        # print("Product : ",product)
        return render(request, 'view_prod.html', locals())

class CategoryView(View):
    def get(self, request, val): # get method use to display and post method use to perform manipulations
        cart = Cart.objects.filter(user=request.user)
        count = cart.count()
        wishlist = Wishlist.objects.filter(user= request.user)
        wish_count = wishlist.count()
        orders = Order.objects.filter(user=request.user)
        order_count = orders.count()
        if val == 'all':
            product = Product.objects.all()
            title = Product.objects.all().values('title')
        else: 
            product = Product.objects.filter(category = val)
            title = Product.objects.filter(category = val).values('title')
        # print("Product : ",product,"title : ",title)
        return render(request, 'category.html', locals()) # locals()-->Return a dictionary containing the current scope's local variables.

class CategoryTitle(View):
    def get(self, request, val):
        cart = Cart.objects.filter(user=request.user)
        count = cart.count()
        wishlist = Wishlist.objects.filter(user= request.user)
        wish_count = wishlist.count()
        orders = Order.objects.filter(user=request.user)
        order_count = orders.count()    
        product= Product.objects.filter(title = val)
        title = Product.objects.filter(category = product[0].category).values('title')
        # print("Product : ",product,"title : ",title)
        return render(request, 'category.html', locals())

class ProductView(View):
    def get(self, request, id):
        cart = Cart.objects.filter(user=request.user)
        count = cart.count()
        wishlist = Wishlist.objects.filter(user= request.user)
        wish_count = wishlist.count()
        orders = Order.objects.filter(user=request.user)
        order_count = orders.count()
        prod_det = Product.objects.get(pk = id)
        wishlist = Wishlist.objects.filter(Q(product = prod_det)&Q(user = request.user))
        print("wish:",wishlist)
        return render(request, 'product-detail.html', locals())

# here we can store entire product into cart table even though it stores only product_id
    # we can access product details via product.id or product.details
def add_to_cart(request):
    cart = Cart.objects.filter(user=request.user)
    count = cart.count()
    wishlist = Wishlist.objects.filter(user= request.user)
    wish_count = wishlist.count()
    orders = Order.objects.filter(user=request.user)
    order_count = orders.count()    
    if request.method == 'POST':
        product_id = request.POST.get('pid')
        price = request.POST.get('dprice')
        product = Product.objects.get(id = product_id)
        print("id:",product_id,"Price:",price)
        item, data = Cart.objects.get_or_create(user = request.user, product = product, totalPrice = price)
        # here we can store entire product into cart table even though it stores only product_id
           # we can access product details via product.id or product.details
        print("product:",item.product, "product_id :", item.product.id,"Product_price:",item.product.discounted_price)
        ('Item:',item, "Data:",data)
        if not data:
            if not item.quantity:
                item.quantity+=1
            item.totalPrice = item.product.discounted_price * item.quantity
            print("Quantity:",item.quantity,"Total Price:",item.totalPrice)
            item.save()
            messages.success(request, 'Added To Cart SuccessFully!!')
        return HttpResponseRedirect('/view_cart/')
    

def view_cart(request):
    cart = Cart.objects.filter(user=request.user)
    count = cart.count()
    wishlist = Wishlist.objects.filter(user= request.user)
    wish_count = wishlist.count()
    orders = Order.objects.filter(user=request.user)
    order_count = orders.count()    
    amount = 0
    for list in cart:
        amount += list.totalPrice
    totalAmount = amount + 40
    return render(request, 'view_cart.html', locals())

def Inc_quantity(request):
    if request.method == 'POST':
        product_id = request.POST.get('pid')
        print("ProductID :",product_id)
        item,data = Cart.objects.get_or_create(product_id = product_id)
        print("ProductID :",product_id,"Item :",item)
        if not data:
            item.quantity += 1
            item.totalPrice = item.product.discounted_price * item.quantity
            item.save()
        return HttpResponseRedirect('/view_cart/')
    


def Decress_quantity(request):
    if request.method == 'POST':
        product_id = request.POST.get('pid')
        item, data = Cart.objects.get_or_create(product_id = product_id)
        if not data:
            item.quantity -= 1
            item.totalPrice -= item.product.discounted_price
            item.save()
            if item.quantity < 1:
                item.delete()
            
        return HttpResponseRedirect('/view_cart/')

def RemoveCart(request):
    if request.method == 'POST':
        product_id = request.POST.get('removeId')
        # product = Product.objects.get(id = product_id)
        # print("product:",product)
        item = Cart.objects.filter(product_id=product_id)
        print("item:",item)
        item.delete()
    return HttpResponseRedirect('/view_cart/')


class Checkout(View):
    def get(self, request):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user)
            count = cart.count()
            wishlist = Wishlist.objects.filter(user= request.user)
            wish_count = wishlist.count()
            orders = Order.objects.filter(user=request.user)
            order_count = orders.count()
            add = Customer.objects.filter(user= request.user)
            print("address:",add)
            cart_items = Cart.objects.filter(user = request.user)
            print("Cart_items:", cart_items)
            famount = 0
            for i in cart_items:
                famount += i.totalPrice
            totalAmount = famount + 40
            razorpay_amount = int(totalAmount * 100)
            client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_SECRET_KEY))
            data = { "amount": razorpay_amount, "currency": "INR", "receipt": "order_rcptid_11" }
            payment_res = client.order.create(data=data)
            print("payment_response:",payment_res)
            #payment_response: {'id': 'order_NVcuKrxoeKpDhz', 'entity': 'order', 'amount': 190, 'amount_paid': 0, 'amount_due': 190, 'currency': 'INR', 'receipt': 'order_rcptid_11', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1706792955}

            order_id = payment_res['id']
            order_status = payment_res['status']
            if order_status == 'created':
                payment = Payment(
                    user = request.user,
                    amount = totalAmount,
                    razorpay_order_id = order_id,
                    razorpay_payment_status = order_status)
                payment.save()   
                # print("payment details :",payment)     
            return render(request, 'checkout.html',locals())
        else:
            return HttpResponseRedirect('/login/')
    

def PaymentDone(request):
    if request.user.is_authenticated:
        # window.location.href = 'http://localhost:8000/payment_done?order_id=${response.razorpay_order_id}&payment_id={respsonse.razorpay_payment_id}&cust_id=${form.elements["custid"].value}'
        # we get all below Id's from above href link
        order_id = request.GET.get('order_id')
        payment_id = request.GET.get('payment_id')
        customer_id = request.GET.get('cust_id')
        print("PaymentDOne :  order_id =",order_id, "payment_id =",payment_id,"customer_id =",customer_id)
        customer = Customer.objects.get(id=customer_id)
        payment = Payment.objects.get(razorpay_order_id = order_id)
        payment.razorpay_payment_id = payment_id
        payment.paid = True
        payment.save()
        cart = Cart.objects.filter(user = request.user)
        status ='ACCEPTED'
        for item in cart:
            Order(user = request.user, customer = customer, product = item.product, quantity = item.quantity,status =status, totalPrice = item.totalPrice,payment = payment).save()
            cart.delete()
        o = Order.objects.filter(user= request.user)
        print("Order :",o)
        return HttpResponseRedirect('/order/')
    else:
        return HttpResponseRedirect('/login/')
    
def OrderPlaced(request):
    cart = Cart.objects.filter(user=request.user)
    count = cart.count()
    wishlist = Wishlist.objects.filter(user= request.user)
    wish_count = wishlist.count()
    order_placed = Order.objects.filter(user = request.user)
    order_count = order_placed.count()
    return render(request, 'orderPlaced.html', locals())

def WishList(request):
    wishlist = Wishlist.objects.filter(user= request.user)
    wish_count = wishlist.count()
    cart = Cart.objects.filter(user=request.user)
    count = cart.count()
    orders = Order.objects.filter(user=request.user)
    order_count = orders.count()
    print("wish:",wishlist)
    return render(request, 'wishlist.html', locals())

def AddToWishlist(request):
    if request.method =='POST':
        prod_id = request.POST.get('pid')
        product = get_object_or_404(Product ,id = prod_id)
        url = reverse('product-details', args=[product.id])
        Wishlist(user = request.user, product = product).save()
        return HttpResponseRedirect(url)
        # return HttpResponseRedirect('/home/')

def RemoveFromWishlist(request):
    if request.method =='POST':
        prod_id = request.POST.get('pid')
        product = get_object_or_404(Product ,id = prod_id)
        wish =  Wishlist.objects.filter(Q(user = request.user)& Q(product = product))
        wish.delete()
        # return HttpResponseRedirect('/home/')
        return HttpResponseRedirect(reverse('product-details', args=[product.id]))