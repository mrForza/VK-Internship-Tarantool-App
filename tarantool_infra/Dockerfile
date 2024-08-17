FROM tarantool/tarantool AS builder

COPY ./app.lua /opt/tarantool

CMD ["tarantool", "/opt/tarantool/app.lua"]
