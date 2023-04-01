from django.shortcuts import render

# Create your views here.
def contactus(request):
    template = 'contactus/contactus.html'
    
    return render(request, template)   