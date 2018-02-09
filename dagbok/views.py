from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View

from .models import Post
from .forms import PostForm
from organizer.models import Medlem

# Create your views here.
class Landing(View):
    template_name = 'dagbok/landing.html'
    medlemmer = Medlem.objects.all()
    def get(self, request):
        return render(
            request,
            self.template_name,
            {'medlemmer':self.medlemmer}
        )
class Dagbok(View):
    template_name = 'dagbok/dagbok.html'
    def get(self, request, slug):
        medlem = get_object_or_404(Medlem, slug=slug)
        posts = Post.objects.filter(slug=slug)
        return render( request, self.template_name, {'posts':posts, 'medlem':medlem} )

class PostMixin:
    def get_object(self, slug, year, month, day):
        return get_object_or_404(
            self.model,
            medlem__slug__iexact=slug,
            date__year=year,
            date__month=month,
            date__day=day
        )

class PostCreate(View, PostMixin):
    form_class = PostForm
    template_name = 'dagbok/create_post.html'

    def get(self, request, slug):
        return render(request, self.template_name, {'form':self.form_class(), 'slug':slug})
    def post(self, request, slug):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            return render(request, self.template_name, {'form':bound_form, 'slug':slug})


class PostEdit(View, PostMixin):
    form_class = PostForm
    model = Post
    template_name = 'dagbok/update_post.html'

    def get(self, request, slug, year, month, day):
        post = self.get_object(slug, year, month, day)
        context = {'form':self.form_class(instance=post), 'post':post}
        return render(request, self.template_name, context)
    def post(self, request, slug, year, month, day):
        post = self.get_object(slug, year, month, day)
        bound_form = self.form_class(request.POST, instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            context = {'form':bound_form, 'post':post,}
            return render(request, self.template_name, context)

class PostDelete(View, PostMixin):
    model = Post
    template_name = 'dagbok/delete_post.html'

    def get(self, request, slug, year, month, day):
        post = self.get_object(slug, year, month, day)
        return render(request, self.template_name, {'post':post})
    def post(self, request, slug, year, month, day):
        post = get_object(slug, year, month, day)
        post.delete()
        return redirect(reverse('dagbok', kwargs={'slug':slug}))
