from dishka import Provider, Scope, provide

from core.settings import CommonSettings, DevSettings, ProdSettings


class DevSettingsProvider(Provider):
    @provide(scope=Scope.APP)
    def create_dev_settings(self) -> CommonSettings:
        return DevSettings(
            database_settings=DatabaseSettings(), jwt_settings=JWTSettings()
        )


class ProdSettingsProvider(Provider):
    @provide(scope=Scope.APP)
    def create_prod_settings(self) -> CommonSettings:
        return ProdSettings(
            database_settings=DatabaseSettings(), jwt_settings=JWTSettings()
        )
