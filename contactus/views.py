from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contactus(request):
    form = ContactForm()
    template = 'contactus/contactus.html'

    context = {
        'form': form        
    }
    
    return render(request, template, context)   