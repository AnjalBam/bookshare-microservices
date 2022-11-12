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
            target: "http://auth:5000",
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