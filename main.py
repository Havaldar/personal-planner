import datetime

from airtable.airtable import Airtable
from twilio.rest import Client
from os.path import join, dirname
from dotenv import get_variables


dotenv_path = join(dirname(__file__), '.env')
env = get_variables(dotenv_path)
airtable_client = Airtable(env['AIRTABLE_BASE_ID'],env['AIRTABLE_API_KEY'])


def text_reminder(client, records):
	return


def archive_records(client, table_name, records):
	return
