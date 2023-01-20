from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("DB_URL")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")

driver = GraphDatabase.driver(uri, auth=(user, password))