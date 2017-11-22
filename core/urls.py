from django.conf.urls import url
from core.views import *
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^favicon.ico$',
    #     RedirectView.as_view( # the redirecting function
    #         url=staticfiles_storage.url('favicon.ico'), # converts the static directory + our favicon into a URL
    #         # in my case, the result would be http://www.tumblingprogrammer.com/static/img/favicon.ico
    #     ),
    #     name="favicon" # name of our view
    # ),
    url(r'^$', home, name='home'),
    url(r'^sobre$', sobre, name='sobre'),
    url(r'^contato$', contato, name='contato'),
    url(r'^alunos$', ListaAlunos.as_view(), name='ListaAlunos'),
    url(r'^aluno/(?P<aluno_id>\d+)/$', alunoInfo, name='aluno_url'),
    url(r'^disciplinas$', ListaDisciplinas.as_view(), name='ListaDisciplinas'),
    url(r'^secretarias$', ListaSecretarias.as_view(), name='ListaSecretarias'),
    url(r'^secretaria/(?P<id>\d+)/$', secretariaAdmin, name='secretaria'),
    url(r'^pdf/(?P<aluno_id>\d+)/$', some_view, name='some_view'),
    url(r'^pdf$', HelloPDFView.as_view(), name='HelloPDFView'),
    url(r'^excel$', excel, name='excel'),
]

# if settings.DEBUG:
#     urlpatterns += static('/static/', document_root='static_files')