from blog.models import Post
from django.views.generic import ListView


class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    queryset = Post.avaliable_objects.all()[:5]
