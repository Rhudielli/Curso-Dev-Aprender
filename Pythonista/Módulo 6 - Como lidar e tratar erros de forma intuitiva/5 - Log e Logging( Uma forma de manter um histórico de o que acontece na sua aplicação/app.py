import logging

# Tipos de Logging
    # debug = Só estou informando informações para desenvolvedores
    # info = Só quero informar algo que está acontecendo no programa, mas que não é um erro Ex: Usuario fez login
    # warning = Quero alertar sobre algo que está acontecendo, possivelmente fora do esperado, porém ainda não é um erro, mas pode gerar um futuramente
    # error = Um erro ocorreu na aplicação
    # critical = Um erro com consequencias graves acaba de ocorrer na aplicação

logging.debug('Logging nivel critical')
logging.info('Logging nivel critical')
logging.warning('Logging nivel critical')
logging.error('Logging nivel critical')
logging.critical('Logging nivel critical')