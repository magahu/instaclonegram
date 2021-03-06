"""Posts views Configuration"""

from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, NewLikeForm, NewCommentForm, SavedPostForm, ReplyForm
from .models import Post, Like, Comment, SavedPost, CommentLike, Reply, ReplyLike
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from users.views import list_notifications
#using class-based views
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic import CreateView

#Create new post using a class based view
class CreatePostView(CreateView, LoginRequiredMixin):
    template_name = 'posts/new_post.html'
    form_class = NewPostForm
    success_url = reverse_lazy('posts:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


#Create new post view
#@login_required
#def new_post(request):
    ##notifications for the navigation bar
    #likes = list_notifications(request)
    ## if this is a POST request we need to process the form data
    #if request.method == 'POST': 
        ## create a form instance and populate it with data from the request:
        #form = NewPostForm(request.POST, request.FILES)
        ##Set the post description as the first comment
        #if form.is_valid(): 
            #form.save()
            # redirect to a new URL:
            #return redirect('posts:home')
    #else:
        # if a GET (or any other method) we'll create a blank form
        #form = NewPostForm(prefix="form")
       
    #return render(request, 'posts/new_post.html', {'form':form, 'likes':likes})


##Home view
#@login_required
#def home(request):
    #posts = Post.objects.all().order_by('-created')
    #for post in posts:
        #post.like = post.like_set.filter(user=request.user, post=post)
        #post.saved = post.savedpost_set.filter(user=request.user)
        ##notifications for the navigation bar
        #likes = list_notifications(request)
         
    ##import pdb; pdb.set_trace()
    #return render(request, 'home.html', {'posts':posts, 'likes':likes})


#Home class-based view
class HomePostsList(ListView, LoginRequiredMixin):
    template_name = 'home.html'
    model = Post
    ordering = ('-created',)
    context_object_name = 'posts'

    def get_context_data(self,**kwargs):
        posts = Post.objects.all().order_by('-created')
        for post in posts:
            post.like = post.like_set.filter(user=self.request.user, post=post)
            post.saved = post.savedpost_set.filter(user=self.request.user)

        context = super(HomePostsList, self).get_context_data(**kwargs)

        context['posts'] = posts
        context['likes'] = list_notifications(self.request)
        return context



#Create like view
@login_required
def new_like(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewLikeForm(request.POST)
       
        post = request.POST['post']
        user = request.POST['user']
        like = Like.objects.filter(post=post, user=user)

        #import pdb; pdb.set_trace()
        # check whether it's valid:
        if like:
            like.delete()
            return redirect(request.META.get('HTTP_REFERER'))
        elif form.is_valid():
            form.save()
            # redirect to a new URL:
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        # if a GET (or any other method) we'll create a blank form
        form = NewLikeForm()
    
    return render(request, 'home.html')


#Create comment view
@login_required
def new_comment(request, pk):
    # if this is a POST request we need to process the form data
    if request.method == 'POST': 
        #import pdb; pdb.set_trace()
        # create a form instance and populate it with data from the request:
        form = NewCommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid(): 
            form.save()
            # redirect to a new URL:
            post = get_object_or_404(Post, pk=pk)
            url = reverse('posts:show-comments', kwargs={'pk':post.pk})
            return redirect(url)
            
    else:
        return redirect('posts:home')


##Show comments
#@login_required
#def list_comments(request, pk, comment_pk=0):
    #post = Post.objects.get(pk=pk)
    #post.like = post.like_set.filter(user=request.user)
    ##pass if is a saved post
    #post.saved = post.savedpost_set.filter(user=request.user)
    ##pass comment whit like user like variable
    #comments = post.comment_set.all()
    #for comment in comments:
        #comment.comment_like = CommentLike.objects.filter(comment=comment, user=request.user)
        #comment.replies = comment.reply_set.all()
    #pass reply with like user variable

        #for reply in comment.replies:
            #reply.reply_like = ReplyLike.objects.filter(reply=reply, user=request.user)
    
    ##notifications for the navigation bar
    #likes = list_notifications(request)
    
    ##if there's a comment to reply
    #comment_to_reply = Comment.objects.filter(pk=comment_pk)
    #if comment_to_reply:
        #reply_to = get_object_or_404(Comment, pk=comment_pk)
    #else:
        #reply_to = 0

    #context = {'post':post, 'likes':likes, 'reply_to':reply_to,
    #'comments':comments}
    ##import pdb; pdb.set_trace()
    #return render(request, 'posts/comments.html', context)


#Show comments class-based views
class PostDetail(DetailView, LoginRequiredMixin):
    template_name = 'posts/comments.html'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    queryset = Post.objects.all()
    context_object_name = 'post'


    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        

        #post = Post.objects.get(pk=pk)
        post.like = post.like_set.filter(user=self.request.user)
        #pass if is a saved post
        post.saved = post.savedpost_set.filter(user=self.request.user)

        context['post'] = post

        comments = post.comment_set.all()
        for comment in comments:
            comment.comment_like = CommentLike.objects.filter(comment=comment, user=self.request.user)
            comment.replies = comment.reply_set.all()
            #pass reply with like user variable
            for reply in comment.replies:
                reply.reply_like = ReplyLike.objects.filter(reply=reply, user=self.request.user)
        
        context['comments'] = post.comment_set.all()

        #if there's a comment to reply
        comment_to_reply = Comment.objects.filter(pk=self.comment_pk)
        if comment_to_reply:
            reply_to = get_object_or_404(Comment, pk=self.comment_pk)
        else:
            reply_to = 0

        context['reply_to'] = reply_to

        return context


#Display users likes
@login_required
def list_likes(request, pk):
    users = []
    likes = Like.objects.filter(post=pk)
    for like in likes:
        user = like.user
        users.append(user)   

    #notifications for the navigation bar
    likes = list_notifications(request)

    context = {'contacts':users, 'label':'Me gusta', 'likes':likes}
    
    return render(request, 'users/contacts.html', context)


#Save-post view
@login_required
def save_post(request):
    if request.method == 'POST':
        form = SavedPostForm(request.POST)
        post = request.POST['post']
        user = request.POST['user']

        saved_post = SavedPost.objects.filter(user=user, post=post)

        if saved_post:
            saved_post.delete()
            return redirect('posts:home')
        elif form.is_valid():
            form.save()
            return redirect('posts:show-saved')

    else:
        form = SavedPostForm()
        return redirect('posts:home', {'form':form})


#List saved posts by the logged user
@login_required
def list_saved_posts(request):
    posts = []
    saved = SavedPost.objects.filter(user=request.user)
    for save in saved:
        post = Post.objects.get(pk=save.post.pk)
        posts.append(post)
   
    #notifications for the navigation bar
    likes = list_notifications(request)

    context = {'saved_posts':posts, 'likes':likes}
    
    return render(request, 'posts/saved_posts.html', context)

    
#Delete the selected post of the logged user
@login_required
def delete_post(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if post.user == request.user:
        post.delete()
        return redirect('posts:home')


#Like comment
@login_required
def like_comment(request, comment_pk):
    
    comment = get_object_or_404(Comment, pk=comment_pk)
    like = CommentLike.objects.filter(comment=comment, user=request.user)

    #import pdb; pdb.set_trace()

    if not like:
        like = CommentLike.objects.create(comment=comment, user=request.user)
    else:
        like.delete()
    
    url = reverse('posts:show-comments', kwargs={'pk':comment.post.pk})
    return redirect(url)


#Redirect to the page with the reply form instead the comment form
@login_required
def new_reply(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    

    context = {'pk':comment.post.pk, 'comment_pk':comment_pk}
    url = reverse('posts:show-comments-reply', kwargs=context)
    return redirect(url)
    

#Create a reply to a comment
def create_reply(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            reply_form.save()
    
    url = reverse('posts:show-comments', kwargs={'pk':comment.post.pk})
    return redirect(url)


#Like reply
def like_reply(request, reply_pk):
    reply = get_object_or_404(Reply, pk=reply_pk)
    reply_like = ReplyLike.objects.filter(reply=reply_pk, user=request.user)
    

    if not reply_like:
        reply_like = ReplyLike.objects.create(reply=reply, user=request.user)
    else:
        reply_like.delete()

    comment = get_object_or_404(Comment, pk=reply.comment.pk)
    url = reverse('posts:show-comments', kwargs={'pk':comment.post.pk})
    return redirect(url)


