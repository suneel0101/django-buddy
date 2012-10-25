install:
	@pip install -r conf/requirements-local.txt
	@gem install compass
sync:
	@python manage.py syncdb
migrate:
	@python manage.py migrate
