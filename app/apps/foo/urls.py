# third-party imports
from django.urls import path

# local imports
from foo.views import FooView

urlpatterns = [path(r"foo", FooView.as_view())]
