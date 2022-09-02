import os
import sys

# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from django.shortcuts import render
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponse
from django.core import serializers
from board.models import Post
from .models import Prod, Prod_property, Prod_ratings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from . import check_recr

def getApi(request):
    property = Prod_property.objects.filter(prod_id__exact=97149727).order_by('option_id')
    property_list = serializers.serialize('json', property)
    return HttpResponse(property_list, content_type="text/json-comment-filtered; charset=utf-8")

def apiTest(request):
    return render(request, 'apiTest.html')

def index(request):
    # 현 시각 Year, month
    # now = timezone.now()
    # kst = now.strftime('%y.%m')

    # new_Prod_list = Prod.objects.order_by('-prod_id')[0:5]
    # print(new_Prod_list)
    # for prod_list in new_Prod_list:
    #     print(prod_list, "\n")
    #     print(prod_list.tags.all())
    new_Prod_list = Prod.objects.order_by('-prod_id')[0:5]
    for prod_list in new_Prod_list:
        print(prod_list)
        new_Prod_list_spec = prod_list.tags.values()
    # print(list(id_Prod.values()))

    context = {'Prod_list': new_Prod_list,
               'Prod_list_spec': new_Prod_list_spec,

               }
    return render(request, 'note_book_service/index.html', context)

def product(request, prod_id):
    Prod_list = Prod.objects.filter(prod_id__contains=prod_id)
    prod_id = Prod.objects.get(prod_id__contains=prod_id)
    ratings = Prod_ratings.objects.filter(prod_id=prod_id)
    # for prod_list in new_Prod_list:

    Prod_tags = prod_id.tags.values()

    Prod_list_spec = Prod_property.objects.filter(prod_id__in=Prod_list.values('prod_id'))

    context = {'Prod_list': Prod_list,
               'Prod_list_spec': Prod_list_spec,
               'Prod_tags': Prod_tags,
               'ratings': ratings
               }
    return render(request, 'note_book_service/product.html', context)

def expolre(request, prod_id):
    Prod_list = Prod.objects.filter(prod_id__contains=prod_id)
    Prod_list_spec = Prod_property.objects.filter(prod_id__in=Prod_list.values('prod_id'))

    context = {'Prod_list': Prod_list,
               'Prod_list_spec': Prod_list_spec,
               }
    return render(request, 'note_book_service/expolre.html', context)

def cmd(request):
    best_commend = 1
    best_commend_list = 2
    comd = {'best_commend' : best_commend,
            'best_commend_list' : best_commend_list,}
    return render(request, 'note_book_service/recommend.html', comd)

def recr(request):

    purpose = request.POST['용도']
    wight = request.POST['휴대성']
    price = request.POST['예산']
    as_ = request.POST['제조사']
    try:
        disp_media = request.POST['영상편집_화질']
    except:
        pass
    disp_color2 = request.POST['디스플레이_색감']
    disp_size = request.POST['디스플레이_크기']

    print(purpose)
    print(wight)
    print(price)
    print(as_)
    # print(disp_media)
    print(disp_color2)
    print(disp_size)

    recr_2 = check_recr.recr_123()
    id = recr_2.check_purpose(purpose)
    print(id.values('prod_id'))
    id = recr_2.check_price(id, price)
    print(id.values('prod_id'))
    # id = recr_2.check_weight(id, wight)
    id = recr_2.check_disp_size(id, disp_size)
    print(id.values('prod_id'))
    id = recr_2.check_disp_color(id, disp_color2)
    print(id.values('prod_id'))
    id = recr_2.check_as(id, as_)
    print(id.values('prod_id'))

    recr_Prod_list = Prod.objects.filter(prod_id__in=id).order_by('-prod_id')[0:10]
    recr_Prod_list_spec = Prod_property.objects.filter(prod_id__in=recr_Prod_list).order_by('option_id')



    context = {'Prod_list': recr_Prod_list,
               'Prod_list_spec': recr_Prod_list_spec,
               }
    return render(request, 'note_book_service/rec_result.html', context)
    # return render(request, 'note_book_service/rec_result.html')

def comm(request):
    posts = Post.objects.all().order_by('-id') #object : ORM에서 사용되는 manage 객체 => all은 모두 가져오는 것. get은 하나.
    context = {'posts':posts}
    return render(request, "note_book_service/community.html", context)
    #return render(request, 'note_book_service/community.html', commu)

def pstif(request):
    best_pstif = 1
    best_pstif_list = 2
    pstt = {'best_pstif' : best_pstif,
            'best_pstif_list' : best_pstif_list,}
    return render(request, 'note_book_service/postinfo.html', pstt)

def wrt(request):
    best_wrt = 1
    best_wrt_list = 2
    wrtt = {'best_wrt' : best_wrt,
            'best_wrt_list' : best_wrt_list,}
    return render(request, 'note_book_service/write.html', wrtt)