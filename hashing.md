# Hashing: A Deep Dive

## 1. Introduction to Hashing
Hashing is a **technique used for mapping data to a fixed-size value** (called a hash code or hash value) using a **hash function**. It is widely used in data structures, cryptography, and databases.

## 2. Why Use Hashing?
- **Efficient Data Retrieval**: Hash tables allow O(1) average time complexity for lookup, insertion, and deletion.
- **Data Integrity**: Cryptographic hash functions help ensure data integrity.
- **Efficient Searching**: Hash-based indexing in databases improves search performance.
- **Load Balancing**: Hashing distributes requests across multiple servers in distributed systems.

## 3. Hash Functions
A **hash function** takes an input (key) and produces a fixed-size output (hash value).

### Properties of a Good Hash Function:
1. **Deterministic**: Same input should always produce the same hash.
2. **Uniform Distribution**: Should minimize collisions by evenly distributing values.
3. **Fast Computation**: Should be efficient in time complexity.
4. **Minimize Collisions**: Should generate unique values as much as possible.

### Common Hash Functions:
- **Modulo Hashing**: `hash(key) = key % table_size`
- **Multiplicative Hashing**: Uses fractional multiplications to distribute keys.
- **Cryptographic Hashing**: SHA-256, MD5 (for security purposes).

## 4. Hash Collisions & Resolution Techniques
Collisions occur when multiple keys map to the same hash index.

### Collision Resolution Methods:
#### 1. **Chaining (Separate Chaining)**
Each index in the hash table maintains a linked list (or other data structures) to store multiple values.
- **Pros**: Simple, handles dynamic key insertion.
- **Cons**: May degrade to O(n) if many collisions occur.

#### 2. **Open Addressing**
Instead of using a separate list, it finds another slot in the table.
- **Linear Probing**: Finds the next available slot sequentially.
- **Quadratic Probing**: Uses a quadratic function to find the next slot.
- **Double Hashing**: Uses another hash function to find an alternative location.

## 5. Hashing in Data Structures
### 1. **Hash Table**
A data structure that stores key-value pairs for quick retrieval.
- **Example**: Python’s dictionary (`dict`), Java’s `HashMap`.

### 2. **Hash Set**
A set implementation using hashing for O(1) lookup time.
- **Example**: Python’s `set`, Java’s `HashSet`.

## 6. Cryptographic Hashing
Used in security applications like password hashing, digital signatures, and data integrity verification.

### Key Cryptographic Hash Functions:
- **MD5** (128-bit, weak security)
- **SHA-1** (160-bit, deprecated due to vulnerabilities)
- **SHA-256** (256-bit, strong security)
- **Bcrypt/Argon2** (for password hashing)

### Properties of Cryptographic Hashes:
1. **Pre-image Resistance**: Hard to find the original input from the hash.
2. **Collision Resistance**: Hard to find two inputs producing the same hash.
3. **Avalanche Effect**: Small changes in input drastically change the hash.

## 7. Hashing Applications
- **Database Indexing**: Hash indexes improve query performance.
- **Password Storage**: Secure password hashing prevents leaks.
- **Blockchain & Digital Signatures**: Cryptographic hashes secure transactions.
- **Load Balancing**: Consistent hashing distributes requests efficiently.
- **Caching (LRU Cache)**: Hashing improves lookup speed in caches.

## 8. Python Implementation


## 9. Comparison of Hashing vs Other Searching Methods
| Method          | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity |
|----------------|--------------------------|-------------------------|------------------|
| Hash Table    | O(1)                       | O(n)                    | O(n)             |
| Binary Search | O(log n)                   | O(log n)                 | O(1)             |
| Linear Search | O(n)                        | O(n)                    | O(1)             |

## 10. Summary
| Feature          | Hashing |
|-----------------|-----------|
| **Time Complexity (Average)** | `O(1)` |
| **Collision Handling** | Chaining, Open Addressing |
| **Cryptographic Security?** | ✅ Yes |
| **Applications** | Indexing, Security, Caching, Load Balancing |

