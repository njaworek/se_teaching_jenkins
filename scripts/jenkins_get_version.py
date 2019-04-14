import jenkins

server = jenkins.Jenkins('http://localhost:8080',
                         username='admin',
                         password='a4ef7fcb464f4694acdbcaa4ac97cc79')  # place password here


user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

plugins = server.get_plugins_info()
print plugins
