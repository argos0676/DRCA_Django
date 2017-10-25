from django.conf.urls import url
from core.views import home, alunos, alunoInfo, disciplinas

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^alunos$', alunos, name='alunos'),
    url(r'^user/(?P<user_id>\d+)/$', alunoInfo, name='aluno_url'),
    url(r'^disciplinas$', disciplinas, name='disciplinas'),
]