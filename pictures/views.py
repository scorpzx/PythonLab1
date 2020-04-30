from django.http import Http404,HttpResponse
from django.shortcuts import render
from django.shortcuts import reverse
from django.views.generic import ListView
from django.shortcuts import redirect
from .models import Picture
from pictures import views

class HomePageView(ListView):
    model = Picture
    paginate_by = 1
    template_name = 'home.html'

def mlike(request):
    try:
        tmp_id=request.GET['mlike']
        a = Picture.objects.get(id = tmp_id)
    except:
        raise Http404("not found")
    Pic =Picture.objects.all()
    a.raiting += 1 
    a.save()
    return redirect('http://127.0.0.1:8000/pictures/?page={}'.format(tmp_id))
   #return render(request, 'home.html/',context={'page_obj':Pic})
   #return HttpResponseRedirect(reverse('app_first_test:main'))
   #return render(request, 'home.html/picture/?page=1')

def mdislike(request):
    try:
        tmp_id=request.GET['mdislike']
        a = Picture.objects.get(id = tmp_id)
    except:
        raise Http404("not found")
    Pic =Picture.objects.all()
    a.raiting -= 1 
    a.save()

    return redirect('http://127.0.0.1:8000/pictures/?page={}'.format(tmp_id))

def like(request, picture_id):
    try:
        a = Picture.objects.get(id = picture_id)
    except:
        raise Http404("not found")

    a.raiting += 1 
    a.save()

    return render(request, 'home.html')

def dislike(request, picture_id):
    try:
        a = Picture.objects.get(id = picture_id)
    except:
        raise Http404("not found")

    a.raiting -= 1 
    a.save()

