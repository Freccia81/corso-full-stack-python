from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput,
        max_length=100,
    )
    email = forms.EmailField()
    message = forms.CharField(
        widget=forms.Textarea
    )

    def send_email(self):
        print(self.cleaned_data['name'], self.cleaned_data['email'], self.cleaned_data['message'])
