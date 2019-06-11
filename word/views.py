from django.shortcuts import render

# Create your views here.

def home(request):
    # text = request.POST.get('mytext', '') 
    return render(request,'home.html')

def index(request):
    # text = request.POST.get('mytext', '') 
    return render(request,'index.html')

def result(request):
    text = request.GET["mytext"]
    sp_sen = text.split(' ')

    mydict={} 
    for i in sp_sen:
        if i in mydict:
            mydict[i] += 1
        else:
            mydict[i] = 1

    # context = {'txt':text}    
    context = {'res':mydict, 'myitem':mydict.items, 'total':len(mydict)} 
    return render(request,'result.html',context)