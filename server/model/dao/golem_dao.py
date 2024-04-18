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



def select_by_email(cur, g: Golem):
    query = '''
        SELECT gol_seq
             , email
             , pwd
             , nickname
          FROM golem 
         WHERE email = %s
    '''
    cur.execute(query, (g.email,))
    data = cur.fetchone()

    result = None
    if data:
        result = Golem(gol_seq=data[0]
                , email=data[1]
                , pwd=data[2]
                , nickname=data[3])   
    
    return result



def update_refresh(cur, g: Golem):
    query = '''
        UPDATE golem 
           SET token = %s 
         WHERE gol_seq = %s
    '''
    cur.execute(query, (g.token, g.gol_seq))

    return cur.rowcount



def update(cur, g: Golem):
    query = '''
        UPDATE golem 
           SET profile_img = %s
             , gender = %s
         WHERE gol_seq = %s
    '''
    cur.execute(query, (g.profile_img
                      , g.gender
                      , g.gol_seq))

    return cur.rowcount 