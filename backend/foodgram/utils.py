def get_list_allowed(allowed: str) -> list:
    return [host.strip() for host in allowed.split(',') if host.strip()]