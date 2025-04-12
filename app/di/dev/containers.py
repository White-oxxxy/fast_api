from functools import lru_cache

from dishka import AsyncContainer, Container, make_container, make_async_container

from .providers.settings import DevSettingsProvider, ProdSettingsProvider


@lru_cache(1)
def get_settings_container() -> Container:
    return make_container(
        DevSettingsProvider(),
        ProdSettingsProvider(),
    )
