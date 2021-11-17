from django.shortcuts import render
from .models import Test_Information
from django.db.models import Q
from django.http import JsonResponse
import time

def getinfo(request):
    text= request.GET.get('button_text', default=".")
    query = request.GET.get('search_res', default=".")
    request.session['textinfo']= text
   

    if request.method == 'GET':

        results = Test_Information.objects.filter(Q(test_name__icontains=query) | Q(synonym__icontains=query))
       
        if results.count() <= 1:
        
            return render(request,'testinformation/getinfo.html',{'results': results})


        elif results.count() > 1:


            return render(request, 'testinformation/resultlist.html', {'results': results})
            

def getinfomultiple(request):
    
    time.sleep(1)
    multipletext= request.session['textinfo']
    results = Test_Information.objects.filter(test_name__icontains=multipletext)
    return render(request, 'testinformation/multipleinfo.html', {'results': results})