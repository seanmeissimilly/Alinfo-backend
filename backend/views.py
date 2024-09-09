from django.http import HttpResponse
from django.core.management import call_command
import io


def backup_database(request):
    out = io.StringIO()
    call_command("backup", stdout=out)
    return HttpResponse(out.getvalue(), content_type="text/plain")
