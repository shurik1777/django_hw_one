#### Для работы с моделью Client: 

1. **Создать нового клиента:**

```
py manage.py client_crud create --name "New Clint" --email "example@example.ru" --phone "+12345678" --address "Moscows city"
```

2. **Прочитать информацию о клиенте:**

```
py manage.py client_crud get --client_id 1
```

3. **Обновить информацию о клиенте:**

```
py manage.py client_crud update --client_id 1 --name "Обновленное Имя" --email "updated@email.com" --phone "8911233443" --address "Perm"
```

4. **Удалить клиента:**

```
py manage.py client_crud delete --client_id 1
```

5. **Показать весь список клиентов:**

```
py manage.py client_crud list
```

#### Для работы с моделью Article:

1. **Создать новый товар:**

```
py manage.py article_crud create --title "Товар" --content "adasdadahacker" --price 2 --amount 5
```

2. **Прочитать информацию о товаре:**

```
py manage.py article_crud get --article_id 1
```

3. **Обновить информацию о товаре:**

```
py manage.py article_crud update --article_id 1 --title "Обновленное Имя" --content "updated@email.com"
```

4. **Удалить товар:**

```
py manage.py article_crud delete --article_id 1
```

5. **Показать весь список товаров:**

```
py manage.py article_crud list
```

#### Для работы с моделью Order:

1. **Создать новый заказ:**

```
py manage.py order_crud create --client_id 1 --product_id 2 --price 8 --date_of_order "2024-06-09"
```

2. **Прочитать информацию о заказе:**

```
py manage.py order_crud get --order_id 1
```

3. **Обновить информацию о заказе:**

```
py manage.py order_crud update --order_id 1 --client_id 1 --article_id 2 --price 7 --date_of_decor "2024-06-10"
```

4. **Удалить заказ:**

```
py manage.py order_crud delete --order_id 1
```

5. **Показать весь список заказов:**

```
py manage.py order_crud list
```
