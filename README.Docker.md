# Using amirdm2mqtt in Docker.

If you want to run this under Docker you can do so. A Dockerfile has been provided so you can build your own container.

## Building

Building should be a simple matter:

    docker build -t amirdm2mqtt .

## Configuration

All configuration for the docker container is handled through environment variables. You can pass these to `docker run` using the -e flag. At a minimum you need to set `WATCHED_METERS`.


| Environment Variable | Default | Required | Description |
| -------------------- | ------- | -------- | ----------- |
| WATCHED_METERS | | Yes | A comma or space separated list of meter ids to watch |
| WH_MULTIPLIER | 1000 | No | multiplier to get reading to Watt Hours (Wh) |
| READINGS_PER_HOUR | 12 | No | number of IDM intervals per hour reported by the meter |
| MQTT_HOST | `127.0.0.1` | No | MQTT host to report to |
| MQTT_PORT | `1883' | No | MQTT port to use |
| MQTT_USER | | No | MQTT username for authentication |
| MQTT_PASSWORD | | No | MQTT password for authentication |


## Running

In order to run your container will need to be both privileged and have a volume mount to `/dev/bus/usb`. You can do that by adding these arguments to `docker run`:

    --privileged -v /dev/bus/usb:/dev/bus/usb

You may also need to give it access to the network for your mqtt server. If you have not yet set one up you can do so with these commands:

    docker network create --attachable mqtt
    docker network connect mqtt <mosquitto_container>

A comman `docker run` command incorporating the above advice along with a common configuration is provided as an example:

    docker run -it --name amridm2mqtt \
        --restart=unless-stopped \
        --network=mqtt \
        --privileged \
        -v /dev/bus/usb:/dev/bus/usb \
        -e WATCHED_METERS=12345678 \
        -e READINGS_PER_HOUR=4 \
        -e MQTT_HOST=mosquitto \
        amridm2mqtt
