from django.shortcuts import render, HttpResponse
from main.models import Contact, Blogs
from django.contrib import messages

# Create your views here.

def homepage(request):
    blogs_list = Blogs.objects.all()[:5]
    
        
    context = {
		"BlogList" : blogs_list,
	}
	# return HttpResponse("This is Homepage")
    return render(request, 'index.html', context)

def about(request):
	# return HttpResponse("This is about page")
    return render(request, 'about.html')

def blogs(request):
	blogs_list = Blogs.objects.all()
	context = {
		"BlogList" : blogs_list,
	}
	# return HttpResponse("This is blogs page")
	return render(request, 'blogs.html', context)

def contact(request):
	if request.method == "POST":
		FirstName = request.POST.get('FirstName')
		LastName = request.POST.get('LastName')
		Email = request.POST.get('Email')
		Message = request.POST.get('Message')
		contact = Contact(FirstName=FirstName, LastName=LastName ,Email=Email , Message=Message)
		contact.save()	
		messages.success(request, 'Your message has been sent succsessfully')
	return render(request, 'contact.html')