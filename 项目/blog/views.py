from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def blog(request,blog_id):
    return render(request, 'blog_detail.html')



def publish(request):
    return render(request, 'pub.html')



