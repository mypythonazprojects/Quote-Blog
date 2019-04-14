from django.db import models
from datetime import date
class QuoteCatergory(models.Model):
    title=models.CharField(max_length=50)
    def __str__(self):
        return self.title


class Quote(models.Model):
    quote=models.TextField()
    author=models.CharField(max_length=200)
    date = models.DateField(("Date"), default=date.today)
    quotecatergory=models.ForeignKey(
        'QuoteCatergory',on_delete=models.CASCADE
    )
    def __str__(self):
        if len(self.quote) > 50:
            return self.quote[:50]+" ..."
        else:
            return self.quote[:50]
