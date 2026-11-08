# AIMS - Use Case Diagram

## Actors

- Customer: Browses DVDs, searches for DVDs, and manages a shopping cart.
- Admin: Manages DVD information and orders.

## Use Cases

```mermaid
flowchart LR
    Customer([Customer])
    Admin([Admin])

    subgraph AIMS["AIMS"]
        Browse((Browse DVDs))
        Search((Search DVDs by title))
        View((View DVD details))
        Add((Add DVD to cart))
        Remove((Remove DVD from cart))
        Cart((View cart))
        Checkout((Checkout))
        ManageDVD((Manage DVDs))
        ManageOrder((Manage orders))
    end

    Customer --> Browse
    Customer --> Search
    Customer --> View
    Customer --> Add
    Customer --> Remove
    Customer --> Cart
    Customer --> Checkout

    Admin --> ManageDVD
    Admin --> ManageOrder