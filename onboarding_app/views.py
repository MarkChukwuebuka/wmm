from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from formtools.wizard.views import SessionWizardView
from .models import Seller
from django import forms
from django.core.files.storage import FileSystemStorage
import os
from django.core.validators import EmailValidator
from django.conf import settings



class SellerForm1(forms.Form):
    name_of_store = forms.CharField(max_length=100)
    

class SellerForm2(forms.Form):
    balance = forms.IntegerField()


class SellerForm3(forms.Form):
    price = forms.IntegerField()


class SellerForm4(forms.Form):
    NETWORK_CHOICES = [
        ('Polygon', 'Polygon'),
        ('Ethereum', 'Ethereum'),
    ]

    network = forms.ChoiceField(choices=NETWORK_CHOICES)

class SellerForm5(forms.Form):
    wallet_address = forms.CharField(max_length=100)


class SellerForm6(forms.Form):
    email = forms.EmailField(max_length=100, validators=[EmailValidator(message='Please enter a valid email address.')])
    

class SellerWizard(SessionWizardView):
    template_name = 'forms/step1.html'
    form_list = [SellerForm1, SellerForm2, SellerForm3, SellerForm4, SellerForm5, SellerForm6]
    file_storage = FileSystemStorage(location=os.path.join(settings.BASE_DIR, 'tmp'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Onboarding Process'
        return context

    def done(self, form_list, **kwargs):
        form_data = {}
        for form in form_list:
            form_data.update(form.cleaned_data)
        seller = Seller.objects.create(**form_data)
        return render(self.request, 'done.html', {'seller': seller})


def results(request):
    context = {
        'sellers' : Seller.objects.all(),
        'title' : 'Results'
    }
    return render(request, 'results.html', context)