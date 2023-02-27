from urllib.parse import urljoin, urlparse
from typing import Any

from flask import redirect, request, url_for

from werkzeug.wrappers import Response


def is_safe_url(target: str) -> bool:
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def redirect_back(default: str = 'kitchen_recipes.index', **kwargs: Any) -> Response:
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if target.endswith('users/login_register'):
            return redirect(url_for(default))
        if is_safe_url(target):
            return redirect(target)

    return redirect(url_for(default, **kwargs))
