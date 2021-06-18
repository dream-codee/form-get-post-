from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def form1(request):
    if request.method == "POST":
        # return HttpResponse(request.POST['First Name'])
        print(request.POST.get("First Name"))
    return render(request, "form1.html")
