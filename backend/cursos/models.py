from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self) -> str:
        return str(self.title)


class Rating(Base):
    course = models.ForeignKey(
        Course, related_name='ratings', on_delete=models.CASCADE)
    evaluator_name = models.CharField(max_length=255)
    email = models.EmailField()
    comments = models.TextField(blank=True, default='')
    note = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        unique_together = ['email', 'course']

    def __str__(self):
        return f'{self.evaluator_name} evaluated the course {self.course} with note {self.note}'
