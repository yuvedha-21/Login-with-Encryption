from userAuth.viewset import GetDataViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('',GetDataViewset)