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
    else:   
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def posts(request):
    # prefetch_related precarica le relazioni direttamente con una query sql
    users = User.objects.prefetch_related('posts')

    return render(request, 'posts.html', {'users': users})


def create_user(request):

    # primo modo per fare una create
    new_user = User.objects.create(
        name='giovanni',
        surname='pippo',
        age=34,
        hobby='disco'
    )

    # # secondo modo per fare una create
    # new_user = User()
    # new_user.name='giovanni'
    # new_user.surname='pippo'
    # new_user.age=34
    # new_user.hobby='disco'

    # new_user.save()

    # terzo modo per fare una create
    # user3 = User.objects.get_or_create(
    #     name='leonardo', 
    #     surname='mazzoleni',
    #     defaults={'name': 'simone', 'surname': 'gigino', 'age': 34, 'hobby': 'ciao'}
    # )

    return render(request, 'users/create.html', {'user': new_user})


def update_user(request):

    # User.objects.update_or_create(
    #     name='leonardo', 
    #     surname='mazzoleni',
    #     defaults={'name': 'simone', 'age': 34, 'hobby': 'ciao'}
    # )

    # primo modo per fare una update
    user = User.objects.filter(id=1)

    user.update(
        name='leonardo', 
        surname='mazzoleni',
    )

    # # secondo modo per fare una update
    # user2 = User.objects.get(id=2)

    # user2.name = 'gianni'
    # user2.surname = 'previtali'
    # user2.save()

    return render(request, 'users/update.html', {'user': user})
