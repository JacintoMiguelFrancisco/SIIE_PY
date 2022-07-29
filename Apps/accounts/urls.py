# accounts/urls.py
from django.urls import path
# View
from .views import login_view, logout_view, signup, update_profile

urlpatterns = [ 
    # Mantenimiento de usuarios
    # Login
    path(
        route='login/',
        view=login_view,
        name='login'
    ),
    # Logout
    path(
        route='logout/',
        view=logout_view,
        name='logout'
    ),
    # Singnup
    path(
        route='signup/',
        view=signup,
        name='signup'
    ),
    # Update
    path(
        route='me/profile/',
        view=update_profile,
        name='update'
    )

]