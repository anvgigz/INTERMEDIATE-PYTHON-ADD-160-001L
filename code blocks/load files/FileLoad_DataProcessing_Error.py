class FileLoadError(Exception):
    def __init__(self, message, filepath=None, original_exception=None):
        super().__init__(message)
        self.filepath = filepath
        self.__cause__ = original_exception

    def log(self):
        print(f"FileLoadError: {self.args[0]}")
        if self.filepath:
            print(f"Attempted path: {self.filepath}")
        if self.__cause__:
            print(f"Original exception: {self.__cause__}")

class DataProcessingError(Exception):
    def __init__(self, message, step=None, original_exception=None):
        super().__init__(message)
        self.step = step
        self.__cause__ = original_exception
        self.__context__ = original_exception.__context__ if original_exception else None

    def log(self):
        print(f"\nHandling DataProcessingError: {self.args[0]} (Step: {self.step})")
        if self.__cause__:
            print(f"Cause of the error: {self.__cause__}")
        if self.__context__:
            print(f"Context of the error: {self.__context__}")