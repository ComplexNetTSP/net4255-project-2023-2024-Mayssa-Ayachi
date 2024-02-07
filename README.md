# Answer to challenge number 8:

In Kubernetes, a NodePort Service and a ClusterIP Service are both mechanisms to expose applications.
* ClusterIP is accessible only within the Kubernetes cluster. It assigns a unique IP address to the service within the cluster and hence it exposes the set of pods in a service to other objects in the cluster.
* NodePort allows access to the service from outside the cluster by opening a specific port on every node, so it exposes the service on each node's IP address at a static port.
