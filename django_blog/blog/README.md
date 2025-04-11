"""
Blog Post Management Features

Features:

- Authenticated users can create, update, and delete posts.
- All users can view blog post lists and details.
- Only the post's author can edit or delete their post.
- Navigation available from list to detail, edit, and delete.
- Uses Django’s class-based views and mixins for access control.

URLs:

- /posts/ : list of posts
- /posts/new/ : create post (login required)
- /posts/<id>/ : view post
- /posts/<id>/edit/ : edit post (author only)
- /posts/<id>/delete/ : delete post (author only)
  """
