const crypto = require('crypto')
const client = require('../db/redis')
const salt = crypto.randomBytes(16).toString('hex')
const keyLength = 512
const iterations = 10000
const digest = 'sha512'
const encoding = 'hex'

const routeAuthMiddleware = async (req, res, next) => {
    const hash = crypto
        .pbkdf2Sync(String(new Date()), salt, iterations, keyLength, digest)
        .toString(encoding)
    const key = hash.slice(0, 10)
    const value = hash.slice(-10)
    try {
        await client.set(key, value, { EX: 3 })
        req.headers['x-request-auth-header'] = key
    } catch (err) {
        return res.status(500).send({
            message: 'Internal Server Error',
            detail: 'Error setting request auth headers',
        })
    }

    next()
}

module.exports = {
    routeAuthMiddleware,
}
