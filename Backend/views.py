from django.core.paginator import Paginator
from django.shortcuts import render, redirect


from Backend.forms import PicForm
from Backend.detect_face_image import detect_image
from Backend.models import Pic


def index(request):
    form = PicForm()
    pics = Pic.objects.all().order_by('-id')
    posts_paginator = Paginator(pics, 5)
    page_number = request.GET.get('page')
    page = posts_paginator.get_page(page_number)
    if request.method == 'POST':
        form = PicForm(request.POST, request.FILES)
        if form.is_valid():
            new_pic = form.save()
            detect_image(new_pic.pic)
        return redirect('index')

    context = {
        'page': page,
        'form': form
    }
    return render(request, 'index.html', context)