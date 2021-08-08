from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = "login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home_view, name='home'),
    path('scheme-create/', views.scheme_create, name='scheme-create'),
    path('do/<int:id>/', views.do, name='do'),
    path('edit/<id>/', views.SchemeEditView.as_view(), name='scheme-edit'),
    path('delete/<int:id>/', views.SchemeDeleteView.as_view(), name='scheme-delete'),
    path('celery-progress/', include('celery_progress.urls')),
    path('generate_data', views.generate_view, name='generate_data'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
