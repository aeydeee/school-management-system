from django.urls import path

from class_group.views import ClassListView, ClassCreateView, ClassUpdateView, SectionUpdateView, SectionManageView

app_name = 'class'

urlpatterns = [
    path('', ClassListView.as_view(), name='class_list'),
    path('add/', ClassCreateView.as_view(), name='add_class'),
    path('edit/<int:pk>/', ClassUpdateView.as_view(), name='edit_class'),

    path('section/', SectionManageView.as_view(), name='section_list'),
    path('section/edit/<int:pk>/', SectionUpdateView.as_view(), name='edit_section'),
]
