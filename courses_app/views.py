from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Course
from .forms import CourseForm

# === Module-level description ===
"""
Views for the courses app based on Django's generic class-based views.

Each view class uses a built-in Django generic view (ListView, DetailView,
CreateView, UpdateView, DeleteView). Where possible, the default behavior of
the generic view is relied upon - these defaults are implemented by Django
itself (Django documentation for ListView, DetailView, CreateView, UpdateView,
and DeleteView). Class attributes such as `model`, `template_name`, `context_object_name`,
`form_class`, and `success_url` are set here to customize that built-in behavior.
"""

class CourseListView(ListView):
    """
    Display a list of Course objects.

    This view uses Django's built-in ListView which:
      - Retrieves a queryset of objects (by default `Model.objects.all()` when
        `model` is provided).
      - Passes the queryset to the template in the context.

    Attributes:
      - model: the model this view works with. By setting `model = Course`,
               ListView will use `Course.objects.all()` as the default queryset
               unless get_queryset() is overridden.
      - template_name: the template file that will be rendered.
      - context_object_name: the name under which the list will be available
                             in the template (avoids relying on the default
                             `object_list` name).
      - ordering: the default ordering applied to the queryset (here newest first).
    """
    model = Course
    template_name = 'courses_app/course_list.html'
    context_object_name = 'courses'
    ordering = ['-created_at']
    
class CourseDetailView(DetailView):
    """
    Display a single Course instance.

    This view uses Django's built-in DetailView which:
      - Retrieves a single object based on URL kwargs (by default it looks for `pk`
        or `slug` depending on the URL configuration).
      - Passes the object to the template context.

    Attributes:
      - model: the model this view works with. Given `model = Course`, DetailView
               will search `Course.objects.all()` for the requested object.
      - template_name: the template file that will be rendered.
      - context_object_name: the name under which the object will be available
                             in the template (instead of the default `object`).
    """
    model = Course
    template_name = 'courses_app/course_detail.html'
    context_object_name = 'course'
    
class CourseCreateView(CreateView):
    """
    Display a form to create a new Course and handle form submission.

    This view uses Django's built-in CreateView which:
      - Displays an empty form on GET requests.
      - Validates form input on POST requests and, if valid, creates a new model
        instance and redirects to `success_url`.

    Attributes:
      - model: the model this view will create instances of.
      - form_class: a Django Form or ModelForm used to render and validate the form.
                    Using `CourseForm` keeps validation and layout consistent.
      - template_name: the template used to render the form.
      - success_url: the URL to redirect to after a successful creation.
    """
    model = Course
    form_class = CourseForm
    template_name = 'courses_app/course_form.html'
    success_url = reverse_lazy('courses:list')
    
    
class CourseUpdateView(UpdateView):
    """
    Display a form to update an existing Course and handle form submission.

    This view uses Django's built-in UpdateView which:
      - Looks up the existing object (by `pk` or `slug` from the URL).
      - Displays a form initialized with that object's data on GET requests.
      - Validates and saves changes on POST requests, then redirects to `success_url`.

    Class attributes (what we set here):
      - model: the model this view will update instances of.
      - form_class: the form used for validation and rendering. Reusing CourseForm
                    keeps the same validation rules as the create form.
      - template_name: the template used to render the update form.
      - success_url: the URL to redirect to after a successful update.
    """
    model = Course
    form_class = CourseForm
    template_name = 'courses_app/course_form.html'
    success_url = reverse_lazy('courses:list')
    
class CourseDeleteView(DeleteView):
    """
    Confirm deletion of a Course and delete it on confirmation.

    This view uses Django's built-in DeleteView which:
      - Renders a confirmation page on GET requests.
      - Deletes the object on POST requests and redirects to `success_url`.

    Class attributes (what we set here):
      - model: the model this view will delete instances of.
      - template_name: the confirmation template to render.
      - success_url: the URL to redirect to after deletion.
    """
    model = Course
    template_name = 'courses_app/course_confirm_delete.html'
    success_url = reverse_lazy('courses:list')
    
    
    

