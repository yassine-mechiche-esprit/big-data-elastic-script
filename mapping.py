import constants
import custom_mapping
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
from elasticsearch import Elasticsearch

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Connection to elasticsearch
es = Elasticsearch(constants.ELASTIC_HOST, port=constants.ELASTIC_PORT, verify_certs = constants.VERIFY_CERTS)

# Prepare the elastic settings to create index
settings = custom_mapping.ELASTIC_MAPPING_SETTINGS

# If index exists delete it
if es.indices.exists(constants.ELASTIC_INDEX):
	es.indices.delete(index=constants.ELASTIC_INDEX, ignore=[400, 404])

# Create the index with the settings defined above
es.indices.create(index = constants.ELASTIC_INDEX, body=settings)

# Index mapping structure
mapping = custom_mapping.ELASTIC_MAPPING

# Add this mapping to the index that we created
response = es.indices.put_mapping(index=constants.ELASTIC_INDEX, doc_type=constants.ELASTIC_DOC_TYPE, body=mapping, include_type_name=constants.ELASTIC_INCLUDE_TYPE_NAME)

# Show the response from mapping
print(response)