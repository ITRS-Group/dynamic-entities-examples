# Dynamic Entity Mapping - examples


This repository contains two examples of how to setup the new Dynamic Entities Mapping in Geneos Gateway configuration.

[Dynamic Entities](https://docs.itrsgroup.com/docs/geneos/current/Gateway_Reference_Guide/dynamic_entities.htm) feature provides the ability to dynamically create Geneos data structures (entity, attribute, sampler, dataview, etc) based on dimensional data from the [Collection Agent](https://docs.itrsgroup.com/docs/geneos/current/Netprobe/introduction/netprobe-overview.html#collection-agent) and its [plugins](https://docs.itrsgroup.com/docs/geneos/current/Netprobe/introduction/netprobe-overview.html#Collection_Agent_plug-ins). This greately reduces the configuration burden and enables Geneos to be more dynamic when monitoring applications in automated and orchestrated environments like Kubernetes and Open Shift.

### Try using MiniGeneos

This is by far the simplest way to get up and runnign quickly. MiniGeneos provides averything you need in a container that you can run in your desktop / laptop. An example python application is used to demonstrate how to instrument an application to send metrics to Geneos and dynamically create entities as applications are deployed. MiniGeneos uses the "basic_mapping.xml" mapping configuration.

1. See [MiniGeneos](https://docs.itrsgroup.com/docs/geneos/current/MiniGeneos/MiniGeneos.html) for how to install
2. [Run an example](https://docs.itrsgroup.com/docs/geneos/current/Netprobe/orchestrated-environments/prerequisites/deploy-strategy.htm#Run_an_example_..159) to understand the mapping and Dynamic Entities functionality

### Try in your Kubernetes or Open Shift environment:
1. See [Installation in an Orchestrated Environment](https://docs.itrsgroup.com/docs/geneos/current/Netprobe/orchestrated-environments/install/install-orchestrated.htm) for how to install Netprobe and Collection Agent in Kubernetes or Open Shift environment.
2. Apply the example "kubernetes_mapping.xml" Gateway include file to your Gateway.
3. You should see Kubernetes metrics in your Active Console.
