import argparse

from viroid.collector.aggregates import DiseasesEndpoints
from viroid.collector.endpoints.covid_19 import Covid19Endpoint
from viroid.collector.endpoints.influenza import InfluenzaEndpoint

ENDPOINTS = {
    'covid19': Covid19Endpoint,
    'influenza': InfluenzaEndpoint
}


def get_endpoints(session, redis):
    """A function to setup and get endpoints.

    Arguments are generally used for debug purposes
    to test certain endpoints without launching the
    others.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--diseases', '-d', type=str, nargs='*', help='List of diseases to monitor.')
    diseases = parser.parse_args().diseases
    if not diseases:
        endpoints = ENDPOINTS.values()
    else:
        endpoints = (v for k, v in ENDPOINTS.items() if any(d in k for d in diseases))
    __set_models(redis, endpoints)
    return DiseasesEndpoints(session, endpoints)


def __set_models(redis, endpoints):
    for e in endpoints:
        e._model._r = redis
