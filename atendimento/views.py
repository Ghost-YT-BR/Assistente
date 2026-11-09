from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AtendimentoInicialForm, AtendimentoNaoEmergencialForm
from .perguntas import PERGUNTAS
from .models import Ocorrencia
 
@login_required
def home(request):
    return render(request, "atendimento/home.html")
 
@login_required
def emergencial(request):
    if request.method == "POST":
        form = AtendimentoInicialForm(request.POST)
        if form.is_valid():
            request.session['dados_iniciais'] = form.cleaned_data
            return redirect('tipo_ocorrencia')
    else:
        form = AtendimentoInicialForm()
    return render(request, "atendimento/emergencial.html", {"form": form})
 
@login_required
def tipo_ocorrencia(request):
    return render(request, "atendimento/tipo_ocorrencia.html", {"tipos": PERGUNTAS.keys()})
 
@login_required
def questionario(request, tipo_nome):
    perguntas_lista = PERGUNTAS.get(tipo_nome, [])
    if request.method == "POST":
        respostas = {}
        for i, pergunta in enumerate(perguntas_lista, start=1):
            respostas[pergunta] = request.POST.get(f"pergunta_{i}", "")
        request.session['tipo_ocorrencia'] = tipo_nome
        request.session['respostas'] = respostas
        return redirect('resumo')
    return render(request, "atendimento/questionario.html", {"tipo": tipo_nome, "perguntas": perguntas_lista})
 
@login_required
def resumo(request):
    dados_iniciais = request.session.get('dados_iniciais', {})
    tipo_ocorrencia = request.session.get('tipo_ocorrencia', '')
    respostas = request.session.get('respostas', {})
    if request.method == "POST":
        nova_ocorrencia = Ocorrencia.objects.create(
            nome_solicitante=dados_iniciais.get('nome', ''),
            telefone=dados_iniciais.get('telefone', ''),
            estado=dados_iniciais.get('estado', ''),
            endereco=dados_iniciais.get('endereco', ''),
            referencia=dados_iniciais.get('referencia', ''),
            tipo_atendimento="EM",
            tipo_ocorrencia=tipo_ocorrencia,
            respostas_questionario=respostas
        )
        request.session.flush()
        return redirect('procedimentos', ocorrencia_id=nova_ocorrencia.id)
    return render(request, "atendimento/resumo.html", {'dados_iniciais': dados_iniciais, 'tipo_ocorrencia': tipo_ocorrencia, 'respostas': respostas})
 
@login_required
def procedimentos(request, ocorrencia_id):
    ocorrencia = Ocorrencia.objects.get(id=ocorrencia_id)
    return render(request, "atendimento/procedimentos.html", {"ocorrencia": ocorrencia})
 
@login_required
def nao_emergencial(request):
    if request.method == "POST":
        form = AtendimentoNaoEmergencialForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            nova_ocorrencia = Ocorrencia.objects.create(
                nome_solicitante=dados['nome'],
                telefone=dados['telefone'],
                endereco=dados['endereco'],
                tipo_atendimento="NE",
                tipo_ocorrencia=dados['tipo_solicitacao'],
                respostas_questionario={"E-mail": dados['email'], "Descrição": dados['descricao']}
            )
            return redirect('procedimentos_ne', ocorrencia_id=nova_ocorrencia.id)
    else:
        form = AtendimentoNaoEmergencialForm()
    return render(request, "atendimento/nao_emergencial.html", {"form": form})
 
@login_required
def procedimentos_ne(request, ocorrencia_id):
    ocorrencia = Ocorrencia.objects.get(id=ocorrencia_id)
    return render(request, "atendimento/procedimentos_ne.html", {"ocorrencia": ocorrencia})