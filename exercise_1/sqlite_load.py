import sqlite3
import pandas

db = sqlite3.connect('voters_sqlite.db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ncvoters(county_id STRING, county_desc STRING, voter_reg_num STRING,status_cd STRING, voter_status_desc STRING, reason_cd STRING, voter_status_reason_desc STRING, absent_ind STRING, name_prefx_cd STRING,last_name STRING, first_name STRING, midl_name STRING, name_sufx_cd STRING, full_name_rep STRING,full_name_mail STRING, house_num STRING, half_code STRING, street_dir STRING, street_name STRING, street_type_cd STRING, street_sufx_cd STRING, unit_designator STRING, unit_num STRING, res_city_desc STRING,state_cd STRING, zip_code STRING, res_street_address STRING, res_city_state_zip STRING, mail_addr1 STRING, mail_addr2 STRING, mail_addr3 STRING, mail_addr4 STRING, mail_city STRING, mail_state STRING, mail_zipcode STRING, mail_city_state_zip STRING, area_cd STRING, phone_num STRING, full_phone_number STRING, drivers_lic STRING, race_code STRING, race_desc STRING, ethnic_code STRING, ethnic_desc STRING, party_cd STRING, party_desc STRING, sex_code STRING, sex STRING, birth_age STRING, birth_place STRING, registr_dt STRING, precinct_abbrv STRING, precinct_desc STRING,municipality_abbrv STRING, municipality_desc STRING, ward_abbrv STRING, ward_desc STRING, cong_dist_abbrv STRING, cong_dist_desc STRING, super_court_abbrv STRING, super_court_desc STRING, judic_dist_abbrv STRING, judic_dist_desc STRING, nc_senate_abbrv STRING, nc_senate_desc STRING, nc_house_abbrv STRING, nc_house_desc STRING,county_commiss_abbrv STRING, county_commiss_desc STRING, township_abbrv STRING, township_desc STRING,school_dist_abbrv STRING, school_dist_desc STRING, fire_dist_abbrv STRING, fire_dist_desc STRING, water_dist_abbrv STRING, water_dist_desc STRING, sewer_dist_abbrv STRING, sewer_dist_desc STRING, sanit_dist_abbrv STRING, sanit_dist_desc STRING, rescue_dist_abbrv STRING, rescue_dist_desc STRING, munic_dist_abbrv STRING, munic_dist_desc STRING, dist_1_abbrv STRING, dist_1_desc STRING, dist_2_abbrv STRING, dist_2_desc STRING, confidential_ind STRING, age STRING, ncid STRING, vtd_abbrv STRING, vtd_desc STRING);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS precinct_votes(county STRING, precinct STRING, total_votes INT, romney_percentage DOUBLE);
''')

cursor.execute('''SELECT COUNT (*) FROM ncvoters;''', )
table_count = cursor.fetchone()[0]
if table_count == 0:
	print("Loading ncvoters data in SQLite")
	df = pandas.read_csv('ncvoter_allc_utf.txt', sep='\t')
	df.to_sql('ncvoters', db, if_exists='append', index=False)

cursor.execute('''SELECT COUNT (*) FROM precinct_votes;''', )
table_count = cursor.fetchone()[0]
if table_count == 0:
	print("Loading precinct_votes data in SQLite")
	df = pandas.read_csv('rprecinct_votes.tsv', sep='\t')
	df.to_sql('precinct_votes', db, if_exists='append', index=False)


db.commit()
db.close()