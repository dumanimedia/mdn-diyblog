from django.shortcuts import render, get_object_or_404, redirect
from .models import Blogger, Post, Comment
from .forms import CustomUserCreationForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator


def home_page(request):
    return render(request, "index.html", {})


def signup_page(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        render(request, "signup.html", {"form": form})
    return render(request, "signup.html", {"form": form})


def posts_page(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)

    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    return render(request, "posts.html", {"page": page})


def create_post_page(request):
    blogger = get_object_or_404(Blogger, user=request.user)
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]

            post = Post(blogger=blogger, title=title, description=description)
            post.save()
            return redirect(f"/blog/{post.pk}")
        return render(request, "create-post.html", {"form": form})
    return render(request, "create-post.html", {"form": form})


def post_details_page(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    already_commented = False
    if request.user.is_authenticated:
        try:
            Comment.objects.get(user=request.user, post=post)
            already_commented = True
        except Comment.DoesNotExist:
            already_commented = False

    context = {
        "post": post,
        "comments": comments,
        "already_commented": already_commented,
    }
    return render(request, "post-details.html", context)


@login_required
def post_comment_page(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    try:
        Comment.objects.get(user=request.user, post=post)
        return redirect(f"/blog/{post_id}")
    except Comment.DoesNotExist:
        pass

    if request.method == "POST":
        comment = Comment(comment=request.POST["comment"], user=request.user, post=post)
        comment.save()

        return redirect(f"/blog/{post_id}")
    return render(request, "post-comment.html", {"post": post})


def bloggers_page(request):
    bloggers = Blogger.objects.all()
    return render(request, "bloggers.html", {"bloggers": bloggers})


def blogger_details_page(request, blogger_id):
    blogger = get_object_or_404(Blogger, pk=blogger_id)
    posts = Post.objects.filter(blogger=blogger)
    return render(request, "blogger-details.html", {"blogger": blogger, "posts": posts})


@login_required
def become_blogger_page(request):
    if request.user.is_staff:
        return redirect("home_page")

    if request.method == "POST":
        user = get_object_or_404(User, username=request.user.username)
        user.is_staff = True
        user.save()

        blogger = Blogger(bio=request.POST["bio"], user=user)
        blogger.save()
        return redirect("/blog/bloggers/")
    return render(request, "become-blogger.html", {})
