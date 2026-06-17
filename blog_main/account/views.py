from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm,UserBlogForm
from account.models import ProfileModel
from blogs.models import Blog
from django.template.defaultfilters import slugify


@login_required(login_url='login')
def profile_dashboard(request):

    profile, created = ProfileModel.objects.get_or_create(
        user=request.user
    )

    blogs = Blog.objects.filter(
        author=request.user
    ).order_by('-created_at')

    total_blogs = blogs.count()

    published_blogs = blogs.filter(
        status='Published'
    ).count()

    draft_blogs = blogs.filter(
        status='Draft'
    ).count()

    context = {
        'profile': profile,
        'blogs': blogs,
        'total_blogs': total_blogs,
        'published_blogs': published_blogs,
        'draft_blogs': draft_blogs,
    }

    return render(
        request,
        'account/profile.html',
        context
    )





@login_required(login_url='login')
def edit_profile(request):

    profile, created = ProfileModel.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        user_form = UserForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile_form.save()

            return redirect('profile_dashboard')

    else:

        user_form = UserForm(
            instance=request.user
        )

        profile_form = ProfileForm(
            instance=profile
        )

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(
        request,
        'account/edit_profile.html',
        context
    )


@login_required(login_url='login')
def add_blog(request):

    if request.method == 'POST':

        form = UserBlogForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            blog = form.save(commit=False)

            blog.author = request.user
            blog.is_featured = False

            blog.save()

            blog.slug = slugify(blog.title) + '-' + str(blog.id)
            blog.save()

            return redirect('profile_dashboard')

    else:

        form = UserBlogForm()

    context = {
        'form': form
    }

    return render(
        request,
        'account/add_blog.html',
        context
    )


@login_required(login_url='login')
def edit_blog(request, pk):

    blog = get_object_or_404(
        Blog,
        pk=pk,
        author=request.user
    )

    if request.method == 'POST':

        form = UserBlogForm(
            request.POST,
            request.FILES,
            instance=blog
        )

        if form.is_valid():

            blog = form.save()

            blog.slug = slugify(blog.title) + '-' + str(blog.id)
            blog.save()

            return redirect('profile_dashboard')

    else:

        form = UserBlogForm(
            instance=blog
        )

    context = {
        'blog': blog,
        'form': form
    }

    return render(
        request,
        'account/edit_blog.html',
        context
    )


@login_required(login_url='login')
def delete_blog(request, pk):

    blog = get_object_or_404(
        Blog,
        pk=pk,
        author=request.user
    )

    blog.delete()

    return redirect('profile_dashboard')