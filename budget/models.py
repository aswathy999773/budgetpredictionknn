from django.db import models
# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=90)
    password=models.CharField(max_length=90)
    type=models.CharField(max_length=90)

class officer(models.Model):
    lid=models.ForeignKey(login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=90)
    lname=models.CharField(max_length=90)
    place=models.CharField(max_length=90)
    postoffice=models.CharField(max_length=90)
    pin=models.BigIntegerField()
    phoneno=models.BigIntegerField()
    department=models.CharField(max_length=500)
    email=models.CharField(max_length=90)
    district= models.CharField(max_length=90)

class contract_company(models.Model):
    lid = models.ForeignKey(login, on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    place = models.CharField(max_length=90)
    postoffice = models.CharField(max_length=90)
    district = models.CharField(max_length=90)
    phoneno = models.BigIntegerField()
    email = models.CharField(max_length=90)
class supplier(models.Model):
    lid = models.ForeignKey(login, on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    place = models.CharField(max_length=90)
    postoffice = models.CharField(max_length=90)
    district = models.CharField(max_length=90)
    phoneno = models.BigIntegerField()
    email = models.CharField(max_length=90)
class work(models.Model):
    type = models.CharField(max_length=90)
    work = models.CharField(max_length=90)
    description = models.CharField(max_length=90)
    date = models.DateField(max_length=90)
    area = models.CharField(max_length=90)
class products(models.Model):
    sid = models.ForeignKey(supplier, on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    details = models.CharField(max_length=90)
    price = models.BigIntegerField()
    qty = models.CharField(max_length=90)
class contractorrequest(models.Model):
    date = models.DateField(max_length=90)
    request = models.CharField(max_length=90)
    cid = models.ForeignKey(contract_company, on_delete=models.CASCADE)
    wid = models.ForeignKey(work, on_delete=models.CASCADE)
    status = models.CharField(max_length=90)
class report(models.Model):
    wid = models.ForeignKey(work, on_delete=models.CASCADE)
    date = models.DateField(max_length=90)
    cid = models.ForeignKey(contract_company, on_delete=models.CASCADE)
    report = models.FileField()

class notification(models.Model):
    notification = models.CharField(max_length=90)
    date = models.DateField(max_length=90)

class instruction(models.Model):
    cid = models.ForeignKey(contract_company, on_delete=models.CASCADE)
    oid = models.ForeignKey(officer, on_delete=models.CASCADE)
    instruction = models.CharField(max_length=90)
class chat(models.Model):
    fid = models.ForeignKey(login, on_delete=models.CASCADE,related_name='fid')
    tid = models.ForeignKey(login, on_delete=models.CASCADE,related_name='tid')
    msg = models.TextField()
    date = models.DateField()




