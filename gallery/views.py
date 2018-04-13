from django.shortcuts import render
from gallery.models import Picture
from django.core.paginator import Paginator


def load_gallery(request):
   # sort_by_type = Picture.objects.all().order_by('p_type')
    #sort_by_price = Picture.objects.all().order_by('p_price')
    #sort_by_name=Picture.objects.all().order_by('p_name')
    all_pictures = Picture.objects.all()
    paginator = Paginator(all_pictures, 6)
    page = request.GET.get('page')
    images = paginator.get_page(page)
    return render(request, 'gallery/gallery.html', {'images': images})


def open_picture(request):
    return render(request, 'gallery/picture.html')
