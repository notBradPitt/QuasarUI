from .pysssss import init

if init(check_imports=["onnxruntime"]):
    from .wd14tagger import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
    __all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
