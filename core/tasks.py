from __future__ import absolute_import, unicode_literals

from .parser import YcombinatorParse
from .models import HackerNews
from appfollow.celery_settings import app
from .serializers import PostSerializer


@app.task(name='update_db')
def update_db():
    try:
        obj = YcombinatorParse()
    except Exception:
        return {'result': 'Connection Error'}

    result = obj.find()
    serializer = PostSerializer(data=result, many=True)
    if not serializer.is_valid():
        return {'result': 'Serialization Error'}
    for r in result:
        HackerNews.objects.get_or_create(
            title=r['title'],
            url=r['link'],
        )
    return {'result': 'Success'}
