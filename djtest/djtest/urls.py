from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView, TemplateView

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(
						template_name="index.html")),
# urlpatterns = patterns('',
# 	url(r'^$', TemplateView.as_view(
# 						template_name="index.html")),
# urlpatterns = patterns('',
# 	url(r'^$', TemplateView.as_view(
# 						template_name="index.html")),
# urlpatterns = patterns('',
# 	url(r'^$', TemplateView.as_view(
# 						template_name="index.html")),
# 	url(r'^static/(?P<path>.*)$'. 'django.views.static.serve', {"document_root": settings.STATIC_ROOT}),
					
)

						