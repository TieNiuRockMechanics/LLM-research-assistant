from __future__ import annotations

import os
import tempfile


_original_mkdtemp = tempfile.mkdtemp


def _sandbox_safe_mkdtemp(suffix=None, prefix=None, dir=None):
    """Create pip temp dirs with an inheritable ACL in the Codex Windows sandbox."""
    if suffix is None:
        suffix = ""
    if prefix is None:
        prefix = tempfile.gettempprefix()
    if dir is None:
        dir = tempfile.gettempdir()

    names = tempfile._get_candidate_names()
    for _ in range(tempfile.TMP_MAX):
        name = next(names)
        path = os.path.abspath(os.path.join(dir, prefix + name + suffix))
        try:
            os.mkdir(path, 0o777)
        except FileExistsError:
            continue
        return path
    raise FileExistsError("No usable temporary directory name found")


tempfile.mkdtemp = _sandbox_safe_mkdtemp
