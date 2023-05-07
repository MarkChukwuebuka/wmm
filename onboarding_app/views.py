from django import forms
from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.core.validators import EmailValidator
from formtools.wizard.views import SessionWizardView
from django.core.exceptions import SuspiciousOperation
from django.utils.crypto import get_random_string
from django.views.generic.edit import FormView
from django.forms.models import model_to_dict
from .models import Seller
from django.contrib import messages



def multistepform(request):
    if request.method == "POST":
    
        name=request.POST.get("name")
        balance=request.POST.get("balance")
        price=request.POST.get("price")
        network=request.POST.get("network")
        wallet_address=request.POST.get("wallet_address")
        email=request.POST.get("email")

        if balance == "":
            balance = 0

        if price == "":
            price = 0
        seller = Seller()
        seller.name_of_store = name
        seller.balance=balance
        seller.price=price
        seller.network=network
        seller.wallet_address=wallet_address
        seller.email=email
        seller.save()
        messages.success(request,"Data Save Successfully")
        return render(request, 'done.html')
        

    return render(request, 'multistepform.html')






# class Step1Form(forms.Form):
#     name_of_store = forms.CharField()
    
# class Step2Form(forms.Form):
#     balance = forms.IntegerField()
    
# class Step3Form(forms.Form):
#     price = forms.IntegerField()
    
# class Step4Form(forms.Form):
#     NETWORK_CHOICES = [
#         ('Polygon', 'Polygon'),
#         ('Ethereum', 'Ethereum'),
#     ]

#     network = forms.ChoiceField(choices=NETWORK_CHOICES)
    
# class Step5Form(forms.Form):
#     wallet_address = forms.CharField()

# class Step6Form(forms.Form):
#     email = forms.EmailField(max_length=100, validators=[EmailValidator(message='Please enter a valid email address.')])
    
# FORMS = [('step1', Step1Form),
#          ('step2', Step2Form),
#          ('step3', Step3Form),
#          ('step4', Step4Form),
#          ('step5', Step5Form),
#          ('step6', Step6Form)]

# TEMPLATES = {'step1': 'step1.html',
#              'step2': 'step2.html',
#              'step3': 'step3.html',
#              'step4': 'step4.html',
#              'step5': 'step5.html',
#              'step6': 'step6.html'}

# class SellerWizardView(FormView):
#     template_name = 'forms/wizard.html'
#     form_class = Step1Form
#     success_url = reverse_lazy('results')

#     def dispatch(self, request, *args, **kwargs):
#         self.entry_key = request.session.get('entry_key')
#         self.entry = None
#         if self.entry_key:
#             try:
#                 self.entry = Seller.objects.get(key=self.entry_key)
#             except Seller.DoesNotExist:
#                 pass
#         if not self.entry:
#             # create a new entry if none exists
#             self.entry_key = get_random_string(length=32)
#             self.entry = Seller.objects.create(key=self.entry_key)
#             # store the entry key in the session
#             request.session['entry_key'] = self.entry_key
#         return super().dispatch(request, *args, **kwargs)

#     def get_form_class(self):
#         # return the form class for the current step
#         return FORMS[self.steps.current][1]

#     def get_form_initial(self, step):
#         # return the initial values for the form
#         if self.entry and step in self.entry.data:
#             return self.entry.data[step]
#         return self.initial_dict.get(step, {})

#     def get_form(self, step=None, data=None, files=None):
#         # return the form for the current step
#         form = super().get_form(step, data, files)
#         form.fields['entry_key'].initial = self.entry_key
#         return form

#     def get_template_names(self):
#         # return the template for the current step
#         return [TEMPLATES[self.steps.current]]

#     def done(self, form_list, **kwargs):
#         # handle form submission
#         if self.entry:
#             # update the form data for the current entry
#             for form in form_list:
#                 step_data = model_to_dict(form.cleaned_data)
#                 step = form.prefix
#                 self.entry.data[step] = step_data
#             self.entry.save()
#         return super().done(form_list, **kwargs)

#     def process_step(self, form):
#         # validate the form data and return the cleaned data
#         if form.is_valid():
#             return form.cleaned_data
#         else:
#             raise SuspiciousOperation("Invalid form submission")

#     def get_success_url(self):
#         return reverse_lazy('results', kwargs={'entry_key': self.entry_key})








































# class SellerForm1(forms.Form):
#     name_of_store = forms.CharField(max_length=100)
    

# class SellerForm2(forms.Form):
#     balance = forms.IntegerField()


# class SellerForm3(forms.Form):
#     price = forms.IntegerField()


# class SellerForm4(forms.Form):
#     NETWORK_CHOICES = [
#         ('Polygon', 'Polygon'),
#         ('Ethereum', 'Ethereum'),
#     ]

#     network = forms.ChoiceField(choices=NETWORK_CHOICES)

# class SellerForm5(forms.Form):
#     wallet_address = forms.CharField(max_length=100)


# class SellerForm6(forms.Form):
#     email = forms.EmailField(max_length=100, validators=[EmailValidator(message='Please enter a valid email address.')])
    

# class SellerWizard(SessionWizardView):
#     template_name = 'forms/step1.html'
#     form_list = [SellerForm1, SellerForm2, SellerForm3, SellerForm4, SellerForm5, SellerForm6]
#     file_storage = FileSystemStorage(location=os.path.join(settings.BASE_DIR, 'tmp'))

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Onboarding Process'
#         return context

#     def done(self, form_list, **kwargs):
#         form_data = {}
#         for form in form_list:
#             form_data.update(form.cleaned_data)
#         seller = Seller.objects.create(**form_data)
#         return render(self.request, 'done.html', {'seller': seller})


def results(request):
    context = {
        'sellers' : Seller.objects.all(),
        'title' : 'Results'
    }
    return render(request, 'results.html', context)