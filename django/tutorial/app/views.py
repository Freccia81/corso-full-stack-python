from django.shortcuts import render, redirect
from .forms import ContactForm


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            # invia email
            form.send_email()

            return redirect('contact')
    else:   
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
