box.cfg()

local user_space = box.schema.create_space(
    'user',
    {
        format={
            {name='login', type='string'},
            {name='password', type='string'},
            {name='name', type='string'},
            {name='surname', type='string'},
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
