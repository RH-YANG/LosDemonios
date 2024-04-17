from model.schemas.domain_schema import Golem



def check_duplicate(cur, item, value):
    query = '''
        SELECT ''' + item + '''
          FROM golem 
         WHERE ''' + item + ''' = %s
    '''
    cur.execute(query, (value,))
    data = cur.fetchone()
    if data:
        is_available = False
    else:
        is_available = True
    
    return is_available
    


def insert(cur, g: Golem):
    query = '''
        INSERT 
          INTO golem (
               email
             , pwd
             , nickname
            )
        VALUES (%s, %s, %s)
    '''
    cur.execute(query, (
                    g.email
                  , g.pwd
                  , g.nickname
    ))
    return cur.rowcount



def current_seq(cur):
    query = '''
        SELECT currval('seq_golem')
    '''
    cur.execute(query)
    data = cur.fetchone()
    if data:
        return data[0]
    else:
        return None    
