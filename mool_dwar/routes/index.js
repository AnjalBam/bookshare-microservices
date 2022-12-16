const STORE_HOST = process.env.STORE_HOST
const STORE_PORT = process.env.STORE_PORT

const AUTH_HOST = process.env.AUTH_HOST
const AUTH_PORT = process.env.AUTH_PORT


const ROUTES = [
    {
        url: '/test_server',
        auth: false,
        proxy: {
            target: "http://test_server:4001",
            changeOrigin: true,
            pathRewrite: {
                [`^/test_server`]: '',
            },
        }
    },
    {
        url: '/auth',
        auth: false,
        proxy: {
            target: `http://${AUTH_HOST}:${AUTH_PORT}`,
            changeOrigin: true,
            pathRewrite: {
                [`^/auth`]: '',
            },
        }
    },
    {
        url: '/store',
        auth: false,
        proxy: {
            target: `http://${STORE_HOST}:${STORE_PORT}`,
            changeOrigin: true,
            pathRewrite: {
                [`^/auth`]: '',
            },
        }
    },
    {
        url: '/premium',
        proxy: {
            target: "https://www.google.com",
            changeOrigin: true,
            pathRewrite: {
                [`^/premium`]: '',
            },
        }
    }
]

exports.ROUTES = ROUTES;