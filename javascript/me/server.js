const http = require('http')
const { readFileSync } = require('fs')

const homePage = readFileSync('../static/index.html')

const server = http.createServer((req, res) => {
    if (req.url = '/') {
        res.writeHead(200, { 'content-type': 'text/html' })
        res.write(homePage)
        res.end()
    }
    else {
        res.writeHead(404, { 'content-type': 'text/html' })
        res.write('<h1>404 - Not Found</h1>')
        res.end()
    }
})

server.listen(5000)
