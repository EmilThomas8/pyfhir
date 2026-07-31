class ResourceRegistry:

    _resources = {}

    @classmethod
    def register(cls, resource):

        cls._resources[
            resource.resource_type
        ] = resource

    @classmethod
    def get(cls, name):

        return cls._resources.get(name)