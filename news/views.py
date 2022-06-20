from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from .forms import NewsForm, NewsFormUp
from .filters import NewsFilter
from django.core.paginator import Paginator
from home.models import Background
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def showEvents(request):
    audios_home = Background.objects.filter(home_page=True)
    context = {}
    news = News.objects.all()
    filtered_news = NewsFilter(
        request.GET,
        queryset = News.objects.all()
    )
    context['filtered_news'] = filtered_news
    paginated_filtered_news = Paginator(filtered_news.qs, 10)
    page_number = request.GET.get('page')
    news_page_obj = paginated_filtered_news.get_page(page_number)
    context['news_page_obj'] = news_page_obj
    total_news = filtered_news.qs.count()
    context['total_news'] = total_news
    context['audios_home'] = audios_home
    return render(request, 'news/events.html', context=context)

@login_required
def showEventsFirst(request):
    context = {}
    news = News.objects.all()
    filtered_news = NewsFilter(
        request.GET,
        queryset = News.objects.all()
    )
    context['filtered_news'] = filtered_news
    paginated_filtered_news = Paginator(filtered_news.qs, 10)
    page_number = request.GET.get('page')
    news_page_obj = paginated_filtered_news.get_page(page_number)
    context['news_page_obj'] = news_page_obj
    total_news = filtered_news.qs.count()
    context['total_news'] = total_news
    return render(request, 'news/events_first.html', context=context)

@login_required
def updateEventFirst(request, id):
    new = News.objects.get(id=id)
    form = NewsFormUp(instance=new)
    if request.method=='POST':
        form = NewsFormUp(request.POST, request.FILES, instance=new)
        if form.is_valid():
            form.save()
            messages.success(request, "The news has been modified successfully")
            return redirect('events_first')
    return render(request, 'news/event_update_first.html', {'form': form, 'new': new})

@login_required
def deleteEventFirst(request, id):
    new = News.objects.get(id=id)
    obj = get_object_or_404(News, id=id)
    if request.method =="POST":
        obj.delete()
        return redirect('events_first')
    return render(request, 'news/news_confirm_delete.html', {'new': new})

@login_required
def addEvent(request):
    form = NewsForm()
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "The news has been added successfully")
            return redirect('events_first')
        else:
            messages.error(request, "Please review form input fields below")
    return render(request, 'news/event_first.html', {'form': form})
