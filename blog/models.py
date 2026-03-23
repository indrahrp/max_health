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