from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contactus/success.html')
    
    
    form = ContactForm()
    template = 'contactus/contactus.html'

    context = {
        'form': form        
    }
    
    return render(request, template, context)   