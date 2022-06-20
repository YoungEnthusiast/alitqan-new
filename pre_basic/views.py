from django.shortcuts import render, redirect
from .models import FirstTerm, SecondTerm, ThirdTerm
from .forms import FirstTermForm, FirstTermFormUp, SecondTermForm, SecondTermFormUp, ThirdTermForm, ThirdTermFormUp
from django.contrib import messages
from django.core.paginator import Paginator
from .filters import FirstFilter, SecondFilter, ThirdFilter
from django.contrib.auth.decorators import login_required#, permission_required
from django.core.mail import send_mail
#from django.template.loader import render_to_string

@login_required
def showFirsts(request):
    context = {}
    filtered_firsts = FirstFilter(
        request.GET,
        queryset = FirstTerm.objects.all()
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'pre_basic/first_list.html', context=context)

@login_required
def updateFirsts(request, id):
    first = FirstTerm.objects.get(id=id)
    form = FirstTermFormUp(instance=first)
    if request.method=='POST':
        form = FirstTermFormUp(request.POST, instance=first)
        if form.is_valid():
            form.save()
            teacher = request.user
            teacher_name = teacher.last_name
            session = form.cleaned_data.get('session')
            pupil = form.cleaned_data.get('pupil')
            pupil_first_name = pupil.user.first_name
            pupil_last_name = pupil.user.last_name
            pupil_email = pupil.user.email
            reg = FirstTerm.objects.get(pupil=pupil)
            literacy_tot = reg.literacy_ca1 + reg.literacy_ca2 + reg.literacy_exam
            numeracy_tot = reg.numeracy_ca1 + reg.numeracy_ca2 + reg.numeracy_exam
            general_studies_tot = reg.general_studies_ca1 + reg.general_studies_ca2 + reg.general_studies_exam
            science_tot = reg.science_ca1 + reg.science_ca2 + reg.science_exam
            cumulative = (reg.literacy_ca1 + reg.numeracy_ca1 + reg.general_studies_ca1
                + reg.science_ca1 + reg.literacy_ca2 + reg.numeracy_ca2
                + reg.general_studies_ca2 + reg.science_ca2 + reg.literacy_exam
                + reg.numeracy_exam + reg.general_studies_exam + reg.science_exam
                )
            reg.literacy_tot = literacy_tot
            reg.numeracy_tot = numeracy_tot
            reg.general_studies_tot = general_studies_tot
            reg.science_tot = science_tot
            reg.cumulative = cumulative
            reg.save()
            send_mail(
                '[' + str(session) + '] SCORES UPDATE',
                'New Scores have been recorded. Current Total: ' + str(cumulative) + "Teacher's Name: " + str(teacher_name) + "Pupil: " + str(pupil) + "Pupil's Name: " + str(pupil_first_name) + str(pupil_last_name),
                'yustaoab@gmail.com',
                [pupil_email],
                fail_silently=False,
                #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            )
            messages.success(request, str(pupil_first_name) + "'s score has been modified successfully")
            return redirect('firsts')
    return render(request, 'pre_basic/first_form_update.html', {'form': form, 'first': first})

@login_required
def addFirst(request, **kwargs):
    form = FirstTermForm()
    if request.method == 'POST':
        form = FirstTermForm(request.POST or None)
        if form.is_valid():
            form.save()
            teacher = request.user
            teacher_name = teacher.last_name
            session = form.cleaned_data.get('session')
            pupil = form.cleaned_data.get('pupil')
            pupil_first_name = pupil.user.first_name
            pupil_last_name = pupil.user.last_name
            pupil_email = pupil.user.email
            reg = FirstTerm.objects.get(pupil=pupil)
            literacy_tot = reg.literacy_ca1 + reg.literacy_ca2 + reg.literacy_exam
            numeracy_tot = reg.numeracy_ca1 + reg.numeracy_ca2 + reg.numeracy_exam
            general_studies_tot = reg.general_studies_ca1 + reg.general_studies_ca2 + reg.general_studies_exam
            science_tot = reg.science_ca1 + reg.science_ca2 + reg.science_exam

            cumulative = (reg.literacy_ca1 + reg.numeracy_ca1 + reg.general_studies_ca1
                + reg.science_ca1 + reg.literacy_ca2 + reg.numeracy_ca2
                + reg.general_studies_ca2 + reg.science_ca2 + reg.literacy_exam
                + reg.numeracy_exam + reg.general_studies_exam + reg.science_exam
                )
            reg.literacy_tot = literacy_tot
            reg.numeracy_tot = numeracy_tot
            reg.general_studies_tot = general_studies_tot
            reg.science_tot = science_tot
            reg.cumulative = cumulative
            reg.save()
            send_mail(
                '[' + str(session) + '] SCORES UPDATE',
                'New Scores have been recorded. Current Total: ' + str(cumulative) + "Teacher's Name: " + str(teacher_name) + "Pupil: " + str(pupil) + "Pupil's Name: " + str(pupil_first_name) + str(pupil_last_name),
                'yustaoab@gmail.com',
                [pupil_email],
                fail_silently=False,
                #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            )
            messages.success(request, str(pupil_first_name) + "'s score has been added successfully")
            return redirect('pre_basic_first')
        else:
            messages.error(request, "Please review form input fields below")
            #return redirect('pre_basic_first')
    return render(request, 'pre_basic/first_form.html', {'form': form})

@login_required
def showFirst(request, **kwargs):
    first = FirstTerm.objects.filter(id=kwargs['pk'])
    response_first = []
    for each in first:
        class_pupils_count = FirstTerm.objects.filter(pupil__classe=each.pupil.classe).count()
        class_pupils = FirstTerm.objects.filter(pupil__classe=each.pupil.classe)

        literacy_tot = 0
        numeracy_tot = 0
        general_studies_tot = 0
        science_tot = 0
        literacy_position = []
        literacy_pos = 0
        numeracy_position = []
        numeracy_pos = 0
        general_studies_position = []
        general_studies_pos = 0
        science_position = []
        science_pos = 0
        for pupil in class_pupils:
            literacy_tot = literacy_tot + pupil.literacy_tot
            numeracy_tot = numeracy_tot + pupil.numeracy_tot
            general_studies_tot = general_studies_tot + pupil.general_studies_tot
            science_tot = science_tot + pupil.science_tot

            literacy_position.append(pupil.literacy_tot)
            literacy_position.sort(reverse=True)
            numeracy_position.append(pupil.numeracy_tot)
            numeracy_position.sort(reverse=True)
            general_studies_position.append(pupil.general_studies_tot)
            general_studies_position.sort(reverse=True)
            science_position.append(pupil.science_tot)
            science_position.sort(reverse=True)

        literacy_avg = round((literacy_tot/class_pupils_count),2)
        numeracy_avg = round((numeracy_tot/class_pupils_count),2)
        general_studies_avg = round((general_studies_tot/class_pupils_count),2)
        science_avg = round((science_tot/class_pupils_count),2)

        for i in range(len(numeracy_position)):
            if numeracy_position[i] == each.numeracy_tot:
                if i in range (10, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (11, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (12, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (0, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "st"
                elif i in range (1, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "nd"
                elif i in range (2, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "rd"
                else:
                    numeracy_pos = str(i + 1) + "th"

        for i in range(len(literacy_position)):
            if literacy_position[i] == each.literacy_tot:
                if i in range (10, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (11, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (12, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (0, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "st"
                elif i in range (1, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "nd"
                elif i in range (2, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "rd"
                else:
                    literacy_pos = str(i + 1) + "th"

        for i in range(len(general_studies_position)):
            if general_studies_position[i] == each.general_studies_tot:
                if i in range (10, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (11, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (12, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (0, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "st"
                elif i in range (1, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "nd"
                elif i in range (2, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "rd"
                else:
                    general_studies_pos = str(i + 1) + "th"

        for i in range(len(science_position)):
            if science_position[i] == each.science_tot:
                if i in range (10, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (11, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (12, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (0, len(science_position), 10):
                    science_pos = str(i + 1) + "st"
                elif i in range (1, len(science_position), 10):
                    science_pos = str(i + 1) + "nd"
                elif i in range (2, len(science_position), 10):
                    science_pos = str(i + 1) + "rd"
                else:
                    science_pos = str(i + 1) + "th"

        response_first.append(each)
    return render(request, 'pre_basic/first_report.html', {'first': response_first,
        'class_pupils_count': class_pupils_count, 'literacy_avg': literacy_avg,
        'numeracy_avg': numeracy_avg, 'general_studies_avg': general_studies_avg,
        'science_avg': science_avg, 'literacy_position': literacy_position,
        'literacy_pos': literacy_pos, 'numeracy_position': numeracy_position,
        'numeracy_pos': numeracy_pos, 'general_studies_position': general_studies_position,
        'general_studies_pos': general_studies_pos, 'science_position': science_position,
        'science_pos': science_pos})

@login_required
def showSeconds(request):
    context = {}
    filtered_seconds = SecondFilter(
        request.GET,
        queryset = SecondTerm.objects.all()
    )
    context['filtered_seconds'] = filtered_seconds
    paginated_filtered_seconds = Paginator(filtered_seconds.qs, 10)
    page_number = request.GET.get('page')
    seconds_page_obj = paginated_filtered_seconds.get_page(page_number)
    context['seconds_page_obj'] = seconds_page_obj
    total_seconds = filtered_seconds.qs.count()
    context['total_seconds'] = total_seconds
    return render(request, 'pre_basic/second_list.html', context=context)

@login_required
def updateSeconds(request, id):
    second = SecondTerm.objects.get(id=id)
    form = SecondTermFormUp(instance=second)
    if request.method=='POST':
        form = SecondTermFormUp(request.POST, instance=second)
        if form.is_valid():
            form.save()
            teacher = request.user
            teacher_name = teacher.last_name
            session = form.cleaned_data.get('session')
            pupil = form.cleaned_data.get('pupil')
            pupil_first_name = pupil.user.first_name
            pupil_last_name = pupil.user.last_name
            pupil_email = pupil.user.email
            reg = SecondTerm.objects.get(pupil=pupil)
            literacy_tot = reg.literacy_ca1 + reg.literacy_ca2 + reg.literacy_exam
            numeracy_tot = reg.numeracy_ca1 + reg.numeracy_ca2 + reg.numeracy_exam
            general_studies_tot = reg.general_studies_ca1 + reg.general_studies_ca2 + reg.general_studies_exam
            science_tot = reg.science_ca1 + reg.science_ca2 + reg.science_exam
            cumulative = (reg.literacy_ca1 + reg.numeracy_ca1 + reg.general_studies_ca1
                + reg.science_ca1 + reg.literacy_ca2 + reg.numeracy_ca2
                + reg.general_studies_ca2 + reg.science_ca2 + reg.literacy_exam
                + reg.numeracy_exam + reg.general_studies_exam + reg.science_exam
                )
            reg.literacy_tot = literacy_tot
            reg.numeracy_tot = numeracy_tot
            reg.general_studies_tot = general_studies_tot
            reg.science_tot = science_tot
            reg.cumulative = cumulative
            reg.save()
            send_mail(
                '[' + str(session) + '] SCORES UPDATE',
                'New Scores have been recorded. Current Total: ' + str(cumulative) + "Teacher's Name: " + str(teacher_name) + "Pupil: " + str(pupil) + "Pupil's Name: " + str(pupil_first_name) + " " + str(pupil_last_name),
                'yustaoab@gmail.com',
                [pupil_email],
                fail_silently=False,
                #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            )
            messages.success(request, str(pupil_first_name) + "'s score has been modified successfully")
            return redirect('seconds')
    return render(request, 'pre_basic/second_form_update.html', {'form': form, 'second': second})

@login_required
def addSecond(request, **kwargs):
    form = SecondTermForm()
    if request.method == 'POST':
        form = SecondTermForm(request.POST or None)
        if form.is_valid():
            form.save()
            teacher = request.user
            teacher_name = teacher.last_name
            session = form.cleaned_data.get('session')
            pupil = form.cleaned_data.get('pupil')
            pupil_first_name = pupil.user.first_name
            pupil_last_name = pupil.user.last_name
            pupil_email = pupil.user.email
            reg = SecondTerm.objects.get(pupil=pupil)
            literacy_tot = reg.literacy_ca1 + reg.literacy_ca2 + reg.literacy_exam
            numeracy_tot = reg.numeracy_ca1 + reg.numeracy_ca2 + reg.numeracy_exam
            general_studies_tot = reg.general_studies_ca1 + reg.general_studies_ca2 + reg.general_studies_exam
            science_tot = reg.science_ca1 + reg.science_ca2 + reg.science_exam

            cumulative = (reg.literacy_ca1 + reg.numeracy_ca1 + reg.general_studies_ca1
                + reg.science_ca1 + reg.literacy_ca2 + reg.numeracy_ca2
                + reg.general_studies_ca2 + reg.science_ca2 + reg.literacy_exam
                + reg.numeracy_exam + reg.general_studies_exam + reg.science_exam
                )
            reg.literacy_tot = literacy_tot
            reg.numeracy_tot = numeracy_tot
            reg.general_studies_tot = general_studies_tot
            reg.science_tot = science_tot
            reg.cumulative = cumulative
            reg.save()
            send_mail(
                '[' + str(session) + '] SCORES UPDATE',
                'New Scores have been recorded. Current Total: ' + str(cumulative) + "Teacher's Name: " + str(teacher_name) + "Pupil: " + str(pupil) + "Pupil's Name: " + str(pupil_first_name) + " " + str(pupil_last_name),
                'yustaoab@gmail.com',
                [pupil_email],
                fail_silently=False,
                #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            )
            messages.success(request, str(pupil_first_name) + "'s score has been added successfully")
            return redirect('pre_basic_second')
        else:
            messages.error(request, "Please review form input fields below")
            #return redirect('pre_basic_second')
    return render(request, 'pre_basic/second_form.html', {'form': form})

@login_required
def showSecond(request, **kwargs):
    second = SecondTerm.objects.filter(id=kwargs['pk'])
    response_second = []
    for each in second:
        class_pupils_count = SecondTerm.objects.filter(pupil__classe=each.pupil.classe).count()
        class_pupils = SecondTerm.objects.filter(pupil__classe=each.pupil.classe)

        literacy_tot = 0
        numeracy_tot = 0
        general_studies_tot = 0
        science_tot = 0
        literacy_position = []
        literacy_pos = 0
        numeracy_position = []
        numeracy_pos = 0
        general_studies_position = []
        general_studies_pos = 0
        science_position = []
        science_pos = 0
        for pupil in class_pupils:
            literacy_tot = literacy_tot + pupil.literacy_tot
            numeracy_tot = numeracy_tot + pupil.numeracy_tot
            general_studies_tot = general_studies_tot + pupil.general_studies_tot
            science_tot = science_tot + pupil.science_tot

            literacy_position.append(pupil.literacy_tot)
            literacy_position.sort(reverse=True)
            numeracy_position.append(pupil.numeracy_tot)
            numeracy_position.sort(reverse=True)
            general_studies_position.append(pupil.general_studies_tot)
            general_studies_position.sort(reverse=True)
            science_position.append(pupil.science_tot)
            science_position.sort(reverse=True)

        literacy_avg = round((literacy_tot/class_pupils_count),2)
        numeracy_avg = round((numeracy_tot/class_pupils_count),2)
        general_studies_avg = round((general_studies_tot/class_pupils_count),2)
        science_avg = round((science_tot/class_pupils_count),2)

        for i in range(len(numeracy_position)):
            if numeracy_position[i] == each.numeracy_tot:
                if i in range (10, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (11, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (12, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (0, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "st"
                elif i in range (1, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "nd"
                elif i in range (2, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "rd"
                else:
                    numeracy_pos = str(i + 1) + "th"

        for i in range(len(literacy_position)):
            if literacy_position[i] == each.literacy_tot:
                if i in range (10, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (11, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (12, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (0, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "st"
                elif i in range (1, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "nd"
                elif i in range (2, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "rd"
                else:
                    literacy_pos = str(i + 1) + "th"

        for i in range(len(general_studies_position)):
            if general_studies_position[i] == each.general_studies_tot:
                if i in range (10, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (11, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (12, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (0, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "st"
                elif i in range (1, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "nd"
                elif i in range (2, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "rd"
                else:
                    general_studies_pos = str(i + 1) + "th"

        for i in range(len(science_position)):
            if science_position[i] == each.science_tot:
                if i in range (10, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (11, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (12, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (0, len(science_position), 10):
                    science_pos = str(i + 1) + "st"
                elif i in range (1, len(science_position), 10):
                    science_pos = str(i + 1) + "nd"
                elif i in range (2, len(science_position), 10):
                    science_pos = str(i + 1) + "rd"
                else:
                    science_pos = str(i + 1) + "th"

        response_second.append(each)
    return render(request, 'pre_basic/second_report.html', {'second': response_second,
        'class_pupils_count': class_pupils_count, 'literacy_avg': literacy_avg,
        'numeracy_avg': numeracy_avg, 'general_studies_avg': general_studies_avg,
        'science_avg': science_avg, 'literacy_position': literacy_position,
        'literacy_pos': literacy_pos, 'numeracy_position': numeracy_position,
        'numeracy_pos': numeracy_pos, 'general_studies_position': general_studies_position,
        'general_studies_pos': general_studies_pos, 'science_position': science_position,
        'science_pos': science_pos})

@login_required
def showThirds(request):
    context = {}
    filtered_thirds = ThirdFilter(
        request.GET,
        queryset = ThirdTerm.objects.all()
    )
    context['filtered_thirds'] = filtered_thirds
    paginated_filtered_thirds = Paginator(filtered_thirds.qs, 10)
    page_number = request.GET.get('page')
    thirds_page_obj = paginated_filtered_thirds.get_page(page_number)
    context['thirds_page_obj'] = thirds_page_obj
    total_thirds = filtered_thirds.qs.count()
    context['total_thirds'] = total_thirds
    return render(request, 'pre_basic/third_list.html', context=context)

@login_required
def updateThirds(request, id):
    third = ThirdTerm.objects.get(id=id)
    form = ThirdTermFormUp(instance=third)
    cum1 = 0
    cum2 = 0
    total_cum = 0
    cum_perc = 0
    if request.method=='POST':
        form = ThirdTermFormUp(request.POST, instance=third)
        if form.is_valid():
            form.save()
            teacher = request.user
            teacher_name = teacher.last_name
            session = form.cleaned_data.get('session')
            pupil = form.cleaned_data.get('pupil')
            pupil_first_name = pupil.user.first_name
            pupil_last_name = pupil.user.last_name
            pupil_email = pupil.user.email
            reg = ThirdTerm.objects.get(pupil=pupil)
            literacy_tot = reg.literacy_ca1 + reg.literacy_ca2 + reg.literacy_exam
            numeracy_tot = reg.numeracy_ca1 + reg.numeracy_ca2 + reg.numeracy_exam
            general_studies_tot = reg.general_studies_ca1 + reg.general_studies_ca2 + reg.general_studies_exam
            science_tot = reg.science_ca1 + reg.science_ca2 + reg.science_exam
            cumulative = (reg.literacy_ca1 + reg.numeracy_ca1 + reg.general_studies_ca1
                + reg.science_ca1 + reg.literacy_ca2 + reg.numeracy_ca2
                + reg.general_studies_ca2 + reg.science_ca2 + reg.literacy_exam
                + reg.numeracy_exam + reg.general_studies_exam + reg.science_exam
                )
            reg.literacy_tot = literacy_tot
            reg.numeracy_tot = numeracy_tot
            reg.general_studies_tot = general_studies_tot
            reg.science_tot = science_tot
            reg.cumulative = cumulative

            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                literacy_tot1 = pup1.literacy_tot
            except:
                literacy_tot1 = None
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                literacy_tot2 = pup2.literacy_tot2
            except:
                literacy_tot2 = None
            if literacy_tot2 == None and literacy_tot1 == None:
                literacy_cum = literacy_tot
            elif literacy_tot2 == None and literacy_tot1 != None:
                literacy_cum = (literacy_tot1 + literacy_tot)/2
            elif literacy_tot2 != None and literacy_tot1 == None:
                literacy_cum = (literacy_tot2 + literacy_tot)/2
            elif literacy_tot2 != None and literacy_tot1 != None:
                literacy_cum = round((literacy_tot2 + literacy_tot1 + literacy_tot)/3, 2)
            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                literacy_tot1 = pup1.literacy_tot
            except:
                pass
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                literacy_tot2 = pup2.literacy_tot
            except:
                pass
            reg.literacy_tot1 = literacy_tot1
            reg.literacy_tot2 = literacy_tot2
            reg.literacy_cum = literacy_cum

            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                numeracy_tot1 = pup1.numeracy_tot
            except:
                numeracy_tot1 = None
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                numeracy_tot2 = pup2.numeracy_tot2
            except:
                numeracy_tot2 = None
            if numeracy_tot2 == None and numeracy_tot1 == None:
                numeracy_cum = numeracy_tot
            elif numeracy_tot2 == None and numeracy_tot1 != None:
                numeracy_cum = (numeracy_tot1 + numeracy_tot)/2
            elif numeracy_tot2 != None and numeracy_tot1 == None:
                numeracy_cum = (numeracy_tot2 + numeracy_tot)/2
            elif numeracy_tot2 != None and numeracy_tot1 != None:
                numeracy_cum = round((numeracy_tot2 + numeracy_tot1 + numeracy_tot)/3, 2)
            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                numeracy_tot1 = pup1.numeracy_tot
            except:
                pass
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                numeracy_tot2 = pup2.numeracy_tot
            except:
                pass
            reg.numeracy_tot1 = numeracy_tot1
            reg.numeracy_tot2 = numeracy_tot2
            reg.numeracy_cum = numeracy_cum

            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                general_studies_tot1 = pup1.general_studies_tot
            except:
                general_studies_tot1 = None
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                general_studies_tot2 = pup2.general_studies_tot2
            except:
                general_studies_tot2 = None
            if general_studies_tot2 == None and general_studies_tot1 == None:
                general_studies_cum = general_studies_tot
            elif general_studies_tot2 == None and general_studies_tot1 != None:
                general_studies_cum = (general_studies_tot1 + general_studies_tot)/2
            elif general_studies_tot2 != None and general_studies_tot1 == None:
                general_studies_cum = (general_studies_tot2 + general_studies_tot)/2
            elif general_studies_tot2 != None and general_studies_tot1 != None:
                general_studies_cum = round((general_studies_tot2 + general_studies_tot1 + general_studies_tot)/3, 2)
            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                general_studies_tot1 = pup1.general_studies_tot
            except:
                pass
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                general_studies_tot2 = pup2.general_studies_tot
            except:
                pass
            reg.general_studies_tot1 = general_studies_tot1
            reg.general_studies_tot2 = general_studies_tot2
            reg.general_studies_cum = general_studies_cum

            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                science_tot1 = pup1.science_tot
            except:
                science_tot1 = None
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                science_tot2 = pup2.science_tot2
            except:
                science_tot2 = None
            if science_tot2 == None and science_tot1 == None:
                science_cum = science_tot
            elif science_tot2 == None and science_tot1 != None:
                science_cum = (science_tot1 + science_tot)/2
            elif science_tot2 != None and science_tot1 == None:
                science_cum = (science_tot2 + science_tot)/2
            elif science_tot2 != None and science_tot1 != None:
                science_cum = round((science_tot2 + science_tot1 + science_tot)/3, 2)
            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                science_tot1 = pup1.science_tot
            except:
                pass
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                science_tot2 = pup2.science_tot
            except:
                pass
            reg.science_tot1 = science_tot1
            reg.science_tot2 = science_tot2
            reg.science_cum = science_cum

            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                cum1 = pup1.cumulative
            except:
                cum1 = None
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                cum2 = pup2.cumulative
            except:
                cum2 = None

            if cum2 == None and cum1 == None:
                total_cum = cumulative
                cum_perc = round((total_cum/4),2)
            elif cum2 == None and cum1 != None:
                total_cum = cum1 + cumulative
                cum_perc = round(total_cum/8, 2)
            elif cum2 != None and cum1 == None:
                total_cum = cum2 + cumulative
                cum_perc = round(total_cum/8, 2)
            elif cum2 != None and cum1 != None:
                total_cum = cum1 + cum2 + cumulative
                cum_perc = round(total_cum/12, 2)
            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                cum1 = pup1.cumulative
            except:
                pass
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                cum2 = pup2.cumulative
            except:
                pass
            reg.cumulative_1st = cum1
            reg.cumulative_2nd = cum2
            reg.all_cumulative = total_cum
            reg.cum_perc = cum_perc
            reg.save()
            send_mail(
                '[' + str(session) + '] SCORES UPDATE',
                'New Scores have been recorded. Current Total: ' + str(cumulative) + "Teacher's Name: " + str(teacher_name) + "Pupil: " + str(pupil) + "Pupil's Name: " + str(pupil_first_name) + " " + str(pupil_last_name),
                'yustaoab@gmail.com',
                [pupil_email],
                fail_silently=False,
                #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            )
            messages.success(request, str(pupil_first_name) + "'s score has been modified successfully")
            return redirect('thirds')
    return render(request, 'pre_basic/third_form_update.html', {'form': form, 'third': third, 'cum_perc': cum_perc})

@login_required
def addThird(request, **kwargs):
    form = ThirdTermForm()
    cum1 = 0
    cum2 = 0
    total_cum0 = 0
    total_cum = 0
    cum_perc = 0
    cum_perc0 = 0
    if request.method == 'POST':
        form = ThirdTermForm(request.POST or None)
        if form.is_valid():
            form.save()
            teacher = request.user
            teacher_name = teacher.last_name
            session = form.cleaned_data.get('session')
            pupil = form.cleaned_data.get('pupil')
            pupil_first_name = pupil.user.first_name
            pupil_last_name = pupil.user.last_name
            pupil_email = pupil.user.email
            reg = ThirdTerm.objects.get(pupil=pupil)
            literacy_tot = reg.literacy_ca1 + reg.literacy_ca2 + reg.literacy_exam
            numeracy_tot = reg.numeracy_ca1 + reg.numeracy_ca2 + reg.numeracy_exam
            general_studies_tot = reg.general_studies_ca1 + reg.general_studies_ca2 + reg.general_studies_exam
            science_tot = reg.science_ca1 + reg.science_ca2 + reg.science_exam

            cumulative = (reg.literacy_ca1 + reg.numeracy_ca1 + reg.general_studies_ca1
                + reg.science_ca1 + reg.literacy_ca2 + reg.numeracy_ca2
                + reg.general_studies_ca2 + reg.science_ca2 + reg.literacy_exam
                + reg.numeracy_exam + reg.general_studies_exam + reg.science_exam
                )
            reg.literacy_tot = literacy_tot
            reg.numeracy_tot = numeracy_tot
            reg.general_studies_tot = general_studies_tot
            reg.science_tot = science_tot
            reg.cumulative = cumulative

            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                literacy_tot1 = pup1.literacy_tot
            except:
                literacy_tot1 = None
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                literacy_tot2 = pup2.literacy_tot2
            except:
                literacy_tot2 = None
            if literacy_tot2 == None and literacy_tot1 == None:
                literacy_cum = literacy_tot
            elif literacy_tot2 == None and literacy_tot1 != None:
                literacy_cum = (literacy_tot1 + literacy_tot)/2
            elif literacy_tot2 != None and literacy_tot1 == None:
                literacy_cum = (literacy_tot2 + literacy_tot)/2
            elif literacy_tot2 != None and literacy_tot1 != None:
                literacy_cum = round((literacy_tot2 + literacy_tot1 + literacy_tot)/3, 2)
            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                literacy_tot1 = pup1.literacy_tot
            except:
                pass
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                literacy_tot2 = pup2.literacy_tot
            except:
                pass
            reg.literacy_tot1 = literacy_tot1
            reg.literacy_tot2 = literacy_tot2
            reg.literacy_cum = literacy_cum

            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                numeracy_tot1 = pup1.numeracy_tot
            except:
                numeracy_tot1 = None
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                numeracy_tot2 = pup2.numeracy_tot2
            except:
                numeracy_tot2 = None
            if numeracy_tot2 == None and numeracy_tot1 == None:
                numeracy_cum = numeracy_tot
            elif numeracy_tot2 == None and numeracy_tot1 != None:
                numeracy_cum = (numeracy_tot1 + numeracy_tot)/2
            elif numeracy_tot2 != None and numeracy_tot1 == None:
                numeracy_cum = (numeracy_tot2 + numeracy_tot)/2
            elif numeracy_tot2 != None and numeracy_tot1 != None:
                numeracy_cum = round((numeracy_tot2 + numeracy_tot1 + numeracy_tot)/3, 2)
            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                numeracy_tot1 = pup1.numeracy_tot
            except:
                pass
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                numeracy_tot2 = pup2.numeracy_tot
            except:
                pass
            reg.numeracy_tot1 = numeracy_tot1
            reg.numeracy_tot2 = numeracy_tot2
            reg.numeracy_cum = numeracy_cum

            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                general_studies_tot1 = pup1.general_studies_tot
            except:
                general_studies_tot1 = None
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                general_studies_tot2 = pup2.general_studies_tot2
            except:
                general_studies_tot2 = None
            if general_studies_tot2 == None and general_studies_tot1 == None:
                general_studies_cum = general_studies_tot
            elif general_studies_tot2 == None and general_studies_tot1 != None:
                general_studies_cum = (general_studies_tot1 + general_studies_tot)/2
            elif general_studies_tot2 != None and general_studies_tot1 == None:
                general_studies_cum = (general_studies_tot2 + general_studies_tot)/2
            elif general_studies_tot2 != None and general_studies_tot1 != None:
                general_studies_cum = round((general_studies_tot2 + general_studies_tot1 + general_studies_tot)/3, 2)
            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                general_studies_tot1 = pup1.general_studies_tot
            except:
                pass
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                general_studies_tot2 = pup2.general_studies_tot
            except:
                pass
            reg.general_studies_tot1 = general_studies_tot1
            reg.general_studies_tot2 = general_studies_tot2
            reg.general_studies_cum = general_studies_cum

            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                science_tot1 = pup1.science_tot
            except:
                science_tot1 = None
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                science_tot2 = pup2.science_tot2
            except:
                science_tot2 = None
            if science_tot2 == None and science_tot1 == None:
                science_cum = science_tot
            elif science_tot2 == None and science_tot1 != None:
                science_cum = (science_tot1 + science_tot)/2
            elif science_tot2 != None and science_tot1 == None:
                science_cum = (science_tot2 + science_tot)/2
            elif science_tot2 != None and science_tot1 != None:
                science_cum = round((science_tot2 + science_tot1 + science_tot)/3, 2)
            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                science_tot1 = pup1.science_tot
            except:
                pass
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                science_tot2 = pup2.science_tot
            except:
                pass
            reg.science_tot1 = science_tot1
            reg.science_tot2 = science_tot2
            reg.science_cum = science_cum

            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                cum1 = pup1.cumulative
            except:
                cum1 = None
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                cum2 = pup2.cumulative
            except:
                cum2 = None

            if cum2 == None and cum1 == None:
                total_cum = cumulative
                cum_perc = round((total_cum/4),2)
            elif cum2 == None and cum1 != None:
                total_cum = cum1 + cumulative
                cum_perc = round(total_cum/8, 2)
            elif cum2 != None and cum1 == None:
                total_cum = cum2 + cumulative
                cum_perc = round(total_cum/8, 2)
            elif cum2 != None and cum1 != None:
                total_cum = cum1 + cum2 + cumulative
                cum_perc = round(total_cum/12, 2)

            try:
                pup1 = FirstTerm.objects.get(pupil=pupil)
                cum1 = pup1.cumulative
            except:
                pass
            try:
                pup2 = SecondTerm.objects.get(pupil=pupil)
                cum2 = pup2.cumulative
            except:
                pass
            reg.cumulative_1st = cum1
            reg.cumulative_2nd = cum2
            reg.all_cumulative = total_cum
            reg.cum_perc = cum_perc
            reg.save()
            send_mail(
                '[' + str(session) + '] SCORES UPDATE',
                'New Scores have been recorded. Current Total: ' + str(cumulative) + "Teacher's Name: " + str(teacher_name) + "Pupil: " + str(pupil) + "Pupil's Name: " + str(pupil_first_name) + " " + str(pupil_last_name),
                'yustaoab@gmail.com',
                [pupil_email],
                fail_silently=False,
                #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            )
            messages.success(request, str(pupil_first_name) + "'s score has been added successfully")
            return redirect('pre_basic_third')
        else:
            messages.error(request, "Please review form input fields below")
            #return redirect('pre_basic_third')
    return render(request, 'pre_basic/third_form.html', {'form': form, 'cum_perc': cum_perc})

@login_required
def showThird(request, **kwargs):
    third = ThirdTerm.objects.filter(id=kwargs['pk'])
    response_third = []
    for each in third:
        class_pupils_count = ThirdTerm.objects.filter(pupil__classe=each.pupil.classe).count()
        class_pupils = ThirdTerm.objects.filter(pupil__classe=each.pupil.classe)

        literacy_cum = 0
        numeracy_cum = 0
        general_studies_cum = 0
        science_cum = 0
        literacy_position = []
        literacy_pos = 0
        numeracy_position = []
        numeracy_pos = 0
        general_studies_position = []
        general_studies_pos = 0
        science_position = []
        science_pos = 0
        for pupil in class_pupils:
            literacy_cum = literacy_cum + pupil.literacy_cum
            numeracy_cum = numeracy_cum + pupil.numeracy_cum
            general_studies_cum = general_studies_cum + pupil.general_studies_cum
            science_cum = science_cum + pupil.science_cum

            literacy_position.append(pupil.literacy_cum)
            literacy_position.sort(reverse=True)
            numeracy_position.append(pupil.numeracy_cum)
            numeracy_position.sort(reverse=True)
            general_studies_position.append(pupil.general_studies_cum)
            general_studies_position.sort(reverse=True)
            science_position.append(pupil.science_cum)
            science_position.sort(reverse=True)

        literacy_avg = round((literacy_cum/class_pupils_count),2)
        numeracy_avg = round((numeracy_cum/class_pupils_count),2)
        general_studies_avg = round((general_studies_cum/class_pupils_count),2)
        science_avg = round((science_cum/class_pupils_count),2)

        for i in range(len(numeracy_position)):
            if numeracy_position[i] == each.numeracy_cum:
                if i in range (10, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (11, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (12, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (0, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "st"
                elif i in range (1, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "nd"
                elif i in range (2, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "rd"
                else:
                    numeracy_pos = str(i + 1) + "th"

        for i in range(len(literacy_position)):
            if literacy_position[i] == each.literacy_cum:
                if i in range (10, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (11, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (12, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (0, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "st"
                elif i in range (1, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "nd"
                elif i in range (2, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "rd"
                else:
                    literacy_pos = str(i + 1) + "th"

        for i in range(len(general_studies_position)):
            if general_studies_position[i] == each.general_studies_cum:
                if i in range (10, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (11, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (12, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (0, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "st"
                elif i in range (1, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "nd"
                elif i in range (2, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "rd"
                else:
                    general_studies_pos = str(i + 1) + "th"

        for i in range(len(science_position)):
            if science_position[i] == each.science_cum:
                if i in range (10, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (11, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (12, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (0, len(science_position), 10):
                    science_pos = str(i + 1) + "st"
                elif i in range (1, len(science_position), 10):
                    science_pos = str(i + 1) + "nd"
                elif i in range (2, len(science_position), 10):
                    science_pos = str(i + 1) + "rd"
                else:
                    science_pos = str(i + 1) + "th"
        response_third.append(each)
    return render(request, 'pre_basic/third_report.html', {'third': response_third,
        'class_pupils_count': class_pupils_count, 'literacy_avg': literacy_avg,
        'numeracy_avg': numeracy_avg, 'general_studies_avg': general_studies_avg,
        'science_avg': science_avg, 'literacy_position': literacy_position,
        'literacy_pos': literacy_pos, 'numeracy_position': numeracy_position,
        'numeracy_pos': numeracy_pos, 'general_studies_position': general_studies_position,
        'general_studies_pos': general_studies_pos, 'science_position': science_position,
        'science_pos': science_pos})

@login_required
def showFirstsUser(request):
    context = {}
    filtered_firsts = FirstFilter(
        request.GET,
        queryset = FirstTerm.objects.filter(pupil__user=request.user, school_fees=True)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'pre_basic/first_list_user.html', context=context)

@login_required
def showSecondsUser(request):
    context = {}
    filtered_seconds = SecondFilter(
        request.GET,
        queryset = SecondTerm.objects.filter(pupil__user=request.user, school_fees=True)
    )
    context['filtered_seconds'] = filtered_seconds
    paginated_filtered_seconds = Paginator(filtered_seconds.qs, 10)
    page_number = request.GET.get('page')
    seconds_page_obj = paginated_filtered_seconds.get_page(page_number)
    context['seconds_page_obj'] = seconds_page_obj
    total_seconds = filtered_seconds.qs.count()
    context['total_seconds'] = total_seconds
    return render(request, 'pre_basic/second_list_user.html', context=context)

@login_required
def showThirdsUser(request):
    context = {}
    filtered_thirds = ThirdFilter(
        request.GET,
        queryset = ThirdTerm.objects.filter(pupil__user=request.user, school_fees=True)
    )
    context['filtered_thirds'] = filtered_thirds
    paginated_filtered_thirds = Paginator(filtered_thirds.qs, 10)
    page_number = request.GET.get('page')
    thirds_page_obj = paginated_filtered_thirds.get_page(page_number)
    context['thirds_page_obj'] = thirds_page_obj
    total_thirds = filtered_thirds.qs.count()
    context['total_thirds'] = total_thirds
    return render(request, 'pre_basic/third_list_user.html', context=context)

@login_required
def showFirstUser(request, **kwargs):
    first = FirstTerm.objects.filter(id=kwargs['pk'])
    response_first = []
    for each in first:
        class_pupils_count = FirstTerm.objects.filter(pupil__classe=each.pupil.classe).count()
        class_pupils = FirstTerm.objects.filter(pupil__classe=each.pupil.classe)

        literacy_tot = 0
        numeracy_tot = 0
        general_studies_tot = 0
        science_tot = 0
        literacy_position = []
        literacy_pos = 0
        numeracy_position = []
        numeracy_pos = 0
        general_studies_position = []
        general_studies_pos = 0
        science_position = []
        science_pos = 0
        for pupil in class_pupils:
            literacy_tot = literacy_tot + pupil.literacy_tot
            numeracy_tot = numeracy_tot + pupil.numeracy_tot
            general_studies_tot = general_studies_tot + pupil.general_studies_tot
            science_tot = science_tot + pupil.science_tot

            literacy_position.append(pupil.literacy_tot)
            literacy_position.sort(reverse=True)
            numeracy_position.append(pupil.numeracy_tot)
            numeracy_position.sort(reverse=True)
            general_studies_position.append(pupil.general_studies_tot)
            general_studies_position.sort(reverse=True)
            science_position.append(pupil.science_tot)
            science_position.sort(reverse=True)

        literacy_avg = round((literacy_tot/class_pupils_count),2)
        numeracy_avg = round((numeracy_tot/class_pupils_count),2)
        general_studies_avg = round((general_studies_tot/class_pupils_count),2)
        science_avg = round((science_tot/class_pupils_count),2)

        for i in range(len(numeracy_position)):
            if numeracy_position[i] == each.numeracy_tot:
                if i in range (10, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (11, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (12, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (0, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "st"
                elif i in range (1, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "nd"
                elif i in range (2, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "rd"
                else:
                    numeracy_pos = str(i + 1) + "th"

        for i in range(len(literacy_position)):
            if literacy_position[i] == each.literacy_tot:
                if i in range (10, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (11, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (12, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (0, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "st"
                elif i in range (1, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "nd"
                elif i in range (2, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "rd"
                else:
                    literacy_pos = str(i + 1) + "th"

        for i in range(len(general_studies_position)):
            if general_studies_position[i] == each.general_studies_tot:
                if i in range (10, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (11, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (12, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (0, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "st"
                elif i in range (1, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "nd"
                elif i in range (2, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "rd"
                else:
                    general_studies_pos = str(i + 1) + "th"

        for i in range(len(science_position)):
            if science_position[i] == each.science_tot:
                if i in range (10, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (11, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (12, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (0, len(science_position), 10):
                    science_pos = str(i + 1) + "st"
                elif i in range (1, len(science_position), 10):
                    science_pos = str(i + 1) + "nd"
                elif i in range (2, len(science_position), 10):
                    science_pos = str(i + 1) + "rd"
                else:
                    science_pos = str(i + 1) + "th"

        response_first.append(each)
    return render(request, 'pre_basic/first_report_user.html', {'first': response_first,
        'class_pupils_count': class_pupils_count, 'literacy_avg': literacy_avg,
        'numeracy_avg': numeracy_avg, 'general_studies_avg': general_studies_avg,
        'science_avg': science_avg, 'literacy_position': literacy_position,
        'literacy_pos': literacy_pos, 'numeracy_position': numeracy_position,
        'numeracy_pos': numeracy_pos, 'general_studies_position': general_studies_position,
        'general_studies_pos': general_studies_pos, 'science_position': science_position,
        'science_pos': science_pos})

@login_required
def showSecondUser(request, **kwargs):
    second = SecondTerm.objects.filter(id=kwargs['pk'])
    response_second = []
    for each in second:
        class_pupils_count = SecondTerm.objects.filter(pupil__classe=each.pupil.classe).count()
        class_pupils = SecondTerm.objects.filter(pupil__classe=each.pupil.classe)

        literacy_tot = 0
        numeracy_tot = 0
        general_studies_tot = 0
        science_tot = 0
        literacy_position = []
        literacy_pos = 0
        numeracy_position = []
        numeracy_pos = 0
        general_studies_position = []
        general_studies_pos = 0
        science_position = []
        science_pos = 0
        for pupil in class_pupils:
            literacy_tot = literacy_tot + pupil.literacy_tot
            numeracy_tot = numeracy_tot + pupil.numeracy_tot
            general_studies_tot = general_studies_tot + pupil.general_studies_tot
            science_tot = science_tot + pupil.science_tot

            literacy_position.append(pupil.literacy_tot)
            literacy_position.sort(reverse=True)
            numeracy_position.append(pupil.numeracy_tot)
            numeracy_position.sort(reverse=True)
            general_studies_position.append(pupil.general_studies_tot)
            general_studies_position.sort(reverse=True)
            science_position.append(pupil.science_tot)
            science_position.sort(reverse=True)

        literacy_avg = round((literacy_tot/class_pupils_count),2)
        numeracy_avg = round((numeracy_tot/class_pupils_count),2)
        general_studies_avg = round((general_studies_tot/class_pupils_count),2)
        science_avg = round((science_tot/class_pupils_count),2)

        for i in range(len(numeracy_position)):
            if numeracy_position[i] == each.numeracy_tot:
                if i in range (10, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (11, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (12, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (0, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "st"
                elif i in range (1, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "nd"
                elif i in range (2, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "rd"
                else:
                    numeracy_pos = str(i + 1) + "th"

        for i in range(len(literacy_position)):
            if literacy_position[i] == each.literacy_tot:
                if i in range (10, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (11, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (12, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (0, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "st"
                elif i in range (1, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "nd"
                elif i in range (2, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "rd"
                else:
                    literacy_pos = str(i + 1) + "th"

        for i in range(len(general_studies_position)):
            if general_studies_position[i] == each.general_studies_tot:
                if i in range (10, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (11, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (12, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (0, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "st"
                elif i in range (1, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "nd"
                elif i in range (2, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "rd"
                else:
                    general_studies_pos = str(i + 1) + "th"

        for i in range(len(science_position)):
            if science_position[i] == each.science_tot:
                if i in range (10, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (11, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (12, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (0, len(science_position), 10):
                    science_pos = str(i + 1) + "st"
                elif i in range (1, len(science_position), 10):
                    science_pos = str(i + 1) + "nd"
                elif i in range (2, len(science_position), 10):
                    science_pos = str(i + 1) + "rd"
                else:
                    science_pos = str(i + 1) + "th"

        response_second.append(each)
    return render(request, 'pre_basic/second_report.html', {'second': response_second,
        'class_pupils_count': class_pupils_count, 'literacy_avg': literacy_avg,
        'numeracy_avg': numeracy_avg, 'general_studies_avg': general_studies_avg,
        'science_avg': science_avg, 'literacy_position': literacy_position,
        'literacy_pos': literacy_pos, 'numeracy_position': numeracy_position,
        'numeracy_pos': numeracy_pos, 'general_studies_position': general_studies_position,
        'general_studies_pos': general_studies_pos, 'science_position': science_position,
        'science_pos': science_pos})

@login_required
def showThirdUser(request, **kwargs):
    third = ThirdTerm.objects.filter(id=kwargs['pk'])
    response_third = []
    for each in third:
        class_pupils_count = ThirdTerm.objects.filter(pupil__classe=each.pupil.classe).count()
        class_pupils = ThirdTerm.objects.filter(pupil__classe=each.pupil.classe)

        literacy_cum = 0
        numeracy_cum = 0
        general_studies_cum = 0
        science_cum = 0
        literacy_position = []
        literacy_pos = 0
        numeracy_position = []
        numeracy_pos = 0
        general_studies_position = []
        general_studies_pos = 0
        science_position = []
        science_pos = 0
        for pupil in class_pupils:
            literacy_cum = literacy_cum + pupil.literacy_cum
            numeracy_cum = numeracy_cum + pupil.numeracy_cum
            general_studies_cum = general_studies_cum + pupil.general_studies_cum
            science_cum = science_cum + pupil.science_cum

            literacy_position.append(pupil.literacy_cum)
            literacy_position.sort(reverse=True)
            numeracy_position.append(pupil.numeracy_cum)
            numeracy_position.sort(reverse=True)
            general_studies_position.append(pupil.general_studies_cum)
            general_studies_position.sort(reverse=True)
            science_position.append(pupil.science_cum)
            science_position.sort(reverse=True)

        literacy_avg = round((literacy_cum/class_pupils_count),2)
        numeracy_avg = round((numeracy_cum/class_pupils_count),2)
        general_studies_avg = round((general_studies_cum/class_pupils_count),2)
        science_avg = round((science_cum/class_pupils_count),2)

        for i in range(len(numeracy_position)):
            if numeracy_position[i] == each.numeracy_cum:
                if i in range (10, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (11, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (12, len(numeracy_position), 100):
                    numeracy_pos = str(i + 1) + "th"
                elif i in range (0, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "st"
                elif i in range (1, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "nd"
                elif i in range (2, len(numeracy_position), 10):
                    numeracy_pos = str(i + 1) + "rd"
                else:
                    numeracy_pos = str(i + 1) + "th"

        for i in range(len(literacy_position)):
            if literacy_position[i] == each.literacy_cum:
                if i in range (10, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (11, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (12, len(literacy_position), 100):
                    literacy_pos = str(i + 1) + "th"
                elif i in range (0, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "st"
                elif i in range (1, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "nd"
                elif i in range (2, len(literacy_position), 10):
                    literacy_pos = str(i + 1) + "rd"
                else:
                    literacy_pos = str(i + 1) + "th"

        for i in range(len(general_studies_position)):
            if general_studies_position[i] == each.general_studies_cum:
                if i in range (10, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (11, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (12, len(general_studies_position), 100):
                    general_studies_pos = str(i + 1) + "th"
                elif i in range (0, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "st"
                elif i in range (1, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "nd"
                elif i in range (2, len(general_studies_position), 10):
                    general_studies_pos = str(i + 1) + "rd"
                else:
                    general_studies_pos = str(i + 1) + "th"

        for i in range(len(science_position)):
            if science_position[i] == each.science_cum:
                if i in range (10, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (11, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (12, len(science_position), 100):
                    science_pos = str(i + 1) + "th"
                elif i in range (0, len(science_position), 10):
                    science_pos = str(i + 1) + "st"
                elif i in range (1, len(science_position), 10):
                    science_pos = str(i + 1) + "nd"
                elif i in range (2, len(science_position), 10):
                    science_pos = str(i + 1) + "rd"
                else:
                    science_pos = str(i + 1) + "th"
        response_third.append(each)
    return render(request, 'pre_basic/third_report_user.html', {'third': response_third,
        'class_pupils_count': class_pupils_count, 'literacy_avg': literacy_avg,
        'numeracy_avg': numeracy_avg, 'general_studies_avg': general_studies_avg,
        'science_avg': science_avg, 'literacy_position': literacy_position,
        'literacy_pos': literacy_pos, 'numeracy_position': numeracy_position,
        'numeracy_pos': numeracy_pos, 'general_studies_position': general_studies_position,
        'general_studies_pos': general_studies_pos, 'science_position': science_position,
        'science_pos': science_pos})
