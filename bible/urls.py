from django.contrib import admin
from django.urls import  re_path, path, include
from graphene_django.views import GraphQLView
from bible.schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
     re_path(r'^graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]