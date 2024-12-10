from django.shortcuts import render
import datetime
# Create your views here.
def conditions(request):
    '''d={'stuname':'Aravind','age':18,'marks':476}
    return render(request,'conditions.html',context=d)'''

    date=datetime.datetime.now()
    msg='hello server!!! Very Very Good'
    h=12
    dict={'date':date,'msg':msg,'h':h}
    return render(request,'conditions.html',dict)