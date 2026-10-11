from datetime import datetime
from django.db import models
from abc import ABC, abstractmethod

# Create your models here.

class BaseEntity(ABC):
    @abstractmethod
    def validate(self):
        pass

    def to_dict(self):
        return {
            key: value
            for key, value in self.__dict__.items()
        }

class Reporter(BaseEntity):
    def __init__(self, id, name, email, team):
        self.id = id
        self.name = name
        self.email = email
        self.team = team

    def validate(self):
        if not self.name:
            raise ValueError('Name cannot be empty')
        if '@' not in self.email:
            raise ValueError('Invalid email')
class Issue(BaseEntity):
    statuses = ["open","in_progress","closed","resolved"]
    priorities = ["low","medium","high","critical"]
    def __init__(self, id, title, description, status, priority, reporter_id):
        # your init here
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.reporter_id = reporter_id
        self.created_at = str(datetime.now())  # Placeholder for creation timestamp
    def validate(self):
        # your validation here
        if not self.title:
            raise ValueError('Title cannot be empty')
        if self.status not in self.statuses:
            raise ValueError('Invalid status')
        if self.priority not in self.priorities:
            raise ValueError('Invalid priority')
        
    def describe(self):
        return f"{self.title} [{self.priority}]"

class CriticalIssue(Issue):
    def describe(self):
        return f"[URGENT] {self.title} — needs immediate attention"

class LowPriorityIssue(Issue):
    def describe(self):
        return f"{self.title} — low priority, handle when free"
# In views.py:
# from issues.models import Reporter, Issue
 