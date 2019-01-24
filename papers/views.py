from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponseBadRequest

from .models import Paper


# Create your views here.
def index(request):
    return render(request, 'index.html')


class PaperListView(generic.ListView):
    model = Paper

    ordering = ['subject', 'year']


def select_paper(request, pk):
    paper = get_object_or_404(Paper, pk=pk)

    if paper.available and request.user.is_authenticated:
        paper.presenter_id = request.user.id
        paper.available = False
        paper.save()
        return HttpResponseRedirect(reverse('papers'))
    else:
        return HttpResponseBadRequest('You are not allowed to choose this.')