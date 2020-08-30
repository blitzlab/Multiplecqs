from django.urls import path
from django.views.generic import TemplateView
from .views import QuestionsList, proccess_result

app_name = 'questions'
urlpatterns = [
    path('', TemplateView.as_view(template_name="questions/welcome.html")),
    path('instructions', TemplateView.as_view(template_name="questions/instructions.html"), name = "instructions"),
    path('challenge', QuestionsList.as_view(), name = "question_list"),
    path('result', proccess_result, name = "proccess_result"),
    path('thankyou', TemplateView.as_view(template_name="questions/thankyou.html"), name = "thankyou"),
]
