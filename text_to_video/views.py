from django.shortcuts import render



def main_view(request):
    var = ""
    return render(request=request, template_name='base.html')
# Create your views here.
