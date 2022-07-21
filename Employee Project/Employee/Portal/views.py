from datetime import datetime
from distutils.command.build_scripts import first_line_re
from django.shortcuts import render,HttpResponse
from Portal.models import Employee,Roles,Department
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
   emps = Employee.objects.all()
   context={
    'emps':emps
   }
   print(context)
   return render(request,'view_emp.html',context)

def rem_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Error occured")    

    emps = Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove_emp.html',context)  

def add_emp(request):
    if request.method=='POST':
        print("POST me hain")
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        dept= int(request.POST['dept'])
        salary= int(request.POST['salary'])
        bonus= int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        role =  int(request.POST['role'])
        new_emp= Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,roles_id=role,hire_date=datetime.now())
        new_emp.save()
        return render(request,'add_emp.html')
    else: 
         return render(request,'add_emp.html')


def filter_emp(request):
    if(request.method=='POST'):
        name=request.POST['name']
        role=request.POST['role']
        dept=request.POST['dept']
        emps = Employee.objects.all();
        print("before filter")
        if name:
            emps = emps.filter(Q(first_name__icontains=name) |  Q(last_name__icontains=name))
        if dept:
            emps =emps.filter(dept__name=dept)
        if role:
            emps = emps.filter(roles__name=role)  
        print("Employees--->",emps)    
        context = {
            'emps':emps
        }  
        return render(request,'view_emp.html',context)        
    else:     
         return render(request,'filter_emp.html')
