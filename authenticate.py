token_file = 'auth/token'

def get_token():
    with open(token_file, 'r') as tf:
        token = tf.read()
    return token