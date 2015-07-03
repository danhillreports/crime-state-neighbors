all: data/raw.xls data/raw.csv data/data.csv

data/raw.xls:
	wget --no-use-server-timestamps \
	https://www.fbi.gov/about-us/cjis/ucr/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/4tabledatadecoverviewpdf/table_4_crime_in_the_united_states_by_region_geographic_division_and_state_2012-2013.xls/output.xls \
	-O $@

data/raw.csv: data/raw.xls
	in2csv $< > $@

data/data.csv:
	python processors/convert_csv.py

