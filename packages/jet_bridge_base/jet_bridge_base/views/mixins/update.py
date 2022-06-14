from jet_bridge_base.configuration import configuration
from jet_bridge_base.responses.json import JSONResponse
from jet_bridge_base.utils.track import track_database_async


class UpdateAPIViewMixin(object):

    def update(self, request, *args, **kwargs):
        track_database_async(request)

        partial = kwargs.pop('partial', False)
        instance = self.get_object(request)
        serializer = self.get_serializer(request, instance=instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(request, serializer)
        return JSONResponse(serializer.representation_data)

    def put(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def patch(self, *args, **kwargs):
        self.update(partial=True, *args, **kwargs)

    def perform_update(self, request, serializer):
        configuration.on_model_pre_update(request.path_kwargs['model'], serializer.instance)
        instance = serializer.save()
        configuration.on_model_post_update(request.path_kwargs['model'], instance)

    def partial_update(self, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(*args, **kwargs)
