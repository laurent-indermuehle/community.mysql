.PHONY: up
up:
	podman run --rm --detach --name db \
	--env MARIADB_ALLOW_EMPTY_ROOT_PASSWORD=true \
	docker.io/mariadb:10.5

.PHONY: provision
provision:
	podman exec -it db bash -c "apt-get update && apt-get install --yes python3.8 python3-pymysql"

.PHONY: exec
exec:
	podman exec -it db bash

.PHONY: down
down:
	podman stop -t 0 db
