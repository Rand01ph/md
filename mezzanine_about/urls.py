# encoding: utf-8

from django.conf.urls import patterns, url

urlpatterns = patterns("mezzanine_about.views",
        url("^$", "about_detail", name="about_detail"),
        url("^test/$", "test", name="test"),
)
