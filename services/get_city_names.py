def city_names(conn):
    try:
        conn.execute(
            """
            select name from city
            where name like 'S%'
            """
            
        ) 
        rows = conn.fetchall()
        return rows   
    except Exception as e :
        print(f'unable to  execute query {e}')
        return None