# encoding: utf-8

from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from .models import AlbumsLibrary, AlbumsFile

@processor_for("albums")
def albums_list(request, page):
    v = list({i.bianhao for i in AlbumsFile.objects.all()})
    cover = []
    for i in v:
        cover.append(AlbumsFile.objects.filter(bianhao=i)[0])
    detail = []
    for i in v:
        detail.append(list(AlbumsFile.objects.filter(bianhao=i)))
    return {"cover": cover, "detail": detail}

