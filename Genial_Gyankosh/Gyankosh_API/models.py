from django.db import models, connection


# Create your models here.

class UserMaster(models.Model):
    UserID = models.BigAutoField(primary_key=True)
    UserName = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Password = models.CharField(max_length=255)
    Isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'UserMaster'


class TechnologyMaster(models.Model):
    TechID = models.BigAutoField(primary_key=True)
    TechName = models.CharField(max_length=30)

    class Meta:
        db_table = 'TechnologyMaster'


class ControlTypeMaster(models.Model):
    ControlID = models.BigAutoField(primary_key=True)
    ControlName = models.CharField(max_length=50)
    TechID = models.ForeignKey('TechnologyMaster', on_delete=models.CASCADE)

    class Meta:
        db_table = 'ControlMaster'


class IssueOriginMaster(models.Model):
    IssOriID = models.BigAutoField(primary_key=True)
    IssOriName = models.CharField(max_length=100)

    class Meta:
        db_table = 'IssueOriginMaster'


class ProblemMaster(models.Model):
    ProblemID = models.BigAutoField(primary_key=True)
    TechID = models.ForeignKey('TechnologyMaster', on_delete=models.CASCADE)
    ControlID = models.ForeignKey('ControlTypeMaster', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    UserID = models.ForeignKey('UserMaster', on_delete=models.CASCADE)
    ProblemTitle = models.CharField(max_length=250)
    ProblemDesc = models.CharField(max_length=1000)
    CreatedDate = models.DateTimeField(auto_now=True)
    UpdatedDate = models.DateTimeField(auto_now=True)
    Isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'ProblemMaster'


class SolutionMaster(models.Model):
    SolutionID = models.BigAutoField(primary_key=True)
    ProblemID = models.ForeignKey('ProblemMaster', on_delete=models.CASCADE)
    IsVerified = models.BooleanField(default=False)
    UserID = models.ForeignKey('UserMaster', on_delete=models.CASCADE)
    SolutionDesc = models.CharField(max_length=1000)
    CreatedDate = models.DateTimeField(auto_now=True)
    UpdatedDate = models.DateTimeField(auto_now=True)
    Isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'SolutionMaster'


class SPModels:
    @staticmethod
    def login(username, password):
        # connection = psycopg2.connect("dbname=Captain user=postgres password= SanDisk@2754")
        cur = connection.cursor()
        cur.callproc('login',[username, password])

        result = cur.fetchall()
        print('+++++++', result)
        cur.close()
        return result
