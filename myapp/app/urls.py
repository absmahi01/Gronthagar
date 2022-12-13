
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from app.views import (
    SendEmailToResetPassword,
    ResetPasswordConfirm
)

urlpatterns = [
    path('',views.home),
    path('contact/',views.Contact,name="contact"),
    path('about/',views.about,name="about"),
    path("category/<slug:value>",views.CategoryView.as_view(),name="category"),
    # path("category-title/<value>",views.CategoryTitle.as_view(),name="category-title"),
    path("product-detail/<int:pk>",views.ProductDetail.as_view(),name="product-detail"),
    path('profile/',views.ProfileView.as_view(), name='profile'),
    path('address/',views.address, name='address'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),
    
    
    #login
    path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html',
    authentication_form=LoginForm),name='login'),
   
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',
    form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(
    template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),

    #password reset
    
    # path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),
    # name='password_reset_complete.html'),

    path('password_reset/', SendEmailToResetPassword.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', ResetPasswordConfirm.as_view(), name='password_reset_confirm'),
    #Cart
    path('add-to-cart/',views.add_to_cart,name="add-to-cart"),
    path('cart/',views.show_cart,name="showcart"),
    path('checkout/',views.checkout.as_view(),name='checkout'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    path('orders/',views.orders,name='orders'),

    #search
    path('search/',views.search,name='search'),

    #payment
    path('paymentdone/',views.payment_done,name='paymentdone'),
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)