from django.db import models
#from django.contrib.auth.models import User
class Session(models.Model):
    session = models.CharField(max_length=20, blank=True, null=True)
    first_head = models.ForeignKey('users.Person', on_delete = models.SET_NULL, blank=True, null=True, verbose_name="Head of School's Name", related_name='session_first_head')
    second_head = models.ForeignKey('users.Person', on_delete = models.SET_NULL, blank=True, null=True, verbose_name="Head of School's Name", related_name='session_second_head')
    third_head = models.ForeignKey('users.Person', on_delete = models.SET_NULL, blank=True, null=True, verbose_name="Head of School's Name", related_name='session_third_head')
    school = models.ImageField(upload_to='stamp_img/%Y/%m/%d', null=True, blank=True, verbose_name="School's Stamp")
    first_number = models.CharField(max_length=7, blank=True, null=True, verbose_name="No of Days School Opens")
    second_number = models.CharField(max_length=7, blank=True, null=True, verbose_name="No of Days School Opens")
    third_number = models.CharField(max_length=7, blank=True, null=True, verbose_name="No of Days School Opens")
    first_next = models.DateField(blank=True, null=True, verbose_name="Next Term Begins")
    second_next = models.DateField(blank=True, null=True, verbose_name="Next Term Begins")
    third_next = models.DateField(blank=True, null=True, verbose_name="Next Term Begins")
    first_report = models.BooleanField(max_length=5, default = False, verbose_name="Open 1st Term Report")
    second_report = models.BooleanField(max_length=5, default = False, verbose_name="Open 2nd Term Report")
    third_report = models.BooleanField(max_length=5, default = False, verbose_name="Open 3rd Term Report")
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.session)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Class(models.Model):
    classe = models.CharField(max_length=20, null=True, verbose_name="Class")
    teacher = models.ForeignKey('users.Person', on_delete=models.SET_NULL, null=True)
    signature = models.ImageField(upload_to='signature_img/%Y/%m/%d', null=True, blank=True, verbose_name="Class Teacher's Signature")
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return str(self.classe)
        except:
            return str(self.id)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

class Subject(models.Model):
    classe = models.ForeignKey('management.Class', on_delete=models.SET_NULL, null=True, verbose_name="Class")
    serial = models.CharField(max_length=2, null=True, verbose_name="S/N")
    subject = models.CharField(max_length=30)
    teacher = models.ForeignKey('users.Person', on_delete=models.SET_NULL, null=True, related_name='subject_teacher')
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return str(self.classe) + " | " + str(self.subject)
        except:
            return str(self.id)

    class Meta:
        ordering = ('-created',)
        # verbose_name = 'Class'
        # verbose_name_plural = 'Classes'
