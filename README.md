# Azure Live Streaming

## Live Streaming of Data Through Edge Gateways Using Azure

### Introduction
Edge computing, a technology that processes data close to its origin, offers benefits like reduced latency, improved security, and increased bandwidth efficiency. This report explores the use of edge gateways for real-time data streaming from edge devices to the cloud via Azure IoT Hub.

### Edge Computing
Edge computing is a distributed computing model that processes and analyzes data at the edge of the network, rather than transmitting it to a central cloud. This approach offers several advantages, including reduced latency, improved security, and increased bandwidth efficiency.

### Edge Gateways
An edge gateway is a device or software that bridges edge devices and the cloud. It collects and filters data, translates data between different protocols, and provides security for data at the edge.

### Azure IoT Hub
Azure IoT Hub is a cloud-based service that enables secure and scalable communication between IoT devices and the cloud. It provides features like device-to-cloud and cloud-to-device messaging, device management, and security for IoT solutions.

### System Architecture
The system architecture for this project includes:
1. Edge devices: The source of the data that will be streamed to the cloud.
2. Edge gateway: Collects data from the edge devices, filters the data, and sends it to the cloud.
3. Azure IoT Hub: Receives data from the edge gateway and stores it in the cloud.
4. Azure Stream Analytics: Analyzes real-time data from Azure IoT Hub.
5. Azure Power BI: Visualizes data from Azure Stream Analytics.

### Implementation
The project was implemented through the following steps:
1. Set up an Azure IoT Hub.
2. Set up an edge gateway on a Linux virtual machine.
3. Connect the edge gateway to Azure IoT Hub.
4. Deploy a temperature sensor module to the edge gateway.
5. Stream data from the temperature sensor to Azure IoT Hub.


