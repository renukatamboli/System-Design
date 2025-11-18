class ConsistentHashing:
    def __init__(self, nodes=None, replicas=3):
        """Initialize the consistent hashing ring.

        Args:
            nodes (list): Initial list of nodes to add to the ring.
            replicas (int): Number of virtual nodes (replicas) for each node.
        """
        self.replicas = replicas
        self.ring = {}
        self.sorted_keys = []
        self.nodes = set()

        if nodes:
            for node in nodes:
                self.add_node(node)

    def _hash(self, key):
        """Hash a key using a simple hash function.

        Args:
            key (str): The key to hash.

        Returns:
            int: The hash value of the key.
        """
        return hash(key) % (2**32)  # Simple hash function for demonstration purposes.
    

    def add_node(self, node):
        """Add a node to the hash ring.

        Args:
            node (str): The node to add.
        """
        self.nodes.add(node)
        for i in range(self.replicas):
            replica_key = f"{node}:{i}"
            hash_value = self._hash(replica_key)
            self.ring[hash_value] = node
            self.sorted_keys.append(hash_value)
        self.sorted_keys.sort()

    def remove_node(self, node):
        """Remove a node from the hash ring.

        Args:
            node (str): The node to remove.
        """
        self.nodes.discard(node)
        for i in range(self.replicas):
            replica_key = f"{node}:{i}"
            hash_value = self._hash(replica_key)
            del self.ring[hash_value]
            self.sorted_keys.remove(hash_value)
        self.sorted_keys.sort()

    def get_node(self, key):
        """Get the node responsible for the given key.

        Args:
            key (str): The key to look up.
        Returns:
            str: The node responsible for the key.
        """
        if not self.ring:
            return None

        hash_value = self._hash(key)
        for node_hash in self.sorted_keys:
            if hash_value <= node_hash:
                return self.ring[node_hash]
        return self.ring[self.sorted_keys[0]]  # Wrap around to the first node
    

# Example usage:
if __name__ == "__main__":
    nodes = ["node1", "node2", "node3"]
    ch = ConsistentHashing(nodes)

    print("Node for key 'my_key':", ch.get_node("my_key"))

    ch.add_node("node4")
    print("Node for key 'my_key' after adding node4:", ch.get_node("my_key"))

    ch.remove_node("node2")
    print("Node for key 'my_key' after removing node2:", ch.get_node("my_key"))
