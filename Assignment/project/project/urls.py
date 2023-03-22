from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from myapp.views import InvoiceViewSet

router = routers.DefaultRouter()
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
