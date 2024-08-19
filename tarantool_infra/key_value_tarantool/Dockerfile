FROM tarantool/tarantool AS builder

COPY ./init.lua /opt/tarantool

CMD ["tarantool", "/opt/tarantool/init.lua"]
