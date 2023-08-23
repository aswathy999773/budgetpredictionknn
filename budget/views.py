from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
# Create your views here.
from budget.models import *
def main(request):
    return render(request,'index.html')
def reg(request):
    return render(request,'regindex.html')
def reg1(request):
    return render(request,'regindex2.html')
@login_required(login_url='/')
def addofficer(request):
    return render(request,'admin/add officer.html')
@login_required(login_url='/')
def addwork(request):
    return render(request,'admin/add work.html')
@login_required(login_url='/')
def addprod(request):
    return render(request,'sup/addprod.html')
@login_required(login_url='/')
def mngprod(request):
    ob=products.objects.filter(sid__lid__id=request.session['lid'])
    return render(request,'sup/manage_prod.html',{'val':ob})
@login_required(login_url='/')
def vprod(request):
    ob=supplier.objects.filter(lid__type='supplier')
    return render(request,'contractor/vprod.html',{'v':ob})
@login_required(login_url='/')
def vprod1(request):
    pr=request.POST['select']
    ob1=supplier.objects.filter(lid__type='supplier')
    ob=products.objects.filter(sid__id=pr)
    return render(request,'contractor/vprod.html',{'val':ob,'v':ob1,'p':int(pr)})
@login_required(login_url='/')
def addmanageofficer(request):
    ob = officer.objects.all()
    return render(request,'admin/add_manage oficer.html',{'val':ob})
@login_required(login_url='/')
def addmanagework(request):
    ob = work.objects.all()
    return render(request,'admin/add_manage work.html',{'val':ob})
@login_required(login_url='/')
def homepage(request):
    return render(request,'admin/homepge.html')
@login_required(login_url='/')
def sentnotification(request):
    ob = notification.objects.all()
    return render(request,'admin/sent notification.html',{'val':ob})
@login_required(login_url='/')
def verifycontractor(request):
    ob = contract_company.objects.all()
    return render(request,'admin/verify contractor.html',{'val':ob})
@login_required(login_url='/')
def verifysup(request):
    ob = supplier.objects.all()
    return render(request,'admin/verifysup.html',{'val':ob})
@login_required(login_url='/')
def viewrqstverify(request):
   return render(request,'admin/view rqst&verify.html')
@login_required(login_url='/')
def searchwithdate(request):
    dates=request.POST['textfield']
    ob=contractorrequest.objects.filter(date=dates)
    return render(request, 'admin/view rqst&verify.html',{'val':ob})

@login_required(login_url='/')
def viewworkstatus(request):
    cont=request.POST['select']
    obb = contract_company.objects.filter(lid__type='company')
    ob=contractorrequest.objects.filter(cid__id=cont)
    return render(request,'admin/view work status.html',{'val1':obb,'val':ob})



def adminwrlkstatusview(request):
    obb = contract_company.objects.filter(lid__type='company')
    return render(request, 'admin/view work status.html',{'val1':obb})


@login_required(login_url='/')
def addreport(request):
    ob=report.objects.filter(cid__lid__id=request.session['lid'])
    return render(request,'contractor/Add report.html',{'val':ob})

@login_required(login_url='/')
def homecontractor(request):
    return render(request,'contractor/homecontractor.html')

@login_required(login_url='/')
def reports(request):
    ob=contractorrequest.objects.filter(cid__lid__id=request.session['lid'])
    return render(request,'contractor/report.html',{'val':ob})

@login_required(login_url='/')
def reportts(request):
    wrk=request.POST['select']
    reports=request.FILES['file']
    fp=FileSystemStorage()
    fs=fp.save(reports.name,reports)
    iob=report()
    iob.report=fs
    iob.wid=work.objects.get(id=wrk)
    iob.cid=contract_company.objects.get(lid__id=request.session['lid'])
    iob.date=datetime.today()
    iob.save()
    messages.success(request, 'Ok')
    return HttpResponse('''<script>window.location='/addreport#about'</script>''')

@login_required(login_url='/')
def update(request,id):
    ob = contractorrequest.objects.get(id=id)
    request.session['coid'] = id
    return render(request,'contractor/update.html', {'val': ob})

@login_required(login_url='/')
def updatewrkstatus(request):
    stat=request.POST['textfield']
    ob=contractorrequest.objects.get(id=request.session['coid'])
    ob.status=stat
    ob.save()
    return HttpResponse('''<script>window.location='/updateworkstatus#about'</script>''')

@login_required(login_url='/')
def updateworkstatus(request):
    ob = contractorrequest.objects.filter(cid__lid__id=request.session['lid'])
    return render(request,'contractor/update work status.html',{'val': ob})

@login_required(login_url='/')
def viewinstruction(request):
    ob = instruction.objects.filter(cid__lid__id=request.session['lid'])
    return render(request,'contractor/view instruction.html',{'val':ob})

@login_required(login_url='/')
def viewnotification(request):
    ob = notification.objects.all()
    return render(request,'contractor/view notification.html',{'val':ob})

@login_required(login_url='/')
def viewworkrqst(request):
    ob = work.objects.all()
    result=[]
    for i in ob:
        obb=contractorrequest.objects.filter(wid__id=i.id,cid__lid__id=request.session['lid'])
        if len(obb)>0:
            i.status="applied"
        else:
            i.status='pending'
        result.append(i)
    return render(request,'contractor/view work and rqst.html',{'val':result})

@login_required(login_url='/')
def homeofficer(request):
    return render(request,'officer/homeofficer.html')
@login_required(login_url='/')
def homesup(request):
    return render(request,'supindex.html')
@login_required(login_url='/')
def viewcontractor(request):
    ob = contract_company.objects.all()
    return render(request,'officer/view contractor.html',{'val':ob})

@login_required(login_url='/')
def viewofficernoti(request):
    ob = notification.objects.all()
    return render(request,'officer/view notification.html',{'val':ob})

@login_required(login_url='/')
def instruction1(request,id):
    request.session['contrid']=id
    return render(request,'officer/instruction.html')

@login_required(login_url='/')
def addinstruction(request):
    inst=request.POST['textfield']
    ob=instruction()
    ob.oid=officer.objects.get(lid__id=request.session['lid'])
    ob.cid=contract_company.objects.get(id=request.session['contrid'])
    ob.instruction=inst
    ob.save()
    messages.success(request, 'Added')
    return HttpResponse('''<script>window.location='/viewcontractor#about'</script>''')

@login_required(login_url='/')
def viewstatus(request):
    ob=contractorrequest.objects.all()
    return render(request,'officer/view work status.html',{'val':ob})

@login_required(login_url='/')
def verifycontractor1(request,id):
    ob=login.objects.get(id=id)
    ob.type='company'
    ob.save()
    messages.success(request, 'Accepted')
    return HttpResponse('''<script>window.location='/verifycontractor#about'</script>''')
@login_required(login_url='/')
def verifysup1(request,id):
    ob=login.objects.get(id=id)
    ob.type='supplier'
    ob.save()
    messages.success(request, 'Accepted')
    return HttpResponse('''<script>window.location='/verifysup#about'</script>''')
@login_required(login_url='/')
def rejectsup(request):
    ob = login.objects.get(id=id)
    ob.type = 'reject'
    ob.save()
    messages.success(request, 'Rejected')
    return HttpResponse('''<script>window.location='/verifysup#about'</script>''')
@login_required(login_url='/')
def rejectcontractor(request):
    ob = login.objects.get(id=id)
    ob.type = 'reject'
    ob.save()
    messages.success(request, 'Rejected')
    return HttpResponse('''<script>window.location='/verifycontractor#about'</script>''')

@login_required(login_url='/')
def workrqst(request,id):
    ob = contractorrequest.objects.get(id=id)
    ob.status='accepted'
    ob.save()
    messages.success(request, 'Accepted')
    return HttpResponse('''<script>window.location='/viewrqstverify#about'</script>''')

@login_required(login_url='/')
def workreject(request,id):
    ob = contractorrequest.objects.get(id=id)
    ob.status = 'reject'
    ob.save()
    messages.success(request, 'Rejected')
    return HttpResponse('''<script>window.location='/viewrqstverify#about'</script>''')
def regcode(request):
    cname=request.POST['textfield']
    place=request.POST['textfield3']
    postoffice= request.POST['textfield4']
    pin= request.POST['textfield5']
    email = request.POST['textfield6']
    phoneno = request.POST['textfield7']
    username= request.POST['textfield8']
    password=request.POST['textfield9']
    district=request.POST['textfield10']
    ob=login()
    ob.username=username
    ob.password=password
    ob.type='pending'
    ob.save()
    iob=contract_company()
    iob.name=cname
    iob.place=place
    iob.postoffice=postoffice
    iob.pin=pin
    iob.email=email
    iob.phoneno=phoneno
    iob.username=username
    iob.password=password
    iob.district=district
    iob.lid=ob
    iob.save()
    messages.success(request, 'Registered')
    return HttpResponse('''<script>window.location='/'</script>''')
def regcode2(request):
    cname=request.POST['textfield']
    place=request.POST['textfield3']
    postoffice= request.POST['textfield4']
    pin= request.POST['textfield5']
    email = request.POST['textfield6']
    phoneno = request.POST['textfield7']
    username= request.POST['textfield8']
    password=request.POST['textfield9']
    district=request.POST['textfield10']
    ob=login()
    ob.username=username
    ob.password=password
    ob.type='pending'
    ob.save()
    iob=supplier()
    iob.name=cname
    iob.place=place
    iob.postoffice=postoffice
    iob.pin=pin
    iob.email=email
    iob.phoneno=phoneno
    iob.username=username
    iob.password=password
    iob.district=district
    iob.lid=ob
    iob.save()
    messages.success(request, 'Registered')
    return HttpResponse('''<script>window.location='/'</script>''')
def logincode(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    try:
        ob=login.objects.get(username=username,password=password)
        if ob.type == 'admin':
            ob1=auth.authenticate(username='admin',password='admin')
            print(ob1,"====================")
            print(ob1,"====================")
            print(ob1,"====================")
            print(ob1,"====================")
            print(ob1,"====================")
            print(ob1,"====================")
            auth.login(request,ob1)
            messages.success(request,'Welcome to Admin homepage')
            return HttpResponse('''<script>window.location='/homepage'</script>''')
        elif ob.type == 'company':
            request.session['lid']=ob.id
            ob1 = auth.authenticate(username='admin', password='admin')
            auth.login(request, ob1)
            messages.success(request, 'Welcome to Contract Company homepage')
            return HttpResponse('''<script>window.location='/homecontractor'</script>''')
        elif ob.type == 'officer':
            request.session['lid'] = ob.id
            ob1 = auth.authenticate(username='admin', password='admin')
            auth.login(request, ob1)
            messages.success(request, 'Welcome to Officer homepage')
            return HttpResponse('''<script>window.location='/homeofficer'</script>''')
        elif ob.type == 'supplier':
            request.session['lid'] = ob.id
            ob1 = auth.authenticate(username='admin', password='admin')
            auth.login(request, ob1)
            messages.success(request, 'Welcome to Supplier homepage')
            return HttpResponse('''<script>window.location='/homesup'</script>''')
        else:
            messages.success(request, 'Invalid')
            return HttpResponse('''<script>window.location='/'</script>''')
    except:
        messages.success(request, 'Invalid')
        return HttpResponse('''<script>window.location='/'</script>''')

@login_required(login_url='/')
def deletedofficer(request,id):
    ob=officer.objects.get(lid__id=id)
    ob.delete()
    iob=login.objects.get(id=id)
    iob.delete()
    messages.success(request, 'Deleted')
    return HttpResponse('''<script>window.location='/addmanageofficer#about'</script>''')


@login_required(login_url='/')
def editofficer(request,id):
    ob=officer.objects.get(id=id)
    request.session['ofid']=id
    return render(request,'admin/edit officer.html',{'val':ob})

@login_required(login_url='/')
def updateofficer(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    place = request.POST['place']
    postoffice = request.POST['post']
    district = request.POST['district']
    phoneno = request.POST['phone']
    email = request.POST['email']
    pin = request.POST['pin']
    iob = officer.objects.get(id=request.session['ofid'])
    iob.fname = fname
    iob.lname = lname
    iob.place = place
    iob.postoffice = postoffice
    iob.email = email
    iob.phoneno = phoneno
    iob.district = district
    iob.pin = pin
    iob.save()
    messages.success(request, 'Updated')
    return HttpResponse('''<script>window.location='/addmanageofficer#about'</script>''')

@login_required(login_url='/')
def officercode(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    place=request.POST['place']
    postoffice=request.POST['post']
    district=request.POST['district']
    phoneno=request.POST['phone']
    email=request.POST['email']
    username=request.POST['uname']
    password=request.POST['pw']
    pin=request.POST['pin']
    dep=request.POST['select']
    ob = login()
    ob.username = username
    ob.password = password
    ob.type = 'officer'
    ob.save()
    iob = officer()
    iob.fname = fname
    iob.lname = lname
    iob.place = place
    iob.department=dep
    iob.postoffice = postoffice
    iob.email = email
    iob.phoneno = phoneno
    iob.username = username
    iob.password = password
    iob.district = district
    iob.pin = pin
    iob.lid = ob
    iob.save()
    messages.success(request, 'Add Officer')
    return HttpResponse('''<script>window.location='/addmanageofficer'</script>''')
@login_required(login_url='/')
def addprod1(request):
    nm = request.POST['textfield']
    descriptions= request.POST['textfield2']
    price = request.POST['textfield3']
    qtyy = request.POST['textfield4']
    iob= products()
    iob.name=nm
    iob.qty=qtyy
    iob.details=descriptions
    iob.price=price
    iob.sid=supplier.objects.get(lid__id=request.session['lid'])
    iob.save()
    messages.success(request, 'Product added...')
    return HttpResponse('''<script>window.location='/mngprod'</script>''')

@login_required(login_url='/')
def workcode(request):
    works = request.POST['textfield']
    descriptions= request.POST['textfield2']
    type = request.POST['textfield3']
    area_const = request.POST['textfield4']
    iob= work()
    iob.work=works
    iob.type=type
    iob.description=descriptions
    iob.date=datetime.today()
    iob.area=area_const
    iob.save()
    messages.success(request, 'Add Work')
    return HttpResponse('''<script>window.location='/addmanagework'</script>''')

@login_required(login_url='/')
def notisent(request):
    return render(request,'admin/snt noti.html')

@login_required(login_url='/')
def notifications(request):
    notifications=request.POST['textfield']
    iob= notification()
    iob.notification=notifications
    iob.date=datetime.today()
    iob.time=datetime.today()
    iob.save()
    messages.success(request, 'Ok')
    return HttpResponse('''<script>window.location='/homepage'</script>''')

@login_required(login_url='/')
def instructions(request,id):
    ob=instruction.objects.get(id=id)
    request.session['inid']=id
    return render(request,'instruction.html')

@login_required(login_url='/')
def instruct(request):
    instructs=request.POST['textfield']
    ob=instruction.objects.get(id=request.session['inid'])
    ob.instruction=instructs
    ob.save()
    messages.success(request, 'Ok')
    return HttpResponse('''<script>window.location='/view contractor.html'</script>''')

@login_required(login_url='/')
def viewofficerreport(request):
    ob = contract_company.objects.filter(lid__type='company')
    return render(request,'officer/view report.html',{'val':ob})

@login_required(login_url='/')
def searchwithcontractor(request):
    contractors=request.POST['select']
    ob = contract_company.objects.all()
    obb= report.objects.filter(cid__id=contractors)
    print(obb,"++",contractors)
    return render(request, 'officer/view report.html', {'val':ob,'val1': obb,})
@login_required(login_url='/')
def viewreport(request):
    ob=contract_company.objects.all()
    return render(request,'admin/view report.html',{'val':ob})
@login_required(login_url='/')
def chat1(request,id):
    request.session['uid']=id
    from django.db.models import Q
    ob1=supplier.objects.get(lid__id=request.session['lid'])
    ob=chat.objects.filter(Q(fid__id=request.session['lid'],tid__id=id)|Q(fid__id=id,tid__id=request.session['lid'])).order_by('id')
    print(ob,"================")
    return render(request,'sup/chat.html',{'data':ob,'fname':ob1.name,'fr':request.session['lid']})
@login_required(login_url='/')
def chat2(request):
    id=request.session['uid']
    from django.db.models import Q
    ob1=supplier.objects.get(lid__id=request.session['lid'])
    ob=chat.objects.filter(Q(fid__id=request.session['lid'],tid__id=id)|Q(fid__id=id,tid__id=request.session['lid'])).order_by('id')
    print(ob,"================")
    return render(request,'sup/chat.html',{'data':ob,'fname':ob1.name,'fr':request.session['lid']})
@login_required(login_url='/')
def chat_s(request):
    msg = request.POST['textarea']
    ob = chat()
    ob.fid = login.objects.get(id=request.session['lid'])
    ob.tid = login.objects.get(id=request.session['uid'])
    ob.date = datetime.today()
    ob.msg = msg
    ob.save()
    return redirect('/chat2')
@login_required(login_url='/')
def viewanddwnmloadreport(request):
    ob = contract_company.objects.all()
    c=request.POST['select']
    oob=report.objects.filter(cid__id=c)
    return render(request, 'admin/view report.html', {'val': ob,'val1':oob})
@login_required(login_url='/')
def chat11(request,id):
    request.session['uid']=id
    from django.db.models import Q
    ob1=contract_company.objects.get(lid__id=request.session['lid'])
    ob=chat.objects.filter(Q(fid__id=request.session['lid'],tid__id=id)|Q(fid__id=id,tid__id=request.session['lid'])).order_by('id')
    print(ob,"================")
    return render(request,'contractor/chat.html',{'data':ob,'fname':ob1.name,'fr':request.session['lid']})
@login_required(login_url='/')
def chat22(request):
    id=request.session['uid']
    from django.db.models import Q
    ob1=contract_company.objects.get(lid__id=request.session['lid'])
    ob=chat.objects.filter(Q(fid__id=request.session['lid'],tid__id=id)|Q(fid__id=id,tid__id=request.session['lid'])).order_by('id')
    print(ob,"================")
    return render(request,'contractor/chat.html',{'data':ob,'fname':ob1.name,'fr':request.session['lid']})
@login_required(login_url='/')
def chat_ss(request):
    msg = request.POST['textarea']
    ob = chat()
    ob.fid = login.objects.get(id=request.session['lid'])
    ob.tid = login.objects.get(id=request.session['uid'])
    ob.date = datetime.today()
    ob.msg = msg
    ob.save()
    return redirect('/chat22')
@login_required(login_url='/')
def editreport(request,id):
    oob=contractorrequest.objects.filter(cid__lid__id=request.session['lid'])
    ob=report.objects.get(id=id)
    request.session['rid']=id
    return render(request,'contractor/editreport.html',{'val1':oob,'val':ob})

@login_required(login_url='/')
def updatereport(request):
    try:
        wrk = request.POST['select']
        reports = request.FILES['file']
        fp = FileSystemStorage()
        fs = fp.save(reports.name, reports)
        iob = report.objects.get(id=request.session['rid'])
        iob.report = fs
        iob.wid = work.objects.get(id=wrk)
        iob.cid = contract_company.objects.get(lid__id=request.session['lid'])
        iob.date = datetime.today()
        iob.save()
        messages.success(request, 'Ok')
        return HttpResponse('''<script>window.location='/addreport'</script>''')
    except:
        wrk = request.POST['select']
        iob = report.objects.get(id=request.session['rid'])
        iob.wid = work.objects.get(id=wrk)
        iob.cid = contract_company.objects.get(lid__id=request.session['lid'])
        iob.date = datetime.today()
        iob.save()
        messages.success(request, 'Ok')
        return HttpResponse('''<script>window.location='/addreport'</script>''')

@login_required(login_url='/')
def deletedreport(request,id):
    ob = report.objects.get(id=id)
    ob.delete()
    messages.success(request, 'Deleted')
    return HttpResponse('''<script>window.location='/addreport'</script>''')

@login_required(login_url='/')
def workrequest(request,id):
    request.session['worid']=id
    return render(request,'contractor/addrequest.html')

@login_required(login_url='/')
def vcompany(request):
    ob=contract_company.objects.filter(lid__type='company')
    return render(request,'sup/company.html',{'v':ob})
@login_required(login_url='/')
def vsup(request):
    ob=supplier.objects.filter(lid__type='supplier')
    return render(request,'contractor/suplier.html',{'v':ob})
@login_required(login_url='/')
def sendrequestforwork(request):
    requ=request.POST['textfield']
    ob=contractorrequest()
    ob.date=datetime.today()
    ob.cid=contract_company.objects.get(lid__id=request.session['lid'])
    ob.wid=work.objects.get(id=request.session['worid'])
    ob.request=requ
    ob.status='pending'
    ob.save()
    messages.success(request, 'Request Sended')
    return HttpResponse('''<script>window.location='/viewworkrqst'</script>''')

@login_required(login_url='/')
def request(request):
    ob = request.objects.all()
    return render(request,'contractor/request.html',{'val':ob})

@login_required(login_url='/')
def deletework(request,id):
    ob = work.objects.get(id=id)
    ob.delete()
    messages.success(request, 'Deleted')
    return HttpResponse('''<script>window.location='/addmanagework'</script>''')
@login_required(login_url='/')
def deleteprod(request,id):
    ob = products.objects.get(id=id)
    ob.delete()
    messages.success(request, 'Deleted')
    return HttpResponse('''<script>window.location='/mngprod'</script>''')
@login_required(login_url='/')
def editwork(request,id):
    ob=work.objects.get(id=id)
    request.session['woid']=id
    return render(request,'admin/editwork.html',{'val':ob})

@login_required(login_url='/')
def updateworks(request):
    works = request.POST['textfield']
    description = request.POST['textfield2']
    type = request.POST['textfield3']
    area1 = request.POST['textfield4']
    iob = work.objects.get(id=request.session['woid'])
    iob.work = works
    iob.description = description
    iob.type = type
    iob.date = datetime.today()
    iob.area=area1
    iob.save()
    messages.success(request, 'Updated')
    return HttpResponse('''<script>window.location='/addmanagework'</script>''')

def logout(request):
    auth.logout(request)
    return render(request,'index.html')
def prediction(request,id):
    request.session['rid']=id
    return render(request, 'contractor/prediction.html')
def predictionbudget(request):
    from budget.prediction import knn_predict
    projecttype = request.GET['textfield']
    projectdescription = request.GET['textfield2']
    projectphasename = request.GET['textfield3']
    projectstatusname = request.GET['textfield4']
    area = request.GET['textfield5']

    X_test=[projecttype ,projectdescription,projectphasename,projectstatusname]
    print(X_test)
    print(area)
    pred = knn_predict(X_test)[0]
    result="below 500000"
    if pred==1:
        result="between 500000 and 1000000"
    elif pred==2:
        result="between 1000000 and 5000000"
    elif pred==3:
        result = "between 5000000 and 25000000"
    elif pred==4:
        result = "between 25000000 and 50000000"
    elif pred==5:
        result = "between 50000000 and 100000000"
    elif pred==6:
        result = "between 100000000 and 150000000"
    elif pred==7:
        result = "Above 150000000 "
    return render(request,"contractor/result.html",{"val":result,'rid':request.session['rid']})