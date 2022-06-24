from django.shortcuts import render, redirect, get_object_or_404
from .models import First, Second, Third
from users.models import Person
from management.models import Class
from .forms import FirstForm, SecondForm, ThirdForm, SecondFormPay,FirstFormUp, FirstFormBeha, FirstFormHead, SecondFormUp, ThirdFormUp, SecondFormBeha, SecondFormHead, FirstFormPay
from django.contrib import messages
from django.core.paginator import Paginator
from .filters import FirstFilter, FirstFilter2, SecondFilter2, FirstFilterPay, SecondFilter, SecondFilterPay, ThirdFilter
from django.contrib.auth.decorators import login_required#, permission_required
from django.core.mail import send_mail
from django.db.models import Sum
#from django.template.loader import render_to_string
import csv
from django.http import HttpResponse
# from weasyprint import HTML, CSS
import tempfile
import datetime

@login_required
def showFirsts(request):
    context = {}
    filtered_firsts = FirstFilter(
        request.GET,
        queryset = First.objects.filter(subject__teacher=request.user)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/first_list.html', context=context)

@login_required
def showSeconds(request):
    context = {}
    filtered_firsts = SecondFilter(
        request.GET,
        queryset = Second.objects.filter(subject__teacher=request.user)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/second_list.html', context=context)

@login_required
def showThirds(request):
    context = {}
    filtered_firsts = ThirdFilter(
        request.GET,
        queryset = Third.objects.filter(subject__teacher=request.user)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/third_list.html', context=context)

@login_required
def showAdminFirsts(request):
    context = {}
    filtered_firsts = FirstFilter(
        request.GET,
        queryset = First.objects.all()
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/admin_first_list.html', context=context)

@login_required
def showFirsts2(request, ):
    context = {}
    filtered_firsts = FirstFilter2(
        request.GET,
        queryset = First.objects.filter(student__classe__teacher=request.user, value=1)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/first_list2.html', context=context)

@login_required
def showSeconds2(request, ):
    context = {}
    filtered_firsts = FirstFilter2(
        request.GET,
        queryset = Second.objects.filter(student__classe__teacher=request.user, value=1)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/second_list2.html', context=context)

@login_required
def showAdminFirsts2(request, ):
    context = {}
    filtered_firsts = FirstFilter2(
        request.GET,
        queryset = First.objects.filter(value=1)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 500)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/admin_first_list2.html', context=context)

@login_required
def showHeadFirsts2(request):
    context = {}
    filtered_firsts = FirstFilter2(
        request.GET,
        queryset = First.objects.filter(session__first_head=request.user, value=1)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 500)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/head_first_list2.html', context=context)

@login_required
def showHeadSeconds2(request):
    context = {}
    filtered_firsts = SecondFilter2(
        request.GET,
        queryset = Second.objects.filter(session__second_head=request.user, value=1)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 500)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/head_second_list2.html', context=context)

@login_required
def showFirsts3(request):
    context = {}
    filtered_firsts = FirstFilter2(
        request.GET,
        queryset = First.objects.filter(student__classe__teacher=request.user, value=1)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/first_list3.html', context=context)

@login_required
def showSeconds3(request):
    context = {}
    filtered_firsts = SecondFilter2(
        request.GET,
        queryset = Second.objects.filter(student__classe__teacher=request.user, value=1)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/second_list3.html', context=context)

@login_required
def showAdminFirsts3(request):
    context = {}
    filtered_firsts = FirstFilter2(
        request.GET,
        queryset = First.objects.filter(value=1)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 500)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/admin_first_list3.html', context=context)

@login_required
def showFirstsUser(request):
    context = {}
    filtered_firsts = FirstFilter(
        request.GET,
        queryset = First.objects.filter(student=request.user, school_fees=True)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/first_list_user.html', context=context)

@login_required
def showSecondsUser(request):
    context = {}
    filtered_firsts = SecondFilter(
        request.GET,
        queryset = Second.objects.filter(student=request.user, school_fees=True)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/second_list_user.html', context=context)

@login_required
def showFirsts3User(request):
    context = {}
    filtered_firsts = FirstFilter(
        request.GET,
        queryset = First.objects.filter(session__first_report=True, student=request.user, value=1, school_fees=True)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/first_list3_user.html', context=context)

@login_required
def showSeconds3User(request):
    context = {}
    filtered_firsts = SecondFilter(
        request.GET,
        queryset = Second.objects.filter(session__first_report=True, student=request.user, value=1, school_fees=True)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/second_list3_user.html', context=context)

@login_required
def updateFirst(request, id):
    first = First.objects.get(id=id)
    form = FirstFormUp(instance=first)
    if request.method=='POST':
        form = FirstFormUp(request.POST, instance=first)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            subject = form.cleaned_data.get('subject')
            class_students_count = Person.objects.filter(classe=student.classe).count()
            reg = First.objects.get(session=session, student=student, subject=subject)
            if reg.subject.teacher != request.user:
                messages.error(request, "You cannot record a score for " + str(subject) + " because you were not assigned as the subject's teacher")
            else:
                reg.student = student
                teacher = request.user
                teacher_name = teacher.last_name
                student_first_name = student.first_name
                student_last_name = student.last_name
                student_email = student.email
                old_total = reg.total
                new_total = reg.ca1 + reg.ca2 + reg.exam
                reg.total = new_total
                reg.save()
                reg1 = First.objects.get(session=session, student=student, subject=subject)
                reg1.subject_total = reg1.subject_total - old_total
                reg1.save()
                reg2 = First.objects.get(session=session, student=student, subject=subject)
                reg2.subject_total = reg2.subject_total + new_total
                reg2.save()
                reg3 = First.objects.get(session=session, student=student, subject=subject)
                reg4 = First.objects.filter(session=session, subject=subject).order_by('-total')
                n = reg4.count()
                d = round((reg3.subject_total/n),2)
                subject_position = []
                subject_pos = 0

                for each in reg4:
                    each.subject_total = reg3.subject_total
                    each.subject_avg = d
                    each.grade = reg3.grade()
                    each.save()

                for each in reg4:
                    subject_position.append(each.total)

                for i in range(len(subject_position)):
                    for each in reg4:
                        temp = subject_position.index(each.total)
                        each.subject_pos = temp + 1
                        each.save()

                reg6 = First.objects.filter(session=session, student=student)
                m = reg6.count()
                all_total = First.objects.filter(session=session, student=student).aggregate(Sum('total'))['total__sum']
                cum_perc = round((all_total/m),2)
                for each in reg6:
                    each.cumulative = all_total
                    each.cum_perc = cum_perc
                    each.static_class = str(each.student.classe)
                    each.static_class_teacher = str(each.student.classe.teacher.first_name) + " " + str(each.student.classe.teacher.last_name)
                    each.static_head_teacher = str(each.session.first_head.first_name) + " " + str(each.session.first_head.last_name)
                    each.static_teacher_signature = each.student.classe.signature
                    each.static_school_stamp = each.session.school
                    each.static_student_image = each.student.photograph
                    each.static_age = each.student.age()
                    each.static_number_in_class = class_students_count
                    each.save()

            # send_mail(
            #     '[' + str(session) + '] SCORES UPDATE',
            #     "New Scores have been recorded. Teacher's Name: " + str(teacher_name) + "student: " + str(student) + "student's Name: " + str(student_first_name) + str(student_last_name),
            #     'yustaoab@gmail.com',
            #     [student_email],
            #     fail_silently=False,
            #     #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            # )
            messages.success(request, str(student_first_name) + "'s score has been modified successfully")
            return redirect('firsts')
    return render(request, 'result/first_update.html', {'form': form, 'first': first})

@login_required
def updateSecond(request, id):
    first = Second.objects.get(id=id)
    form = SecondFormUp(instance=first)
    if request.method=='POST':
        form = SecondFormUp(request.POST, instance=first)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            subject = form.cleaned_data.get('subject')
            class_students_count = Person.objects.filter(classe=student.classe).count()
            reg = Second.objects.get(session=session, student=student, subject=subject)
            if reg.subject.teacher != request.user:
                messages.error(request, "You cannot record a score for " + str(subject) + " because you were not assigned as the subject's teacher")
            else:
                reg.student = student
                teacher = request.user
                teacher_name = teacher.last_name
                student_first_name = student.first_name
                student_last_name = student.last_name
                student_email = student.email
                old_total = reg.total
                new_total = reg.ca1 + reg.ca2 + reg.exam
                reg.total = new_total
                reg.save()
                reg1 = Second.objects.get(session=session, student=student, subject=subject)
                reg1.subject_total = reg1.subject_total - old_total
                reg1.save()
                reg2 = Second.objects.get(session=session, student=student, subject=subject)
                reg2.subject_total = reg2.subject_total + new_total
                reg2.save()
                reg3 = Second.objects.get(session=session, student=student, subject=subject)
                reg4 = Second.objects.filter(session=session, subject=subject).order_by('-total')
                n = reg4.count()
                d = round((reg3.subject_total/n),2)
                subject_position = []
                subject_pos = 0

                for each in reg4:
                    each.subject_total = reg3.subject_total
                    each.subject_avg = d
                    each.grade = reg3.grade()
                    each.save()

                for each in reg4:
                    subject_position.append(each.total)

                for i in range(len(subject_position)):
                    for each in reg4:
                        temp = subject_position.index(each.total)
                        each.subject_pos = temp + 1
                        each.save()

                reg6 = Second.objects.filter(session=session, student=student)
                m = reg6.count()
                all_total = Second.objects.filter(session=session, student=student).aggregate(Sum('total'))['total__sum']
                cum_perc = round((all_total/m),2)
                for each in reg6:
                    each.cumulative = all_total
                    each.cum_perc = cum_perc
                    each.static_class = str(each.student.classe)
                    each.static_class_teacher = str(each.student.classe.teacher.first_name) + " " + str(each.student.classe.teacher.last_name)
                    each.static_head_teacher = str(each.session.second_head.first_name) + " " + str(each.session.second_head.last_name)
                    each.static_teacher_signature = each.student.classe.signature
                    each.static_school_stamp = each.session.school
                    each.static_student_image = each.student.photograph
                    each.static_age = each.student.age()
                    each.static_number_in_class = class_students_count
                    each.save()

            # send_mail(
            #     '[' + str(session) + '] SCORES UPDATE',
            #     "New Scores have been recorded. Teacher's Name: " + str(teacher_name) + "student: " + str(student) + "student's Name: " + str(student_first_name) + str(student_last_name),
            #     'yustaoab@gmail.com',
            #     [student_email],
            #     fail_silently=False,
            #     #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            # )
            messages.success(request, str(student_first_name) + "'s score has been modified successfully")
            return redirect('seconds')
    return render(request, 'result/second_update.html', {'form': form, 'first': first})

@login_required
def updateThird(request, id):
    first = Third.objects.get(id=id)
    form = ThirdFormUp(instance=first)
    if request.method=='POST':
        form = ThirdFormUp(request.POST, instance=first)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            subject = form.cleaned_data.get('subject')
            class_students_count = Person.objects.filter(classe=student.classe).count()
            reg = Third.objects.get(session=session, student=student, subject=subject)
            if reg.subject.teacher != request.user:
                messages.error(request, "You cannot record a score for " + str(subject) + " because you were not assigned as the subject's teacher")
            else:
                reg.student = student
                teacher = request.user
                teacher_name = teacher.last_name
                student_first_name = student.first_name
                student_last_name = student.last_name
                student_email = student.email

                old_total = reg.total
                old_terms_total = reg.terms_total
                new_total = reg.ca1 + reg.ca2 + reg.exam
                reg.total = new_total
                reg.save()

                reg1 = Third.objects.get(session=session, student=student, subject=subject)
                reg1.subject_total = reg1.subject_total - old_total
                reg1.terms_total = reg1.terms_total - old_total
                reg1.save()
                reg2 = Third.objects.get(session=session, student=student, subject=subject)
                reg2.subject_total = reg2.subject_total + new_total
                reg2.terms_total = reg2.terms_total + new_total
                reg2.save()


                #####
                try:
                    reg7 = Third.objects.get(session=session, student=student)
                    reg7.value = 1
                    reg7.save()
                except:
                    pass
                reg4 = Third.objects.filter(session=session, subject=subject).order_by('-terms_total')
                n = reg4.count()
                try:

                    reg5 = Third.objects.filter(session=session, subject=subject)[1]
                    d = round((reg5.subject_total/(3*n)),2)
                    subject_position = []
                    # subject_pos =
                except:

                    reg5 = Third.objects.filter(session=session, subject=subject)[0]
                    d = round((reg5.subject_total/(3*n)),2)
                    subject_position = []
                    # subject_pos = 0
                for each in reg4:
                    each.subject_total = reg5.subject_total
                    each.subject_avg = d
                    each.grade = reg5.grade()
                    each.save()

                for each in reg4:
                    subject_position.append(each.terms_total)

                for i in range(len(subject_position)):
                    for each in reg4:
                        temp = subject_position.index(each.terms_total)
                        each.subject_pos = temp + 1
                        each.save()

                reg6 = Third.objects.filter(session=session, student=student)
                m = reg6.count()
                all_total = Third.objects.filter(session=session, student=student).aggregate(Sum('terms_total'))['terms_total__sum']
                cum_perc = round((all_total/m),2)
                for each in reg6:
                    each.cumulative = all_total
                    each.cum_perc = cum_perc
                    each.static_class = str(each.student.classe)
                    each.static_class_teacher = str(each.student.classe.teacher.first_name) + " " + str(each.student.classe.teacher.last_name)
                    each.static_head_teacher = str(each.session.third_head.first_name) + " " + str(each.session.third_head.last_name)
                    each.static_teacher_signature = each.student.classe.signature
                    each.static_school_stamp = each.session.school
                    each.static_student_image = each.student.photograph
                    each.static_age = each.student.age()
                    each.static_number_in_class = class_students_count
                    each.save()
                try:
                    reg8 = Third.objects.get(session=session, student=student, value=1)
                    if reg8.school_fees == True:
                        reg9 = Third.objects.filter(session=session, student=student)[0]
                        reg9.school_fees = True
                        reg9.save()
                except:
                    pass

            # send_mail(
            #     '[' + str(session) + '] SCORES UPDATE',
            #     "New Scores have been recorded. Teacher's Name: " + str(teacher_name) + "student: " + str(student) + "student's Name: " + str(student_first_name) + str(student_last_name),
            #     'yustaoab@gmail.com',
            #     [student_email],
            #     fail_silently=False,
            #     #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            # )
            messages.success(request, str(student_first_name) + "'s score has been modified successfully")
            return redirect('thirds')
    return render(request, 'result/third_update.html', {'form': form, 'first': first})

@login_required
def updateAdminFirst(request, id):
    first = First.objects.get(id=id)
    form = FirstFormUp(instance=first)
    if request.method=='POST':
        form = FirstFormUp(request.POST, instance=first)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            subject = form.cleaned_data.get('subject')
            class_students_count = Person.objects.filter(classe=student.classe).count()
            reg = First.objects.get(session=session, student=student, subject=subject)
            reg.student = student
            teacher = request.user
            teacher_name = teacher.last_name
            student_first_name = student.first_name
            student_last_name = student.last_name
            student_email = student.email
            old_total = reg.total
            new_total = reg.ca1 + reg.ca2 + reg.exam
            reg.total = new_total
            reg.save()
            reg1 = First.objects.get(session=session, student=student, subject=subject)
            reg1.subject_total = reg1.subject_total - old_total
            reg1.save()
            reg2 = First.objects.get(session=session, student=student, subject=subject)
            reg2.subject_total = reg2.subject_total + new_total
            reg2.save()
            reg3 = First.objects.get(session=session, student=student, subject=subject)
            reg4 = First.objects.filter(session=session, subject=subject).order_by('-total')
            n = reg4.count()
            d = round((reg3.subject_total/n),2)
            subject_position = []
            subject_pos = 0

            for each in reg4:
                each.subject_total = reg3.subject_total
                each.subject_avg = d
                each.grade = reg3.grade()
                # subject_position.append(each.total)
                # subject_position.sort(reverse=True)
                each.save()
            for each in reg4:
                subject_position.append(each.total)

            for i in range(len(subject_position)):
                for each in reg4:
                    temp = subject_position.index(each.total)
                    each.subject_pos = temp + 1
                    each.save()
            reg6 = First.objects.filter(session=session, student=student)
            m = reg6.count()
            all_total = First.objects.filter(session=session, student=student).aggregate(Sum('total'))['total__sum']
            cum_perc = round((all_total/m),2)
            for each in reg6:
                each.cumulative = all_total
                each.cum_perc = cum_perc
                each.static_class = str(each.student.classe)
                each.static_class_teacher = str(each.student.classe.teacher.first_name) + " " + str(each.student.classe.teacher.last_name)
                each.static_head_teacher = str(each.session.first_head.first_name) + " " + str(each.session.first_head.last_name)
                each.static_teacher_signature = each.student.classe.signature
                each.static_school_stamp = each.session.school
                each.static_student_image = each.student.photograph
                each.static_age = each.student.age()
                each.static_number_in_class = class_students_count
                each.save()

        # send_mail(
        #     '[' + str(session) + '] SCORES UPDATE',
        #     "New Scores have been recorded. Teacher's Name: " + str(teacher_name) + "student: " + str(student) + "student's Name: " + str(student_first_name) + str(student_last_name),
        #     'yustaoab@gmail.com',
        #     [student_email],
        #     fail_silently=False,
        #     #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
        # )
            messages.success(request, str(student_first_name) + "'s score has been modified successfully")
            return redirect('admin_firsts')
    return render(request, 'result/admin_first_update.html', {'form': form, 'first': first})

@login_required
def updateFirstBeha(request, id):
    first = First.objects.get(id=id)
    form = FirstFormBeha(instance=first)
    if request.method=='POST':
        form = FirstFormBeha(request.POST, instance=first)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            reg = First.objects.get(id=id)
            if reg.student.classe.teacher != request.user:
                messages.error(request, "Only the class teacher of " + str(reg.student.classe) + " fill skills/attitudes for a student in the class.")
            else:
                reg.student = student
                teacher = request.user
                teacher_name = teacher.last_name
                student_first_name = student.first_name
                student_last_name = student.last_name
                student_email = student.email
                reg.save()
                reg1 = First.objects.filter(session=session, student=student)
                for each in reg1:
                    each.number_present = reg.number_present
                    each.concentration = reg.concentration
                    each.responsiveness = reg.responsiveness
                    each.comprehension = reg.comprehension
                    each.interest = reg.interest
                    each.homework = reg.homework
                    each.reading = reg.reading
                    each.writing = reg.writing
                    each.spoken = reg.spoken
                    each.innovative = reg.innovative
                    each.save()
            # send_mail(
            #     '[' + str(session) + '] SCORES UPDATE',
            #     "New Scores have been recorded. Teacher's Name: " + str(teacher_name) + "student: " + str(student) + "student's Name: " + str(student_first_name) + str(student_last_name),
            #     'yustaoab@gmail.com',
            #     [student_email],
            #     fail_silently=False,
            #     #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            # )
            messages.success(request, str(student_first_name) + "'s attitude to study and scholastic skills have been recorded successfully")
            return redirect('firsts2')
    return render(request, 'result/first_update_beha.html', {'form': form, 'first': first})

@login_required
def updateSecondBeha(request, id):
    first = Second.objects.get(id=id)
    form = SecondFormBeha(instance=first)
    if request.method=='POST':
        form = SecondFormBeha(request.POST, instance=first)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            reg = Second.objects.get(id=id)
            if reg.student.classe.teacher != request.user:
                messages.error(request, "Only the class teacher of " + str(reg.student.classe) + " fill skills/attitudes for a student in the class.")
            else:
                reg.student = student
                teacher = request.user
                teacher_name = teacher.last_name
                student_first_name = student.first_name
                student_last_name = student.last_name
                student_email = student.email
                reg.save()
                reg1 = Second.objects.filter(session=session, student=student)
                for each in reg1:
                    each.number_present = reg.number_present
                    each.concentration = reg.concentration
                    each.responsiveness = reg.responsiveness
                    each.comprehension = reg.comprehension
                    each.interest = reg.interest
                    each.homework = reg.homework
                    each.reading = reg.reading
                    each.writing = reg.writing
                    each.spoken = reg.spoken
                    each.innovative = reg.innovative
                    each.save()
            # send_mail(
            #     '[' + str(session) + '] SCORES UPDATE',
            #     "New Scores have been recorded. Teacher's Name: " + str(teacher_name) + "student: " + str(student) + "student's Name: " + str(student_first_name) + str(student_last_name),
            #     'yustaoab@gmail.com',
            #     [student_email],
            #     fail_silently=False,
            #     #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            # )
            messages.success(request, str(student_first_name) + "'s attitude to study and scholastic skills have been recorded successfully")
            return redirect('seconds2')
    return render(request, 'result/second_update_beha.html', {'form': form, 'first': first})

@login_required
def updateFirstHead(request, id):
    first = First.objects.get(id=id)
    form = FirstFormHead(instance=first)
    if request.method=='POST':
        form = FirstFormHead(request.POST, instance=first)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            reg = First.objects.get(id=id)
            if reg.session.first_head != request.user:
                messages.error(request, "Only the head of schools can enter the comment.")
            else:
                reg.student = student
                teacher = request.user
                teacher_name = teacher.last_name
                student_first_name = student.first_name
                student_last_name = student.last_name
                student_email = student.email
                reg.save()
                reg1 = First.objects.filter(session=session, student=student)
                for each in reg1:
                    each.number_present = reg.number_present
                    # each.static_number = str(reg.session.first_number)
                    # each.absent = int(each.static_number) - each.number_present
                    each.save()
            # send_mail(
            #     '[' + str(session) + '] SCORES UPDATE',
            #     "New Scores have been recorded. Teacher's Name: " + str(teacher_name) + "student: " + str(student) + "student's Name: " + str(student_first_name) + str(student_last_name),
            #     'yustaoab@gmail.com',
            #     [student_email],
            #     fail_silently=False,
            #     #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            # )
                messages.success(request, str(student_first_name) + "'s comment has been recorded successfully")
                return redirect('head_firsts2')
    return render(request, 'result/first_update_head.html', {'form': form, 'first': first})

@login_required
def updateSecondHead(request, id):
    first = Second.objects.get(id=id)
    form = SecondFormHead(instance=first)
    if request.method=='POST':
        form = SecondFormHead(request.POST, instance=first)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            reg = Second.objects.get(id=id)
            if reg.session.second_head != request.user:
                messages.error(request, "Only the head of schools can enter the comment.")
            else:
                reg.student = student
                teacher = request.user
                teacher_name = teacher.last_name
                student_first_name = student.first_name
                student_last_name = student.last_name
                student_email = student.email
                reg.save()
                reg1 = Second.objects.filter(session=session, student=student)
                for each in reg1:
                    each.number_present = reg.number_present
                    # each.static_number = str(reg.session.first_number)
                    # each.absent = int(each.static_number) - each.number_present
                    each.save()
            # send_mail(
            #     '[' + str(session) + '] SCORES UPDATE',
            #     "New Scores have been recorded. Teacher's Name: " + str(teacher_name) + "student: " + str(student) + "student's Name: " + str(student_first_name) + str(student_last_name),
            #     'yustaoab@gmail.com',
            #     [student_email],
            #     fail_silently=False,
            #     #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            # )
                messages.success(request, str(student_first_name) + "'s comment has been recorded successfully")
                return redirect('head_seconds2')
    return render(request, 'result/second_update_head.html', {'form': form, 'first': first})

@login_required
def updateAdminFirstBeha(request, id):
    first = First.objects.get(id=id)
    form = FirstFormBeha(instance=first)
    if request.method=='POST':
        form = FirstFormBeha(request.POST, instance=first)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            reg = First.objects.get(id=id)
            reg.student = student
            teacher = request.user
            teacher_name = teacher.last_name
            student_first_name = student.first_name
            student_last_name = student.last_name
            student_email = student.email
            reg.save()
            reg1 = First.objects.filter(session=session, student=student)
            for each in reg1:
                each.number_present = reg.number_present
                each.concentration = reg.concentration
                each.responsiveness = reg.responsiveness
                each.comprehension = reg.comprehension
                each.interest = reg.interest
                each.homework = reg.homework
                each.reading = reg.reading
                each.writing = reg.writing
                each.spoken = reg.spoken
                each.innovative = reg.innovative
                each.save()
        # send_mail(
        #     '[' + str(session) + '] SCORES UPDATE',
        #     "New Scores have been recorded. Teacher's Name: " + str(teacher_name) + "student: " + str(student) + "student's Name: " + str(student_first_name) + str(student_last_name),
        #     'yustaoab@gmail.com',
        #     [student_email],
        #     fail_silently=False,
        #     #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
        # )
            messages.success(request, str(student_first_name) + "'s attitude to study and scholastic skills have been recorded successfully")
            return redirect('admin_firsts2')
    return render(request, 'result/admin_first_update_beha.html', {'form': form, 'first': first})

@login_required
def addFirst(request, id):
    stud = Person.objects.get(id=id)
    teacher = request.user
    teacher_name = teacher.last_name
    student_first_name = stud.first_name
    student_last_name = stud.last_name
    student_email = stud.email
    form = FirstForm(request=request)
    if request.method=='POST':
        form = FirstForm(request.POST or None, request=request)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            subject = form.cleaned_data.get('subject')
            class_students_count = Person.objects.filter(classe=stud.classe).count()
            reg = First.objects.filter(session=session, subject=subject)[0]
            if reg.subject.teacher != request.user:
                messages.error(request, "You cannot record a score for " + str(subject) + " because you were not assigned as the subject's teacher")
                reg.delete()
            else:
                try:
                    reg2 = First.objects.filter(session=session, student=stud, subject=subject)[0]
                    messages.error(request, student_first_name + " already exists in the score sheet for " + str(subject) +". To modify, click Scores by the left panel")
                    reg.delete()
                except:
                    reg.student = stud
                    teacher = request.user
                    teacher_name = teacher.last_name
                    student_first_name = stud.first_name
                    student_last_name = stud.last_name
                    student_email = stud.email
                    total = reg.ca1 + reg.ca2 + reg.exam
                    reg.total = total
                    reg.save()
                    try:
                        reg7 = First.objects.get(session=session, student=stud)
                        reg7.value = 1
                        reg7.save()
                    except:
                        pass
                    reg4 = First.objects.filter(session=session, subject=subject).order_by('-total')
                    n = reg4.count()
                    try:
                        reg3 = First.objects.filter(session=session, subject=subject)[1]
                        reg3.subject_total = reg3.subject_total + total
                        reg3.save()
                        reg5 = First.objects.filter(session=session, subject=subject)[1]
                        d = round((reg5.subject_total/n),2)
                        subject_position = []
                        # subject_pos =
                    except:
                        reg3 = First.objects.filter(session=session, subject=subject)[0]
                        reg3.subject_total = reg3.subject_total + total
                        reg3.save()
                        reg5 = First.objects.filter(session=session, subject=subject)[0]
                        d = round((reg5.subject_total/n),2)
                        subject_position = []
                        # subject_pos = 0
                    for each in reg4:
                        each.subject_total = reg5.subject_total
                        each.subject_avg = d
                        each.grade = reg5.grade()
                        each.save()

                    for each in reg4:
                        subject_position.append(each.total)

                    for i in range(len(subject_position)):
                        for each in reg4:
                            temp = subject_position.index(each.total)
                            each.subject_pos = temp + 1
                            each.save()

                    reg6 = First.objects.filter(session=session, student=stud)
                    m = reg6.count()
                    all_total = First.objects.filter(session=session, student=stud).aggregate(Sum('total'))['total__sum']
                    cum_perc = round((all_total/m),2)
                    for each in reg6:
                        each.cumulative = all_total
                        each.cum_perc = cum_perc
                        each.static_class = str(each.student.classe)
                        each.static_class_teacher = str(each.student.classe.teacher.first_name) + " " + str(each.student.classe.teacher.last_name)
                        each.static_head_teacher = str(each.session.first_head.first_name) + " " + str(each.session.first_head.last_name)
                        each.static_teacher_signature = each.student.classe.signature
                        each.static_school_stamp = each.session.school
                        each.static_student_image = each.student.photograph
                        each.static_age = each.student.age()
                        each.static_number_in_class = class_students_count
                        each.save()
                    try:
                        reg8 = First.objects.get(session=session, student=stud, value=1)
                        if reg8.school_fees == True:
                            reg9 = First.objects.filter(session=session, student=stud)[0]
                            reg9.school_fees = True
                            reg9.save()
                    except:
                        pass


                    # send_mail(
                    #     '[' + str(session) + '] SCORES UPDATE',
                    #     "New Scores have been recorded. Teacher's Name: " + str(teacher_name) + "student: " + str(stud) + "student's Name: " + str(student_first_name) + str(student_last_name),
                    #     'yustaoab@gmail.com',
                    #     [student_email],
                    #     fail_silently=False,
                    #     #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
                    # )
                    messages.success(request, str(student_first_name) + "'s score has been added successfully")
                    return redirect('staff_students_first')
        else:
            messages.error(request, "Please review form input fields below")
    return render(request, 'result/first.html', {'form': form, 'student_first_name': student_first_name, 'student_last_name': student_last_name,})

@login_required
def addSecond(request, id):
    stud = Person.objects.get(id=id)
    teacher = request.user
    teacher_name = teacher.last_name
    student_first_name = stud.first_name
    student_last_name = stud.last_name
    student_email = stud.email
    form = SecondForm(request=request)
    if request.method=='POST':
        form = SecondForm(request.POST or None, request=request)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            subject = form.cleaned_data.get('subject')
            class_students_count = Person.objects.filter(classe=stud.classe).count()
            reg = Second.objects.filter(session=session, subject=subject)[0]
            if reg.subject.teacher != request.user:
                messages.error(request, "You cannot record a score for " + str(subject) + " because you were not assigned as the subject's teacher")
                reg.delete()
            else:
                try:
                    reg2 = Second.objects.filter(session=session, student=stud, subject=subject)[0]
                    messages.error(request, student_first_name + " already exists in the score sheet for " + str(subject) +". To modify, click Scores by the left panel")
                    reg.delete()
                except:
                    reg.student = stud
                    teacher = request.user
                    teacher_name = teacher.last_name
                    student_first_name = stud.first_name
                    student_last_name = stud.last_name
                    student_email = stud.email
                    total = reg.ca1 + reg.ca2 + reg.exam
                    reg.total = total
                    reg.save()
                    try:
                        reg7 = Second.objects.get(session=session, student=stud)
                        reg7.value = 1
                        reg7.save()
                    except:
                        pass
                    reg4 = Second.objects.filter(session=session, subject=subject).order_by('-total')
                    n = reg4.count()
                    try:
                        reg3 = Second.objects.filter(session=session, subject=subject)[1]
                        reg3.subject_total = reg3.subject_total + total
                        reg3.save()
                        reg5 = Second.objects.filter(session=session, subject=subject)[1]
                        d = round((reg5.subject_total/n),2)
                        subject_position = []
                        # subject_pos =
                    except:
                        reg3 = Second.objects.filter(session=session, subject=subject)[0]
                        reg3.subject_total = reg3.subject_total + total
                        reg3.save()
                        reg5 = Second.objects.filter(session=session, subject=subject)[0]
                        d = round((reg5.subject_total/n),2)
                        subject_position = []
                        # subject_pos = 0
                    for each in reg4:
                        each.subject_total = reg5.subject_total
                        each.subject_avg = d
                        each.grade = reg5.grade()
                        each.save()

                    for each in reg4:
                        subject_position.append(each.total)

                    for i in range(len(subject_position)):
                        for each in reg4:
                            temp = subject_position.index(each.total)
                            each.subject_pos = temp + 1
                            each.save()

                    reg6 = Second.objects.filter(session=session, student=stud)
                    m = reg6.count()
                    all_total = Second.objects.filter(session=session, student=stud).aggregate(Sum('total'))['total__sum']
                    cum_perc = round((all_total/m),2)
                    for each in reg6:
                        each.cumulative = all_total
                        each.cum_perc = cum_perc
                        each.static_class = str(each.student.classe)
                        each.static_class_teacher = str(each.student.classe.teacher.first_name) + " " + str(each.student.classe.teacher.last_name)
                        each.static_head_teacher = str(each.session.second_head.first_name) + " " + str(each.session.second_head.last_name)
                        each.static_teacher_signature = each.student.classe.signature
                        each.static_school_stamp = each.session.school
                        each.static_student_image = each.student.photograph
                        each.static_age = each.student.age()
                        each.static_number_in_class = class_students_count
                        each.save()
                    try:
                        reg8 = Second.objects.get(session=session, student=stud, value=1)
                        if reg8.school_fees == True:
                            reg9 = Second.objects.filter(session=session, student=stud)[0]
                            reg9.school_fees = True
                            reg9.save()
                    except:
                        pass


                    # send_mail(
                    #     '[' + str(session) + '] SCORES UPDATE',
                    #     "New Scores have been recorded. Teacher's Name: " + str(teacher_name) + "student: " + str(stud) + "student's Name: " + str(student_first_name) + str(student_last_name),
                    #     'yustaoab@gmail.com',
                    #     [student_email],
                    #     fail_silently=False,
                    #     #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
                    # )
                    messages.success(request, str(student_first_name) + "'s score has been added successfully")
                    return redirect('staff_students_second')
        else:
            messages.error(request, "Please review form input fields below")
    return render(request, 'result/second.html', {'form': form, 'student_first_name': student_first_name, 'student_last_name': student_last_name,})

@login_required
def addThird(request, id):
    stud = Person.objects.get(id=id)
    teacher = request.user
    teacher_name = teacher.last_name
    student_first_name = stud.first_name
    student_last_name = stud.last_name
    student_email = stud.email
    form = ThirdForm(request=request)
    if request.method=='POST':
        form = ThirdForm(request.POST or None, request=request)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            subject = form.cleaned_data.get('subject')
            class_students_count = Person.objects.filter(classe=stud.classe).count()
            reg = Third.objects.filter(session=session, subject=subject)[0]
            if reg.subject.teacher != request.user:
                messages.error(request, "You cannot record a score for " + str(subject) + " because you were not assigned as the subject's teacher")
                reg.delete()
            else:
                try:
                    reg2 = Third.objects.filter(session=session, student=stud, subject=subject)[0]
                    messages.error(request, student_first_name + " already exists in the score sheet for " + str(subject) +". To modify, click Scores by the left panel")
                    reg.delete()
                except:
                    reg.student = stud
                    teacher = request.user
                    teacher_name = teacher.last_name
                    student_first_name = stud.first_name
                    student_last_name = stud.last_name
                    student_email = stud.email
                    total = reg.ca1 + reg.ca2 + reg.exam
                    reg.total = total
                    try:
                        first_reg = First.objects.get(session=session, student=stud, subject=subject)
                        terms_total0 = first_reg.total + total
                        terms_subject_total0 = first_reg.subject_total + total
                    except:
                        first_reg = First.objects.filter(session=session, subject=subject)[0]
                        terms_total0 = total + total
                        terms_subject_total0 = first_reg.subject_total + total + total
                    try:
                        second_reg = Second.objects.get(session=session, student=stud, subject=subject)
                        terms_total1 = second_reg.total + terms_total0
                        terms_subject_total1 = second_reg.subject_total + terms_subject_total0
                        reg.terms_total = terms_total1
                        reg.subject_total = terms_subject_total1
                    except:
                        second_reg = Second.objects.filter(session=session, subject=subject)[0]
                        terms_total1 = terms_total0 + total
                        terms_subject_total1 = second_reg.subject_total + terms_subject_total0 + total
                        reg.terms_total = terms_total1
                        reg.subject_total = terms_subject_total1
                    reg.save()
                    try:
                        reg7 = Third.objects.get(session=session, student=stud)
                        reg7.value = 1
                        reg7.save()
                    except:
                        pass
                    reg4 = Third.objects.filter(session=session, subject=subject).order_by('-terms_total')
                    n = reg4.count()
                    try:
                        # reg3 = Third.objects.filter(session=session, subject=subject)[1]
                        # reg3.subject_total = reg3.subject_total + terms_total1
                        # reg3.save()
                        reg5 = Third.objects.filter(session=session, subject=subject)[1]
                        d = round((reg5.subject_total/(3*n)),2)
                        subject_position = []
                        # subject_pos =
                    except:
                        # reg3 = Third.objects.filter(session=session, subject=subject)[0]
                        # reg3.subject_total = reg3.subject_total + terms_total1
                        # reg3.save()
                        reg5 = Third.objects.filter(session=session, subject=subject)[0]
                        d = round((reg5.subject_total/(3*n)),2)
                        subject_position = []
                        # subject_pos = 0
                    for each in reg4:
                        each.subject_total = reg5.subject_total
                        each.subject_avg = d
                        each.grade = reg5.grade()
                        each.save()

                    for each in reg4:
                        subject_position.append(each.terms_total)

                    for i in range(len(subject_position)):
                        for each in reg4:
                            temp = subject_position.index(each.terms_total)
                            each.subject_pos = temp + 1
                            each.save()

                    reg6 = Third.objects.filter(session=session, student=stud)
                    m = reg6.count()
                    all_total = Third.objects.filter(session=session, student=stud).aggregate(Sum('terms_total'))['terms_total__sum']
                    cum_perc = round((all_total/m),2)
                    for each in reg6:
                        each.cumulative = all_total
                        each.cum_perc = cum_perc
                        each.static_class = str(each.student.classe)
                        each.static_class_teacher = str(each.student.classe.teacher.first_name) + " " + str(each.student.classe.teacher.last_name)
                        each.static_head_teacher = str(each.session.third_head.first_name) + " " + str(each.session.third_head.last_name)
                        each.static_teacher_signature = each.student.classe.signature
                        each.static_school_stamp = each.session.school
                        each.static_student_image = each.student.photograph
                        each.static_age = each.student.age()
                        each.static_number_in_class = class_students_count
                        each.save()
                    try:
                        reg8 = Third.objects.get(session=session, student=stud, value=1)
                        if reg8.school_fees == True:
                            reg9 = Third.objects.filter(session=session, student=stud)[0]
                            reg9.school_fees = True
                            reg9.save()
                    except:
                        pass
                    # send_mail(
                    #     '[' + str(session) + '] SCORES UPDATE',
                    #     "New Scores have been recorded. Teacher's Name: " + str(teacher_name) + "student: " + str(stud) + "student's Name: " + str(student_first_name) + str(student_last_name),
                    #     'yustaoab@gmail.com',
                    #     [student_email],
                    #     fail_silently=False,
                    #     #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
                    # )
                    messages.success(request, str(student_first_name) + "'s score has been added successfully")
                    return redirect('staff_students_third')
        else:
            messages.error(request, "Please review form input fields below")
    return render(request, 'result/third.html', {'form': form, 'student_first_name': student_first_name, 'student_last_name': student_last_name,})

@login_required
def showReportUser(request, pk, **kwargs):
    first = First.objects.get(id=pk)
    student = first.student
    session = first.session
    firsts = First.objects.all()
    firsts_student = First.objects.filter(session=session, student=student).order_by('subject__serial')
    obtainable = First.objects.filter(session=session, student=student).count()
    obtainable = 100 * obtainable
    grade_general = first.grade_general
    teacher_comment = first.teacher_comment
    head_comment = first.head_comment
    response_first = []
    response_first_student = []
    for each in firsts:
        response_first.append(each)
    for each in firsts_student:
        response_first_student.append(each)
    return render(request, 'result/first_report_user.html', {'firsts':response_first,
    'firsts_student':response_first_student, 'first': first, 'obtainable':obtainable, 'grade_general':grade_general,
    'teacher_comment':teacher_comment, 'head_comment':head_comment})

@login_required
def showReportUserSecond(request, pk, **kwargs):
    first = Second.objects.get(id=pk)
    student = first.student
    session = first.session
    firsts = Second.objects.all()
    firsts_student = Second.objects.filter(session=session, student=student).order_by('subject__serial')
    obtainable = Second.objects.filter(session=session, student=student).count()
    obtainable = 100 * obtainable
    grade_general = first.grade_general
    teacher_comment = first.teacher_comment
    head_comment = first.head_comment
    response_first = []
    response_first_student = []

    for each in firsts:
        response_first.append(each)
    for each in firsts_student:
        response_first_student.append(each)
    return render(request, 'result/second_report_user.html', {'firsts':response_first,
    'firsts_student':response_first_student, 'first': first, 'obtainable':obtainable, 'grade_general':grade_general,
    'teacher_comment':teacher_comment, 'head_comment':head_comment})

@login_required
def showReportCt(request, pk, **kwargs):
    first = First.objects.get(id=pk)
    student = first.student
    session = first.session
    firsts = First.objects.all()
    firsts_student = First.objects.filter(session=session, student=student).order_by('subject__serial')
    obtainable = First.objects.filter(session=session, student=student).count()
    obtainable = 100 * obtainable
    grade_general = first.grade_general
    teacher_comment = first.teacher_comment
    head_comment = first.head_comment
    response_first = []
    response_first_student = []
    for each in firsts:
        response_first.append(each)
    for each in firsts_student:
        response_first_student.append(each)
    return render(request, 'result/first_report_ct.html', {'firsts':response_first, 'firsts_student':response_first_student, 'first': first, 'obtainable':obtainable, 'grade_general':grade_general,
    'teacher_comment':teacher_comment, 'head_comment':head_comment})

@login_required
def showReportCtSecond(request, pk, **kwargs):
    first = Second.objects.get(id=pk)
    student = first.student
    session = first.session
    firsts = Second.objects.all()
    firsts_student = Second.objects.filter(session=session, student=student).order_by('subject__serial')
    obtainable = Second.objects.filter(session=session, student=student).count()
    obtainable = 100 * obtainable
    grade_general = first.grade_general
    teacher_comment = first.teacher_comment
    head_comment = first.head_comment
    response_first = []
    response_first_student = []
    for each in firsts:
        response_first.append(each)
    for each in firsts_student:
        response_first_student.append(each)
    return render(request, 'result/second_report_ct.html', {'firsts':response_first,
    'firsts_student':response_first_student, 'first': first, 'obtainable':obtainable, 'grade_general':grade_general,
    'teacher_comment':teacher_comment, 'head_comment':head_comment})

@login_required
def showReportHead(request, pk, **kwargs):
    first = First.objects.get(id=pk)
    student = first.student
    session = first.session
    firsts = First.objects.all()
    firsts_student = First.objects.filter(session=session, student=student).order_by('subject__serial')
    obtainable = First.objects.filter(session=session, student=student).count()
    obtainable = 100 * obtainable
    grade_general = first.grade_general
    teacher_comment = first.teacher_comment
    head_comment = first.head_comment
    response_first = []
    response_first_student = []
    for each in firsts:
        response_first.append(each)
    for each in firsts_student:
        response_first_student.append(each)
    return render(request, 'result/first_report_head.html', {'firsts':response_first,
    'firsts_student':response_first_student, 'first': first, 'obtainable':obtainable, 'grade_general':grade_general,
    'teacher_comment':teacher_comment, 'head_comment':head_comment})

@login_required
def showReportHeadSecond(request, pk, **kwargs):
    first = Second.objects.get(id=pk)
    student = first.student
    session = first.session
    firsts = Second.objects.all()
    firsts_student = Second.objects.filter(session=session, student=student).order_by('subject__serial')
    obtainable = Second.objects.filter(session=session, student=student).count()
    obtainable = 100 * obtainable
    grade_general = first.grade_general
    teacher_comment = first.teacher_comment
    head_comment = first.head_comment
    response_first = []
    response_first_student = []
    for each in firsts:
        response_first.append(each)
    for each in firsts_student:
        response_first_student.append(each)
    return render(request, 'result/second_report_head.html', {'firsts':response_first, 'firsts_student':response_first_student, 'first': first, 'obtainable':obtainable, 'grade_general':grade_general,
    'teacher_comment':teacher_comment, 'head_comment':head_comment})

@login_required
def showReportAdmin(request, pk, **kwargs):
    first = First.objects.get(id=pk)
    student = first.student
    session = first.session
    firsts = First.objects.all()
    firsts_student = First.objects.filter(session=session, student=student).order_by('subject__serial')
    obtainable = First.objects.filter(session=session, student=student).count()
    obtainable = 100 * obtainable
    grade_general = first.grade_general
    teacher_comment = first.teacher_comment
    head_comment = first.head_comment
    response_first = []
    response_first_student = []
    class_students_count = Person.objects.filter(classe__teacher=request.user).count()
    for each in firsts:
        response_first.append(each)
    for each in firsts_student:
        response_first_student.append(each)
    return render(request, 'result/first_report_admin.html', {'firsts':response_first, 'firsts_student':response_first_student, 'first': first, 'obtainable':obtainable, 'grade_general':grade_general,
    'teacher_comment':teacher_comment, 'head_comment':head_comment})

@login_required
def deleteFirst(request, id):
    first = First.objects.get(id=id)
    obj = get_object_or_404(First, id=id)
    session = first.session
    student = first.student
    subject = first.subject
    reg = First.objects.get(session=session, student=student, subject=subject)
    old_total = reg.total
    value = reg.value
    if request.method =="POST":
        obj.delete()
        try:
            reg1 = First.objects.filter(session=session, subject=subject)[0]
            reg1.subject_total = reg1.subject_total - old_total
            reg1.save()
        except:
            pass
        try:
            reg2 = First.objects.filter(session=session, subject=subject)[0]
            reg4 = First.objects.filter(session=session, subject=subject).order_by('-total')
            n = reg4.count()
            d = round((reg2.subject_total/n),2)
            subject_position = []
            subject_pos = 0

            for each in reg4:
                each.subject_total = reg2.subject_total
                each.subject_avg = d
                each.grade = reg2.grade()
                each.save()
            for each in reg4:
                subject_position.append(each.total)

            for i in range(len(subject_position)):
                for each in reg4:
                    temp = subject_position.index(each.total)
                    each.subject_pos = temp + 1
                    each.save()

        except:
            pass
        try:
            reg6 = First.objects.filter(session=session, student=student)
            m = reg6.count()
            all_total = First.objects.filter(session=session, student=student).aggregate(Sum('total'))['total__sum']
            cum_perc = round((all_total/m),2)
            for each in reg6:
                each.cumulative = all_total
                each.cum_perc = cum_perc
                each.static_class = str(each.student.classe)
                each.save()
            reg7 = First.objects.filter(session=session, student=student)[0]
            if value == 1:
                reg7.value = 1
                reg7.save()
        except:
            pass

        return redirect('firsts')
    return render(request, 'result/firsts_confirm_delete.html', {'first': first})

@login_required
def deleteSecond(request, id):
    first = Second.objects.get(id=id)
    obj = get_object_or_404(Second, id=id)
    session = first.session
    student = first.student
    subject = first.subject
    reg = Second.objects.get(session=session, student=student, subject=subject)
    old_total = reg.total
    value = reg.value
    if request.method =="POST":
        obj.delete()
        try:
            reg1 = Second.objects.filter(session=session, subject=subject)[0]
            reg1.subject_total = reg1.subject_total - old_total
            reg1.save()
        except:
            pass
        try:
            reg2 = Second.objects.filter(session=session, subject=subject)[0]
            reg4 = Second.objects.filter(session=session, subject=subject).order_by('-total')
            n = reg4.count()
            d = round((reg2.subject_total/n),2)
            subject_position = []
            subject_pos = 0

            for each in reg4:
                each.subject_total = reg2.subject_total
                each.subject_avg = d
                each.grade = reg2.grade()
                each.save()
            for each in reg4:
                subject_position.append(each.total)

            for i in range(len(subject_position)):
                for each in reg4:
                    temp = subject_position.index(each.total)
                    each.subject_pos = temp + 1
                    each.save()
        except:
            pass
        try:
            reg6 = Second.objects.filter(session=session, student=student)
            m = reg6.count()
            all_total = Second.objects.filter(session=session, student=student).aggregate(Sum('total'))['total__sum']
            cum_perc = round((all_total/m),2)
            for each in reg6:
                each.cumulative = all_total
                each.cum_perc = cum_perc
                each.static_class = str(each.student.classe)
                each.save()
            reg7 = Second.objects.filter(session=session, student=student)[0]
            if value == 1:
                reg7.value = 1
                reg7.save()
        except:
            pass

        return redirect('seconds')
    return render(request, 'result/seconds_confirm_delete.html', {'first': first})

@login_required
def deleteAdminFirst(request, id):
    first = First.objects.get(id=id)
    obj = get_object_or_404(First, id=id)
    session = first.session
    student = first.student
    subject = first.subject
    reg = First.objects.get(session=session, student=student, subject=subject)
    old_total = reg.total
    value = reg.value
    if request.method =="POST":
        obj.delete()
        try:
            reg1 = First.objects.filter(session=session, subject=subject)[0]
            reg1.subject_total = reg1.subject_total - old_total
            reg1.save()
        except:
            pass
        try:
            reg2 = First.objects.filter(session=session, subject=subject)[0]
            reg4 = First.objects.filter(session=session, subject=subject).order_by('-total')
            n = reg4.count()
            d = round((reg2.subject_total/n),2)
            subject_position = []
            subject_pos = 0

            for each in reg4:
                each.subject_total = reg2.subject_total
                each.subject_avg = d
                each.grade = reg2.grade()
                each.save()
            for each in reg4:
                subject_position.append(each.total)

            for i in range(len(subject_position)):
                for each in reg4:
                    temp = subject_position.index(each.total)
                    each.subject_pos = temp + 1
                    each.save()
        except:
            pass
        try:
            reg6 = First.objects.filter(session=session, student=student)
            m = reg6.count()
            all_total = First.objects.filter(session=session, student=student).aggregate(Sum('total'))['total__sum']
            cum_perc = round((all_total/m),2)
            for each in reg6:
                each.cumulative = all_total
                each.cum_perc = cum_perc
                each.static_class = str(each.student.classe)
                each.save()
            reg7 = First.objects.filter(session=session, student=student)[0]
            if value == 1:
                reg7.value = 1
                reg7.save()
        except:
            pass

        return redirect('admin_firsts')
    return render(request, 'result/firsts_admin_confirm_delete.html', {'first': first})

@login_required
def showFirstsPay(request):
    context = {}
    filtered_firsts = FirstFilterPay(
        request.GET,
        queryset = First.objects.filter(value=1)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/first_pay.html', context=context)

@login_required
def showSecondsPay(request):
    context = {}
    filtered_firsts = SecondFilterPay(
        request.GET,
        queryset = Second.objects.filter(value=1)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/second_pay.html', context=context)

def updateFirstPay(request, id):
    first = First.objects.get(id=id)
    form = FirstFormPay(instance=first)
    if request.method=='POST':
        form = FirstFormPay(request.POST, instance=first)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            reg = First.objects.get(id=id)
            reg.student = student
            student_first_name = student.first_name
            student_last_name = student.last_name
            student_email = student.email
            reg.save()
            reg1 = First.objects.filter(session=session, student=student)
            for each in reg1:
                each.school_fees = reg.school_fees
                each.save()

            messages.success(request, "The student's payment has been modified successfully")
            return redirect('firsts_pay')
    return render(request, 'result/payment_update_first.html', {'form': form, 'first':first})

def updateSecondPay(request, id):
    first = Second.objects.get(id=id)
    form = SecondFormPay(instance=first)
    if request.method=='POST':
        form = SecondFormPay(request.POST, instance=first)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            reg = Second.objects.get(id=id)
            reg.student = student
            student_first_name = student.first_name
            student_last_name = student.last_name
            student_email = student.email
            reg.save()
            reg1 = Second.objects.filter(session=session, student=student)
            for each in reg1:
                each.school_fees = reg.school_fees
                each.save()

            messages.success(request, "The student's payment has been modified successfully")
            return redirect('seconds_pay')
    return render(request, 'result/payment_update_second.html', {'form': form, 'first':first})

def exportCSVSecondScores(request):
    seconds = Second.objects.all().order_by('-subject__classe')
    response = HttpResponse(content_type='text/csv')
    now = datetime.datetime.now().strftime('%A_%d_%b_%Y')
    response['Content-Disposition'] = 'attachment; filename=Second term scores downloaded on ' + str(now) + '.csv'

    writer = csv.writer(response)
    writer.writerow(['Session', 'Class', 'Subject', 'Scholar', 'Total', 'Grade'])

    for each in seconds:
        writer.writerow(
            [each.session, each.subject.classe, each.subject.subject, each.student, each.total, each.grade()]
        )
    return response
