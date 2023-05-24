### My learning into this course from Udemy

**Some commands interesting**

```bash
python manage.py shell
>>> from rest_framework.renderers import JSONRenderer
>>> from backend.cursos.models import Cours
>>> from backend.cursos.serializers import CourseSerialize

>>> curso = Course.objects.latest('id')
# curso
# curso.title
>>> serializer = CourseSerializer(curso)
>>> serializer.data
# it's a dict -> don't have a double quote, it have a single quote
>>> JSONRenderer().render(serializer.data)
# this command has a binary string output
_______________________________________________
print dir(request)
# show all available methods -> It's GREAT
request.data
request.query_params
request.user
# key attributes to inspect when necessary
```

**Learning steps**

- Creating some **models** and executing migrate
- Registering them on **admin.py** only to help to add data on database
- Creating the **serializers** and using django **shell**
- Creating the first **views** and **urls**
- Looking into attributes from **request**
