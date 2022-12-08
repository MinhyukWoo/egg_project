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
    # TODO: class 번호(정수)에 대응하는 감정 키워드 정의하기
    classToEmotionWord = {
        0: {"명사": "슬픔", "ㄹ": "슬플", "과거형어간": "슬펐"},
        1: {"명사": "기쁨", "ㄹ": "기쁠", "과거형어간": "기뻤"},
    }

    import random

    resultClass = random.randint(0, len(classToEmotionWord) - 1)  # test를 위해 무작위 값 설정
    emotionWord = classToEmotionWord[resultClass]
    resultEmotion = emotionWord["과거형어간"]
    # TODO: 웹 크롤링 코드 구현하기
    # TODO: 윀 크롤링 할 때 검색할 키워드 정하기
    searchKeyword = emotionWord["ㄹ"] + " 때 보는 영상"
    return render(
        request,
        "diary/feedback.html",
        {"emotion": resultEmotion, "searchKeyword": searchKeyword},
    )
