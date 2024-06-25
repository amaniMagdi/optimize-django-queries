from django.shortcuts import render
from .models import Post, Auther
from django.db.models import Prefetch

# Create your views here.
"""
Django tip:

* Select_related vs prefetch_related

    Use select_related() on OneToOneField or ForeignKey when you need a single object
    Use prefetch_related() on ManyToManyFields or reverse relations when you need many objects

* select_related replaces multiple queries being performed by a single INNER JOIN at the database level
* prefecth_related replaces multiple queries being performed by only 2 SQL queries, then it will inner join the data using Python.

"""
def main_view(request):
    data = []
    ########select_related => get all authers of posts, ForeignKey
    # posts = Post.objects.select_related('auther').all()
    # data = [post.auther.name for post in posts]
    ########prefetch_related => get authers of a post (post by post), ManyToMany
    # posts = Post.objects.prefetch_related('authers').all()
    # for post in posts:
    #     authers = post.authers.all()
    #     for auther in authers:
    #         data.append(auther.name)
    #######use Prefetch class with prefetch_related to get posts of all authers, reverse ForeignKey
    authers = Auther.objects.all().prefetch_related(
        Prefetch('post_set', queryset=Post.objects.all())
    )
    for auther in authers:
        posts = auther.post_set.all()
        for post in posts:
            data.append(post.title)
    return render(request, "main.html", {"data":data})