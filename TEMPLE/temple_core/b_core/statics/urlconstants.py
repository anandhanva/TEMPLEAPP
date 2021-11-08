from requests.models import ProtocolError


PROTO="http://"
IP_DEV="192.168.0.238"
IP_UAT=""
IP_PROD=""
PORT="8002"
ENDPOINT="/android"


BASE_URL=PROTO+IP_DEV+':'+PORT+ENDPOINT
LOGIN=BASE_URL+"login"
