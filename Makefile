%.svg: %.csv
	docker run -i gms-flamegraph < $^ > $@

gms-flamegraph:
	docker build -t gms-flamegraph .
