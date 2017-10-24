from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^alunos$', views.alunos),
    url(r'^user/(?P<user_id>\d+)/$', "core.views.alunoInfo", name='aluno_url'),
]