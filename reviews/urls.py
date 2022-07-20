from django.urls import path

from . import views

# name is used for reverse
urlpatterns = [
    # path("", views.index, name="index"),
    # path("thank-you", views.thank_you, name="thank-you"),
    path("", views.ReviewView.as_view(), name="review"),
    path("thank-you", views.ThankYouView.as_view(), name="thank-you"),
    path("reviews", views.ReviewsListView.as_view(), name="reviews"),
    path("reviews/favorite", views.AddFavoriteView.as_view(), name="favorites"),
    path("reviews/<int:pk>", views.SingleReviewView.as_view(), name="review-detail"),
]
