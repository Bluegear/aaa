from django.contrib.auth.models import User
from django.db import transaction, IntegrityError
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View

from mcweb.forms import SignUpForm
from mcweb.models import Merchant


class RegistrationView(View):
    def get(self, request):
        """
        Return signup form.
        """
        form = SignUpForm()
        return render(request, 'mcweb/signup.html', {'form': form})

    @transaction.atomic
    def post(self,request):
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            try:
                user = User.objects.create_user(form_data['merchant_user_name'],form_data['merchant_email'],form_data['merchant_password'])
                merchant = Merchant.objects.create(user=user,display_name=form_data['merchant_name'],redirect_url=form_data['merchant_redirect_url'],address=form_data['merchant_address'])
                user.save()
                merchant.save()
            except IntegrityError:
                form._errors['merchant_user_name'] = ["Username already used"]
                return  render(request, 'mcweb/signup.html', {'form': form})
        else :
            return  render(request, 'mcweb/signup.html', {'form': form})
        return render(request, 'mcweb/signup_complete.html', {'form': form})
