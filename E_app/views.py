from django.shortcuts import render,HttpResponse
from . models import FilesUpload
# Create your views here.
def home(request):
    if request.method == 'POST':
        file2 = request.POST["file"]
        document = FilesUpload.objects.create(file=file2)
        document.save()
        return HttpResponse("your file uploaded")
    return render(request,'E_app/home.html')


def index(request):

    context={'books':FilesUpload.objects.all()}
    return render(request,'E_app/index.html',context)