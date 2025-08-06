# *E-commerce*

##  В проект добавлены следующие классы
- Category
```
C параметрами:

name
description
products

category_count
product_count
```

- Order
```
C параметрами:

product
quantity
total_price
```

- Product
```
C параметрами:

name
description
price
quantity
```

- Наследники класса Product

  * Smartphone
  ```
  С параметрами:
  
  name
  description
  price
  quantity
  
  efficiency
  model
  memory
  color
  ```
  
  * LawnGrass
  ```
  С параметрами:
  
  name
  description
  price
  quantity
  
  country
  germination_period
  color
  ```
- Базовые абстрактные классы
  + BaseProduct
  ```
  С методами:
  
  new_product
  __str__
  __add__
  getter - product_price
  setter - product_price
  ```
  
  + BasePay
  ```
  С методами:
  
  __init__
  ```
### Реализована загрузка категорий из json-файла

```
Для работы с файлом нужно разместить его по пути ...\E-commerce\data\
```