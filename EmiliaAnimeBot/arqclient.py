from aiohttp import ClientSession
from Python_ARQ import ARQ
from EmiliaAnimeBot import ARQ_API_KEY

ARQ_API_URL = "https://thearq.tech"
ARQ_API_KEY = 'EFCXID-RWBBHW-ZDYIMH-PMQPHS-ARQ'
# my own API KEY Change it to your own

aiohttpsession = ClientSession()

arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
