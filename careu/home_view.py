'''module for render template'''
from django.shortcuts import render
from .home_model import BadMentalHealth, Symptoms, CareUTeam

def home(request):
    '''to render home view with all object correspond'''
    data1 = BadMentalHealth("Bipolar Disorder","Mental Disorder that causes unusual shifts in mood",'careu/bipolar.png',Symptoms.bipolar_name1,Symptoms.bipolar_desc1) # pylint: disable=line-too-long
    data2 = BadMentalHealth("Stress","feeling of emotional or physical tension.",'careu/stress.png',Symptoms.stress_name1,Symptoms.stress_desc1) # pylint: disable=line-too-long
    data3 = BadMentalHealth("Anxiety","feeling of fear or apprehension about what's to come.",'careu/anxiety.png','Panic','feelings of danger, panic, or dread') # pylint: disable=line-too-long
    data4 = BadMentalHealth("dementia","deterioration in memory, thinking, behaviour and the ability to perform everyday activities.",'careu/dementia.png','Memory loss','Memory loss, which is usually noticed by a spouse or someone else') # pylint: disable=line-too-long
    data5 = BadMentalHealth("insomnia","have difficulty falling asleep, or staying asleep as long as desired.",'careu/insomnia.png','Tiredness','Daytime tiredness or sleepiness.') # pylint: disable=line-too-long
    data6 = BadMentalHealth("schizophrenia","extremely disordered thinking and behavior that impairs daily functioning.",'careu/schizophrenia.png','Hallucinations','These usually involve seeing or hearing things that don`t exist.') # pylint: disable=line-too-long
    data = [data1,data2,data3,data4,data5,data6]
    context = {
        'data': data,
        "username" : "Anonim" if not request.user.is_authenticated else request.user.username
    }
    return render(request, 'home2.html',context)

def team(request):
    '''team careu'''
    data1 = CareUTeam("M. Fauzi Ridwan", 1906351070, "https://www.linkedin.com/in/muhamad-fauzi-ridwan-199260172/", "careu/fauzi.png")
    data2 = CareUTeam("Kirene Naomi", 1906353473, "", "-")
    data3 = CareUTeam("Yusuf Fakhri", 1906351096, "https://www.linkedin.com/in/ysfakhrialdrian/", "-")
    data4 = CareUTeam("Jesika Avonia", 1906398686, "", "-")
    data = [data1,data2,data3,data4]
    context = {
        'data':data
    }
    return render(request, 'team.html', context)

def journal(request):
    '''journa'''
    return render(request, 'journal.html')

def chat(request):
    '''chat'''
    return render(request, 'chat.html')
