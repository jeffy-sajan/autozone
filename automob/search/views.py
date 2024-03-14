from django.shortcuts import render
from django.db.models import Q
from shop.models import Part



def search(request):
    q=""
    product = None
    if(request.method=="POST"):
        q = request.POST['q']
        if q:
            product = Part.objects.filter(Q(name__icontains=q)|Q(desc__icontains=q))
    return render(request,'search.html',{'p':product ,'query':q})