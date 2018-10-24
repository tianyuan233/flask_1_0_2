from app import create_app

app = create_app()

if __name__ == '__main__':

    app.run(debug=app.config['DEBUG'],
            host=app.config['HOST'],
            port=app.config['PORT'],
            )

    # from app import setting
    # config = dict()
    # print(dir(setting))
    # for key in dir(setting):
    #         if key.isupper():
    #             config[key] = getattr(setting, key)

    # print(config)
#     testing = ConfigAttribute('TESTING')
#     print(testing)