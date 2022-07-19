import random
import string

from django.db import models


valid_characters = string.ascii_letters + string.digits + "_"


class ShortUrl(models.Model):
    short = models.CharField(
        max_length=6, 
        unique=True, 
        db_index=True
    )

    full_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)

    # Gets updated at every save, so we can use this for the lastRedirect time
    updated_at = models.DateTimeField(auto_now=True)

    hit_count = models.PositiveIntegerField(default=0)

    @staticmethod
    def generate_code() -> str:
        exists = True
        while exists:
            code = ''.join(random.choice(valid_characters) for _ in range(6))
            exists = ShortUrl.objects.filter(short=code).exists()
        return code

    @staticmethod
    def shortcode_is_valid(input: str) -> bool:
        if type(input) != str:
            return False

        if len(input) != 6:
            return False
        
        return all(c in valid_characters for c in input)
