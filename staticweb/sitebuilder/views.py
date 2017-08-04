import os

from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template import Template
from django.utils._os import safe_join

def get_page_or_404(name):
    """Return page content as a Django template or raise 404 error."""
    try:
        file_path = safe_join(settings.SITE_PAGES_DIRECTORY, name)
        print('**************************3', file_path)
    except ValueError:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path):
            print('**************************4', file_path)
            raise Http404('Page Not Found')

    with open(file_path, 'r') as f:
        print('**************************6', file_path)
        page = Template(f.read())
        print('**************************7', page)

    return page

def page(request, slug='index'):
    """Render the requested page if found."""
    file_name = '{}.html'.format(slug)
    print('**************************1', file_name)
    page = get_page_or_404(file_name)
    print('**************************2', page)
    context = {
        'slug': slug,
        'page': page,
    }
    return render(request, 'page.html', context)
