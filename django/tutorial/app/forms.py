from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'pt-2 text-xl'}),
        max_length=100,
    )
    email = forms.EmailField()
    message = forms.CharField(
        widget=forms.Textarea
    )

   # quando fate form.is_valid() django esegue prima tutti i metodi clean con nome
   # ovvero quelli che hanno clean_<nome_campo> nel nome, poi esegue il clean() principale.
   # Se uno di questi metodi: clean_<nome_campo>, non passa, dentro al cleaned_data di clean()
   # non troverete il campo che ha fallito la validazione.

    def clean(self):
        cleaned_data = super().clean()

        if 'ciao' in self.cleaned_data['message'] and '@' not in self.cleaned_data['email']:
            raise forms.ValidationError('Nell\'email ci vuole la @ e non puoi scrivere ciao nel messaggio.')
        
        return cleaned_data
    

    def clean_name(self):
        if '@' in self.cleaned_data['name']:
            raise forms.ValidationError('La @ non è permessa nel nome.')
        
        return self.cleaned_data['name']
    

    def send_email(self):
        print(self.cleaned_data['name'], self.cleaned_data['email'], self.cleaned_data['message'])
