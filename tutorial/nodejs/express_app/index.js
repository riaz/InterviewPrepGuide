const express = require('express')
const app = express()

const port = 8080

app.get('/', (req, res) => {
    res.send('Hello World')
});

app.get('/riaz', (req, res) => {
    res.send('Hello World, riaz')
});

app.listen(port, () => {
    console.log(`server is running in the port ${port}`)
})
