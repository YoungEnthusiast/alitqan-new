from django.shortcuts import render, reverse, redirect
from .forms import ContactForm
from videos.models import Video
from news.models import News
from .models import Background
from django.core.mail import send_mail

def showHome(request):
    audios_home = Background.objects.filter(home_page=True)
    videos_home = Video.objects.filter(home_page=True)
    news_home = News.objects.filter(home_page=True)

    context = {'videos_home': videos_home, 'news_home': news_home, 'audios_home': audios_home}
    return render(request, 'home/home.html', context)

def showAdmission(request):
    audios_home = Background.objects.filter(home_page=True)
    return render(request, 'home/admission.html', {'audios_home': audios_home})

def showAbout(request):
    audios_home = Background.objects.filter(home_page=True)
    return render(request, 'home/about.html', {'audios_home': audios_home})

def showContact(request):
    audios_home = Background.objects.filter(home_page=True)
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            send_mail(
                'Contact Al-Itqan Model Academy',
                'A message was sent by ' + name + '. Please log in to admin panel to read message',
                'yustaoab@gmail.com',
                [email],
                fail_silently=False,
                #html_message = render_to_string('home/home1.html')
            )
            messages.success(request, str(name) + ", your message will receive attention shortly")
        else:
            return redirect('contact')
    return render(request, 'home/contact_form.html', {'form': form, 'audios_home': audios_home})
