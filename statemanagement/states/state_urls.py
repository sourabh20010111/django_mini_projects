from django.urls import path
from .views import StateListView, StateDetailView, StateCreateView, StateUpdateView, StateDeleteView

urlpatterns = [
    path('', StateListView.as_view(), name='state-list'),
    path('state/<int:pk>/', StateDetailView.as_view(), name='state-detail'),
    path('state/create/', StateCreateView.as_view(), name='state-create'),
    path('state/<int:pk>/update/', StateUpdateView.as_view(), name='state-update'),
    path('state/<int:pk>/delete/', StateDeleteView.as_view(), name='state-delete'),
]
