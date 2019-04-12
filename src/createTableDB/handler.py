import boto3
import pymysql
import os
import logging
import sys

rds_host = os.environ['DB_ADDRESS']
name = 'root'
password = 'password'
db_name = os.environ['DB_ID']
port = os.environ['DB_PORT']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
  conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=10000)
  print(conn)
except:
  logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
  sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
def handler(message, context):
  with conn.cursor() as cur:
    cur.execute("create table Employee3 ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")
    conn.commit()
    for row in cur:
      print(row)
  conn.commit()

  return "Added %d items from RDS MySQL table" %(item_count)