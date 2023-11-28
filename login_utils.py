from flask import session, request
from hashlib import sha512


def get_headers():
    user_agent = request.headers.get("User-Agent")
    address = request.headers.get("X-Forwarded-For", request.remote_addr)
    return user_agent,address

def get_session_identifier():
    user_agent,address = get_headers()
    if user_agent is not None:
        user_agent = user_agent.encode("utf-8")
    
    if address is not None:
        # An 'X-Forwarded-For' header includes a comma separated list of the
        # addresses, the first address being the actual remote address.
        address = address.encode("utf-8").split(b",")[0].strip()
    base = f"{address}|{user_agent}"
    if str is bytes:
        base = str(base, "utf-8", errors="replace")  # pragma: no cover
    h = sha512()
    h.update(base.encode("utf8"))
    return h.hexdigest()

def login_user(app,user, remember=False, duration=None, force=False, fresh=True):
    """
    Logs a user in. You should pass the actual user object to this. If the
    user's `is_active` property is ``False``, they will not be logged in
    unless `force` is ``True``.

    This will return ``True`` if the log in attempt succeeds, and ``False`` if
    it fails (i.e. because the user is inactive).

    :param user: The user object to log in.
    :type user: object
    :param remember: Whether to remember the user after their session expires.
        Defaults to ``False``.
    :type remember: bool
    :param duration: The amount of time before the remember cookie expires. If
        ``None`` the value set in the settings is used. Defaults to ``None``.
    :type duration: :class:`datetime.timedelta`
    :param force: If the user is inactive, setting this to ``True`` will log
        them in regardless. Defaults to ``False``.
    :type force: bool
    :param fresh: setting this to ``False`` will log in the user with a session
        marked as not "fresh". Defaults to ``True``.
    :type fresh: bool
    """
    print("###USER",user)
    session["user_id"] = user[0]
    session["type"] = user[4]
    session["_fresh"] = fresh
    session["_id"] = get_session_identifier()
    print("IDENTIFIER##########",get_session_identifier())
    if remember:
        session["_remember"] = "set"
        if duration is not None:
            try:
                # equal to timedelta.total_seconds() but works with Python 2.6
                session["_remember_seconds"] = (
                    duration.microseconds
                    + (duration.seconds + duration.days * 24 * 3600) * 10**6
                ) / 10.0**6
            except AttributeError as e:
                raise Exception(
                    f"duration must be a datetime.timedelta, instead got: {duration}"
                ) from e
 
    return True