setup:
	docker-compose up -d
teardown:
	docker-compose down -v
watch:
	poetry run pytest -f --lf --color=yes