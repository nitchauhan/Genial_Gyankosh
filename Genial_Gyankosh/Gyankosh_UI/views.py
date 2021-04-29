from django.http import JsonResponse
from django.shortcuts import render, redirect
from Gyankosh_API.views import *


# Create your views here.
def login(request):
    print('----***--', request.POST)
    # print('login called',request.session['userid'])
    if 'userid' in request.session:
        response = redirect('dashboard', permanent=True)
        return response

    if request.method == "POST":
        request.data = {'username': request.POST.get('EmailID'), 'password': request.POST.get('Password')}
        print(request.data)
        r = Login()
        res = r.login(request)
        print(res)
        if res.data.get('status') == 'Success':
            request.session['userid'] = res.data.get('data').get('userid')
            request.session['fullname'] = res.data.get('data').get('fullname')
            response = redirect('dashboard', permanent=True)
            return response
        else:
            return render(request, 'login.html', {'flag': '1'})


    else:
        return render(request, 'login.html', {'flag': '0'})


def dashboard(request):
    print(request)
    print(request.POST)
    if 'fullname' not in request.session and 'userid' not in request.session:
        response = redirect('login', permanent=True)
        return response

    print('----------))))))')
    ip = "1.22.229.67"
    r = Dashboard()
    request.data = []
    res = r.get_dashboard_count(request)
    res1 = r.get_dashboard_quelist(request)
    print('-----------',res1)
    print('-----------',res)
    if res.data.get('status') == 'Success' and res1.data.get('status') == 'Success':
        return render(request, 'dashboard.html',
                      {'total_count': res.data.get('data').get('total_que'), 'solved_count': res.data.get('data').get('solved'),
                       'name': request.session['fullname'], 'questions': res1.data.get('data')})
    else:
        return render(request, 'login.html', {'flag': '1'})


def verifyans(request, solution_id, problem_id):
    print(request)
    print(request.POST)
    print('----------')
    ip = "1.22.229.67"
    request.data = {'ProblemID': problem_id, 'SolutionID': solution_id}
    r = Answer()
    res = r.vrify_answer(request)
    if res.data.get('status') == 'Success':
        response = redirect('question', permanent=True, problem_id=problem_id)
        print('gggg')
        return response
    else:
        return render(request, 'login.html', {'flag': '1'})


def logout(request):
    print(request)
    print(request.POST)
    print('----------')
    del request.session['userid']
    del request.session['fullname']
    response = redirect('login', permanent=True)
    return response


def questions(request):
    print(request)
    print(request.POST)
    print('----------')
    ip = "1.22.229.67"
    request.data = []
    r = Dashboard()
    r1 = Question()
    res = r.get_dashboard_quelist(request)
    res1 = r1.get_basic_autocomplete(request)
    if res.data.get('status') == 'Success' and res1.data.get('status') == 'Success':
        return render(request, 'questions.html',
                      {'name': request.session['fullname'], 'questions': res.data.get('data'), 'techlist': res1.data.get('data')})
    else:
        return render(request, 'login.html', {'flag': '1'})


def question(request):
    print(request, 'question')
    if request.method == "POST":
        request.data = {
            'TechID': request.POST.get('TechID') if request.POST.get('TechID') != 'undefined' else 0,
            'ControlID': request.POST.get('ControlID') if request.POST.get('ControlID') != 'undefined' else 0,
            'USERID': request.session['userid'], 'ProblemTitle': request.POST.get('ProblemTitle'),
            'ProblemDesc': request.POST.get('ProblemDesc'), 'TechName': request.POST.get('Tech'),
            'ControlName': request.POST.get('Control')
        }
        r = Question()
        res = r.ins_question(request)
        print(res)
        if res.data.get('status') == 'Success':
            response = redirect('dashboard', permanent=True)
        else:
            response = redirect('login', permanent=True)
        return response

    else:
        request.data = []
        r = Question()
        res = r.get_basic_autocomplete(request)
        if res.data.get('status') == 'Success':
            return render(request, 'question.html',
                          {'techlist': res.data.get('data')})
        else:
            return render(request, 'login.html', {'flag': '1'})


def answerbyid(request, problem_id):
    print('---------***', problem_id)

    if request.method == "POST":
        print('gj18')
        request.data = {'ProblemID': request.POST.get('ProblemID'), 'USERID': request.session['userid'],
                        'SolutionDesc': request.POST.get('SolutionDesc')}
        r = Answer()
        print('going')
        res = r.ins_answer(request)
        print('back')
        if res.data.get('status') == "Success":
            # response = redirect('answer', permanent=True, problem_id=request.POST.get('ProblemID'))
            # print('gggg')
            return redirect('dashboard', permanent=True)
        else:
            return render(request, 'login.html', {'flag': '1'})
    elif request.method == "GET":
        request.data = {'ProblemID': problem_id}
        r = Question()
        r1 = Answer()
        res = r.get_question_byid(request)
        res1 = r1.previous_answers(request)
        if res.data.get('status') == 'Success' and res1.data.get('status') == 'Success':
            print(res.data.get('data'))
            return render(request, 'answer.html',
                          {'quedtl': res.data.get('data')[0], 'anslist': res1.data.get('data')})
        else:
            return render(request, 'login.html', {'flag': '1'})


def ins_answer(request):
    print('00000')
    print('________', request.POST)
    print('s9559')
    if request.method == "POST":
        print('gj18')
        request.data = {'ProblemID': request.POST.get('ProblemID'), 'USERID': request.session['userid'],
                        'SolutionDesc': request.POST.get('SolutionDesc')}
        r = Answer()
        print('going')
        res = r.ins_answer(request)
        print('back')
        if res.data.get('status') == "Success":
            response = redirect('question', permanent=True, problem_id=request.POST.get('ProblemID'))
            print('gggg')
            return response
        else:
            return render(request, 'login.html', {'flag': '1'})


def load_control(request):
    techid = request.POST.get('TechID')
    request.data = {'TechID': techid}
    r = Question()
    res = r.get_control_autocomplete(request)
    if res.data.get('status') == 'Success':
        return JsonResponse({'controllist': res.data.get('data')})
    else:
        return render(request, 'login.html', {'flag': '1'})


def load_que(request):
    tag = request.POST.get('tag')
    request.data = {'tag': tag}
    r = Question()
    res = r.get_que_search_result(request)
    if res.data.get('status') == 'Success':
        return JsonResponse({'quelist': res.data.get('data')})
    else:
        return render(request, 'login.html', {'flag': '1'})
