from django.core.paginator import Paginator
from ..models import Question
from django.shortcuts import render, get_object_or_404

def index(request):
    page = request.GET.get('page', '1')
    #return HttpResponse("안녕하세요. board의 index 페이지입니다.")
    question_list = Question.objects.order_by('-created_at')
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'board/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'board/question_detail.html', context)