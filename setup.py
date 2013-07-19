from setuptools import setup


install_requires = ('requests', 'boto')

setup(
    name='heroku-s3-pgbackups',
    licence='BSD',
    version='0.1',
    url='http://github.com/incuna/heroku-s3-pgbackups',
    scripts=['pg_export_backup'],
    install_requires=install_requires,
    description='Backs up heroku Pgbackups to external S3',
    long_description='Usage: python pg_export_backup. You will need pgbackups installed on your app, and you probably want to set this up to run on Heroku scheduler.',
    author='Incuna Ltd',
    author_email='admin@incuna.com',
)
