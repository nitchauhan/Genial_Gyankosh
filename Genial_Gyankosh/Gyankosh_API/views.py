from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import UserMasterSerializer


class Login(ModelViewSet):
    queryset = UserMaster.objects.all()
    serializer_class = UserMasterSerializer

    @action(methods=['post'],detail=False)
    def login(self, request):
        print(request.data)
        login_obj = SPModels.login(request.data.get('username'), request.data.get('password'))
        print(login_obj)
        if login_obj[0][0] != -1:
            datadict = {'userid': login_obj[0][0], 'fullname': login_obj[0][1]}
            senddata = {'status': 'Success', 'data': datadict}
        else:
            datadict = {'userid': -1, 'fullname': 'NA'}
            senddata = {'status': 'Fail', 'data': datadict}
        return Response(senddata)


class Dashboard(ModelViewSet):
    queryset = UserMaster.objects.all()
    serializer_class = UserMasterSerializer

    @action(methods=['post'], detail=False)
    def get_dashboard_count(self, request):
        print(request.data)
        try:
            db_obj_total = ProblemMaster.objects.filter(Isactive=True).count()
            db_obj_solved = ProblemMaster.objects.filter(status=True).count()
            datadict = {'total_que': db_obj_total, 'solved': db_obj_solved}
            senddata = {'status': 'Success', 'data': datadict}
        except Exception:
            senddata = {'status': 'Fail'}
        return Response(senddata)

    @action(methods=['post'], detail=False)
    def get_dashboard_quelist(self, request):
        print(request.data)
        try:
            db_obj_total = ProblemMaster.objects.all().order_by('-ProblemID')[:10]
            print(db_obj_total)
            datalist = []
            for i in db_obj_total:
                datalist.append({'quoid': i.ProblemID, 'question': i.ProblemTitle})
            senddata = {'status': 'Success', 'data': datalist}
        except Exception:
            senddata = {'status': 'Fail'}
        return Response(senddata)


class Question(ModelViewSet):
    queryset = UserMaster.objects.all()
    serializer_class = UserMasterSerializer

    @action(methods=['post'], detail=False)
    def get_que_search_result(self, request):
        print(request.data)
        try:
            tech_obj = ProblemMaster.objects.filter(ProblemTitle__icontains=request.data.get('tag'),
                                                    ProblemDesc__icontains=request.data.get('tag')).order_by(
                'ProblemTitle')
            datalist = []
            for i in tech_obj:
                datalist.append({
                    'ProblemID': i.ProblemID,
                    'ProblemTitle': i.ProblemTitle
                })
            senddata = {'status': 'Success', 'data': datalist}
            print(senddata)
        except Exception:
            senddata = {'status': 'Fail'}
        return Response(senddata)

    @action(methods=['post'], detail=False)
    def ins_question(self, request):
        print(request.data)
        try:
            if request.data.get('TechID') == 0:
                tech_obj = TechnologyMaster.objects.create(
                    TechName=request.data.get('TechName')
                )
                print(tech_obj)
                techid = tech_obj.TechID
            else:
                techid = request.data.get('TechID')

            if request.data.get('ControlID') == 0:
                control_obj = ControlTypeMaster.objects.create(
                    ControlName=request.data.get('ControlName'),
                    TechID_id=techid
                )
                controlid = control_obj.ControlID
            else:
                controlid = request.data.get('ControlID')

            problem_obj = ProblemMaster.objects.create(
                TechID_id=techid,
                ControlID_id=controlid,
                status=False,
                UserID_id=request.data.get('USERID'),
                ProblemTitle=request.data.get('ProblemTitle'),
                ProblemDesc=request.data.get('ProblemDesc')
            )
            senddata = {'status': 'Success'}
        except Exception as e:
            print(str(e))
            senddata = {'status': 'Fail'}
        print('send data -> ', senddata)
        return Response(senddata)

    @action(methods=['post'], detail=False)
    def get_basic_autocomplete(self, request):
        print(request.data)
        try:
            tech_obj = TechnologyMaster.objects.all().order_by('TechName')
            datalist = []
            for i in tech_obj:
                datalist.append({
                    'TechID': i.TechID,
                    'TechName': i.TechName
                })
            senddata = {'status': 'Success', 'data': datalist}
            print(senddata)
        except Exception:
            senddata = {'status': 'Fail'}
        return Response(senddata)

    @action(methods=['post'], detail=False)
    def get_control_autocomplete(self, request):
        print(request.data)
        try:
            tech_obj = ControlTypeMaster.objects.filter(TechID_id=request.data.get('TechID')).order_by('ControlName')
            datalist = []
            for i in tech_obj:
                datalist.append({
                    'ControlID': i.ControlID,
                    'ControlName': i.ControlName
                })
            senddata = {'status': 'Success', 'data': datalist}
            print(senddata)
        except Exception:
            senddata = {'status': 'Fail'}
        return Response(senddata)

    @action(methods=['post'], detail=False)
    def get_question_byid(self, request):
        print(request.data)
        try:
            prob_obj = ProblemMaster.objects.prefetch_related().get(ProblemID=request.data.get('ProblemID'))
            datalist = []
            datalist.append({
                'TechName': prob_obj.TechID.TechName, 'ControlName': prob_obj.ControlID.ControlName,
                'CreatedDate': prob_obj.CreatedDate, 'ProblemTitle': prob_obj.ProblemTitle,
                'ProblemDesc': prob_obj.ProblemDesc, 'ProblemID': prob_obj.ProblemID,
                'UserName': prob_obj.UserID.FirstName + ' ' + prob_obj.UserID.LastName,
                'UserID_QA': prob_obj.UserID_id
            })
            senddata = {'status': 'Success', 'data': datalist}
            print(senddata)
        except Exception as e:
            print(str(e))
            senddata = {'status': 'Fail'}
        return Response(senddata)


class Answer(ModelViewSet):
    queryset = UserMaster.objects.all()
    serializer_class = UserMasterSerializer

    @action(methods=['post'], detail=False)
    def vrify_answer(self, request):
        print(request.data)
        try:
            sol_objs = SolutionMaster.objects.filter(ProblemID_id=request.data.get('ProblemID'), IsVerified=True)
            print(sol_objs)
            if sol_objs:
                for x in sol_objs:
                    x.IsVerified = False
                    x.save()

            sol_obj = SolutionMaster.objects.get(SolutionID=request.data.get('SolutionID'))
            sol_obj.IsVerified = True
            sol_obj.save()
            senddata = {'status': 'Success'}
            print(senddata)
        except Exception as e:
            print(str(e))
            senddata = {'status': 'Fail'}
        return Response(senddata)

    @action(methods=['post'], detail=False)
    def previous_answers(self, request):
        print(request.data)
        try:
            sol_obj = SolutionMaster.objects.prefetch_related().filter(ProblemID_id=request.data.get('ProblemID'))
            datalist = []
            for i in sol_obj:
                datalist.append({
                    'IsVerified': i.IsVerified, 'CreatedDate': i.CreatedDate, 'SolutionDesc': i.SolutionDesc,
                    'SolutionID': i.SolutionID,
                    'UserName': i.UserID.FirstName + ' ' + i.UserID.LastName
                })
            senddata = {'status': 'Success', 'data': datalist}
            print(senddata)
        except Exception as e:
            print(str(e))
            senddata = {'status': 'Fail'}
        return Response(senddata)

    @action(methods=['post'], detail=False)
    def ins_answer(self, request):
        print(request.data, 'called')
        try:
            sol_obj = SolutionMaster.objects.create(
                ProblemID_id=request.data.get('ProblemID'),
                UserID_id=request.data.get('USERID'),
                SolutionDesc=request.data.get('SolutionDesc')
            )
            senddata = {'status': 'Success'}
        except Exception as e:
            print(str(e))
            senddata = {'status': 'Fail'}
        print('send data -> ', senddata)
        return Response(senddata)
