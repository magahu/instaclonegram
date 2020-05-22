"""Posts views Configuration"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#Home view
@login_required
def posts(request):
    return render(request, 'home.html')


#Create new post view
@login_required
def new_post(request):
    if request.method == 'POST':
        pass
    return render(request, 'posts/new_post.html')

