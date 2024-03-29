import os
from mimetypes import MimeTypes
from urllib.request import pathname2url
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from text_to_video.logic import main

def main_view(request):
    file_name = "outp.mp4"
    mime = MimeTypes()
    url = pathname2url(file_name)
    mimetype, encoding = mime.guess_type(url)
    context = {}
    text = ""
    try:
        text = request.GET['text']
    except Exception:
        pass
    main(text, file_name).release()
    file = open(file_name,'rb')
    response = HttpResponse(file.read(), content_type=mimetype)
    response['Content-Length'] = os.path.getsize(file_name)
    response['Content-Disposition'] = \
        "attachment; filename=\"%s\"; filename*=utf-8''%s" % \
        (file_name, file_name)
    return response
    return FileResponse(file, as_attachment=True)
    return render(request=request, template_name='base.html', context=context)
