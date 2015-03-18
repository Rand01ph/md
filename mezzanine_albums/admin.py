from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from mezzanine_albums.models import AlbumsLibrary, AlbumsFile


class AlbumsFileInline(TabularDynamicInlineAdmin):
    model = AlbumsFile


class AlbumsLibraryAdmin(PageAdmin):
    inlines = (AlbumsFileInline,)


admin.site.register(AlbumsLibrary, AlbumsLibraryAdmin)

