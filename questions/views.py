from django.shortcuts import render
from .models import Question, Option
from django.views.generic import ListView

# Create your views here.
class QuestionsList(ListView):
    model = Question
    # paginate_by = 4
    context_object_name = 'questions'
    template_name = "questions/questions.html"

def proccess_result(request):
    if request.method == "POST" or None:
        answers = request.POST
        score = 0 # Initialize candidate'score.
        point = 1 * 5 # Each question will be graded on a 5 point score.
        total = 10 * 5 # Total questions * 5 to get total grade point
        pass_score = 75 # Average pass score 75%.

        questions = Question.objects.all()
        for question in questions:
            if str(question.id) in answers:
                for option in question.options.all():

                    if answers[str(question.id)] == str(option):
                        if option.answer is True:
                            score += point
        percent =(score/(score+(total-score)))*100
        passed = percent >= pass_score
    return render(request, "questions/result.html",
                    {"correct": score//5, "total":total//5,
                    "percentagescore":percent, "passed":passed}
                )
