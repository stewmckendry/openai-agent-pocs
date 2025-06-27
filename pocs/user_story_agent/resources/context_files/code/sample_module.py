"""Simplified login module used by the postal portal."""

from hashlib import sha256


def existing_login(username: str, password: str) -> bool:
    """Validate the user's credentials.

    Parameters
    ----------
    username: str
        Email address associated with the account.
    password: str
        Raw password provided by the user.

    Returns
    -------
    bool
        ``True`` if the credentials match an active account, ``False`` otherwise.
    """

    # In production we would query the database for the stored password hash.
    stored_hash = "2bb80d537b1da3e38bd30361aa855686bde0"  # truncated example
    incoming = sha256(password.encode()).hexdigest()

    return incoming == stored_hash
