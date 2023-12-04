from django.shortcuts import render

# Create your views here.
def badge(request):
    return render(request,'badge.html')
def breadcrumb(request):
    return render(request,'breadcrumb.html')
def buttons(request):
    return render(request,'buttons.html')
def button_groups(request):
    return render(request,'button_groups.html')
def collapse(request):
    return render(request,'collapse.html')
def droupdowns(request):
    return render(request,'droupdowns.html')
def forms(request):
    return render(request,'forms.html')
def input_groups(request):
    return render(request,'input_groups.html')
def jumbotron(request):
    return render(request,'jumbotron.html')
def list_group(request):
    return render(request,'list_group.html')
def media_object(request):
    return render(request,'media_object.html')