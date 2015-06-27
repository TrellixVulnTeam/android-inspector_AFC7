# coding=utf-8

from model import Operation


class OperationsManager(object):
    def __init__(self, definitions_database, repositories_manager):
        self.definitions_database = definitions_database
        self.repositories_manager = repositories_manager

    def get_operations_info(self, data_type, data_source, device_info):
        """
        :param data_type: string
        :param data_source: DataSource
        :param device_info: DeviceInfo
        :rtype : set(OperationInfo)
        """
        if not self.definitions_database.exists_data_type(data_type):
            raise ValueError("'{0}' is not a defined DataType.".format(data_type))

        if not self.definitions_database.exists_data_source_type(data_source.type_):
            raise ValueError("'{0}' of the specified DataSource is not a defined DataSourceType."
                             .format(data_source.type_))

        if not self.definitions_database.has_all_required_param_values(data_source):
            raise ValueError("DataSource with type '{0}' must specify all its corresponding parameters."
                             .format(data_source.type_))

        return self.definitions_database.query_operations_info(data_type, data_source, device_info)

    def get_operation(self, id_):
        """
        :param id_: UUID
        :rtype : Operation
        """
        info = self.definitions_database.get_operation_exec_info(id_)

        extractor = self.repositories_manager.get_extractor(info['extractor_id'])
        inspector = self.repositories_manager.get_inspector(info['inspector_id'])
        param_values = info['param_values']

        return Operation(extractor, inspector, param_values)