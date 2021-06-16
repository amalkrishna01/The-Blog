from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView , DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category,Profile,Comment
from django.urls import reverse_lazy, reverse
from .forms import PostForm,ProfilePageForm,CommentForm
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect

from django.views import generic


# Create your views here.

def home(request):
    return render(request,'home.html')

#def landing(request):
#   return render(request,'landing.html')
def test(request):
    return render(request,'test.html')
'''
def profile(request):
    return render(request,'edit_profile.html')

'''

def LikeView(request,pk):
    post = get_object_or_404(Post , id = request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    
    
    #return HttpResponseRedirect(reverse('detail', args[str(pk)]))
    return redirect('detail', post.pk)    




def CategoryView(request,cats):
    category = Category.objects.filter(name = cats).first()
    if(category):
        post = category.post_set.all()
        return render(request,'categories.html',{'cats':cats ,'category_posts' : post })
    return HttpResponse('Invalid Tag')

class landing(ListView):
    model = Post
    template_name = 'landing.html'
    ordering = ['-post_date']

    def get_context_data(self,*args ,**kwargs): 
        cat_menu = Category.objects.all()
        context = super(ListView, self).get_context_data(*args ,**kwargs)
        context["cat_menu"] = cat_menu 
        return context     
        
    
class detail(DetailView):
    model = Post
    template_name = 'detail.html'

    def get_context_data(self,*args ,**kwargs): 
        cat_menu = Category.objects.all()
        context = super(DetailView, self).get_context_data(*args ,**kwargs)
        
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu 
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class Addpost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html' 
    #fields = '__all__'

class Editpost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'updatepost.html'

class Deletepost(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('landing')



class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'user.html'

    def get_context_data(self,*args ,**kwargs): 
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args ,**kwargs)
        
        page_user = get_object_or_404(Profile , id = self.kwargs['pk'])
        

        context["page_user"] = page_user 
        return context  


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'edit_profile.html'
    fields = ['bio','profile_pic','website_url','instagram_url']



    success_url = reverse_lazy('landing')


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'create_profile.html'
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comments.html' 
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    
    success_url = reverse_lazy('landing')
