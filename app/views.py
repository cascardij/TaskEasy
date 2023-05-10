from django.http import HttpResponse

def index(request):
    return HttpResponse("O TaskEasy é um projeto de gerenciamento de tarefas que oferece opções personalizáveis ​​para uso pessoal, trabalho e escolar. Com recursos como lembretes, metas e objetivos a curto e longo prazo,")

# Create your views here.
