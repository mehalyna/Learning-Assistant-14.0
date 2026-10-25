"""Tests for the completed Study Resources Board starter functionality."""
from django.test import TestCase
from django.urls import reverse

from .models import StudyResource


class StudyResourceTests(TestCase):
    def setUp(self):
        self.resource = StudyResource.objects.create(
            title="Python guide",
            subject="Python",
            url="https://example.com/python",
            description="A useful introduction.",
        )

    def test_string_representation_is_the_title(self):
        self.assertEqual(str(self.resource), "Python guide")

    def test_resource_list_returns_http_200(self):
        response = self.client.get(reverse("resource_list"))
        self.assertEqual(response.status_code, 200)

    def test_empty_resource_list_displays_empty_state(self):
        StudyResource.objects.all().delete()
        response = self.client.get(reverse("resource_list"))
        self.assertContains(response, "No resources have been added yet.")

    def test_existing_resource_appears_on_list(self):
        response = self.client.get(reverse("resource_list"))
        self.assertContains(response, "Python guide")
        self.assertContains(response, "Python")

    def test_resource_detail_returns_http_200(self):
        response = self.client.get(
            reverse("resource_detail", args=[self.resource.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python guide")
        self.assertContains(response, "https://example.com/python")

    def test_missing_resource_detail_returns_http_404(self):
        response = self.client.get(reverse("resource_detail", args=[99999]))
        self.assertEqual(response.status_code, 404)

    def test_list_links_to_resource_detail(self):
        response = self.client.get(reverse("resource_list"))
        self.assertContains(
            response,
            reverse("resource_detail", args=[self.resource.pk]),
        )

    def test_base_navigation_is_available(self):
        response = self.client.get(reverse("resource_list"))
        self.assertContains(response, "Add a resource")
        self.assertContains(response, "Study Resources Board")

    def test_add_resource_page_is_a_safe_placeholder(self):
        response = self.client.get(reverse("add_resource"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "not available yet")

    def test_add_resource_post_does_not_create_a_resource_yet(self):
        response = self.client.post(
            reverse("add_resource"),
            {
                "title": "Another guide",
                "subject": "Python",
                "url": "https://example.com/another-guide",
                "description": "Not saved by the starter.",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(StudyResource.objects.count(), 1)

    def test_delete_confirmation_get_does_not_delete_resource(self):
        response = self.client.get(
            reverse("delete_resource", args=[self.resource.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.resource.title)
        self.assertContains(response, "csrfmiddlewaretoken")
        self.assertTrue(StudyResource.objects.filter(pk=self.resource.pk).exists())

    def test_delete_post_does_not_delete_resource_yet(self):
        response = self.client.post(
            reverse("delete_resource", args=[self.resource.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No resource has been deleted.")
        self.assertTrue(StudyResource.objects.filter(pk=self.resource.pk).exists())

    def test_missing_delete_resource_returns_http_404(self):
        response = self.client.get(reverse("delete_resource", args=[99999]))
        self.assertEqual(response.status_code, 404)
