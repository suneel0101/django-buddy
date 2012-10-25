install:
	@pip install -r conf/requirements-local.txt
sync:
	@python manage.py syncdb
migrate:
	@python manage.py migrate
