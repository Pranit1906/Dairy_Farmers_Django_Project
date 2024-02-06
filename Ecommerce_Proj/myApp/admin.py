from django.contrib import admin
from .models import Product,Customer,Cart,Payment,Order,Wishlist
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','discounted_price','category')
    search_fields = ('title','category',)
    list_filter = ('category',)

admin.site.register(Product, ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','user','name', 'city', 'state','locality', 'pincode')
    search_fields = ('user','name','state','locality',)
    list_filter = ('state', 'city',)

admin.site.register(Customer, CustomerAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'product', 'quantity', 'totalPrice')
    search_fields = ('user', 'product')
    list_filter = ('user', 'quantity', 'totalPrice')

admin.site.register(Cart, CartAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid')
    search_fields = ('razorpay_order_id','razorpay_payment_status','razorpay_payment_id')
    list_filter = ('razorpay_payment_status','paid')

admin.site.register(Payment, PaymentAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'customer','product','quantity','status','ordered_date','payment','totalPrice')
    search_fields = ('product','ordered_date','payment')
    list_filter = ('ordered_date','totalPrice','status')

admin.site.register(Order, OrderAdmin)

class WishListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','product')
    search_fields = ('product',)
    list_filter = ('user','product')

admin.site.register(Wishlist, WishListAdmin)