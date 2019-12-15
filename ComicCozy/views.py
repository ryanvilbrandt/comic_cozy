from django.db.models import QuerySet
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from ComicCozy.models import Comic


class ComicView(generic.DetailView):
    model = Comic
    template_name = 'ComicCozy/index.html'
    queryset = Comic.objects.filter(post_date__lte=timezone.now())

    def get_object(self, queryset=None):
        if len(self.queryset) == 0:
            raise Http404("No comics found.")
        latest_comic = self.queryset.latest()
        print(latest_comic)
        if 'pk' not in self.kwargs and 'slug' not in self.kwargs:
            comic = latest_comic
        else:
            comic = super().get_object(queryset)
        comic.earliest_id = self.queryset.earliest().id
        comic.latest_id = latest_comic.id
        try:
            comic.previous_id = self.queryset.filter(post_date__lt=comic.post_date).latest().id
        except self.model.DoesNotExist:
            comic.previous_id = comic.earliest_id
        try:
            comic.next_id = self.queryset.filter(post_date__gt=comic.post_date).earliest().id
        except self.model.DoesNotExist:
            comic.next_id = comic.latest_id
        return comic

#
#
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'ComicCozy/detail.html'
#
#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'ComicCozy/results.html'
#
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'ComicCozy/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('ComicCozy:results', args=(question.id,)))
