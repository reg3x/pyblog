from django.test import TestCase, Client, LiveServerTestCase
from blogengine import models
from . import factories
from django.core.urlresolvers import reverse


class BaseAcceptanceTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()


class BaseViewTest(BaseAcceptanceTest):

    def test_index(self):
        # Create the post
        post = factories.PostFactory()

        # Create the tag
        tag = factories.TagFactory()

        # Add the tag to the Category
        post.tags.add(tag)

        # Check the post has been saved
        all_posts = models.Post.objects.all()
        self.assertEquals(len(all_posts),1)

        # Check the tag has been saved
        all_tags = models.Tag.objects.all()
        self.assertEquals(len(all_tags),1)

        # Open the client
        # should use blogengine:home instead of /
        response = self.client.get(reverse('blogengine:home'))
        self.assertEquals(response.status_code, 200)

        # Check the post is shown at the response
        only_post = all_posts[0]
        only_tag = all_tags[0]
        self.assertContains(response, only_post.title)
        self.assertContains(response, only_post.text)
        self.assertContains(response, only_post.category)
        self.assertContains(response, only_tag.name)
        self.assertContains(response, only_post.pub_date.strftime('%b'))

    def test_post_page(self):
        pass
