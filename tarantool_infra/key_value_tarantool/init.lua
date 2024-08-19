box.cfg()

local user_space = box.schema.create_space(
    'key_value_store',
    {
        format={
            {name='key', type='string'},
            {name='value', type='*'},
        },
        if_not_exists=true
    }
    
)

user_space:create_index(
    'primary',
    {
        parts={1, 'string'},
        if_not_exists=true
    }
)