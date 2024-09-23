from django.shortcuts import render,HttpResponse

# Create your views here.
def movie_list(request):
    return HttpResponse("电影列表")


def movie_detail(request,movie_id):
    return HttpResponse(f"你的电影id:{movie_id}")