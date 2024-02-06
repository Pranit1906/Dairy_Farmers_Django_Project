from django.urls import path
from . import views

# username :- Ecommerce_Proj password :- admin@123
urlpatterns = [
    path('base/',views.Base, name='base'),
    path('home/',views.Home, name='home'),
    path('about/',views.About, name='about'),
    path('contact/',views.Contact, name='contact'),
    path('view/', views.View_Prod.as_view(), name='view'),
    path('search/', views.Search, name='search'),

    # Products Urls
    path('category/<slug:val>/',views.CategoryView.as_view(), name='category'),
    path('category/<val>/',views.CategoryTitle.as_view(), name='category-title'),
    path('view/<val>/',views.View_Prod_title.as_view(), name='view-title'),
    path('product-details/<int:id>/', views.ProductView.as_view(), name='product-details'),

    # Profile Urls
    path('profile_create/', views.ProfileCreateView.as_view(), name='profile_create'),
    path('profile_view/',views.ProfileDisplay, name='profile_view'),
    path('profile_update/<int:id>/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile_delete/<int:id>/', views.ProfileDeleteView.as_view(), name='profile_delete'),

    # login Urls
    path('register/',views.RegistrationView.as_view(), name='register'),
    path('login/',views.LoginView.as_view(), name='login'),
    path('logout/', views.Logout, name='logout'),

    # password_Reset_Change Urls
    path('password_change/',views.UserPasswordChangeView.as_view(), name='password_change'),
    path('password_reset/', views.UserPassResetView.as_view(), name='password_reset'),
    path('password_reset_done/', views.UserPassResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.UserPassResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', views.UserPasRestComplete.as_view(), name='password_reset_complete'),

    # Cart Urls
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/',views.view_cart, name='view_cart'),
    path('remove_cart/', views.RemoveCart, name='remove_cart'),
    path('Increase_quantity', views.Inc_quantity, name='Increase_quantity'),
    path('Decrease_quantity', views.Decress_quantity, name='Decrease_quantity'),

    # Checkout and Payment Urls
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('payment_done/', views.PaymentDone, name='payment_done'),
    path('order/' ,views.OrderPlaced, name='order'),

    # Wishlist Urls
    path('wishlist/', views.WishList, name='wishlist'),
    path('addtowishlist/', views.AddToWishlist, name='add_to_wishlist'),
    path('removefromwishlist/', views.RemoveFromWishlist, name='remove_from_wishlist')

]