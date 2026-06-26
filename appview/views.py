from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import Product,ProductVariant
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def home2(request):
    return render(request,"home2.html")

def product2(request):
    data={}
    pid = request.session.get('pid')

    data['product']=Product.objects.get(pid=pid)
    data['variants']=ProductVariant.objects.filter(pid=pid)

    data["heads"] = {}
    for row in data["variants"]:
        arr = row.combination.split("-") 
        for r in arr:
            head,value = r.split(":") 
            if(head in data["heads"]):
                data["heads"][head].append(value)
            else:
                data["heads"][head]=[]
                data["heads"][head].append(value)
        
    for row in data["heads"]:
        data["heads"][row] = set(data["heads"][row])
    print(data["heads"])
    return render(request,'product2.html',data)