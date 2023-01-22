from django.shortcuts import render, HttpResponseRedirect
from myapp.forms import ChuvasForm
from myapp.models import Chuvas

def home(request):
  return render(request, 'home.html')

def crud(request):
  if not request.user.is_authenticated:
    return HttpResponseRedirect('/account/login')

  listatotal = Chuvas.objects.all()
  return render(request, 'crud.html', {'listatotal': listatotal})

def create(request):
  if not request.user.is_authenticated:
    return HttpResponseRedirect('/account/login')

  if request.method == 'POST':
    form = ChuvasForm(request.POST)
    if form.is_valid():
      form.save()
    return HttpResponseRedirect('/crud')
  else:
    return render(request, 'form.html', {'form': ChuvasForm(), 'title': 'Adicionar registro'})

def update(request, id):
  if not request.user.is_authenticated:
    return HttpResponseRedirect('/account/login')

  if request.method == 'POST':
    registro_a_atualizar = Chuvas.objects.get(pk=id)
    editando = ChuvasForm(request.POST, instance=registro_a_atualizar)
    if editando.is_valid():
      editando.save()
    return HttpResponseRedirect('/crud')
  else:
    registro_a_atualizar = Chuvas.objects.get(pk=id)
    editando = ChuvasForm(instance=registro_a_atualizar)
  return render(request, 'form.html', {'form': editando, 'title': 'Editar registro'})

def listagem(request):
  listatotal = Chuvas.objects.all()
  return render(request, 'listagem.html', {'listatotal': listatotal})

def consulta(request):
  buscar = request.GET.get('busca')
  if buscar:
    resultados = Chuvas.objects.filter(data__icontains=buscar)
    return render(request, 'consulta.html', {'mostrar': True, 'resultados': resultados})
  return render(request, 'consulta.html', {'mostrar': False})

def delete(request, id):
  if not request.user.is_authenticated:
    return HttpResponseRedirect('/account/login')

  registro_a_apagar = Chuvas.objects.get(pk=id)
  registro_a_apagar.delete()
  return HttpResponseRedirect('/crud')

def sobre(request):
  return render(request, 'sobre.html')