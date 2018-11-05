## *Basics about MQTT* 

### MQTT is called MQ Telemetry Transport. 
Earlier it was called as Message Queuing Telemetry Transport. But as there is no option queue in the MQTT protocol. So we now refer it as MQ Telemetry Transport. This is useful for connections with remote locations where a small code footprint is required and/or network bandwidth is at a premium.

MQTT is a lightweight protocol to publish or subscribe messaging between to machines. It follows M2M(machine to machine) communication. 

MQTT is becoming one of the main protocols for IOT (internet of things) deployments in a couple of years. This is a protocol based on the TV and Radio broadcasting techniques in which we don't know if anybody or client actually listening to the broadcast. 


### MQTT Versions 
    1) MQTT-> It has various released versions, for example, MQTT v3.1 and MQTT v5. This kind of version used for TCP/IP networks.
    2) MQTT-SN -> This version is not much popular. It specified around 2013. It is designed to work over UDP, ZigBee supported transport.
       If you have some network which uses Zigbee standard then you can use this protocol.

### MQTT Clients
    There are lots of MQTT clients available for different languages such as Java,  Python, JAVAscripts but our focus will be Python. We have  Eclipse Paho MQTT Python client library for MQTT client and server communication.
    *Paho MQTT Python client library* If you want to know how to install this library or documentation of this library then please visit 
    https://pypi.org/project/paho-mqtt/

### MQTT Broker or Server
    Earlier it was called a broker, but now most people refer it as Server. You will see people referring both the terminology. If you want to use MQTT Broker or server then you can easily find it. There are many free hosted brokers like [Mosquitto]https://mosquitto.org/. You can also have commercial one like HiveMQ[https://www.hivemq.com/].
    I will suggest going for Mosquitto as it is easy and freely available.
       
       
