from django.urls import path
from . import views


urlpatterns = [
    # Rutas de la aplicación User
    path("login/", views.MyTokenObtainPairView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("put/", views.putUser),
    path("put/<int:pk>/", views.putUserSolo),
    path("image/", views.uploadImage),
    path("userProfile/", views.getUserProfile),
    path("<int:pk>/", views.getSoloUser),
    path("getUsers/", views.getUsers),
    path("delete/<int:pk>/", views.deleteUser),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
