from django.shortcuts import render
from django.http import  HttpResponseRedirect
from .forms import CatalogueForm
from django.contrib import messages
from django.urls import reverse_lazy


# def CatalogueFormView(request):
#     if request.method=="POST":
#         form=ProductsForm(request.POST)
#         if form.is_valid():
#             product=form.save()
#             messages.add_message(request, messages.SUCCESS, 'Registro exitoso')
#             return HttpResponseRedirect(reverse_lazy('CatalogueFormView', args=[provider.id]))
#     else:
#         form=ProductsForm()
#     return render(request, "CatalogueRegister.html", {'form':form})
