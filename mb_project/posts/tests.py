from django.test import TestCase
from posts.models import Post
from django.urls import reverse

# Create your tests here.


class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just a text')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_oject_name = f'{ post.text }'
        self.assertEqual(expected_oject_name, 'just a text')

class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text='this is another text')

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_renders_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        
                