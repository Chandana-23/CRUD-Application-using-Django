from django.shortcuts import redirect, render

from baseapp.models import Student

# Create your views here.
def home(request):
    return render(request,'base.html')

def create(request):
    return render(request,'create.html')

def add(request):
    if request.method=='POST':
        roll = int(request.POST['roll'])
        fname = request.POST['fname']
        lname = request.POST['lname']
        dob = request.POST['dob']
        phone = request.POST['phone']
        email = request.POST['email']
        s = Student(roll=roll,fname=fname,lname=lname,dob=dob,phone=phone,email=email)
        s.save()
        return render(request,'success.html')
    else:
        return render(request,'error.html')

def read(request):
    d = Student.objects.all()
    return render(request,'read.html',{'data':d})

def update(request):
    if request.method == 'POST':
        roll = int(request.POST['roll'])
        fname = request.POST['fname']
        lname = request.POST['lname']
        dob = request.POST['dob']
        phone = request.POST['phone']
        email = request.POST['email']
        d = Student.objects.all()
        l = [i.roll for i in d]
        print(l)
        if roll in l:
            Student.objects.filter(roll=roll).update(fname=fname,lname=lname,dob=dob,phone=phone,email=email)
            return render(request,'success.html')
        else:
            return render(request,'error.html')
    return render(request,'update.html')


def delete(request,roll):
    Student.objects.get(roll=roll).delete()
    return redirect('read')

def deleteall(request):
    Student.objects.all().delete()
    return redirect('read')