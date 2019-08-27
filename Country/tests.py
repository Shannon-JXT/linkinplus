from django.test import TestCase


# Create your tests here.
class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)
        """

class viewTests(TestCase):
    def test_index_view_no_article(self):
        """
        If no Articles exist,
        'latest_article_list' should be empty

        response = self.client.get()
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_article_list'], [])
        """