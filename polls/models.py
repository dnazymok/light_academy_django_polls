from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Test(models.Model):
    test_text = models.CharField(max_length=200)
    test_description = models.CharField(max_length=600)
    questions = models.ManyToManyField(Question)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.test_text


class Testrun(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    finished_at = models.DateTimeField(auto_now_add=True)


class TestrunQuestion(models.Model):
    testrun = models.ForeignKey(Testrun, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)

