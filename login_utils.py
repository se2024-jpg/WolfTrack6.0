'''
MIT License

Copyright (c) 2024 Girish G N, Joel Jogy George, Pravallika Vasireddy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from flask import session, request
from hashlib import sha512

def get_headers():
    """Retrieve the User-Agent and the client's IP address from the request headers."""
    user_agent = request.headers.get("User-Agent")
    address = request.headers.get("X-Forwarded-For", request.remote_addr)
    return user_agent, address

def get_session_identifier():
    """Generate a unique session identifier based on the user's IP address and User-Agent."""
    user_agent, address = get_headers()
    user_agent_bytes = user_agent.encode("utf-8") if user_agent else b""
    address_bytes = address.encode("utf-8").split(b",")[0].strip() if address else b""

    base = f"{address_bytes.decode('utf-8')}|{user_agent_bytes.decode('utf-8')}"
    h = sha512()
    h.update(base.encode("utf-8"))
    return h.hexdigest()

def login_user(app, user, remember=False, duration=None, force=False, fresh=True):
    """
    Logs a user in. You should pass the actual user object to this. If the
    user's `is_active` property is ``False``, they will not be logged in
    unless `force` is ``True``.

    This will return ``True`` if the log in attempt succeeds, and ``False`` if
    it fails (i.e. because the user is inactive).
    
    :param user: The user object to log in.
    :param remember: Whether to remember the user after their session expires.
    :param duration: The amount of time before the remember cookie expires. 
    :param force: If the user is inactive, setting this to ``True`` will log
        them in regardless. Defaults to ``False``.
    :param fresh: If ``False``, the session will be marked as not "fresh". 
    """
    print("###USER", user)
    session["user_id"] = user[0]
    session["type"] = user[4]
    session["_fresh"] = fresh
    session["_id"] = get_session_identifier()
    print("IDENTIFIER##########", session["_id"])

    if remember:
        session["_remember"] = "set"
        if duration is not None:
            if not isinstance(duration, (int, float)):
                try:
                    # Calculate total seconds for remember duration
                    session["_remember_seconds"] = (
                        duration.total_seconds()
                    )
                except AttributeError as e:
                    raise ValueError(
                        f"Duration must be a datetime.timedelta, instead got: {duration}"
                    ) from e
    return True
