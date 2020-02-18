from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ContactUs 

def form(request):
	rec = None
	if request.GET.get('method') == 'edit':
		rec = ContactUs.objects.filter(id = request.GET.get('id')).get()
	elif request.GET.get('method') == 'delete':
		rec = ContactUs.objects.filter(id = request.GET.get('id')).get()
		rec.delete()
		return HttpResponseRedirect('/bootstrap_form/form') 
		
	if request.method == 'POST':
		if request.GET.get('method') == 'edit':
			rec.name = request.POST.get('name')
			rec.email = request.POST.get('email')
			rec.address = request.POST.get('address')
			rec.save()

			return HttpResponseRedirect('/bootstrap_form/form') 
		else:
			contact = ContactUs(
				name = request.POST.get('name'),
				email = request.POST.get('email'),
				address = request.POST.get('address')
			) 
			contact.save()
	data = ContactUs.objects.all()	
	return render(request, 'bootstrap_form/index.html', {'data':data , 'rec': rec })

def form_delete(request):
	pass

def form_edit(request):
	pass