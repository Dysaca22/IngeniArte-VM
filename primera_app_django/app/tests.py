import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse


from .models import Question

""" Test was_published_recently old """
def test_was_published_recently_with_old_question(self):
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)

""" Test was_published_recently new """
def test_was_published_recently_with_recent_question(self):
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)

""" Método crear question """
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

""" Test vista default """
class QuestionIndexViewTests(TestCase):
    """ Test mensaje No question y empty list"""
    def test_no_questions(self):
        response = self.client.get(reverse('app:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No app are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    """ Creación de pregunta y aparición en lista """
    def test_past_question(self):
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('app:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    """ Creación question futura """
    def test_future_question(self):
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('app:index'))
        self.assertContains(response, "No app are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    """ Creación question pasada y futura """
    def test_future_question_and_past_question(self):
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('app:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    """ Creación questions pasadas """
    def test_two_past_questions(self):
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('app:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )

""" Test vista Detail """
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('app:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('app:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)