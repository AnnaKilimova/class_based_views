from django.test import TestCase
from django.urls import reverse
from courses_app.models import Course

"""
Unit tests for Course-related views.

These tests use Django's built-in TestCase class, which provides:
    - An isolated test database for each test run.
    - A test client (`self.client`) for simulating HTTP requests.
    - Convenient assertion methods for checking responses and database state.

Each test class below checks one group of views:
    1. Course list page
    2. Course detail page
    3. Course creation
    4. Course updating
    5. Course deletion
"""


# === 1. Course List View Tests ===
class CourseListViewTest(TestCase):
    """Tests for the CourseListView (list of all courses)."""

    def setUp(self):
        """Create two Course objects for testing."""
        Course.objects.create(title="Python Basics")
        Course.objects.create(title="Django Advanced")

    def test_course_list_view_status_code(self):
        """The list view should return HTTP 200 (OK)."""
        url = reverse('courses:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_course_list_view_uses_correct_template(self):
        """The list view should render the correct template file."""
        url = reverse('courses:list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'courses_app/course_list.html')

    def test_course_list_view_shows_courses(self):
        """The rendered page should display the created course titles."""
        url = reverse('courses:list')
        response = self.client.get(url)
        self.assertContains(response, "Python Basics")
        self.assertContains(response, "Django Advanced")


# === 2. Course Detail View Tests ===
class CourseDetailViewTest(TestCase):
    """Tests for the CourseDetailView (viewing a single course)."""

    def setUp(self):
        """Create one Course instance for testing."""
        self.course = Course.objects.create(title="Python Basics")

    def test_course_detail_view_status_code(self):
        """The detail view should return HTTP 200 for an existing course."""
        url = reverse('courses:detail', args=[self.course.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_course_detail_view_uses_correct_template(self):
        """The detail view should use the correct template file."""
        url = reverse('courses:detail', args=[self.course.pk])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'courses_app/course_detail.html')

    def test_course_detail_view_displays_title(self):
        """The page should contain the course title."""
        url = reverse('courses:detail', args=[self.course.pk])
        response = self.client.get(url)
        self.assertContains(response, "Python Basics")


# === 3. Course Creation Tests ===
class CourseCreateViewTest(TestCase):
    """Tests for the CourseCreateView (creating a new course)."""

    def test_create_course_view_creates_course(self):
        """Submitting valid data should create a new course and redirect."""
        url = reverse('courses:create')
        data = {
            'title': 'New Course',
            'description': 'Some description'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Course.objects.count(), 1)
        self.assertEqual(Course.objects.first().title, 'New Course')


# === 4. Course Update Tests ===
class CourseUpdateViewTest(TestCase):
    """Tests for the CourseUpdateView (editing an existing course)."""

    def setUp(self):
        """Create a Course instance to update."""
        self.course = Course.objects.create(title="Old Title")

    def test_update_course(self):
        """Submitting valid data should update the course title."""
        url = reverse('courses:update', args=[self.course.pk])
        data = {'title': 'Updated Title'}
        response = self.client.post(url, data)
        self.course.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.course.title, 'Updated Title')


# === 5. Course Deletion Tests ===
class CourseDeleteViewTest(TestCase):
    """Tests for the CourseDeleteView (deleting a course)."""

    def setUp(self):
        """Create a Course instance to delete."""
        self.course = Course.objects.create(title="Delete Me")

    def test_delete_course(self):
        """A POST request should delete the course and redirect."""
        url = reverse('courses:delete', args=[self.course.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Course.objects.count(), 0)
