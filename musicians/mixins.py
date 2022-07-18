class SwitchMethodMixin:
    def get_serializer_class(self, *args, **kwargs) -> None:
        return self.serializer_map.get(self.request.method, self.serializer_class)