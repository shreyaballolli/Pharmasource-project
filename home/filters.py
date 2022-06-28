import django_filters
from .models import *

class donor1Filter(django_filters.FilterSet):
      class Meta:
          model=donor1
          fields = ["Tabletname"]