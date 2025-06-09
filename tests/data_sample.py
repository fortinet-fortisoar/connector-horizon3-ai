"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

config = {
    "verify_ssl": True,
    "api_token": "add api token here",
    "server_url": "https://api.horizon3ai.com/"
}
invalid_config = {
    "api_token": "invalid-token",
    "server_url": "https://api.horizon3ai.com",
    "verify_ssl": True
}

connector_info = {
    "connector_name": "horizon-ai",
    "connector_version": "1.0.0"
}
