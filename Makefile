.PHONY: help \
	frontend-dev \
	frontend-test \
	frontend-test-watch \
	infra-up \
	infra-down \
	infra-logs \
	infra-stop \
	dev

help:
	@echo "Comandos disponíveis:"
	@echo ""
	@echo "Frontend"
	@echo "  make frontend-dev"
	@echo "  make frontend-test"
	@echo "  make frontend-test-watch"
	@echo ""
	@echo "Backend"
	@echo ""
	@echo "Infra"
	@echo "  make infra-up"
	@echo "  make infra-stop"
	@echo "  make infra-down"
	@echo "  make infra-logs"
	@echo ""
	@echo "Projeto"
	@echo "  make dev"

frontend-dev:
	cd frontend && npm run dev

frontend-test:
	cd frontend && npm run test

frontend-test-watch:
	cd frontend && npm run test:watch

infra-up:
	docker compose -f infra/compose.yaml up -d

infra-stop:
	docker compose -f infra/compose.yaml stop

infra-down:
	docker compose -f infra/compose.yaml down

infra-logs:
	docker compose -f infra/compose.yaml logs -f

dev:
	$(MAKE) infra-up
	$(MAKE) frontend-dev