from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from .models import Course
from .models import Applicant, Application


def home(request):

    return render(request,
                  'public/index.html')


# LOGIN

def login_page(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(username=username,
                            password=password)

        if user is not None:

            login(request, user)

            if user.is_staff:

                return redirect('/admin-dashboard/')

            else:

                return redirect('/dashboard/')

    return render(request,
                  'public/login.html')


# REGISTER

def register_page(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        email = request.POST.get('email')

        password = request.POST.get('password')

        user = User.objects.create_user(

            username=username,

            email=email,

            password=password

        )

        Applicant.objects.create(

            user=user,

            phone='',

            institution='',

            designation='',

            state=''

        )

        return redirect('/login/')

    return render(request,
                  'public/register.html')


# PUBLIC COURSES PAGE

def courses(request):

    all_courses = Course.objects.all()

    return render(request,
                  'public/courses.html',
                  {'courses': all_courses})


# APPLICANT DASHBOARD

@login_required
def applicant_dashboard(request):

    if request.user.is_staff:

        return redirect('/admin-dashboard/')

    return render(request,
                  'applicant/applicant_dashboard.html')


# ADMIN DASHBOARD

@login_required
def admin_dashboard(request):

    if not request.user.is_staff:

        return render(request,'public/access_denied.html')

    return render(request,
                  'admin_panel/admin_dashboard.html')


# CREATE COURSE

@login_required
def create_course(request):

    if not request.user.is_staff:

        return redirect('/dashboard/')

    if request.method == 'POST':

        title = request.POST.get('title')

        duration = request.POST.get('duration')

        start_date = request.POST.get('start_date')

        end_date = request.POST.get('end_date')

        eligibility = request.POST.get('eligibility')

        seats = request.POST.get('seats')

        description = request.POST.get('description')

        Course.objects.create(

            title=title,

            duration=duration,

            start_date=start_date,

            end_date=end_date,

            eligibility=eligibility,

            seats=seats,

            description=description

        )

    return render(request,
                  'admin_panel/create_course.html')


# MANAGE COURSES

@login_required
def manage_courses(request):

    if not request.user.is_staff:

        return redirect('/dashboard/')

    courses = Course.objects.all()

    return render(request,
                  'admin_panel/manage_courses.html',
                  {'courses': courses})


# EDIT COURSE

@login_required
def edit_course(request, id):

    if not request.user.is_staff:

        return redirect('/dashboard/')

    course = Course.objects.get(id=id)

    if request.method == 'POST':

        course.title = request.POST.get('title')

        course.duration = request.POST.get('duration')

        course.start_date = request.POST.get('start_date')

        course.end_date = request.POST.get('end_date')

        course.eligibility = request.POST.get('eligibility')

        course.seats = request.POST.get('seats')

        course.description = request.POST.get('description')

        course.save()

        return redirect('/manage-courses/')

    return render(request,
                  'admin_panel/edit_course.html',
                  {'course': course})


# DELETE COURSE

@login_required
def delete_course(request, id):

    if not request.user.is_staff:

        return redirect('/dashboard/')

    course = Course.objects.get(id=id)

    course.delete()

    return redirect('/manage-courses/')


# APPLY COURSE

@login_required
def apply_course(request, id):

    if request.user.is_staff:

        return redirect('/admin-dashboard/')

    course = Course.objects.get(id=id)

    applicant = Applicant.objects.get(user=request.user)

    already_applied = Application.objects.filter(

        applicant=applicant,
        course=course

    ).exists()

    if already_applied:

        return render(request,
                      'applicant/already_applied.html')

    if request.method == 'POST':

        qualification = request.POST.get('qualification')

        experience = request.POST.get('experience')

        address = request.POST.get('address')

        statement = request.POST.get('statement')

        Application.objects.create(

            applicant=applicant,

            course=course,

            qualification=qualification,

            experience=experience,

            address=address,

            statement=statement

        )

        return redirect('/my-applications/')

    return render(request,
                  'applicant/apply_course.html',
                  {'course': course})

# VIEW APPLICATIONS

@login_required
def view_applications(request):

    if not request.user.is_staff:

        return redirect('/dashboard/')

    applications = Application.objects.all()

    return render(request,
                  'admin_panel/view_applications.html',
                  {'applications': applications})

@login_required
def my_applications(request):

    if request.user.is_staff:

        return redirect('/admin-dashboard/')

    applicant = Applicant.objects.get(user=request.user)

    applications = Application.objects.filter(
        applicant=applicant
    )

    return render(request,
                  'applicant/my_applications.html',
                  {'applications': applications})

def info_page(request, title, content):

    return render(request,
                  'public/info_page.html',
                  {
                      'title': title,
                      'content': content
                  })

def objective(request):

    content = """

    <h2>
        Objectives of HRDC-BHU
    </h2>

    <p>
        Objectives of the HRDC-BHU are to enable newly appointed and serving lecturers to:
    </p>

    <ul>

        <li>
            Understand the significance of education in general and higher education in particular in both global and Indian contexts.
        </li>

        <li>
            Understand the relationship between education and economic, socio-economic, and cultural development with special reference to Indian democracy, secularism, and social equity.
        </li>

        <li>
            Acquire and improve teaching skills at the college and university level to achieve the goals of higher education.
        </li>

        <li>
            Remain updated with the latest developments in their respective subjects.
        </li>

        <li>
            Understand the organization and management of colleges and universities and recognize the role of teachers in the overall system.
        </li>

        <li>
            Utilize opportunities for development of personality, creativity, and initiative.
        </li>

        <li>
            Promote computer literacy and the use of ICT in teaching and learning processes.
        </li>

    </ul>

    """

    return render(request,
                  'public/info_page.html',
                  {
                      'title': 'Objective',
                      'content': content
                  })

def philosophy(request):

    content = """

    <h2>
        Teacher as the Central Element
    </h2>

    <p>
        HRDC's main philosophy is based on the belief that the teacher is central to the entire educational system.
    </p>

    <p>
        While teachers are universally recognized as the pivot of education, adequate opportunities for professional development are often lacking. Therefore, mechanisms must be developed within the framework of a knowledge society to continuously support teacher growth and advancement.
    </p>

    <p>
        Teachers are not merely expected to transmit information. They must also guide students to meet the challenges of life and become responsible citizens along with trained professionals.
    </p>

    <h2>
        Changing Role of Teachers
    </h2>

    <p>
        Earlier, teachers often learned the art of teaching through observation of senior colleagues and mentors. However, modern educational demands require organized and systematic orientation and training programmes for newly appointed teachers.
    </p>

    <p>
        The expansion of higher education in India transformed the system from elitist education to mass-based education. While this expansion is a major achievement, it has also led to challenges in maintaining educational standards.
    </p>

    <p>
        In the present era of rapid knowledge growth and information explosion, teachers carry greater responsibility to continuously improve themselves and remain academically updated.
    </p>

    <h2>
        Educational Technology and Information Technology
    </h2>

    <p>
        Educational technology and Information Technology (IT) have become essential components of modern teaching.
    </p>

    <p>
        UGC has introduced specially designed orientation and refresher courses focused on ICT, e-content development, and digital teaching tools.
    </p>

    <p>
        These programmes aim to:
    </p>

    <ul>

        <li>
            Create internet-literate and computer-literate teachers.
        </li>

        <li>
            Promote the use of software tools in teaching.
        </li>

        <li>
            Encourage e-content development and digital learning methods.
        </li>

        <li>
            Improve technological awareness among teachers irrespective of discipline.
        </li>

    </ul>

    <p>
        Knowledge acquisition is viewed as a two-way process between teachers and students, enabling collective advancement of knowledge.
    </p>

    <h2>
        Continuous Professional Development
    </h2>

    <p>
        Knowledge in every discipline is expanding rapidly. Teachers must continuously update themselves to avoid becoming academically outdated.
    </p>

    <p>
        While many teachers independently work to improve their skills and methodologies, HRDC emphasizes structured and organized orientation programmes to support a large number of teachers at the college and university level.
    </p>

    <h2>
        Orientation Programmes
    </h2>

    <p>
        Orientation programmes for newly appointed lecturers emphasize the role of teachers as agents of socio-economic change and national development.
    </p>

    <p>
        These programmes are flexible rather than rigid and focus on:
    </p>

    <ul>

        <li>
            Developing self-reliance among teachers.
        </li>

        <li>
            Encouraging awareness of social, intellectual, and moral responsibilities.
        </li>

        <li>
            Helping teachers discover their potential.
        </li>

        <li>
            Promoting confidence and awareness in educational responsibilities.
        </li>

    </ul>

    <p>
        The programmes aim to make education relevant, dynamic, and socially meaningful.
    </p>

    <h2>
        National Development and Education
    </h2>

    <p>
        Orientation programmes must create awareness regarding the problems faced by Indian society and establish education as an important solution for national progress.
    </p>

    <p>
        Teachers must understand educational goals in the broader context of constitutional values and national development.
    </p>

    <h2>
        Role of Educational Administrators
    </h2>

    <p>
        HRDC also recognizes that orientation programmes can only succeed when educational administrators understand their significance.
    </p>

    <p>
        Therefore, orientation programmes are also planned for:
    </p>

    <ul>

        <li>
            Heads of Departments
        </li>

        <li>
            Principals
        </li>

        <li>
            Academic officers
        </li>

        <li>
            Educational administrators
        </li>

    </ul>

    <p>
        Such exposure helps administrators actively participate in academic development and encourages better supervision and leadership in higher education.
    </p>

    <h2>
        Exchange of Academic Ideas
    </h2>

    <p>
        HRDC promotes exchange of ideas within the academic and educational environment through interaction among teachers, resource persons, researchers, and students.
    </p>

    <p>
        Lectures by eminent scholars and experts are regularly planned to enhance academic interest and create a vibrant intellectual atmosphere within the university.
    </p>

    """

    return render(request,
                  'public/info_page.html',
                  {
                      'title': 'Philosophy',
                      'content': content
                  })

def functions(request):

    content = """

    <h2>
        Functions of HRDC-BHU
    </h2>

    <p>
        The Human Resource Development Centre (HRDC-BHU) plans, organizes, implements, monitors, and evaluates orientation programmes for newly appointed college and university lecturers.
    </p>

    <p>
        HRDC also organizes refresher courses for serving teachers along with orientation programmes and workshops for senior administrators, Assistant Registrars, Section Officers, Heads of Departments, Principals, and other academic officers.
    </p>

    <h2>
        Major Functions
    </h2>

    <p>
        Specifically, HRDC-BHU performs the following functions:
    </p>

    <ul>

        <li>
            Formulate orientation programmes according to UGC guidelines.
        </li>

        <li>
            Identify resource persons from various fields of specialization for orientation and refresher courses.
        </li>

        <li>
            Familiarize resource persons with the philosophy and guidelines of the programmes.
        </li>

        <li>
            Maintain a library containing reference and source materials required for courses.
        </li>

        <li>
            Develop specially designed teaching and training materials for effective implementation of programmes.
        </li>

        <li>
            Organize, monitor, and evaluate orientation and refresher courses for teachers.
        </li>

        <li>
            Promote a culture of learning and self-improvement among teachers at the tertiary level.
        </li>

        <li>
            Organize orientation programmes for senior administrators and decision-makers in higher education.
        </li>

        <li>
            Provide opportunities for teachers to exchange experiences and learn from peers.
        </li>

        <li>
            Provide a platform for teachers to remain updated with the latest developments in various disciplines.
        </li>

        <li>
            Encourage teachers to widen their knowledge and pursue research activities.
        </li>

        <li>
            Introduce innovative teaching methods and new developments in higher education.
        </li>

        <li>
            Publish academic materials aimed at enhancing teaching and research capabilities.
        </li>

        <li>
            Conduct capability enhancement programmes for non-academic staff to strengthen the teaching-learning environment.
        </li>

    </ul>

    <h2>
        Academic Planning
    </h2>

    <p>
        Thrust areas and resource persons for each refresher course are decided by the HRDC faculty in consultation with the Course Coordinator.
    </p>

    <h2>
        Meetings with University Officers
    </h2>

    <p>
        HRDC also organizes meetings with university officers and academic administrators in order to:
    </p>

    <ul>

        <li>
            Familiarize administrators with the philosophy and importance of orientation and refresher courses.
        </li>

        <li>
            Encourage them to actively depute teachers for participation in programmes.
        </li>

        <li>
            Help administrators understand their evolving supervisory roles in higher education.
        </li>

        <li>
            Facilitate educational reforms through appropriate modifications in management systems at different levels.
        </li>

    </ul>

    """

    return render(request,
                  'public/info_page.html',
                  {
                      'title': 'Functions',
                      'content': content
                  })

def responsibility(request):

    content = """

    <h2>
        Responsibilities of HRDC-BHU
    </h2>

    <p>
        The Human Resource Development Centre (HRDC-BHU) caters to the academic and professional needs of teachers and educational administrators from colleges and universities.
    </p>

    <p>
        HRDC-BHU maintains its own official website where all important information, notices, and updates are regularly posted and maintained.
    </p>

    <h2>
        Academic Record Maintenance
    </h2>

    <p>
        In order to make Orientation Programmes (OPs) and Refresher Courses (RCs) more effective, HRDC-BHU maintains systematic records related to:
    </p>

    <ul>

        <li>
            Participants and their academic achievements.
        </li>

        <li>
            Professional growth and teaching capabilities of teachers.
        </li>

        <li>
            Course-wise records of resource persons and participants.
        </li>

        <li>
            Year-wise and subject-wise details of programmes conducted.
        </li>

        <li>
            Reading materials and academic resources produced during courses.
        </li>

    </ul>

    <p>
        Copies of reading materials and publications are also preserved in the HRDC library for academic reference.
    </p>

    <h2>
        Establishment and Growth
    </h2>

    <p>
        At present, there are 66 Human Resource Development Centres functioning across India.
    </p>

    <p>
        The Academic Staff College at Banaras Hindu University was established during the Seventh Five-Year Plan in the year 1987 by the University Grants Commission (UGC).
    </p>

    <h2>
        Directors of HRDC-BHU
    </h2>

    <p>
        The following distinguished academicians have served as Directors of the Centre:
    </p>

    <ul>

        <li>
            Prof. B. B. Dhar
        </li>

        <li>
            Prof. M. S. Srinivasan
        </li>

        <li>
            Prof. V. S. Jaiswal
        </li>

        <li>
            Prof. K. K. Narang
        </li>

        <li>
            Prof. Janardan Singh
        </li>

        <li>
            Prof. Kumar Pankaj
        </li>

        <li>
            Prof. B. B. Bansal
        </li>

        <li>
            Prof. S. N. Upadhyay
        </li>

        <li>
            Prof. Kamal Sheel
        </li>

    </ul>

    <p>
        The present Director of HRDC-BHU is Prof. A. V. Sharma.
    </p>

    <h2>
        Transition to UGC-HRDC
    </h2>

    <p>
        From April 01, 2015, the University Grants Commission officially changed the name of UGC-Academic Staff Colleges to UGC-Human Resource Development Centres (UGC-HRDC).
    </p>

    """

    return render(request,
                  'public/info_page.html',
                  {
                      'title': 'Responsibility',
                      'content': content
                  })

def isro_edusat(request):

    content = """

    <h2>
        ISRO-EDUSAT Centre
    </h2>

    <p>
        HRDC-BHU has an EDUSAT Centre which regularly receives educational transmissions from organizations such as:
    </p>

    <ul>

        <li>
            CEC-UGC
        </li>

        <li>
            NCERT
        </li>

        <li>
            DST
        </li>

        <li>
            ISRO
        </li>

        <li>
            IGNOU
        </li>

        <li>
            Indian Institute of Remote Sensing (IIRS)
        </li>

    </ul>

    <p>
        The centre facilitates live interaction between experts and participants attending various courses organized by HRDC-BHU.
    </p>

    <p>
        The EDUSAT Centre has been recognized by the Indian Institute of Remote Sensing (IIRS), Dehradun as a University Centre for EDUSAT-based distance learning programmes.
    </p>

    <p>
        Since 2009 onwards, the centre has been regularly organizing programmes related to:
    </p>

    <ul>

        <li>
            Remote Sensing
        </li>

        <li>
            Geographic Information System (GIS)
        </li>

        <li>
            Global Positioning System (GPS)
        </li>

    </ul>

    <h2>
        Computer Laboratory
    </h2>

    <p>
        HRDC-BHU also maintains a well-equipped modern computer laboratory established with the financial assistance of UGC.
    </p>

    <p>
        The laboratory contains 25 Core i3 computer systems to support training, academic activities, and ICT-based learning programmes.
    </p>

    """

    return render(request,
                  'public/info_page.html',
                  {
                      'title': 'ISRO-EDUSAT Centre',
                      'content': content
                  })

def facilities(request):

    content = """

    <h2>
        Smart Classroom
    </h2>

    <p>
        HRDC-BHU has a modern Smart Classroom facility with a seating capacity of 70 participants.
    </p>

    <h2>
        Hostel and Guest House Facility
    </h2>

    <p>
        HRDC-BHU has its own guest house facility to accommodate a limited number of participants on a first-come-first-served basis.
    </p>

    <p>
        In addition to this, accommodation is also available in other guest houses of Banaras Hindu University on payment basis according to the respective guest house rates.
    </p>

    <p>
        Available guest house facilities include:
    </p>

    <ul>

        <li>
            University Guest House
        </li>

        <li>
            Faculty Guest House
        </li>

        <li>
            IIT Guest House
        </li>

        <li>
            Bhatnagar Guest House
        </li>

        <li>
            Transit House
        </li>

    </ul>

    <h2>
        Multipurpose Hall
    </h2>

    <p>
        UGC-HRDC, BHU has a dedicated multipurpose hall for academic and training activities.
    </p>

    <h2>
        Computer Laboratory
    </h2>

    <p>
        HRDC-BHU maintains a well-established Computer Laboratory equipped with 25 personal computers.
    </p>

    <p>
        Internet facilities are available on each system for participants and faculty members.
    </p>

    <h2>
        Library
    </h2>

    <p>
        UGC-HRDC, BHU has its own library containing approximately 2305 books along with monthly subscribed magazines.
    </p>

    <p>
        Participants are also provided access to:
    </p>

    <ul>

        <li>
            Cyber Library of BHU
        </li>

        <li>
            Central Library of BHU
        </li>

    </ul>

    <h2>
        Feedback System
    </h2>

    <p>
        Participants of every course regularly submit feedback regarding lectures and programme activities.
    </p>

    <p>
        At the end of each programme, participants also submit a comprehensive report of the course.
    </p>

    <h2>
        Best Practices
    </h2>

    <ul>

        <li>
            HRDC-BHU distributes plant saplings instead of bouquets to guests during formal functions.
        </li>

        <li>
            A 30-minute review session is conducted daily in addition to the regular six-hour contact sessions.
        </li>

        <li>
            Paperless programmes are encouraged and implemented.
        </li>

        <li>
            Participants are facilitated to use the university Cyber Library from 8:00 A.M. to 11:00 P.M.
        </li>

    </ul>

    """

    return render(request,
                  'public/info_page.html',
                  {
                      'title': 'Facilities',
                      'content': content
                  })

def programme_courses(request):

    content = """

    <h2>
        Full-Time Programmes (Orientation Programmes and Refresher Courses)
    </h2>

    <ul>

        <li>
            Programmes organized by BHU-HRDC are conducted on a full-time basis and maintain a residential character throughout the duration of the course.
        </li>

        <li>
            Participating lecturers are deputed by their respective colleges and universities for the entire duration of the programme.
        </li>

        <li>
            Teachers attending the programme are treated as being on duty with full pay and allowances by their sponsoring institutions.
        </li>

        <li>
            Participants are selected from institutions across India to promote national integration.
        </li>

        <li>
            A course generally consists of 20 or more participants.
        </li>

        <li>
            If sufficient participants are not available, BHU-HRDC coordinates with nearby HRDCs to exchange participants and ensure optimal enrollment.
        </li>

        <li>
            All courses are organized through BHU-HRDC.
        </li>

        <li>
            While conducting Refresher Courses, active involvement of the concerned department faculty is ensured.
        </li>

        <li>
            Punctuality, regularity, active participation, and purposefulness are strongly emphasized.
        </li>

        <li>
            Successful participants are awarded certificates. BHU-HRDC may withhold certificates for valid reasons.
        </li>

        <li>
            Centres of Excellence and specialized institutions may seek UGC approval to conduct sponsored Refresher Courses based on merit and relevance.
        </li>

        <li>
            E-content development and learning-object technologies are integrated into Orientation Programmes and Refresher Courses, with additional e-courses planned for the future.
        </li>

    </ul>

    <h2>
        Short-Term Courses (2–6 Days)
    </h2>

    <p>
        Apart from Orientation Programmes and Refresher Courses, BHU-HRDC plans to conduct short-term programmes ranging from two to six days.
    </p>

    <p>
        These programmes are primarily intended for the professional development of senior faculty members, including Professors and Associate Professors.
    </p>

    <h2>
        Interaction Programmes (21 Days)
    </h2>

    <p>
        Students pursuing Ph.D. and Post-Doctoral studies from Centres of Advanced Studies (CAS) and Departments of Special Assistance (DSA) may participate in special interaction programmes organized under the Refresher Course scheme.
    </p>

    <p>
        These programmes are generally conducted in the form of workshops and seminars with a duration of approximately three weeks.
    </p>

    <p>
        The primary objective is to facilitate meaningful interaction between research scholars and teachers.
    </p>

    <p>
        Student participants receive TA/DA benefits similar to those provided to Refresher Course participants.
    </p>

    <h2>
        Orientation Programmes for Administrative and Non-Academic Staff
    </h2>

    <p>
        BHU-HRDC also plans to organize orientation programmes, seminars, and workshops for academic planners and administrators, including Group 'A' officers.
    </p>

    <p>
        In addition, professional development programmes of approximately six days are proposed for non-academic Group 'B' and Group 'C' staff with the support of UGC.
    </p>

    """

    return render(
        request,
        'public/info_page.html',
        {
            'title': 'Courses',
            'content': content
        }
    )

def curriculum(request):

    content = """

    <h2>
        Course Preparation for Refresher Courses
    </h2>

    <p>
        The curriculum of Refresher Courses is developed in consultation with the concerned academic departments.
    </p>

    <p>
        The course structure includes core subject content, emerging areas of knowledge, practical and laboratory components, computer applications, and recent advancements relevant to the discipline.
    </p>

    <h2>
        Components of Orientation Programmes
    </h2>

    <p>
        Orientation Programmes consist of four major components with a minimum of 144 contact hours spread over 24 working days.
    </p>

    <h3>
        Component A: Society, Environment, Development and Education
    </h3>

    <ul>
        <li>Constitution of India and secularism</li>
        <li>National integration</li>
        <li>Status of women and children</li>
        <li>Inclusive development</li>
        <li>Environmental awareness and biodiversity</li>
        <li>Economic issues and national development</li>
        <li>Urbanization and modernization</li>
        <li>Youth power</li>
        <li>Role and responsibility of teachers</li>
        <li>Value-based education</li>
        <li>Indian culture and identity</li>
        <li>Human rights</li>
        <li>Sustainable development</li>
        <li>Globalization, privatization and liberalization</li>
        <li>Public interest movements</li>
        <li>Aesthetics</li>
    </ul>

    <h3>
        Component B: Philosophy of Education and Pedagogy
    </h3>

    <ul>
        <li>Philosophy of education</li>
        <li>Indian education system and policies</li>
        <li>Economics of education</li>
        <li>Quality assurance and accreditation</li>
        <li>Learner psychology and motivation</li>
        <li>Teaching methods and classroom techniques</li>
        <li>Educational technology and ICT</li>
        <li>Curriculum design</li>
        <li>Evaluation and examination reforms</li>
        <li>Distance and open learning systems</li>
    </ul>

    <h3>
        Component C: Resource Awareness and Knowledge Generation
    </h3>

    <ul>
        <li>Information and Communication Technology</li>
        <li>Information networks and databases</li>
        <li>Libraries and documentation centres</li>
        <li>Museums, laboratories and centres of excellence</li>
        <li>Research projects and publications</li>
        <li>Industry-university linkages</li>
    </ul>

    <h3>
        Component D: Management and Personality Development
    </h3>

    <ul>
        <li>Communication skills</li>
        <li>Scientific temper and critical thinking</li>
        <li>Creativity and innovation</li>
        <li>Leadership and team building</li>
        <li>Administrative skills</li>
        <li>Educational management</li>
        <li>Student guidance and counselling</li>
        <li>Mental health and values</li>
        <li>Career planning and time management</li>
        <li>Teacher effectiveness and accountability</li>
    </ul>

    <h2>
        Information Technology Orientation
    </h2>

    <p>
        HRDC organizes interdisciplinary Refresher Courses in IT Awareness. IT orientation is also incorporated into other Orientation Programmes and Refresher Courses.
    </p>

    <h2>
        Eligibility and Target Group
    </h2>

    <p>
        Teachers working in universities and colleges covered under Section 2(f) of the UGC Act are eligible to participate in Orientation Programmes and Refresher Courses.
    </p>

    <ul>
        <li>Newly appointed lecturers with up to six years of service may attend Orientation Programmes.</li>
        <li>Completion of an Orientation Programme is generally required before attending a Refresher Course.</li>
        <li>A minimum gap of one year is normally maintained between two courses.</li>
        <li>Part-time, ad-hoc, temporary and contract teachers may also participate subject to eligibility conditions.</li>
    </ul>

    <h2>
        Duration of Programmes
    </h2>

    <ul>
        <li>
            Orientation Programme: 4 weeks, 24 working days, 144 contact hours.
        </li>

        <li>
            Refresher Course: 3 weeks, 18 working days, 108 contact hours.
        </li>
    </ul>

    <p>
        Participants who fail to complete the required contact hours may be allowed to make up the deficiency in another programme at their own expense.
    </p>

    <h2>
        Refresher Courses During Teacher Fellowship
    </h2>

    <p>
        Teachers on fellowship may attend Refresher Courses relevant to their research area provided they surrender fellowship living expenses for the course period and submit the required undertaking.
    </p>

    """

    return render(
        request,
        'public/info_page.html',
        {
            'title': 'Curriculum',
            'content': content
        }
    )

def course_coordinator(request):

    content = """

    <h2>
        Course Coordinator
    </h2>

    <p>
        The HRDC may appoint, if required, one Coordinator for a Refresher Course.
    </p>

    <p>
        A lump-sum honorarium of Rs. 6,000 is admissible to the Coordinator for the course.
    </p>

    <p>
        In special circumstances, more than one Coordinator may be appointed. In such cases, the honorarium amount is equally shared among the Coordinators.
    </p>

    <p>
        Coordinators are not entitled to receive honorarium for taking classes in the same course for which they are serving as Coordinator.
    </p>

    <h2>
        Orientation Programmes
    </h2>

    <p>
        In the case of Orientation Programmes, the Director may appoint one member of the academic staff as the Coordinator of the programme.
    </p>

    <p>
        Such Coordinators are not entitled to receive any honorarium for coordinating the programme.
    </p>

    """

    return render(
        request,
        'public/info_page.html',
        {
            'title': 'Course Coordinator',
            'content': content
        }
    )

def teaching_staff(request):

    return render(
        request,
        'public/teaching_staff.html',
        {
            'title': 'Teaching Staff'
        }
    )