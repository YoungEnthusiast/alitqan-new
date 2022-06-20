from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Video
from .forms import VideoForm, VideoFormUp, CategoryForm, CategoryFormUp
from .filters import VideoFilter, CategoryFilter
from django.core.paginator import Paginator
from home.models import Background
from django.contrib.auth.decorators import login_required#, permission_required
from django.contrib import messages

def showVideos(request, category_slug=None):
    audios_home = Background.objects.filter(home_page=True)
    context = {}
    videos = Video.objects.all()
    filtered_videos = VideoFilter(
        request.GET,
        queryset = Video.objects.all()
    )
    context['filtered_videos'] = filtered_videos
    paginated_filtered_videos = Paginator(filtered_videos.qs, 9)
    page_number = request.GET.get('page')
    videos_page_obj = paginated_filtered_videos.get_page(page_number)
    context['videos_page_obj'] = videos_page_obj
    total_videos = filtered_videos.qs.count()
    context['total_videos'] = total_videos
    context['audios_home'] = audios_home
    return render(request, 'videos/gallery.html', context=context)

def showVideosFirst(request, category_slug=None):
    context = {}
    videos = Video.objects.all()
    filtered_videos = VideoFilter(
        request.GET,
        queryset = Video.objects.all()
    )
    context['filtered_videos'] = filtered_videos
    paginated_filtered_videos = Paginator(filtered_videos.qs, 9)
    page_number = request.GET.get('page')
    videos_page_obj = paginated_filtered_videos.get_page(page_number)
    context['videos_page_obj'] = videos_page_obj
    total_videos = filtered_videos.qs.count()
    context['total_videos'] = total_videos
    return render(request, 'videos/gallery_first.html', context=context)

def showCategoriesFirst(request, category_slug=None):
    context = {}
    categories = Category.objects.all()
    filtered_categories = CategoryFilter(
        request.GET,
        queryset = Category.objects.all()
    )
    context['filtered_categories'] = filtered_categories
    paginated_filtered_categories = Paginator(filtered_categories.qs, 9)
    page_number = request.GET.get('page')
    categories_page_obj = paginated_filtered_categories.get_page(page_number)
    context['categories_page_obj'] = categories_page_obj
    total_categories = filtered_categories.qs.count()
    context['total_categories'] = total_categories
    return render(request, 'videos/categories_first.html', context=context)

@login_required
def updateVideoFirst(request, id):
    video = Video.objects.get(id=id)
    form = VideoFormUp(instance=video)
    if request.method=='POST':
        form = VideoFormUp(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, "The video has been modified successfully")
            return redirect('videos_first')
    return render(request, 'videos/gallery_update_first.html', {'form': form, 'video': video})

@login_required
def updateCategoryFirst(request, id):
    category = Category.objects.get(id=id)
    form = CategoryFormUp(instance=category)
    if request.method=='POST':
        form = CategoryFormUp(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "The category has been modified successfully")
            return redirect('categories_first')
    return render(request, 'videos/category_update_first.html', {'form': form, 'category': category})


@login_required
def deleteVideoFirst(request, id):
    video = Video.objects.get(id=id)
    obj = get_object_or_404(Video, id=id)
    if request.method =="POST":
        obj.delete()
        return redirect('videos_first')
    return render(request, 'videos/gallery_confirm_delete.html', {'video': video})

@login_required
def deleteCategoryFirst(request, id):
    category = Category.objects.get(id=id)
    obj = get_object_or_404(Category, id=id)
    if request.method =="POST":
        obj.delete()
        return redirect('categories_first')
    return render(request, 'videos/category_confirm_delete.html', {'category': category})

@login_required
def addCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "The category has been added successfully")
            return redirect('categories_first')
        else:
            messages.error(request, "Please review form input fields below")
    return render(request, 'videos/category_first.html', {'form': form})

@login_required
def addVideo(request):
    form = VideoForm()
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "The video has been added successfully")
            return redirect('videos_first')
        else:
            messages.error(request, "Please review form input fields below")
    return render(request, 'videos/video_first.html', {'form': form})
