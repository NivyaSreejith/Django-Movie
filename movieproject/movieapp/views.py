from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import Movie
from .forms import MovieForm

# Create your views here.
# def index(request):
#     movie=Movie.objects.all()
#     context={'result':movie}
#     return render(request,'index.html',context)

def index(request):
     obj=Movie.objects.all()
     return render(request,'index.html',{'result':obj})

# def detail(request,movie_id):
#     return HttpResponse('this is movie no. %s' % movie_id)

def detail(request,movie_id):
    obj=Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':obj})

def add_movie(request):
     if request.method=='POST':
          name=request.POST.get('name')
          desc=request.POST.get('desc')
          year=request.POST.get('year')
          img=request.FILES['img']
          movie=Movie(name=name,desc=desc,year=year,img=img)
          movie.save()
          return redirect ('/')
     return render(request,'add.html')
     
     

def update(request,id):
     movie=Movie.objects.get(id=id)
     form=MovieForm(request.POST or None, request.FILES,instance=movie)
     if form.is_valid():
          form.save()
          return redirect ('/')
     return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
     if request.method=='POST':
          movie=Movie.objects.get(id=id)
          movie.delete()
          return redirect('/')
     return render(request,'delete.html')


     