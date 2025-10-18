# Data Science Sprint 19
## Healthcare project

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