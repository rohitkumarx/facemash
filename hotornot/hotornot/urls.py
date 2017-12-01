from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    
    #url(r'^$', 'blogs.views.home', name='home'),
    #url(r'^contact/$', 'blogs.views.contact', name='contact'),
   	#url(r'^custom_query/$', 'blogs.views.custom_query', name='custom_query'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'peepcompare.views.play', name='play'),
    url(r'^increment/(?P<winner_id>[0-9]+)/(?P<losser_id>[0-9]+)/$', 'peepcompare.views.increment', name='increment'),
    url(r'^api/auth/token/', obtain_jwt_token),
    url(r'^api/facemash/',include("peepcompare.face_mash_api.urls", namespace="facemash_api")),
    url(r'^api/users/', include("peepcompare.users_api.urls", namespace="users_api"))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
$ curl -X POST -d "username=root&password=root" http://127.0.0.1:8000/api/auth/token/


curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InJvb3QiLCJ1c2VyX2lkIjoxLCJlbWFpbCI6InJvb3RAcm9vdC5jb20iLCJleHAiOjE1MTIwNjY3NTB9.SXchk-lD3aP2bMdhxdms6bYuTJ9mthEZI6MJg4Xd9ms" http://127.0.0.1:8000/api/facemash/
curl -X POST -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InJvb3QiLCJ1c2VyX2lkIjoxLCJlbWFpbCI6InJvb3RAcm9vdC5jb20iLCJleHAiOjE1MTIwNjY3NTB9.SXchk-lD3aP2bMdhxdms6bYuTJ9mthEZI6MJg4Xd9ms"  -H "Content-Type: application/json" -d '{"username":"rootx","password":"rootx"}' http://127.0.0.1:8000/api/users/register/?type=post

curl http://127.0.0.1:8000/api/facemash/
'''