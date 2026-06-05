from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):

    title = models.CharField(max_length=200)

    course_type = models.CharField(max_length=100)

    course_code = models.CharField(max_length=20)

    mode = models.CharField(max_length=20)

    start_date = models.DateField()

    end_date = models.DateField()

    seat_status = models.CharField(
        max_length=20,
        default='Vacant'
    )

    is_visible = models.BooleanField(default=True)

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

    full_name = models.CharField(max_length=100)

    category = models.CharField(max_length=50, blank=True)

    is_pwd = models.BooleanField(default=False)

    aadhaar_number = models.CharField(max_length=12, blank=True)

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
    official_address = models.TextField(max_length= 100,blank=True)

    official_state = models.CharField(max_length=100, blank=True)

    official_pin = models.CharField(max_length=10, blank=True)

    mailing_address = models.TextField(max_length= 100, blank=True)

    mailing_state = models.CharField(max_length=100, blank=True)

    mailing_pin = models.CharField(max_length=10, blank=True)

    # Contact Details
    mobile_number = models.CharField(max_length=10, blank=True)

    alternate_number = models.CharField(max_length=10, blank=True)

    email = models.EmailField(max_length= 30,blank=True)

    # Academic Details
    highest_qualification = models.CharField(max_length=150, blank=True)

    qualification_status = models.CharField(max_length=100, blank=True)

    subject_specialization = models.CharField(max_length=50, blank=True)

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

    generated_application_docx = models.FileField(
        upload_to='application_uploads/generated_docs/',
        blank=True,
        null=True
    )

    generated_application_pdf = models.FileField(
        upload_to='application_uploads/generated_pdfs/',
        blank=True,
        null=True
    )
    application_number = models.CharField(
    max_length=30,
    unique=True,
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

    remarks = models.TextField(blank=True, default = '')

    application_date = models.DateTimeField(auto_now_add=True)

    class Meta:

        unique_together = ['applicant', 'course']

    def __str__(self):

        return f"{self.full_name} - {self.course.title}"
    
class EarlierAttendedCourse(models.Model):

    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name='earlier_courses'
    )

    course_name = models.CharField(max_length=200, blank=True)

    completion_month_year = models.CharField(max_length=20, blank=True)

    center_name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.course_name

class Document(models.Model):

    application = models.ForeignKey(Application,
                                    on_delete=models.CASCADE)

    document = models.FileField(upload_to='documents/')

    uploaded_at = models.DateTimeField(auto_now_add=True)


class Certificate(models.Model):

    application = models.OneToOneField(
        Application,
        on_delete=models.CASCADE
    )

    certificate_id = models.CharField(
        max_length=100,
        unique=True,
        blank=True
    )

    generated_at = models.DateTimeField(
        auto_now_add=True
    )

    certificate_file = models.FileField(
        upload_to='certificates/',
        blank=True,
        null=True
    )

    qr_code = models.ImageField(
        upload_to='certificates/qr_codes/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.certificate_id

class ContactMessage(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
class CourseSchedule(models.Model):

    pdf_file = models.FileField(
        upload_to='course_schedules/',
        blank=True,
        null=True
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Tentative Course Schedule"

