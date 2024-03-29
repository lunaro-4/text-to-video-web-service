from django.shortcuts import render
from text_to_video.logic import main

def main_view(request):
    context = {}
    text = ""
    try:
        text = request.GET['text']
    except Exception:
        pass
    main(text, "outpp.mp4")
    return render(request=request, template_name='base.html', context=context)
