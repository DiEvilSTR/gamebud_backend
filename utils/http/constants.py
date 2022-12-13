class HttpMethod:
    DELETE = 'DELETE' # Delete entity
    GET = 'GET' # Get entity
    PATCH = 'PATCH' # Partial entity update
    POST = 'POST' # Create entity
    PUT = 'PUT' # Replace the entire entity


class HttpStatus:
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204

    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
