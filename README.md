# 📘 Linked List Implementations in Python

This repository provides a theoretical overview of fundamental types of Linked Lists in Data Structures: Singly, Doubly, and Circular Linked Lists. Each type is explained in terms of its structure, operations, and practical use cases.

## What is a Linked List?
A Linked List is a linear data structure where each element (node) is connected using pointers. Unlike arrays, linked lists do not store elements in contiguous memory locations. They provide efficient insertion and deletion operations.

Each node typically contains:
- **Data:** The value stored in the node.
- **Pointer(s):** Reference(s) to the next and/or previous node.

# Linked Lists Overview

## 🔹 Singly Linked List

### Structure
Each node has:
- `data`: stores the value  
- `next`: points to the next node in the list  
- The last node’s `next` is `None`.

### Characteristics
- Unidirectional traversal (from head to end)  
- Efficient insertion and deletion at the beginning  
- Inefficient for backward traversal  

### Use Cases
- Implementing stacks, queues  
- Simple dynamic memory allocation  

---

## 🔹 Doubly Linked List

### Structure
Each node has:
- `data`: stores the value  
- `prev`: points to the previous node  
- `next`: points to the next node  

### Characteristics
- Bidirectional traversal (forward and backward)  
- Extra memory required for the `prev` pointer  
- More flexible than singly linked list for operations like delete and insert  

### Use Cases
- Navigation systems (forward/backward history)  
- Implementing complex data structures like Deques  

---

## 🔹 Circular Linked List

### Structure
- Similar to singly or doubly linked lists  
- The last node points back to the first node, forming a circle  

### Characteristics
- No `None` at the end; traversal can be infinite if not handled carefully  
- Can be singly or doubly circular  
- Useful in round-robin scheduling  

### Use Cases
- CPU task scheduling (Round-robin)  
- Multiplayer games (player turns)  
- Buffering systems  
