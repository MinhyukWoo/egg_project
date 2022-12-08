from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def index(request: HttpRequest):
    """
    첫 페이지를 보여주는 view
    링크로 어느 페이지로 이동할지 결정할 수 있다.
    """
    return render(request, "diary/index.html", {"url": request.get_host()})


def chatting(request: HttpRequest):
    """
    Chatting 페이지를 보여주는 view
    먼지와 대화 나눌 수 있다.
    """
    # TODO: 사용자에게 건낼 질문 리스트 정해서 questions 초기값 변경하기
    questions = ["오늘 어떤 일이 있었어요?", "기분은 어땠어요?"]
    return render(
        request,
        "diary/chatting.html",
        {"questions": questions},
    )


def feedback(request: HttpRequest):
    """
    Feedback 페이지를 보여주는 view
    먼지와 나눈 대화를 바탕으로 AI가 판단한 피드백을 알려준다.
    """
    return render(request, "diary/feedback.html")
