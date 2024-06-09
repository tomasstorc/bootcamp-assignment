# Bootcamp Assignment

## High-Level Overview

You will create an externally accessible VM with managed identity and an internally accessible Key Vault and PostgreSQL database. The Key Vault and database should have internally resolvable domain names. To test the functionality of the deployed solution, you will create a secret in the Key Vault using a Python script provided in this repository. You will connect to the database with a client of your choice using your Entra ID account.

## Resources Deployment

### Task 1 - Resource Group (RG)

- Create a resource group.
- The location is up to you.

### Task 2 - Virtual Network (VNET)

- In the created resource group, create a virtual network with two subnets, each subnet should have 30 assignable IP addresses.
- Use an address space with the minimum needed IP addresses.
- One subnet should be delegated to the PostgreSQL flexible server.

### Task 3 - Virtual Machine (VM)

- Create a Windows virtual machine.
- Choose a SKU with 2 vCPUs and 4GB RAM.
- The VM should have a private IP as well as a public IP.
- Enable system-assigned managed identity for the VM.
- No redundancy required.

### Task 4 - DNS

- Create two private DNS zones.
- One zone for the Key Vault and a second zone for the PostgreSQL flexible server.
- Link the zones to your created VNET.

### Task 5 - Key Vault

- Create a Key Vault with Premium SKU.
- No public access is allowed, only private.
- RBAC-based access to keys, secrets, and certificates.

### Task 6 - PostgreSQL Flexible Server

- Create a PostgreSQL flexible server.
- No public access, only private.
- Storage size should be 32GB.
- Entra ID auth only, assign your user account as admin.

### Task 7 - Network Security Group (NSG)

- Create a network security group so that only the RDP port is accessible from the internet. Any other inbound connection to the subnet with the VM and Key Vault should be disabled.
- There is no need for an NSG for the subnet with PostgreSQL as it is accessible only from the private network.

### Task 8 - RBAC

- The VM's managed identity should be able to create secrets in the created Key Vault.

### Task 9 - Secret Creation

- In this repository, download `main.py` and `requirements.txt`.
- Connect to the created VM and copy the downloaded files.
- Install Python.
- Set the following environment variables:
  - `KV_URI` - URI of the Key Vault, the domain name should be resolved to a private IP address.
  - `SECRET_VALUE` - value of the secret, can be whatever you want.
- In the directory where the files are copied, run:

```
pip install -r requirements.txt
python main.py
```

- after that secret should be created

### Task 10 - Connect to database

- Connect to created VM and download software of your choice to connect to PostgreSQL server
- use your Entra ID account

## Requirements

### Connectivity

- Only VM is accessible from the internet, other resources are accessible from private network via domain name

### Deployment

- IaC should be used for resources creation, choice of tool is up to you (Terraform, Crossplane,...)
- Use tags for better organization
- State file should be in remote location (if using IaC with state file)
- Solution should be stored in GIT repository

### Secrets

- You will need to provide passwords for VM and database, do not store them in GIT
- GitOps based deployment may need some secret as well, again, do not store it as plain text

### Costs

- With respect to the requirements try to use SKU which will minimize costs.

## Bonus tasks

### Task 1 - Configure VM Insights

- Enable VM Insights for created Virtual machine

### Task 2 - GitOps-based deployment of IaC solution

- Solution should apply IaC changes whenever there is some kind of event in GIT repository related to the code
