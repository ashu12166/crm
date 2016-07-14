from django.shortcuts import render_to_response, render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


def test(request):
    return "123"


@csrf_exempt
def login(request):
    # c = {}
    # c.update(csrf(request))
    return render(request, 'envato.rathemes.com/infinity/topbar/login.html')

@csrf_exempt
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('message_board:list')
    else:
        return HttpResponse('notauthenticate....please login with correct detail', status=403)


def post_view(request):
    return HttpResponse('thisisthepost', status=403)

# ('blog/post_list.html',
# 								{'username': request.user.first_name})
