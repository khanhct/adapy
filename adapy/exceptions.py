class InvalidKeyFile(Exception):
    ''' Raised when the key file format is invalid '''
    pass

class InvalidPermissionFormat(Exception):
    ''' Raised when the permission format is invalid'''
    pass

class ADAKeyError(Exception):
    ''' Raised when there is an ADAKey error '''
    pass

class ADAMsigInvalidProposal(Exception):
    ''' Raised when an invalid proposal is queried'''
    pass

class ADABufferInvalidType(Exception):
    ''' Raised when trying to encode/decode an invalid type '''
    pass

class ADAInvalidSchema(Exception):
    ''' Raised when trying to process a schema '''
    pass

class ADAUnknownObj(Exception):
    ''' Raised when an object is not found in the ABI '''
    pass

class ADAAbiProcessingError(Exception):
    ''' Raised when the abi action cannot be processed '''
    pass

class ADASetSameCode(Exception):
    ''' Raised when the code would not change on a set'''
    pass

class ADASetSameAbi(Exception):
    ''' Raised when the abi would not change on a set'''
    pass