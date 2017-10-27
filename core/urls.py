from django.conf.urls import url
from core.views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^alunos$', ListaAlunos.as_view(), name='ListaAlunos'),
    url(r'^user/(?P<user_id>\d+)/$', alunoInfo, name='aluno_url'),
    url(r'^disciplinas$', ListaDisciplinas.as_view(), name='ListaDisciplinas'),
    url(r'^secretarias$', ListaSecretarias.as_view(), name='ListaSecretarias'),
    url(r'^pdf/(?P<user_id>\d+)/$', some_view, name='some_view'),
    #url(r'^admin/core/aluno/(?P<user_id>\d+)/change/$', admin.site.root, name='ListaProfessores'),
]