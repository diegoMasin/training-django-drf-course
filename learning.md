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
```
