from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'eng_software/index.html')

def curso(request):
    return render(request, 'eng_software/curso.html')

def processo_seletivo(request):
    return render(request, 'eng_software/processo_seletivo.html')

def publico_alvo(request):
    return render(request, 'eng_software/publico_alvo.html')

def investimento(request):
    return render(request, 'eng_software/investimento.html')

def onde_fazer(request):
    return render(request, 'eng_software/onde_fazer.html')
