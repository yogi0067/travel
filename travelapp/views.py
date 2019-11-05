from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.

def home(request):
    destobj1 = Destination()
    destobj1.destName= 'Chandigarh'
    destobj1.destPrice= 1000
    destobj1.destDesc= 'Janat'
    destobj1.destImage= 'destination_1.jpg'
    destobj1.destOffer= True

    destobj2 = Destination()
    destobj2.destName= 'Bathinda'
    destobj2.destPrice= 1000
    destobj2.destDesc= 'City of lakes '
    destobj2.destImage= 'destination_2.jpg'
    destobj2.destOffer= False

    destobj3 = Destination()
    destobj3.destName= 'Patiala'
    destobj3.destPrice= 1000
    destobj3.destDesc= 'Royal City'
    destobj3.destImage= 'destination_3.jpg'
    destobj3.destOffer= True

    destobj =[destobj1, destobj2, destobj3]
    return render(request,'index.html', {'dest1': destobj})
