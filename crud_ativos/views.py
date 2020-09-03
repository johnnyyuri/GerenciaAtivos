from django.shortcuts import render, redirect
from .form import AtivoForm, ColabForm
from django.http import HttpResponse
from .models import Ativo, Colaborador

def listagem(request):
    data = {}
    data['ativos'] = Ativo.objects.all()
    data['colabs'] = Colaborador.objects.all()
    return render(request, 'crud_ativos/listagem.html', data)

def new_ativo(request):
    data = {}
    form = AtivoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_list')
    data['form'] = form
    return render(request, 'crud_ativos/nuativo.html', data)

def new_colab(request):
    data = {}
    form = ColabForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_list')
    data['form'] = form
    return render(request, 'crud_ativos/nucolab.html', data)

def updateativo(request, pk):
    data = {}
    ativo = Ativo.objects.get(pk=pk)
    form = AtivoForm(request.POST or None, instance=ativo)
    if form.is_valid():
        form.save()
        return redirect('url_list')
    data['form'] = form
    data['ativo'] = ativo
    return render(request, 'crud_ativos/nuativo.html', data)

def updatecolab(request, pk):
    data = {}
    colaborador = Colaborador.objects.get(pk=pk)
    form = ColabForm(request.POST or None, instance=colaborador)
    if form.is_valid():
        form.save()
        return redirect('url_list')
    data['form'] = form
    data['colaborador'] = colaborador
    return render(request, 'crud_ativos/nucolab.html', data)

def deleteativo(request, pk):
    ativo = Ativo.objects.get(pk=pk)
    ativo.delete()
    return redirect('url_list')

def deletecolab(request, pk):
    colaborador = Colaborador.objects.get(pk=pk)
    colaborador.delete()
    return redirect('url_list')