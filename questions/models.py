from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Model for story

class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("Story Tittle", max_length = 200, unique=True, null = True, blank = True)
    text = RichTextField(null = True, blank = True)
    slug = models.SlugField(max_length=100, null = True, blank = True)
    pub_date = models.DateTimeField('Date Published', auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(Story, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Stories"

# Model for questions

class Question(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, null = True)
    question_text = models.CharField("Question Text", max_length=200, unique=True, null = True, blank = True)
    pub_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.question_text

# Model for question's options
class Option(models.Model):
    question = models.ForeignKey(Question, related_name="options", on_delete=models.CASCADE)
    option_text = models.CharField("Option Text", max_length=200, null = True, blank = True)
    answer = models.BooleanField(default=False)
    position = models.PositiveIntegerField(null = True, blank = True)

    def __str__(self):
        return self.option_text

    unique_together = [
            # no duplicated choice per question
            ("question", "answer"),
            # no duplicated position per question
            ("question", "position")
        ]
        # ordering = ("position",)
