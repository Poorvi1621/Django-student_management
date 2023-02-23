from django.shortcuts import render,redirect
from .models import AddCourses
from.models import AddStudents
from django.contrib import messages
from django.contrib import auth 
from django.contrib.auth.models import User

def index(request):
     return render(request,'index.html')
def uregs(request):
    if request.method=='POST':
        uname=request.POST['uname']
        email=request.POST['email']
        pwd=request.POST['pwd']
        user=User.objects.create_user(username=uname,password=pwd,email=email)
        user.save()
        return render(request,'index.html')
     
    else:
        return render(request,'sign-up.html')    

def ulogin(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return render(request,'dashboard.html')
        else:
            messages.info(request,'Invalid userid and password')
            return render(request,'index.html')
    else:
        return render(request,'signup.html')

# def courses(request):
#         c=courses()
#         c.coursename=request.POST['coursename']
#         c.fees=request.POST['fees']
#         c.comment=request.POST['comment']
#         c.date=request.POST['date']
#         c.save()
#         cr=courses.objects.all()
#         return render (request,'courses.html',{'cr':cr})  


def signup(request):
     return render(request,'sign-up.html')        

def welcome(request):
     return render(request,'dashboard.html')     
def courses(request):
     return render(request,'courses.html') 

def courses(request):
    stu = AddCourses.objects.all()
    return render(request, 'courses.html', 
                  { 'request':request,
                      'stu':stu,
                   
                    #   'stu':AddCourses.objects.all()
                   }
                  ) 

def addcourses(request):
    if request.method == "POST":
        c_name= request.POST['CourseName']
        c_fees= request.POST['CourseFees']
        c_duration= request.POST['Duration']
        c_desc= request.POST['CourseDesc']
        messages.success(request, "Course Added Successfully!!")
        AddCourses.objects.create(course=c_name, fees=c_fees, duration= c_duration, desc=c_desc)
        return redirect('courses')

def update_course(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        c_name= request.POST['CourseName']
        c_fees= request.POST['CourseFees']
        c_duration= request.POST['Duration']
        c_desc= request.POST['CourseDesc']
        AddCourses.objects.filter(id=uid).update(course=c_name, fees=c_fees, 
                                                duration= c_duration,
                                                desc=c_desc)
        return redirect('/courses/')                
    

def delete(request,id):   
        AddCourses.objects.filter(id=id).delete()
        return redirect('courses')  


def addstudent(request):
        if request.method == "POST":
            stu_name= request.POST.get("Name")
            stu_email= request.POST.get("Email")
            stu_mobile= request.POST.get("Mobile")
            stu_college= request.POST.get("College")
            stu_degree= request.POST.get("Degree")
            stu_address= request.POST.get("Address")
            stu_addcourse_id = request.POST.get("course")
            total_amount= request.POST.get("qty")
            paid_amount= request.POST.get("cost")
            due_amount= request.POST.get("DueAmount")
            stu_course= AddCourses.objects.get(id=stu_addcourse_id)
            if AddStudents.objects.filter(semail=stu_email).exists():
                messages.error(request, "Email id already exists")
                return redirect('addstudent')
        
            elif AddStudents.objects.filter(smobile=stu_mobile).exists():
                messages.error(request, "Mobile Number already exists")
                return redirect('addstudent')
            else:
                AddStudents.objects.create( sname=stu_name, 
                                            semail=stu_email, 
                                            smobile=stu_mobile,
                                            scollege=stu_college,
                                            sdegree=stu_degree,
                                            saddress=stu_address,
                                            scourse=stu_course,
                                            total_amount=total_amount,
                                            paid_amount=paid_amount,
                                            due_amount=due_amount,
                                            )
                messages.success(request, "Student Added Successfully!!")
                stu=AddStudents.objects.all()
                addcourses= AddCourses.objects.all()
                return render(request, 'viewstudents.html', {'stu':stu, 'addcourses':addcourses})
        else:
            stu=AddStudents.objects.all()
            addcourses= AddCourses.objects.all()
            return render(request, 'viewstudents.html', {'stu':stu, 'addcourses':addcourses})
        
          
 
def viewstudents(request):
     stu=AddStudents.objects.all()
     addcourses= AddCourses.objects.all()
     return render(request, 'viewstudents.html', {'stu':stu, 'addcourses':addcourses})
                      
def update_view(request, uid):
    res = AddCourses.objects.get(id=uid)
    return render(request, 'updatecourse.html', context={
        'stu': res,
    })
   
def delete(request):   
         id=request.GET['id']
         AddCourses.objects.get(id=id).delete()
         return redirect('courses')    
       
def update_course(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        c_name= request.POST['CourseName']
        c_fees= request.POST['CourseFees']
        c_duration= request.POST['Duration']
        c_desc= request.POST['CourseDesc']
        AddCourses.objects.filter(id=uid).update(course=c_name, fees=c_fees, 
                                                duration= c_duration,
                                                desc=c_desc)
        return redirect('/courses/')                

def profile(request):
    return render(request,'profile.html')


def addteacher(request):
     if request.method == "POST":
            stu_name= request.POST.get("Name")
            stu_email= request.POST.get("Email")
            stu_mobile= request.POST.get("Mobile")
            stu_address= request.POST.get("Address")
            Alternate_Contact_NO= request.POST.get("qty")
            Experience= request.POST.get("cost")
            Previous_salary= request.POST.get("DueAmount")
            if AddTeacher.objects.filter(semail=stu_email).exists():
                messages.error(request, "Email id already exists")
                return redirect('addteacher')
        
            elif AddTeacher.objects.filter(smobile=stu_mobile).exists():
                messages.error(request, "Mobile Number already exists")
                return redirect('addteacher')
            else:
                AddTeacher.objects.create( sname=stu_name, 
                                            semail=stu_email, 
                                            smobile=stu_mobile,
                                            saddress=stu_address,
                                            Alternate_Contact_NO=Alternate_Contact_NO,
                                            Experience=Experience,
                                            Previous_salary=Previous_salary,
                                            )
                messages.success(request, "teacher Added Successfully!!")
                stu=AddTeacher.objects.all()
                return render(request, 'teacher.html', {'stu':stu,
                                                                 })
     else:
            stu=AddTeacher.objects.all()
            return render(request, 'teacher.html', {'stu':stu})
