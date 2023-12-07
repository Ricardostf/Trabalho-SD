# Primeira Aplicação

Este documento tem como objetivo apresentar a primeira aplicação desenvolvida com o framework Django. Aqui será apresentará conceitos simples e basicos para uma breve introdução ao framework. O tutorial foi desenvolvido para o sistema operacional Linux, mas pode ser adaptado para outros sistemas operacionais.

## Roadpmap
- [Instalação](#instalação)
- [Criando o modelo](#criando-o-modelo)
- [Criando a API](#criando-a-api)
- [Criando as views](#criando-as-views)
- [Criando as rotas](#criando-as-rotas)
- [CRUD](#crud)
- [Testando a API](#testando-a-api)


## Instalação
Primeiramente, crie uma pasta para ser o diretório do projeto.  
Em seguida, abra o terminal nesse diretório e execute os comandos que serão listados abaixo:

```bash
python3 -m venv .venv
```

Esse módulo venv oferece suporte à criação de “ambientes virtuais” leves, cada um com seu próprio conjunto independente de pacotes Python instalados em seus diretórios. Para verificar se foi instalado, realize o comando:

```bash
ls -a
```

Agora, precisamos ativar o .venv. Para isso, execute o seguinte comando:
```bash
. .venv/bin/activate
```

Utilizaremos o gerenciador de pacotes pip para instalar o Django e o Django REST Framework. Para instalar o pip, execute os seguintes comandos:

```bash
pip install django
```

```bash
pip install djangorestframework
```
Vamos criar agora um projeto Django. Para isso, execute o seguinte comando:

```bash
django-admin startproject sensors .
```
>Aqui estamos criando um projeto chamado sensors. O ponto no final do comando indica que o projeto será criado no diretório atual. Caso queira criar o projeto em outro diretório, substitua o ponto pelo caminho do diretório.

Para verificar se o projeto foi criado com sucesso, execute o seguinte comando:

    
```bash
python3 manage.py runserver
```
O erro apresentado é normal, pois ainda não fizemos as migrações do banco de dados. Para isso, execute o seguinte comando:

```bash
python3 manage.py migrate
```
>Migrações são como o Django armazena alterações no modelo (e, portanto, no esquema do banco de dados) - eles são apenas arquivos no sistema de arquivos. Você pode ler o código de migração para ver o que eles fazem em um nível de SQL básico (eles são projetados para serem legíveis), mas em geral, eles são projetados para serem modificados através do sistema de migração do Django, em vez de alterados manualmente. - [Django Migrations](https://docs.djangoproject.com/en/3.0/topics/migrations/)

No Django, possuímos uma plataforma de administração que nos permite gerenciar os dados do banco de dados.Adicione o seguinte texto em frente a url do servidor no navegador:

```bash
/admin
```
>Exemplo: <http://127.0.0.1:8000/admin>

Esta plataforma nos permite gerenciar os dados do banco de dados, desde todos os usários cadastrados até todos os sensores cadastrados. Para criar um usuário para acessar a plataforma, execute o seguinte comando:

```bash
python3 manage.py createsuperuser
```

>Vamos criar um usuário com o nome admin e senha admin para facilitar o acesso.

## Criando o modelo
Agora vamos criar o modelo que será utilizado para armazenar os dados dos sensores. Para isso, criamos um arquivo chamado models.py dentro do diretório sensors. 
    
```bash
sensores
├── asgi.py
├── __init__.py
├── models.py # Crie este arquivo
├── __pycache__
│   ├── __init__.cpython-310.pyc
│   ├── settings.cpython-310.pyc
│   ├── urls.cpython-310.pyc
│   └── wsgi.cpython-310.pyc
├── settings.py
├── urls.py
└── wsgi.py
```
Com o arquivo criado, vamos adicionar o seguinte código:

```python
from django.db import models

class Sensors(models.Model):
    name = models.CharField(max_length=255)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # define o que vai ser exibido
    def __str__(self):
        return self.name
```

Para que o Django reconheça o modelo criado, precisamos adicionar o nome do aplicativo no arquivo settings.py. Para isso, adicione o seguinte código:

```python
INSTALLED_APPS = [
    'sensors', # Adicione esta linha
    'rest_framework', # Adicione esta linha também
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    ...
]
```
Agora precisamos fazer as migrações do banco de dados para que o Django crie as tabelas do modelo. Para isso, execute o seguinte comando:

```bash
python3 manage.py makemigrations sensors
python3 manage.py migrate sensors
```

Precisamos também registrar o modelo no arquivo admin.py. Para isso, adicione o seguinte código:

```python
from django.contrib import admin
from .models import Sensors

admin.site.register(Sensors)
```

>Rode o servidor novamente e acesse a plataforma de administração. Você verá que agora existe uma opção chamada Sensors. Clique nela e você verá que é possível adicionar, editar e excluir sensores.
>
> ```bash
>python3 manage.py runserver
>```

## Criando a API
Agora vamos criar a API que será utilizada para acessar os dados dos sensores. Para isso, criamos um arquivo chamado serializers.py dentro do diretório sensors.

```bash
sensores
├── asgi.py
├── __init__.py
├── models.py
├── __pycache__
│   ├── __init__.cpython-310.pyc
│   ├── settings.cpython-310.pyc
│   ├── urls.cpython-310.pyc
│   └── wsgi.cpython-310.pyc
├── serializers.py # Crie este arquivo
├── settings.py
├── urls.py
└── wsgi.py
```
>Um serializador é uma classe que define como um modelo e instâncias de modelo são convertidos em JSON. - [Django REST Framework](https://www.django-rest-framework.org/api-guide/serializers/)

Com o arquivo criado, vamos adicionar o seguinte código:
```python
from rest_framework import serializers
from .models import Sensors

class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = ['id', 'name', 'value', 'timestamp']
```
        

## Criando as views
Agora vamos criar as views que serão utilizadas para acessar os dados dos sensores. Para isso, criamos um arquivo chamado views.py dentro do diretório sensors.

```bash
sensores
├── asgi.py
├── __init__.py
├── models.py
├── __pycache__
│   ├── __init__.cpython-310.pyc
│   ├── settings.cpython-310.pyc
│   ├── urls.cpython-310.pyc
│   └── wsgi.cpython-310.pyc
├── serializers.py
├── settings.py
├── urls.py
├── views.py # Crie este arquivo
└── wsgi.py
```
>Uma view é uma função que recebe uma solicitação da web e retorna uma resposta da web. Esta resposta pode ser o HTML de uma página da web, o JSON de uma API, um redirecionamento ou uma variedade de outras coisas. - [Django Views](https://docs.djangoproject.com/en/3.0/topics/http/views/)

Após criar o arquivo, adicione o seguinte código:

```python
from django.http import JsonResponse
from .models import Sensors
from .serializers import SensorsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def sensors_list(request, format=None):

    if request.method == 'GET':
        sensors = Sensors.objects.all()
        serializer = SensorsSerializer(sensors, many=True)
        return Response(serializer.data)
    
```

## Criando as rotas
Agora vamos criar as rotas que serão utilizadas para acessar os dados dos sensores. Para isso, abra o arquivo urls.py dentro do diretório sensors e substitua o código existente pelo seguinte:

```python
from django.contrib import admin
from django.urls import path
from sensors import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', views.sensors_list),
]
```

## CRUD
Vamos agora criar as views para realizar o CRUD (Create, Read, Update e Delete) dos sensores. Para isso, abra o arquivo views.py dentro do diretório sensors e substitua o código existente pelo seguinte:

```python
from django.http import JsonResponse
from .models import Sensors
from .serializers import SensorsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def sensors_list(request, format=None):

    if request.method == 'GET':
        sensors = Sensors.objects.all()
        serializer = SensorsSerializer(sensors, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = SensorsSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def sensors_detail(request, id, format=None):
    
    try:
        sensor = Sensors.objects.get(pk=id)
    except Sensors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        serializer = SensorsSerializer(sensor)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SensorsSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
            
    elif request.method == 'DELETE':
        sensor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

Para que as rotas funcionem, precisamos adicionar as seguintes linhas no arquivo urls.py:

```python
    path('sensors/<int:id>/', views.sensors_detail),
```

## Testando a API
Para testar a API, precisaremos do Postman, no entanto, o escopo deste tutorial não permite a instalação do Postman. Então será utilizado o curl para testar a API. Para isso, abra o terminal e execute os seguintes comandos:

```bash
# GET
curl http://127.0.0.1:8000/sensors/
```

```bash
# POST
curl -X POST -H "Content-Type: application/json" -d '{"name":"sensor1", "value": 1.0}' http://127.0.0.1:8000/sensors/
```

```bash
# PUT
curl -X PUT -H "Content-Type: application/json" -d '{"name":"sensor1", "value": 2.0}' http://127.0.0.1:8000/sensors/1/
```

```bash
# DELETE
curl -X DELETE http://127.0.0.1:8000/sensors/1/
```
