CREATE DATABASE alinfo
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'es_ES.UTF-8'
    LC_CTYPE = 'es_ES.UTF-8'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    TEMPLATE = template0;

CREATE OR REPLACE FUNCTION prevent_superuser_delete()
RETURNS TRIGGER AS $$
BEGIN
    IF OLD.is_superuser THEN
        RAISE EXCEPTION 'No puedes eliminar a un superusuario.';
    END IF;
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER before_user_delete
BEFORE DELETE ON users_user
FOR EACH ROW
EXECUTE FUNCTION prevent_superuser_delete();
