# NateQK

<p align="center">
  <a href="https://github.com/RaidyQK/NateQK/actions/workflows/runner.yml">
    <img src="https://github.com/RaidyQK/NateQK/actions/workflows/runner.yml/badge.svg" alt="🔗 GHA">
  </a>
</p>


## Roadmap to 1.0 release

A few **need** to be completed things before 1.0 release
> [!NOTE]
> as this is a discord bot, we will only use a major.minor release cycle, any bug fixes will be pushed
> to the same minor version, any breaking changes or massive changes will update the major version.
> we will have a webpage with the latest version on it and maybe a few other details in json form
> This will be important as it will allow us to tell the user when their bot is out of date

> [!NOTE]
> Unless we get paid to do so, we will not maintain old versions of the bot
> We will use renovate to provide security updates though

- [ ] Full suite of commands
  - [x] Purge
  - [x] Ping
  - [ ] Ban
  - [ ] Unban
  - [ ] Kick
  - [ ] Channel Lock(Locks a channel so that only users with a certain role or above a certain role can talk in it)
  - [ ] Channel Un-Lock
  - [ ] Warn(Warn's a user adding a warning tick to the user in the db)
  - [ ] [Backup command](#backup-command)
- [ ] Database Backups
  I have no idea how hard this will be, because I don't work with nosql


## Backup command
This will take a backup of the datbase, and all other relevent data and store it in a .tar.gz
archive, there will be a max amount of allowed backups, and it will delete the oldest ones first.
The backups will be stored in this format *{month-day-year--time_version}.tar.gz*
