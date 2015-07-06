all: data/raw.xls data/raw.csv data/state_hash.json data/stateface.json data/data.csv

data/raw.xls:
	wget --no-use-server-timestamps \
	https://www.fbi.gov/about-us/cjis/ucr/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/4tabledatadecoverviewpdf/table_4_crime_in_the_united_states_by_region_geographic_division_and_state_2012-2013.xls/output.xls \
	-O $@

data/raw.csv: data/raw.xls
	in2csv $< > $@

data/state_hash.json:
	wget --no-use-server-timestamps \
	https://gist.githubusercontent.com/mshafrir/2646763/raw/f2a89b57193e71010386a73976df92d32221d7ba/states_hash.json \
	-O $@

data/stateface.json:
	wget --no-use-server-timestamps \
	http://propublica.github.io/stateface/reference/stateface.json -O $@

data/data.csv:
	python processors/convert_csv.py

