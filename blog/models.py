from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=20, default='teal')  # for UI styling

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class BookReview(models.Model):
    RATING_CHOICES = [(i, f"{i} stars") for i in range(1, 6)]
    STATUS_CHOICES = [
        ('read', 'Read'),
        ('reading', 'Currently Reading'),
        ('wishlist', 'Wish List'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='read')
    summary = models.TextField(max_length=300)
    review_content = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='book_reviews'
    )
    buy_link = models.URLField(blank=True, help_text="Direct link to buy the book")
    affiliate_link = models.URLField(blank=True, help_text="Your Amazon affiliate link")
    recommended = models.BooleanField(default=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} by {self.author}"

    def stars_display(self):
        return "★" * self.rating + "☆" * (5 - self.rating)

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    summary = models.TextField(max_length=300)
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts'
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def reading_time(self):
        word_count = len(self.content.split())
        minutes = max(1, round(word_count / 200))
        return f"{minutes} min read"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link_label = models.CharField(max_length=100)
    link_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    tagline = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    twitter = models.URLField(blank=True)
    substack = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    author_reply = models.TextField(blank=True)
    replied_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"