from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .openapi import chatResponse
from .models import Chat,User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@method_decorator(csrf_exempt, name="dispatch")
class Signup(View):

    def get(self,request):
        return render(request, "signup.html")

    def post(self, request):
        data = request.POST
        user = User.objects.filter(email=data['email']).first()
        if user:
            return JsonResponse({"msg":"Already exist!"},status=400)

        if data['password']!=data['confirm_password']:
            return JsonResponse({"msg":"Password not match!"},status=400)
       
        User.objects.create_user(username=data['name'],email=data['email'],password=data['password'],mobile=data['mobile'])
        print(User.objects.all())
        return JsonResponse({"msg":"User Creted"},status=201)


@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(login_required, name="dispatch")
class Home(View):
    
    def get(self, request):
        chats = Chat.objects.filter(user=request.user)
        return render(request, 'index.html',{"chats":chats})

    def post(self,request):
        data = request.POST.get("text")
        res = chatResponse(data)
        if res[:5] == "Error":
            return JsonResponse({"msg":res},status=400)
        user=request.user
        chat = Chat.objects.create(user=user,author_request=data,author_response=res)
        if not chat:
            return JsonResponse({"msg":"Something went wrong"+res},status=400)
        return JsonResponse({"msg":res})



@method_decorator(csrf_exempt, name="dispatch")
class LoginView(View):
    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        error = []
        if user is not None:
            login(request,user)
            return redirect('/chat/')

        error.append("Invalid credentials!")
        return render(request,"login.html",context={"request":request, "error":error})


def logoutView(request):
    logout(request)
    return redirect('/login')
  