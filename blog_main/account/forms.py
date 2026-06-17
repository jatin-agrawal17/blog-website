from django import forms
from django.contrib.auth.models import User
from blogs.models import Blog
from account.models import ProfileModel


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
        )


class ProfileForm(forms.ModelForm):

    class Meta:
        model = ProfileModel
        fields = (
            'profile_image',
            'bio',
            'linkedin',
        )


class UserBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'title',
            'category',
            'featured_image',
            'short_description',
            'blog_body',
            'status',
        )