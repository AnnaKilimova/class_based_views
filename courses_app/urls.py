from django.urls import path
from .views import (
    CourseListView,
    CourseDetailView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
)

# The app_name defines a namespace for URL names.
# It allows us to use namespaced references in templates {% url 'courses:list' %}.
app_name = 'courses'

'''
Path parameters:
    - <int:pk> is used for views that operate on a single object.
      Django's DetailView, UpdateView, and DeleteView expect either:
        * 'pk' (primary key)
        * or 'slug' (if slug_field and slug_url_kwarg are defined)
      Using 'pk' in the URL pattern ensures compatibility with Django's
      default expectations for object lookups.

Important:
    The name of the path parameter (here, 'pk') must match what the view expects.
    If you change the parameter name in the URL (for example, to 'course_id'),
    you must also change the expected keyword in the view. Otherwise, Django
    will raise a “No course found matching the query” or similar error because
    it cannot match the parameter.
'''
urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('create/', CourseCreateView.as_view(), name='create'),
    path('<int:pk>/', CourseDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', CourseUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CourseDeleteView.as_view(), name='delete'),
]