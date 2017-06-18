import datetime

from airtable.airtable import Airtable
from twilio.rest import Client
from os.path import join, dirname
from dotenv import get_variables

AIRTABLE_BASE_URL = "https://api.airtable.com/v0"
AIRTABLE_BASE_ID = "app2tEnrXO9tQxei0"
AIRTABLE_API_KEY = "keyRfbMDzIzUtCuPs"
AIRTABLE_TABLE_NAME = "To Do"

dotenv_path = join(dirname(__file__), '.env')
env = get_variables(dotenv_path)
airtable_client = Airtable(env['AIRTABLE_BASE_ID'],env['AIRTABLE_API_KEY'])


def text_reminder(client, records):
	return


def archive_records(client, table_name, records):
	return
