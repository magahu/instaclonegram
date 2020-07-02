from django.contrib import admin
from posts.models import Post, Like, Comment, SavedPost, CommentLike, Reply, ReplyLike

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(SavedPost)
admin.site.register(CommentLike)
admin.site.register(Reply)
admin.site.register(ReplyLike)