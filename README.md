# diploma_backend

## Запуск:

- В директории ```./infra``` поднять контейнеры:

```console
docker-compose up -d --build
```
### При первом запуске:
- Собрать статику
```
sudo docker-compose exec backend python manage.py collectstatic --noinput
```
- Применить миграции:
```
sudo docker-compose exec backend python manage.py migrate --noinput
```
