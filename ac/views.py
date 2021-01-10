from ac.models import Manager
from django.db.models import manager
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from profilee.models import Employee
from django.http import HttpResponse
from datetime import datetime
from django import forms 
from profilee.models import Employee 
from profilee.forms import EmployeeForm
from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)



@login_required(login_url='/login')
def addemp(request): 
    pass
    print("stard")
    # # [discription,cost,types,credit/debit]
    # entry=[]
    # print("started")
    if request.method=='POST':
        print("stard")
        entry=request.POST.dict()
        # print(entry)
        a=Employee.objects.filter(empid=entry["empid"]).first()
        print("================")
        print(bool(a))
        print("=================")
        if a:
            messages.info(request,'Emp id exist!!!')
            print("stardssss")
        else :    
            newe=Employee.objects.create(Manager = request.user,
            empid = entry["empid"],
            fname = entry["fname"],
            lname = entry["lname"],
            address = entry["address"],
            DOB = entry["dob"],
                mob = entry["mob"],
                city = entry["city"],
                )
            newe.save();
                # print("starsssssssssted")
            messages.info(request,'succefully added!!!')
        return redirect("index")
        try:
            pass
            
            # else:
            #     messages.info(request,'Invalid transaction!!!')    
        except:
            pass
            messages.info(request,'except!!!')
    return render(request, 'tables.html')



@login_required(login_url='/login')
def viewmodel(request,id): 
    context ={} 
    tabb=Employee.objects.filter(Manager_id=request.user,empid=id)
    # add the dictionary during initialization 
    form = EmployeeForm(request.POST or None)
    if form.is_valid(): 
        form.save() 
    context['form']= form 
    return render(request, "view.html", {'tab':tabb})

@login_required(login_url='/login')
def editmodel(request,id): 
    context ={} 
    tabb=Employee.objects.filter(Manager_id=request.user,id=id).first()
    # add the dictionary during initialization 
    # print(tabb.id)
    # form = EmployeeForm(request.POST or None)
    # if form.is_valid(): 
    #     form.save() 
    # context['form']= form 
    if request.method == 'POST':
            entry=request.POST.dict()
            print("-----------------------")
            print([type(i) for i in entry.values()])
            print("-----------------------")
            nb=int(entry["empid"])
            tabb.fname='nk'
            nkk=[int(request.POST["empid"]),request.POST["fname"],request.POST["lname"],request.POST["address"],request.POST["dob"],request.POST["mob"],request.POST["city"]]
            print(nkk)
            # tabb.empid = request.POST["empid"]
            # tabb.fname = request.POST["fname"],
            # tabb.lname = entry["lname"][1:-2],
            # tabb.address = request.POST["address"],
            # tabb.DOB = request.POST["dob"],
            # tabb.mob = request.POST["mob"],
            # tabb.city = request.POST["city"]
            # tabb.save()
            tabb.empid = request.POST["empid"]
            tabb.fname = request.POST["fname"]
            tabb.lname = entry["lname"][1:-2]
            tabb.address = request.POST["address"]
            tabb.DOB = request.POST["dob"]
            tabb.mob = request.POST["mob"]
            tabb.city = request.POST["city"]
            tabb.save()
            messages.info(request,'successfully Edited!!!')
    return render(request, "edit.html", {'tab':tabb})

@login_required(login_url='/login')
def deletemodel(request, id):
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
    # fetch the object related to passed id 
    obj = get_object_or_404(Employee, id = id) 
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return HttpResponseRedirect("/") 
    return render(request, "del.html",{'tab':obj}) 

@login_required(login_url='/login')
def index (request):
    global dash
    contextt ={}     
    dash={}
    # add the dictionary during initialization 
    form = EmployeeForm(request.POST or None) 
    if form.is_valid(): 
        form.save()   
    dash['form']= form 
    # return render(request, "create_view.html", context) 
    aaa=Manager.objects.filter(user=request.user)
    tabb=Employee.objects.filter(Manager_id=request.user)
    add=aaa[0].address
    company=aaa[0].company
    print("===================")
    print("index")
    print("===================")
    nk=[]
    nkk=[]
    for i in range(0,len(add),15):
        pass
        nk.append(add[i:i+15])
        nkk.append(company[i:i+15])
        # nk.append("\n")
    print("===================")
    print(nkk)
    print("===================")
    return render(request, 'tables.html',{'aaa':aaa[0],'address':nk,'tab':tabb,'company':nkk})

def login(request):
    # print("strdddat")
    if request.method== 'POST':
        # print("strat")
        username = request.POST['UserName']
        name = request.POST['UserName']
        password = request.POST['Password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("index")
            # login_mesaage(request.POST['UserName'])
            # return redirect("welcome")
        else:
            messages.info(request,'invalid credentials or Ask for activation')
            return redirect('login')

    else:
        return render(request,'log.html')    

def register(request):
    global reg
    reg=dict()
    if request.method == 'POST':
        reg['FirstName']=first_name = request.POST['FirstName']
        reg['LastName']=last_name = request.POST['LastName']
        password1 = request.POST['PasswordA']
        password2 = request.POST['PasswordB']
        reg['Email']=email = request.POST['Email']
        reg['UserName']=username=request.POST['Email']
        reg['address']=address=request.POST['address']
        reg['dob']=dob=request.POST['dob']
        reg['company']=company=request.POST['company']
        # reg['UserName']=username = request.POST['UserName']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name,is_active='True')
                user.save();
                user = auth.authenticate(username=username,password=password1)
                if user is not None:
                    auth.login(request, user)
                man=Manager.objects.create(user=request.user,DOB=dob,address=address,company=company)
                man.save();
                messages.info(request,'Email Taken')
                print('user created')
                # reg_mesaage()
                # 
                return redirect("index")

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')
        return redirect('/')
        
    else:
        return render(request,'reg.html')

@login_required(login_url='/login')
def logout(request):
    auth.logout(request)  
    return redirect('login')   
