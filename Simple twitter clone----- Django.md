# Simple twitter clone----- Django

# 1. setting up  Django

1. virtualvenv

```python
py -3 -m venv django
```

activate

```
django\Scripts\activate
```

2. install Django

```
pip install django
```



2. First Django app

start a random project

```
django-admin startproject random_projcet
```

```
python manage.py runserver
```

![image-20200530003912082](C:\Users\TC\AppData\Roaming\Typora\typora-user-images\image-20200530003912082.png)

3. file path

   ![image-20200530004151837](C:\Users\TC\AppData\Roaming\Typora\typora-user-images\image-20200530004151837.png)

   

3. add feed

   1. The high-level framework
      Overview
      The high-level feed-generating framework is supplied by the Feed class. To create a feed, write a Feed class and point to an instance of it in your URLconf.

      Feed classes
      A Feed class is a Python class that represents a syndication feed. A feed can be simple (e.g. a “site news” feed, or a basic feed displaying the latest entries of a blog) or more complex (e.g. a feed displaying all the blog entries in a particular category, where the category is variable).

      Feed classes subclass django.contrib.syndication.views.Feed. They can live anywhere in your codebase.

      Instances of Feed classes are views which can be used in your URLconf.

4. Django的migrations

   1. ```cmd
      python manage.py  migrate
      ```

5. add superuser 

   1. ```Django
      python manage.py createsuperuser
      ```

      