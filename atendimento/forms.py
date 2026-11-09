from django import forms
 
class AtendimentoInicialForm(forms.Form):
    nome = forms.CharField(
        label="Nome do solicitante",
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-lg",
            "placeholder": "Digite o nome completo"
        })
    )
    telefone = forms.CharField(
        label="Telefone",
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-lg",
            "placeholder": "(00) 00000-0000"
        })
    )
    estado = forms.CharField(
        label="Estado",
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-lg",
            "placeholder": "Ex.: São Paulo"
        })
    )
    endereco = forms.CharField(
        label="Endereço",
        max_length=255,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-lg",
            "placeholder": "Rua, número, bairro..."
        })
    )
    referencia = forms.CharField(
        label="Ponto de referência",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 4,
            "placeholder": "Ex.: Em frente ao mercado..."
        })
    )
 
class AtendimentoNaoEmergencialForm(forms.Form):
    TIPO_SOLICITACAO_CHOICES = [
        ('Contrato', 'Contrato (Dúvidas, alterações ou renovações)'),
        ('Pagamento', 'Pagamento (Pendências, cobranças ou comprovantes)'),
        ('Outros', 'Outros (Demais solicitações)'),
    ]
 
    nome = forms.CharField(
        label="Nome completo",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"})
    )
    telefone = forms.CharField(
        label="Telefone de contato",
        max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"})
    )
    email = forms.EmailField(
        label="E-mail de contato",
        widget=forms.EmailInput(attrs={"class": "form-control form-control-lg"})
    )
    endereco = forms.CharField(
        label="Endereço / Localidade",
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"})
    )
    tipo_solicitacao = forms.ChoiceField(
        label="Tipo de solicitação",
        choices=TIPO_SOLICITACAO_CHOICES,
        widget=forms.Select(attrs={"class": "form-select form-select-lg"})
    )
    descricao = forms.CharField(
        label="Descrição detalhada",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5})
    )