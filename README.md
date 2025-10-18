# Data Science Sprint 19
## Healthcare project

### Системные требования

 - Ubuntu 24.04.3 LTS, 6.14.0-33-generic
 - Python 3.12.3
 - Docker version 28.5.1, build e180ab8
 - Docker Compose version v2.40.0
 - scikit-learn 1.7.2

### Исследования и обучение модели

 - [jupyter notebook](./jupyter-notebook/sprint_19_project_healtcare.ipynb)

### Предсказания на тестовых данных

 - [predictions.csv](./predictions.csv)

### Запуск приложения

```sh
sudo docker compose up -d --build
```

### Тестовый запрос

```sh
cd ./test/
sudo chmod +x ./test.sh
./test.sh
```

### Пример ответа

```sh
[{"id":7746,"prediction":0},{"id":4202,"prediction":0},{"id":6632,"prediction":1},{"id":4639,"prediction":0}]
```