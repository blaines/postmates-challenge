# Geocoding Service

## Setup

- Install Python 3.7.0
- Install Dependencies in `Pipfile.lock` (I use `pipenv install`)
- Set `HERE_APP_ID` and `HERE_APP_CODE` environment variables

Then try to test or execute the server

## Testing

Run `make test`

This will start the local service, and run full end to end tests

## Execution

Run `make run`

This will start the server and begin handling tests

## Integration

Responses are in JSON format similar to the following: 
`{"lat": 000.000, "lng": 000.000, "service": "osm", "status": 20001}`

Two services are integrated, Open Street Map and HERE.

### HERE
- 50004: Error, Unauthorized
- 50001: Error, Missing Key (Probably empty result)
- 50002: Error, Missing Index (Probably empty result)
- 50003: Error, Non-200 Response Status

### Open Street Map
- 50011: Error, Missing Key (Probably empty result)
- 50012: Error, Missing Index (Probably empty result)
- 50013: Error, Non-200 Response Status