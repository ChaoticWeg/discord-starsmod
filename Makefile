.PHONY: install run

install:
	python -m pip install -r requirements.txt --user

clean:
	-@rm new_reports.json >/dev/null 2>&1
	-@rm *.log >/dev/null 2>&1
