from django.db import models
from tasks.models import Project, Task


class BugReport(models.Model):
    STATUS_CHOICES = (
        ("New", "Новая"),
        ("In_progress", "В работе"),
        ("Completed", "Завершена"),
    )

    PRIORITY_CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )

    title = models.CharField(
        max_length=100,
        verbose_name="Краткое описание бага",
    )
    description = models.TextField(verbose_name="Полное описание бага")
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="bug_reports"
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bug_reports",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="New",
        verbose_name="Статус бага",
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=1,
        verbose_name="Приоритет бага",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания записи",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время последнего обновления записи",
    )

    def __str__(self):
        return self.title


class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ("Consideration", "Рассмотрение"),
        ("Accepted", "Принято"),
        ("Rejected", "Отклонено"),
    ]

    PRIORITY_CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )

    title = models.CharField(
        max_length=100,
        verbose_name="Название запроса на новую функцию",
    )
    description = models.TextField(verbose_name="Описание запроса")
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="feature_requests",
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="feature_requests",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Рассмотрение",
        verbose_name="Статус запроса",
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=1,
        verbose_name="Приоритет запроса",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания запроса",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время последнего обновления запроса",
    )

    def __str__(self):
        return self.title
