from django.shortcuts import render
from links.models import CatalogName, LinkList


def index(request):
    links = LinkList.objects.order_by('priority')
    catalogs = CatalogName.objects.order_by('priority')
    context = {'catalogs': catalogs, 'links': links}
    return render(request, 'links/links.html', context=context)
