from django.test import TestCase

from polls.models import Test, Question


class IndexViewTestCase(TestCase):
    def setUp(self):
        for i in range(10):
            Test.objects.create(test_text=i)

    def test_index(self):
        resp = self.client.get('/polls/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context["latest_tests_list"].count(), 10)


class DetailViewTestCase(TestCase):
    def setUp(self):
        Test.objects.create(test_text='some text')

    def test_poll_detail_is_exist(self):
        resp = self.client.get("/polls/1/")
        self.assertEqual(resp.status_code, 200)


class TestrunViewTestCase(TestCase):
    def setUp(self):
        test = Test.objects.create(test_text='some text')
        question = Question.objects.create(question_text='some q_text')
        test.questions.add(question)

    def test_get_testrun(self):
        resp = self.client.get("/polls/1/run")
        self.assertEqual(resp.status_code, 200)
