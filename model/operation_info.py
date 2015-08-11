# coding=utf-8


class DataType(object):
    def __init__(self, namespace, name):
        self.namespace = namespace
        self.name = name

    def __repr__(self):
        return '{0}:{1}'.format(self.namespace, self.name)

    def __eq__(self, other):
        return self.namespace == other.namespace and self.name == other.name


class DataSource(object):
    def __init__(self, namespace, type_, info):
        self.namespace = namespace
        self.type_ = type_
        self.info = info

    def __repr__(self):
        return '{0}:{1}:{2}'.format(self.namespace, self.type_, self.info)

    def __eq__(self, other):
        return self.namespace == other.namespace and self.type_ == other.type_ and self.info == other.info


class OperationInfo(object):
    def __init__(self, id_, data_type, data_source, supported_device_models, supported_os_versions):
        self.id_ = id_
        self.data_type = data_type
        self.data_source = data_source
        self.supported_device_models = supported_device_models
        self.supported_os_versions = supported_os_versions

    def __repr__(self):
        return '{{\n' \
               '\tid: {0}\n' \
               '\tdata_type: {1}\n' \
               '\tdata_source: {2}\n' \
               '\tsupported_device_models: {3}\n' \
               '\tsupported_os_models: {4}\n' \
               '}}\n' \
            .format(self.id_, self.data_type, self.data_source, self.supported_device_models,
                    self.supported_os_versions)

    def __eq__(self, other):
        return self.id_ == other.id_ \
               and self.data_type == other.data_type \
               and self.data_source.__eq__(other.data_source) \
               and self.supported_device_models == other.supported_device_models \
               and self.supported_os_versions == other.supported_os_versions


class DeviceInfo(object):
    def __init__(self, os_version, device_model):
        self.os_version = os_version
        self.device_model = device_model
