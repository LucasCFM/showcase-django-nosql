cd /app && \
coverage run --source='.' manage.py test && \
coverage html -d /test-coverage