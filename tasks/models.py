from django.db import models
from django.conf import settings



class Task(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    completed = models.BooleanField(default=False, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


    
    indexes = [
        models.Index(fields=["owner", "completed"], name="task_owner_completed_idx"),
        ]

    
    verbose_name = "Task"
    verbose_name_plural = "Tasks"

    def __str__(self):
        
        return f"{self.title} ({self.owner.username})"