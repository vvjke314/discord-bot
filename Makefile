all: run

cenzfill:
	@python3 scripts/to_json.py

run: cenzfill
	@python3 bot/test_bot.py
