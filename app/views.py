from django.shortcuts import render
from django.views.decorators.csrf import *
from app.models import *
from django.http import *
# Create your views here.
def index(request):
	return render(request,'index.html',{})
@csrf_exempt
def savedata(request):
	if request.method=='POST':
		name=request.POST.get('name')
		address=request.POST.get('address')
		phone=request.POST.get('phone')
		identity=request.POST.get('identity')
		reason=request.POST.get('reason')
		obj=Data(
			Name=name,
			Address=address,
			Phone=phone,
			Identity=identity,
			Reason=reason
			)
		obj.save()
		return HttpResponse("<script>alert('Data Saved!'); window.location.replace('/index/')</script>")
	else:
		return Http404