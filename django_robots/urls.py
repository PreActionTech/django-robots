import django

from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(
        r'^$',
        TemplateView.as_view(
            template_name='robots/robots.txt',
            content_type='text/plain'
        ),
        name='robots'
    ),
]

if django.VERSION < (1, 9):
    from django.conf.urls import patterns

    urlpatterns = patterns(
        '',
        url(
            r'^$',
            TemplateView.as_view(
                template_name='robots/robots.txt',
                content_type='text/plain'
            ),
            name='robots'
        ),
    )
