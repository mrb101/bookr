from django.shortcuts import render


class TopicList(ListView):
    model = Topic
    tempalte_name = 'topics/list.html'
    context_object_name = 'topics'


class TopicDetail(DetailView):
    model = Topic
    template_name = 'topics/detail.html'
    context_object_name= 'topic'


class TopicCrate(CreateView):
    pass


class TopicUpdate(UpdateView):
    pass


