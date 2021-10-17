
from django.contrib import admin
from django.urls import path, include
from either import views as eitherViews
from work import views as workViews
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', eitherViews.home, name = 'home'),
    path('about', eitherViews.about, name = 'about'),
    path('registration/', eitherViews.register, name = 'registration'),
    path('login/',authViews.LoginView.as_view(template_name='either/login.html') , name = 'login'),
    path('profile/', eitherViews.profile, name = 'profile'),
    path('profile/favorites', eitherViews.CreateFavoriteView.as_view(), name = 'favorites'),
    path('exit/',authViews.LogoutView.as_view(template_name='either/exit.html') , name = 'exit'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
