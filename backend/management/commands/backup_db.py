import os
from django.core.management.base import BaseCommand
from decouple import config


class Command(BaseCommand):
    help = "Realiza un respaldo de la base de datos"

    def handle(self, *args, **kwargs):
        db_name = config("DATABASE_NAME")
        db_user = config("DATABASE_USER")
        db_password = config("DATABASE_PASSWORD")
        db_host = config("DATABASE_HOST")
        db_port = config("DATABASE_PORT")
        backup_file = f"{db_name}_backup.sql"

        # Comando para realizar el respaldo
        command = f"PGPASSWORD={db_password} pg_dump -U {db_user} -h {db_host} -p {db_port} {db_name} > {backup_file}"
        os.system(command)

        self.stdout.write(
            self.style.SUCCESS(
                f"Respaldo de la base de datos guardado en {backup_file}"
            )
        )
