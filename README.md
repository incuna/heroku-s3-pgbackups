# Heroku S3 PgBackups

Gives permanence to your pgbackups but pushing them to an external S3 bucket.

## Sorry, what was the problem?

Heroku postgres comes with an additional addon called pgbackups, which is
great. Unforuntately if you delete the app, then the backups vanish as well.
This simple script is designed to be called

## Usage

`python pg_export_backup`. You will need pgbackups installed on your app, and
you probably want to set this up to run on Heroku scheduler.

## Configuration

All configuration values are taken from the environment.

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_STORAGE_BUCKET_NAME`

All of these variables can be superceeded by prepending `PGBACKUPS_` - that is
if you wish to use a different bucket to the default you may be using elsewhere
in the application you can set `PGBACKUPS_AWS_STORAGE_BUCKET_NAME`.

- `PGBACKUPS_PREFIX` - Backups will be uploaded to a name in the bucket of the
  form `PGBACKUPS_PREFIX-timestamp.dump`.

Note that the location of the current backup will be taken from
`PGBACKUPS_URL`.

## Dependencies

Requires requests and boto.

## Caveats

The database dump will be uploaded with the timestamp. If you wish to expire
some backups, move them to glacier or anything else then that is up to you. At
present it doesn't stream, so if your dump is too big to fit in memory it will
fail.
