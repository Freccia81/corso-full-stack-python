from django.shortcuts import render, redirect
from .models import User
from .forms import ContactForm


def index(request):
    utenti = User.objects.all()

    utente_singolo = User.objects.get(id=1)

    utente_filtrato = list(User.objects.filter(age__gt=20).filter(hobby='pesca').only('name'))

    utente_esempio = User.objects.raw('SELECT * FROM app_user WHERE age > 20')

    # SELECT * FROM users
    # WHERE age >= 18
    # WHERE hobby IS NOT NULL;
    test = User.objects.get_adult_users().has_hobby()

    return render(request, 'index.html', {'test': test, 'users': utenti, 'singolo': utente_singolo, 'filtrato': utente_filtrato, 'utenti_raw': utente_esempio})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            # invia email
            form.send_email()

            return redirect('contact')

    return render(request, 'contact.html', {'form': ContactForm()})


def posts(request):
    # prefetch_related precarica le relazioni direttamente con una query sql
    users = User.objects.prefetch_related('posts')

    return render(request, 'posts.html', {'users': users})
