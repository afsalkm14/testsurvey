from django.shortcuts import render
from myapp.forms import SurveyForm
# from survey.models import Survey
from .models import Survey
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .models import Survey

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def sur(request):
    if request.method == 'POST':
        nm = request.POST.get('nm')
        ag = request.POST.get('ag')
        gen = request.POST.get('gen')
        pre = request.POST.get('pre')
        mar = request.POST.get('mar')
        gridRadios = request.POST.get('gridRadios')
        gridRadioss = request.POST.get('gridRadioss')
        slide= request.POST.get('slide')

        name = nm
        age = ag
        gender = gen
        pregnancy = pre
        marital = mar
        diet = gridRadios
        ratefollow = gridRadioss
        rate = slide

        print(nm, ag, gen, pre, mar, gridRadios, gridRadioss,slide)
        ul = Survey.objects.filter(name=nm, age=ag, gender=gen, pregnancy=pre, marital=mar, diet=gridRadios, ratefollow=gridRadioss, rate=slide)
        ul = Survey(name=nm, age=ag, gender=gen, pregnancy=pre, marital=mar, diet=gridRadios, ratefollow=gridRadioss, rate=slide)
        ul.save()
        msg = 'Added succesfully'
        context = {'msg': msg}
        return render(request, 'home.html',context)
    else:
            return render(request, 'index.html')

def show(request):
    cm_l = Survey.objects.all()
    context={'user_list':cm_l}
    return render(request,'show.html',context)

def index(request):
    obj= Survey.objects.count()
    context ={'count':obj}
    male=Survey.objects.all().filter(gender='Male').count()
    female = Survey.objects.all().filter(gender='Female').count()
    married = Survey.objects.all().filter(marital='Married').count()
    veg = Survey.objects.all().filter(diet='Vegetarian').count()
    rice = Survey.objects.all().filter(ratefollow='Rice').count()
    wheat = Survey.objects.all().filter(ratefollow='Wheat').count()
    jower = Survey.objects.all().filter(ratefollow='Jower').count()
    context = {'count': obj,
               'count_male':male,
               'count_female':female,
               'count_married':married,
               'count_veg':veg,
               'count_rice':rice,
               'count_wheat':wheat,
               'count_jower':jower,}
    return render(request,"index.html",context)


def pie_chart(request):
    labels = []
    data = []

    queryset = Survey.objects.order_by('id')[:4]
    for city in queryset:
        labels.append(city.ratefollow)
        data.append(city.rate)

    return render(request, "pie_chart.html", {
        'labels': labels,
        'data': data,
    })



