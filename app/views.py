from django.shortcuts import render
from app.forms import ReviewForm
from django.views.generic.edit import FormView
from django.http.response import HttpResponse


class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg = 'Thanks for review!'
        return HttpResponse(msg)
