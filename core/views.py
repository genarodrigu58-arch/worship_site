from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Song, Announcement, Post
from .forms import ProfileForm

# -----------------------------
# Canciones
# -----------------------------
# views.py
@login_required
def song_list(request):
    q = request.GET.get('q', '')
    if q:
        songs = Song.objects.filter(title__icontains=q).order_by('title')
    else:
        songs = Song.objects.all().order_by('title')
    return render(request, 'core/songs.html', {'songs': songs})

# -----------------------------
# Anuncios
# -----------------------------
@login_required
def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    return render(request, 'core/announcements.html', {'announcements': announcements})

# -----------------------------
# Posts: ver y crear
# -----------------------------
@login_required
def posts(request):
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Post.objects.create(author=request.user, content=content)
            return redirect('posts')
    posts_list = Post.objects.all().order_by('-created_at')
    return render(request, 'core/posts.html', {'posts': posts_list})

# -----------------------------
# Editar post
# -----------------------------
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            post.content = content
            post.save()
            return redirect('posts')
    return render(request, 'core/edit_post.html', {'post': post})

# -----------------------------
# Borrar post
# -----------------------------
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    post.delete()
    return redirect('posts')

# -----------------------------
# Agregar comentario a un post
# -----------------------------
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            post.comments.create(author=request.user, content=content)
    return redirect('posts')

# -----------------------------
# Editar perfil
# -----------------------------
@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'core/edit_profile.html', {'form': form})

# -----------------------------
# Logout manual
# -----------------------------
def manual_logout(request):
    logout(request)
    return redirect('login')
