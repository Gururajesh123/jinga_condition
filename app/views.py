from django.shortcuts import render

# Create your views here.
def jinga(request):

    return render(request,'jinga.html',context={'name':'rajesh'})

def condition(request):
    d={'a':1000,'b':157,'c':3456}
    return render(request,'condition.html',context=d)