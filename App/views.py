from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import*
from django.contrib import messages 


# Create your views here.
def index(request):
    question = Poll.objects.all()
    context = {
        'question':question
    }
    return render(request,'home.html',context)
def createquestion(request):
    if request.method=='POST':
        question = request.POST.get('question')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        create_question = Poll.objects.create(question=question,option_A=option1,option_B=option2,option_C=option3)
        messages.success(request, 'Question is Submitted')

           
    return render(request,'question.html')

def vote(request,poll_id):
    poll = Poll.objects.get(id=poll_id)
    if request.method=='POST':
        select = request.POST.get('poll')
       
        if select =='option1':
            poll.option_A_count += 1
        
        elif select =='option2':
            poll.option_B_count +=1
           
        elif select =='option3':
            poll.option_C_count +=1
            
        else:
            return HttpResponse(400,'Invalid Form')
        
        poll.save()
        url=f'/result/{poll_id}'
        return redirect(url)

    context = {
        'poll':poll
    }
    return render(request,'vote.html',context)


def result(request,poll_id):
    poll = Poll.objects.get(id=poll_id)
    context = {
        'poll':poll
    }
    return render(request,'result.html',context)

