from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.core.paginator import Paginator, EmptyPage
from django.http import  HttpResponse, HttpResponseNotFound, Http404
from models import Question, Answer


def paginate(request, qs):
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, 10)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return [paginator, page]


def new(request):
    qs = Question.objects.order_by('-added_at')
    paginator, page = paginate(request, qs)
    paginator.baseurl = '/?page='
    return render(request, 'qa/templates/question_list.html', {'page': page, 'paginator': paginator})


def popular(request):
    qs = Question.objects.order_by('-rating')
    paginator, page = paginate(request, qs)
    paginator.baseurl = '/popular/?page='
    return render(request, 'qa/templates/question_list.html', {'page': page, 'paginator': paginator})


def question(request, slug):
    qa = get_object_or_404(Question, slug=slug)
    answers = Answer.filter(question=qa)[:]
    return render(request, 'qa/templates/question.html', {'question': qa, 'answers': answers})


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def notfound(request, *args, **kwargs):
    return HttpResponseNotFound('Page not found')