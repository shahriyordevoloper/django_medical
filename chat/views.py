from django.shortcuts import render ,redirect
from .models import Sick,Hurujs,Xulosa
from django.http import HttpResponse,JsonResponse
import datetime
from django.core.exceptions import ObjectDoesNotExist
     

def faq(request):
    return render(request ,'mein/faq.html')
def detail(request,id):
    sick = Sick.objects.get(id=id)
    return render(request ,'mein/sick-detail.html',{'sick':sick})

def xulosa(request):

    if request.method == 'POST':
        try:
            person_id = request.POST.get('person_id')
            Xulosa.objects.create(
                person=Sick.objects.get(username=person_id),
                body=request.POST.get('body')
            )
          

            return redirect("xulosa")

        except ObjectDoesNotExist:
            return render(request ,'mein/xulosa.html', {'persons':Sick.objects.all()  ,'error':'Hatolik bor'}  )
            
        
    return render(request ,'mein/xulosa.html', {'persons':Sick.objects.all() }  )




def home(request):
    if request.user.is_active:
        all_bemor = Sick.objects.all().filter(user=request.user).order_by('-date_times')
        yoq = Sick.objects.filter(is_xuruj=True,user=request.user)

        datas=[]

        data_from =request.GET.get('date_from')
        data_to = request.GET.get('date_to')

        for i in all_bemor:
            h = {'count':i.persons.filter().count(), 
                'sick':i
                }
            datas.append(h)


        if data_from and data_to :
            datas=[]
            for i in all_bemor:
                h = {'count':i.persons.filter(date_times__gte=data_from+' 00:00',date_times__lt=data_to+' 23:59').count(), 
                    'sick':i
                    }
                
                if h['count'] > 0:

                    datas.append(h)
                else:
                    pass




        return render(request , 'mein/index.html', {'all_bemor':all_bemor,'yoq':yoq ,  'datas':datas})
    

    else:
        return redirect('accounts/login/')



def create_huruj(request,id):
    print(request)
    sick = Sick.objects.get(id=id)
    Hurujs.objects.create(
        person=sick
    )
    sick.is_xuruj = True
    sick.save()
    return redirect('/')

def create_huruj1(request,id):
    print(request)
    sick = Sick.objects.get(id=id)
    Hurujs.objects.create(
        person=sick
    )
    sick.is_xuruj = True
    sick.save()

    return redirect('/tables_all/')


def create_huruj2(request,id):
    print(request)
    sick = Sick.objects.get(id=id)
    Hurujs.objects.create(
        person=sick
    )
    sick.is_xuruj = True
    sick.save()
    return redirect('/comingtype/')




def user_create(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if  request.GET.get('username')  and  request.GET.get('dori') and  request.GET.get('dori_miqdor'):
            print(request.GET.get('tarif'))
            Sick.objects.create(
                username=request.GET.get('username'),
                dori_name=request.GET.get('dori'),
                dori_miqdor=request.GET.get('dori_miqdor'),
                is_xuruj=request.GET.get('tarif'),
                user=request.user,
                xulosa='',
            )

            return JsonResponse({'data':'data'},safe=False)

    return render(request , 'mein/register.html')

def comingtype(request):
    all_bemor = Sick.objects.all().filter(user=request.user).order_by('-date_times')
    yoq = Sick.objects.filter(user=request.user, is_xuruj=True)

    datas=[]

    data_from =request.GET.get('date_from')
    data_to = request.GET.get('date_to')


    for i in yoq:
        h = {'count':i.persons.filter().count(), 
            'sick':i
            }
        datas.append(h)


    if data_from and data_to :
        datas=[]
        for i in yoq:
            h = {'count':i.persons.filter(date_times__gte=data_from+' 00:00',date_times__lt=data_to+' 23:59').count(), 
                'sick':i
                }
            if h['count'] > 0:

                datas.append(h)
            else:
                pass

    return render(request , 'mein/comingtype.html',{'datas':datas })

def tables(request):
    all_bemor = Sick.objects.all().filter(user=request.user).order_by('-date_times')
    yoq = Sick.objects.filter(user=request.user)
    datas=[]




    data_from =request.GET.get('date_from')
    data_to = request.GET.get('date_to')


    for i in yoq:
        h = {'count':i.persons.filter().count(), 
            'sick':i
            }
        
        datas.append(h)


    if data_from and data_to :
        datas=[]
        for i in yoq:
            h = {'count':i.persons.filter(date_times__gte=data_from+' 00:00',date_times__lt=data_to+' 23:59').count(), 
                'sick':i
                }
            if h['count'] > 0:

                datas.append(h)
            else:
                pass


        # return render(request , 'mein/index.html', {'all_bemor':all_bemor,'yoq':yoq , 'huruj':hurujs   })
    
    return render(request , 'mein/tables-general.html',{'datas':    datas })



def delete(request,id):
    d = Sick.objects.get(id=id)
    d.delete()
    return redirect('/')
def delete1(request,id):
    d = Sick.objects.get(id=id)
    d.delete()
    return redirect('tables_all')

def delete2(request,id):
    d = Sick.objects.get(id=id)
    d.delete()
    return redirect('comingtype')

def update_sick(request,id):
    sick = Sick.objects.get(id=id)
    sick.username = request.GET.get('username')
    sick.dori_name = request.GET.get('dori')
    sick.dori_miqdor = request.GET.get('dori_miqdori')
    sick.is_xuruj = request.GET.get('talvasa')
    sick.date_times = datetime.datetime.now()

    
    sick.save()
    return redirect('/')

def update_sick1(request,id):
    sick = Sick.objects.get(id=id)
    sick.username = request.GET.get('username')
    sick.dori_name = request.GET.get('dori')
    sick.dori_miqdor = request.GET.get('dori_miqdori')
    sick.is_xuruj = request.GET.get('talvasa')
    sick.date_times = datetime.datetime.now()

    
    sick.save()
    return redirect('/tables_all/')

def update_sick2(request,id):
    sick = Sick.objects.get(id=id)
    sick.username = request.GET.get('username')
    sick.dori_name = request.GET.get('dori')
    sick.dori_miqdor = request.GET.get('dori_miqdori')
    sick.is_xuruj = request.GET.get('talvasa')
    sick.date_times = datetime.datetime.now()

    
    sick.save()
    return redirect('comingtype')



def handler_404(request,exception):
    
    return render(request, "404.html")