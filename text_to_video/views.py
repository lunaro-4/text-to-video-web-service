import os
from mimetypes import MimeTypes
from urllib.request import pathname2url
from django.http import HttpResponse
from django.shortcuts import render
from text_to_video.logic import main, SIZE, LENGH_IN_SECONDS, FPS
from text_to_video.SQL import sql_main
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt





@csrf_exempt
def get_handler(request):
    text = ""
    context = {}
    try:
        text = request.GET['text']
    except Exception:
        return render(request=request, template_name='video_form.html', context=context)
    return return_video(text)

@csrf_exempt
def post_handler(request): 
    data = request.POST
    print(data)
    text, size_x, size_y, fps, length = data['text'], data['size_x'], data['size_y'], data['fps'], data['length']
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
    if length == '':
        length = None
    else:
        length = int(length)
    return return_video(text,size, fps, length)


@csrf_exempt
def sql_insert(text, size, fps, length ):
    if size == None:
        size = SIZE
    if fps == None:
        fps = FPS
    if length == None:
        length = LENGH_IN_SECONDS
    sql_main((datetime.today(), text, size[0], size[1], fps, length))

    

@csrf_exempt
def return_video(text, size = None, fps = None, length = None ):
    file_name = "outp.mp4"
    mime = MimeTypes()
    url = pathname2url(file_name)
    mimetype = mime.guess_type(url)[0]
    main(text, file_name, size, fps, length).release()
    file = open(file_name,'rb')
    response = HttpResponse(file.read(), content_type=mimetype)
    response['Content-Length'] = os.path.getsize(file_name)
    response['Content-Disposition'] = \
        "attachment; filename=\"%s\"; filename*=utf-8''%s" % \
        (file_name, file_name)
    sql_insert(text, size, fps, length)
    return response


@csrf_exempt
def main_view(request):
    if request.method == 'GET':
        return get_handler(request)
    else:
        return post_handler(request)
        


@csrf_exempt
def show_home(request):
    return render(request=request, template_name='home.html')
