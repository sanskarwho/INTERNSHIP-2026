from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):

    title = models.CharField(max_length=200)

    duration = models.CharField(max_length=100)

    start_date = models.DateField()

    end_date = models.DateField()

    eligibility = models.TextField()

    seats = models.IntegerField()

    description = models.TextField()

    is_visible = models.BooleanField(default=True)

    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Applicant(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)

    phone = models.CharField(max_length=15)

    institution = models.CharField(max_length=200)

    designation = models.CharField(max_length=100)

    state = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class Application(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    applicant = models.ForeignKey(Applicant,
                                  on_delete=models.CASCADE)

    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE)

    qualification = models.CharField(max_length=200)

    experience = models.TextField()

    address = models.TextField()

    statement = models.TextField()

    application_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:

        unique_together = ['applicant', 'course']

    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default='Pending')

    remarks = models.TextField(blank=True, null=True)

    signed_form = models.FileField(upload_to='signed_forms/',
                                   blank=True,
                                   null=True)

    def __str__(self):
        return f"{self.applicant} - {self.course}"

class Document(models.Model):

    application = models.ForeignKey(Application,
                                    on_delete=models.CASCADE)

    document = models.FileField(upload_to='documents/')

    uploaded_at = models.DateTimeField(auto_now_add=True)


class Certificate(models.Model):

    application = models.OneToOneField(Application,
                                       on_delete=models.CASCADE)

    certificate_id = models.CharField(max_length=100,
                                      unique=True)

    generated_at = models.DateTimeField(auto_now_add=True)

    certificate_file = models.FileField(upload_to='certificates/')