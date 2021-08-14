from blog.models import Post, PostView
from blog.views.utils import get_client_ip

from django.views.generic import DetailView
from django.shortcuts import redirect
from django.http import HttpRequest


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    queryset = Post.avaliable_objects


    def get(self, request: HttpRequest, *args, **kwargs):           
        response = super().get(request, *args, **kwargs)
        self.increase_views(request)
        return response
        
    def increase_views(self, request):
        ip = get_client_ip(request)
        if ip:
            PostView.objects.get_or_create(
                ip=ip,
                post=self.object,
            )


def random_post(request):
    object = Post.avaliable_objects.order_by('?').first()
    return redirect(object)
