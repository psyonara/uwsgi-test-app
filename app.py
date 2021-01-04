import sys

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    msg = f"Hello World from {sys.version}!"
    return [msg.encode()]
