import django_filters
from .models import Project,Business1,Freelancer
class ProjectFilter(django_filters.FilterSet):
    stifund_range = django_filters.NumberFilter(field_name='stipend', lookup_expr='gte',label="Minimum Stipend")  # Assuming 'stifund' is a field in your Project model
    category = django_filters.CharFilter(field_name='category', lookup_expr='icontains')  # Assuming 'category' is a field in your Project model

    class Meta:
        model = Project
        fields = ['stifund_range', 'category']

class Business_search(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='company_name', lookup_expr='icontains')  # Assuming 'category' is a field in your Project model
    class Meta:
        model = Business1
        fields = ['company_name']
        
class Freelancer_search(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')  # Assuming 'category' is a field in your Project model
    class Meta:
        model = Freelancer
        fields = ['name']