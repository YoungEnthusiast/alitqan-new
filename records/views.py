from django.shortcuts import render#, redirect
from .models import Pupil, Student
#from .forms import PupilForm, FirstTermForm, SecondTermForm, ThirdTermForm, ClassForm, TermBeginForm, TermEndForm
#from django.db.models import Count
from django.contrib import messages
from django.core.paginator import Paginator
from .filters import PupilFilter, StudentFilter#, SecondFilter, ThirdFilter
from django.contrib.auth.decorators import login_required#, permission_required

@login_required
def showPupils(request):
    context = {}
    filtered_pupils = PupilFilter(
        request.GET,
        queryset = Pupil.objects.all()
    )
    context['filtered_pupils'] = filtered_pupils
    paginated_filtered_pupils = Paginator(filtered_pupils.qs, 10)
    page_number = request.GET.get('page')
    pupils_page_obj = paginated_filtered_pupils.get_page(page_number)
    context['pupils_page_obj'] = pupils_page_obj
    total_pupils = filtered_pupils.qs.count()
    context['total_pupils'] = total_pupils
    return render(request, 'records/pupils.html', context=context)

@login_required
def showPupil(request, pk, **kwargs):
    pupil = Pupil.objects.get(id=pk)
    context = {'pupil': pupil}
    return render(request, 'records/pupil_detail.html', context)

@login_required
def showStudents(request):
    context = {}
    filtered_students = StudentFilter(
        request.GET,
        queryset = Student.objects.all()
    )
    context['filtered_students'] = filtered_students
    paginated_filtered_students = Paginator(filtered_students.qs, 10)
    page_number = request.GET.get('page')
    students_page_obj = paginated_filtered_students.get_page(page_number)
    context['students_page_obj'] = students_page_obj
    total_students = filtered_students.qs.count()
    context['total_students'] = total_students
    return render(request, 'records/students.html', context=context)

@login_required
def showStudent(request, pk, **kwargs):
    student = Student.objects.get(id=pk)
    context = {'student': student}
    return render(request, 'records/student_detail.html', context)
