from django.shortcuts import render
a = []
for i in range(1000):
	a.append(i)
b = ['if you want to contact me','AbdulAziz@gmaíl.com']

def index(request):
	return render(request,'personal/home.html')
def contacts(request):
	return render(request,'personal/contacts.html',{'contacts':b})

