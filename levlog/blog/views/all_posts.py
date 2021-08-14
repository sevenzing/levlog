from blog.models import Post
from django.views.generic import ListView


class AllPostsView(ListView):
    model = Post
    template_name = 'blog/all_posts.html'
    paginate_by = 3
    queryset = Post.avaliable_objects.order_by('-created_on').all()
