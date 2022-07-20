from django import forms

from .models import Review

# class ReviewForm(forms.Form):  # Form Class
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty!",
#         "max_length": "Please enter a shorter name!",
#     })
#     review_text = forms.CharField(
#         label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):  # ModelForm Class
    class Meta:
        model = Review
        # fields = ['user_name', 'review_text', ]
        # OR
        # exclude = ["owner_comments"]
        # OR
        fields = '__all__'
        labels = {
            "user_name": "Your name",
            "review_text": "Your Feedback",
            "rating": "Your Rating",
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name!",
            }
        }
