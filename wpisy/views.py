from django.shortcuts import render, redirect
from . models import Wpis
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def wpisy_list(request):
    wpisy = Wpis.objects.all().order_by('date')
    return render(request, 'wpisy/wpisy_list.html', {'wpisy': wpisy} )

def wpisy_detail(request, slug):
    #return HttpResponse(slug)
    wpis = Wpis.objects.get(slug=slug)
    return render(request, 'wpisy/wpisy_detail.html', {'wpis': wpis})


@login_required(login_url= '/konta/logowanie/')
def wpis_nowy(request):
    if request.method == 'POST':
        form = forms.NowyWpis(request.POST, request.FILES)
        if form.is_valid():
            # zapisz wpis na bloga do bazy danych
            instancja = form.save(commit=False)
            instancja.autor = request.user
            instancja.save()
            return redirect('wpisy:list')
    else:
        form =  forms.NowyWpis()
    form = forms.NowyWpis()
    return render(request, 'wpisy/wpis_nowy.html', { 'form':form })