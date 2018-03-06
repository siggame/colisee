# Docker Compose Deployment

## Architecture Notes

### Runner

- Communicates with a "locked down" docker in docker container
  - Joueur clients run in this DinD container
  - Joueur clients can only communicate with the game server
- Communicates with Cerveau (game server)
- Communicates with database
- It is important to reduce the network reach of runner, runtime (DinD), and the game server
- Writes to filesystem

### Builder

- Communicates with a DinD container
- Communicates with a docker registry (image repo)
- Communicates with a database
- Writes to filesystem

### API

- Communicates with a database (to retrieve game logs for visualizer)
- Reads from filesystem

### Other Services

- Should not be on networks which allow external communication (no need)
- Should not write to disk

## Deploying to Production

- Copy the [.env.template](.env.template) to `.env` in the `deploy` directory
- Update the fields in the `.env` file to their appropriate values:
  - Appropriate values will depend on the deployment, but most of them should be obvious
  - Values which refer to hostnames should not collide with the corresponding service name;
    they need to be unique in order to avoid issues with name resolution.
    - (ie. `GAME_SERVER_HOST != game_server`)
- From the root directory run `./deploy/prepare.sh`
- Verify the generated files:
  - Check `docker-compose.yml`
  - Check each environment file in [deploy/envs](../deploy/envs)
    - Ignore env files with `.template` extension
  - If any values need to be changed or added do so now
- From the root directory run `./deploy/up.sh`
- Verify services started correctly by examing logs with `docker-compose logs -f`
- When it is necessary to take down colisee, from the root directory run `./deploy/down.sh`
  - **NOTE**: this may leave things in a weird state, but should be safe; it may be wise to spin things down individually until active services reach an idle state
