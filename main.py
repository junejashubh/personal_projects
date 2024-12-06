import functions_framework

# Register a function with an HTTP trigger
@functions_framework.http
def hello_world(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
    Returns:
        The response text.
    """
    return "Hello, World!"