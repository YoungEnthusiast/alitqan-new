from django.shortcuts import render, redirect, get_object_or_404
from .models import Session, Class, Subject
from .forms import SessionForm, SessionFormUp, ClassForm, ClassFormUp, SubjectForm
from django.contrib import messages
from django.core.paginator import Paginator
from .filters import SessionFilter, ClassFilter, SubjectFilter
from django.contrib.auth.decorators import login_required#, permission_required
#from django.db.models import Sum

@login_required
def showSessionsFirst(request):
    context = {}
    filtered_sessions = SessionFilter(
        request.GET,
        queryset = Session.objects.all()
    )
    context['filtered_sessions'] = filtered_sessions
    paginated_filtered_sessions = Paginator(filtered_sessions.qs, 500)
    page_number = request.GET.get('page')
    sessions_page_obj = paginated_filtered_sessions.get_page(page_number)
    context['sessions_page_obj'] = sessions_page_obj
    total_sessions = filtered_sessions.qs.count()
    context['total_sessions'] = total_sessions
    return render(request, 'management/sessions_first.html', context=context)

@login_required
def showClassesFirst(request):
    context = {}
    filtered_classes = ClassFilter(
        request.GET,
        queryset = Class.objects.all()
    )
    context['filtered_classes'] = filtered_classes
    paginated_filtered_classes = Paginator(filtered_classes.qs, 500)
    page_number = request.GET.get('page')
    classes_page_obj = paginated_filtered_classes.get_page(page_number)
    context['classes_page_obj'] = classes_page_obj
    total_classes = filtered_classes.qs.count()
    context['total_classes'] = total_classes
    return render(request, 'management/classes_first.html', context=context)

@login_required
def showSubjectsFirst(request):
    context = {}
    filtered_subjects = SubjectFilter(
        request.GET,
        queryset = Subject.objects.all()
    )
    context['filtered_subjects'] = filtered_subjects
    paginated_filtered_subjects = Paginator(filtered_subjects.qs, 500)
    page_number = request.GET.get('page')
    subjects_page_obj = paginated_filtered_subjects.get_page(page_number)
    context['subjects_page_obj'] = subjects_page_obj
    total_subjects = filtered_subjects.qs.count()
    context['total_subjects'] = total_subjects
    return render(request, 'management/subjects_first.html', context=context)

@login_required
def updateSessionFirst(request, id):
    session = Session.objects.get(id=id)
    form = SessionFormUp(instance=session)
    if request.method=='POST':
        form = SessionFormUp(request.POST, request.FILES, instance=session)
        if form.is_valid():
            form.save()
            messages.success(request, "The session has been modified successfully")
            return redirect('sessions_first')
    return render(request, 'management/session_update_first.html', {'form': form, 'session': session})

@login_required
def updateClassFirst(request, id):
    classe = Class.objects.get(id=id)
    form = ClassFormUp(instance=classe)
    if request.method=='POST':
        form = ClassFormUp(request.POST, request.FILES, instance=classe)
        if form.is_valid():
            form.save()
            messages.success(request, "The class has been modified successfully")
            return redirect('classes_first')
    return render(request, 'management/class_update_first.html', {'form': form, 'classe': classe})

@login_required
def updateSubjectFirst(request, id):
    subject = Subject.objects.get(id=id)
    form = SubjectForm(instance=subject)
    if request.method=='POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            messages.success(request, "The subject has been modified successfully")
            return redirect('subjects_first')
    return render(request, 'management/subject_update_first.html', {'form': form, 'subject': subject})

@login_required
def deleteSessionFirst(request, id):
    session = Session.objects.get(id=id)
    obj = get_object_or_404(Session, id=id)
    if request.method =="POST":
        obj.delete()
        return redirect('sessions_first')
    return render(request, 'management/sessions_confirm_delete.html', {'session': session})

@login_required
def deleteClassFirst(request, id):
    classe = Class.objects.get(id=id)
    obj = get_object_or_404(Class, id=id)
    if request.method =="POST":
        obj.delete()
        return redirect('classes_first')
    return render(request, 'management/classes_confirm_delete.html', {'classe': classe})

@login_required
def deleteSubjectFirst(request, id):
    subject = Subject.objects.get(id=id)
    obj = get_object_or_404(Subject, id=id)
    if request.method =="POST":
        obj.delete()
        return redirect('subjects_first')
    return render(request, 'management/subjects_confirm_delete.html', {'subject': subject})

@login_required
def addSession(request):
    form = SessionForm()
    if request.method == 'POST':
        form = SessionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "The session has been added successfully")
            return redirect('sessions_first')
        else:
            messages.error(request, "Please review form input fields below")
            #return redirect('pre_basic_first')
    return render(request, 'management/session_first.html', {'form': form})

@login_required
def addClass(request):
    form = ClassForm()
    if request.method == 'POST':
        form = ClassForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "The class has been added successfully")
            return redirect('classes_first')
        else:
            messages.error(request, "Please review form input fields below")
            #return redirect('pre_basic_first')
    return render(request, 'management/class_first.html', {'form': form})

@login_required
def addSubject(request):
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST or None)
        if form.is_valid():
            form.save()
            classe = form.cleaned_data.get('classe')
            subject = form.cleaned_data.get('subject')
            reg = Subject.objects.filter(classe=classe, subject=subject)[0]
            try:
                reg2 = Subject.objects.filter(classe=classe, subject=subject)[1]
                messages.error(request, str(classe) + " | " + str(subject) + " already exists.")
                reg.delete()
            except:
                messages.success(request, "The subject has been added successfully")
                return redirect('subjects_first')
        else:
            messages.error(request, "Please review form input fields below")

    return render(request, 'management/subject_first.html', {'form': form})
