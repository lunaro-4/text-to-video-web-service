import os
from mimetypes import MimeTypes
from urllib.request import pathname2url
from django.http import HttpResponse
from django.shortcuts import render
from text_to_video.logic import main

def get_handler(request):
    text = ""
    context = {}
    try:
        text = request.GET['text']
    except Exception:
        return render(request=request, template_name='video_form.html', context=context)
    return return_video(text)

def post_handler(request): 
    data = request.POST
    print(data)
    text, size_x, size_y, fps = data['text'], data['size_x'], data['size_y'], data['fps']
    size = (size_x, size_y)
    if text =='':
        get_handler(request)
    else:
        text = str(text)
    if size_x == '' or size_y == '':
        size = None
    else:
        try:
            size_x = int(size_x)
            size_y = int(size_y)
            size = (size_x, size_y)
        except Exception:
            return get_handler(request)
    if fps == '':
        fps =None
    else:
        try:
            fps = int(fps)
        except Exception:
            return get_handler(request)
    return return_video(text,size, fps)

def return_video(text, size = None, fps = None ):
    file_name = "outp.mp4"
    mime = MimeTypes()
    url = pathname2url(file_name)
    mimetype = mime.guess_type(url)[0]
    main(text, file_name, size, fps).release()
    file = open(file_name,'rb')
    response = HttpResponse(file.read(), content_type=mimetype)
    response['Content-Length'] = os.path.getsize(file_name)
    response['Content-Disposition'] = \
        "attachment; filename=\"%s\"; filename*=utf-8''%s" % \
        (file_name, file_name)
    return response

def main_view(request):
    if request.method == 'GET':
        return get_handler(request)
    else:
        return post_handler(request)
        


def show_home(request):
    return render(request=request, template_name='home.html')
