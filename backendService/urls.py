from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.Homepage, name="home"),
    path("mypage/", views.customerHomepage, name="mypage"),
    path("customerdata/", views.customerData, name = "customerdata"),
    path("templateone/", views.templateOne, name="templateone"),
    path("templatetwo/", views.templateTwo, name="templatetwo"),
    path("templatethree/", views.templateThree, name="templatethree"),
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path("templateselection/", views.Templateselection, name="templateselection"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
