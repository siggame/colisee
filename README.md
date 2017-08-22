# siggame/colisee

## Table Of Contents
- [Description](#description)
- [Services](#services)
  - [Colisee](#colisee-services)
  - [Other](#other-services)
- Docker On R99

## Description

## Services
### Colisee Services
|Service|Description|Issues|CI|
|---|---|---|---|
|[siggame/colisee-db](https://github.com/siggame/colisee-db)|Database to hold any persistent data needed for Arena & Web operation.|[![Open Issues](https://img.shields.io/github/issues-raw/siggame/colisee-db.svg?style=flat-square)](http://github.com/siggame/colisee-db)|[![Travis](https://img.shields.io/travis/siggame/colisee-db.svg?style=flat-square)](https://travis-ci.org/siggame/colisee-db)|
|[siggame/colisee-builder](https://github.com/siggame/colisee-builder)|Service which builds given source code into a docker image.|[![Open Issues](https://img.shields.io/github/issues-raw/siggame/colisee-builder.svg?style=flat-square)](http://github.com/siggame/colisee-builder)|[![Travis](https://img.shields.io/travis/siggame/colisee-builder.svg?style=flat-square)](https://travis-ci.org/siggame/colisee-builder)|
|[siggame/colisee-matchmaker](https://github.com/siggame/colisee-matchmaker)|Service which schedules random games to play.|[![Open Issues](https://img.shields.io/github/issues-raw/siggame/colisee-matchmaker.svg?style=flat-square)](http://github.com/siggame/colisee-matchmaker)|[![Travis](https://img.shields.io/travis/siggame/colisee-matchmaker.svg?style=flat-square)](https://travis-ci.org/siggame/colisee-matchmaker)|
|[siggame/colisee-tournament](https://github.com/siggame/colisee-tournament)|Service which schedules game in a tournament fashion.|[![Open Issues](https://img.shields.io/github/issues-raw/siggame/colisee-tournament.svg?style=flat-square)](http://github.com/siggame/colisee-tournament)|[![Travis](https://img.shields.io/travis/siggame/colisee-tournament.svg?style=flat-square)](https://travis-ci.org/siggame/colisee-tournament)|
|[siggame/colisee-runner](https://github.com/siggame/colisee-runner)|Service which dequeues scheduled games off the database and plays them.|[![Open Issues](https://img.shields.io/github/issues-raw/siggame/colisee-runner.svg?style=flat-square)](http://github.com/siggame/colisee-runner)|[![Travis](https://img.shields.io/travis/siggame/colisee-runner.svg?style=flat-square)](https://travis-ci.org/siggame/colisee-runner)|
|[siggame/colisee-visapi](https://github.com/siggame/colisee-visapi)|Service that provides endpoints to interact with the SIG-Game visualizer.|[![Open Issues](https://img.shields.io/github/issues-raw/siggame/colisee-visapi.svg?style=flat-square)](http://github.com/siggame/colisee-visapi)|[![Travis](https://img.shields.io/travis/siggame/colisee-visapi.svg?style=flat-square)](https://travis-ci.org/siggame/colisee-visapi)|

### Other Services
|Service|Description|CI|
|---|---|---|
|[siggame/registre](https://github.com/siggame/registre)|Simple web application that records registration data in a simple CSV format.|[![Travis](https://img.shields.io/travis/siggame/colisee-registre.svg?style=flat-square)](https://travis-ci.org/siggame/registre)|
|[siggame/tourneyjs](https://github.com/siggame/tourneyjs)|JavaScript utility that abstracts tournament algorithms into their own generic code base.|[![Travis](https://img.shields.io/travis/siggame/tourneyjs.svg?style=flat-square)](https://travis-ci.org/siggame/tourneyjs)|
|[siggame/discordbot](https://github.com/siggame/discordbot)|Discord Bot that aids in SIG-Game Discord operations.||

