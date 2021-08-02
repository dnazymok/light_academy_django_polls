from django.db import models


class Test(models.Model):
    test_text = models.CharField(max_length=200)
    test_description = models.CharField(max_length=600)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.test_text


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Testrun(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    finished_at = models.DateTimeField(auto_now_add=True)

