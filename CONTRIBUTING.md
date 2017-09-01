# Contributing

Normally, ACM SIG-Game devs will be doing the majority of the contributing, but we love contributions from the open source community. Feel free to submit pull requests and the project maintainer will take a look at it as soon as they can.

## Table Of Contents
- [General](#general)
- [Git](#git)
- [JavaScript](#javascript)
- [TypeScript](#typescript)

## General
- Prefer Unix line endings over Windows line endings
- Prefer 4 space indents
- New repos should be connected with Travis CI
- New service/API repos should be connected to DockerHub

## GitHub
- Prefer Markdown files over wiki
- GitHub projects should be taken advantage of.
- The following issue labels should adhere to the following:
  - Severity
    - `severity/normal` -  This issue should be prioritized over others.
    - `severity/high` - This issue needs to be worked NOW.
    - Note: If no severity given, low priority
  - Issue Type
    - `type/development` - New code needs to be written
    - `type/housekeeping` - The project/documentation needs to be updated
    - `type/discussion` - Issue thread for discussing the project, (includes feature requests)
    - `type/bug` - Old code needs to be fixed

## Git
- Prefer branching over forking if a member of ACM SIG-Game
- Prefer adding individually over `git commit -A`
- `develop` branch might contain failing code that the team is working towards a stable state.
- `master` branch should have all tests passing
- `stable` should be after master can confidently be used in production
- personal development branches should be used to "save your work" to the cloud without writing to master
- personal development branches follow the pattern `personal/INITIALS/DESCRIPTION`. For example `personal/rfs/dbfix`
- only major version changes should be tagged
 
## JavaScript
- Prefer lambdas `()=>{}` over scoped anonymous functions `function(){}`
- Prefer callbacks over synchronous execution
- Prefer promises over callbacks
- Prefer brackets on same line as control structure `if(foo) {` over seperate line `if(foo)\n{`
- Prefer libraries with large numbers of downloads. Don't choose a package with <200k downloads/month

## TypeScript
- Prefer async/await over promises
- Prefer `strict` compiler setting
