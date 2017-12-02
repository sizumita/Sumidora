from django.shortcuts import render

# Create your views here.

def mainpage(request):
    if request.method == 'POST':
        q = request.POST['name']

        return render(request, 'jump.html',
                      {
                       'name' : q,
                       })
    return render(request,'mainpage.html')

def data(request, **kwargs):
    q = kwargs['name']
    return render(request,'data.html',{'name':q},dict(kwargs))