from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        if name == 'lary' and pwd == '123':
            response = HttpResponse('ok')
            response.set_cookie('login','true')
            return response
    return render(request,'login.html')

def index(request):
    ret = request.COOKIES.get('login')
    if not ret:
        return redirect('/login/')
    return render(request,'index.html')