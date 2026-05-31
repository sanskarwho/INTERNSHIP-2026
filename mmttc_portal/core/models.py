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
        ('Submitted', 'Submitted'),
        ('PDF Generated', 'PDF Generated'),
        ('Waiting for Signed Form', 'Waiting for Signed Form'),
        ('Signed Form Uploaded', 'Signed Form Uploaded'),
        ('Under Review', 'Under Review'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    applicant = models.ForeignKey(Applicant,
                                  on_delete=models.CASCADE)

    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE)

    # Personal Details
    title = models.CharField(max_length=20, blank=True)

    full_name = models.CharField(max_length=200)

    category = models.CharField(max_length=50, blank=True)

    is_pwd = models.BooleanField(default=False)

    aadhaar_number = models.CharField(max_length=20, blank=True)

    photograph = models.ImageField(upload_to='photographs/',
                                   blank=True,
                                   null=True)

    date_of_birth = models.DateField(blank=True, null=True)

    applicant_type = models.CharField(max_length=100, blank=True)

    # Service Details
    present_designation = models.CharField(max_length=150, blank=True)

    appointment_date = models.DateField(blank=True, null=True)

    scale_of_pay = models.CharField(max_length=100, blank=True)

    nature_of_appointment = models.CharField(max_length=100, blank=True)

    # Address Details
    official_address = models.TextField(blank=True)

    official_state = models.CharField(max_length=100, blank=True)

    official_pin = models.CharField(max_length=10, blank=True)

    mailing_address = models.TextField(blank=True)

    mailing_state = models.CharField(max_length=100, blank=True)

    mailing_pin = models.CharField(max_length=10, blank=True)

    # Contact Details
    mobile_number = models.CharField(max_length=15, blank=True)

    alternate_number = models.CharField(max_length=15, blank=True)

    email = models.EmailField(blank=True)

    # Academic Details
    highest_qualification = models.CharField(max_length=150, blank=True)

    qualification_status = models.CharField(max_length=100, blank=True)

    subject_specialization = models.CharField(max_length=200, blank=True)

    # Earlier Course Details
    earlier_course_attended = models.BooleanField(default=False)

    earlier_course_name = models.CharField(max_length=200, blank=True)

    earlier_course_place = models.CharField(max_length=200, blank=True)

    earlier_course_duration = models.CharField(max_length=100, blank=True)

    # Accommodation
    accommodation_required = models.BooleanField(default=False)

    # Document Uploads
    photograph = models.ImageField(
        upload_to='application_uploads/photographs/',
        blank=True,
        null=True
    )

    appointment_letter = models.FileField(
        upload_to='application_uploads/appointment_letters/',
        blank=True,
        null=True
    )

    relieving_order = models.FileField(
        upload_to='application_uploads/relieving_orders/',
        blank=True,
        null=True
    )

    id_proof = models.FileField(
        upload_to='application_uploads/id_proofs/',
        blank=True,
        null=True
    )

    signature = models.ImageField(
        upload_to='application_uploads/signatures/',
        blank=True,
        null=True
    )

    other_document = models.FileField(
        upload_to='application_uploads/other_documents/',
        blank=True,
        null=True
    )

    generated_application_pdf = models.FileField(
        upload_to='application_uploads/generated_pdfs/',
        blank=True,
        null=True
    )

    signed_form = models.FileField(
        upload_to='application_uploads/signed_forms/',
        blank=True,
        null=True
    )

    # Status
    status = models.CharField(max_length=50,
                              choices=STATUS_CHOICES,
                              default='Submitted')

    remarks = models.TextField(blank=True, null=True)

    application_date = models.DateTimeField(auto_now_add=True)

    class Meta:

        unique_together = ['applicant', 'course']

    def __str__(self):

        return f"{self.full_name} - {self.course.title}"

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

class ContactMessage(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject