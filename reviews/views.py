from django.http import HttpResponseRedirect
# from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.


# def index(request, slug):
#     return render(request, "")


# Class based view
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    # def get(self, request):
    #     form = ReviewForm()

    #     return render(request, "reviews/review.html", {
    #         "form": form,
    #     })

    # def post(self, request):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")

    #     return render(request, "reviews/review.html", {
    #         "form": form,
    #     })


# TemplateView when returning a Template for a GET request
class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "My Message Context"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    # object_list
    context_object_name = "reviews"  # default name is object_list

    def get_queryset(self):  # QuerySet
        base_query = super().get_queryset()
        data = base_query.filter(rating__gte=1)  # Filter Data
        return data


class SingleReviewView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get["favorite_review"]
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # review_id = kwargs.get("id")
    #     review_id = kwargs["id"]
    #     selected_review = Review.objects.get(pk=review_id)
    #     context["review"] = selected_review
    #     return context


# def thank_you(request):  # Function based view
#     return render(request, "reviews/thank_you.html")


# def review(request):  # Function based view
#     if request.method == "POST":
#         #     # entered_username = request.POST.get("username")
#         # existing_model = Review.objects.get(pk=review_id)
#         # form = ReviewForm(request.POST, instance = existing_model)
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             # review_data = Review(
#             #     user_name=form.cleaned_data['user_name'],
#             #     review_text=form.cleaned_data['review_text'],
#             #     rating=form.cleaned_data['rating'],
#             # )
#             # review_data.save()
#             form.save()

#         # Redirects to new url with GET request method
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form": form,
#     })


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST.get("review_id")
        # review_id = request.POST["review_id"]
        # fav_review = Review.objects.get(pk=review_id)
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
