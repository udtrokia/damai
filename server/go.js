
const Koa  = require('koa')
const log = require('koa-logger')
let app = new Koa()
app.use(log())
app.listen(3000)

app.use(async ctx=>(
    console.log(ctx.request.headers)
))
