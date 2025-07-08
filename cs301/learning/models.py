from django.db import models
from django.contrib.auth.models import User


#THIS IS THE TABLE FOR THE MODULES
class Module(models.Model):
    module_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    sequence = models.PositiveIntegerField(help_text="Order in which modules appear")

    def __str__(self):
        return self.title
 
#THIS IS THE MODEL/TABLE FOR LEARNING MATERIALS    
class LearningMaterial(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=200)
    content = models.TextField(help_text="Main lesson content in text")
    is_adaptive = models.BooleanField(default=False)

    def __str__(self):
        return self.title    
    

#THIS IS THE QUIZ TABLE
class Quiz(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

#THIS IS THE QUIZ QUESTION TABLE
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='coding_questions')
    title = models.CharField(max_length=200)
    description = models.TextField(help_text="The problem statement for the coding question.")
    starter_code = models.TextField(blank=True, help_text="Optional starter code for students.")
    expected_output = models.TextField(help_text="Expected output when the correct code is run.")
    max_score = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.title    
    
STATUS_CHOICES = [
        ('N', 'Not Started'),
        ('P', 'In Progress'),
        ('C', 'Completed'),
]

#THIS IS THE PROGRESS TABLE
class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress_records')
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')
    score = models.FloatField(blank=True, null=True)
    last_accessed = models.DateTimeField(auto_now=True)
    recommended_next_material = models.ForeignKey(
        LearningMaterial, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='recommended_to'
    )

    class Meta:
        unique_together = ('user', 'module')

    def __str__(self):
        return f"{self.user.username} - {self.module.title}"    