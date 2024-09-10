from import_export import resources
from .models import Suggestion

class SuggestionResource(resources.ModelResource):
    class Meta:
        model = Suggestion


