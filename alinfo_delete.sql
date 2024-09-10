-- Termina todas las conexiones a la base de datos "alinfo"
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'alinfo'
  AND pid <> pg_backend_pid();

-- Borra la base de datos "alinfo"
DROP DATABASE alinfo;