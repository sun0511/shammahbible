from django.shortcuts import render

def post_list(request):
    return render(request, 'first/post_list.html')