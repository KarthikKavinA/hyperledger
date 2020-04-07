#################################################     *ALL TOPICS*     ##################################################
### Blockchain and its Features ###
	* Decentralized --- Replication of ledger across the n/w participants in a blockchain network.
	* Collaboration --- Replication of ledger with, each of whom collaborate in its maintenance.
	* Systems of Proof --- "Immutability" of transactions in ledger makes it simple to determine the provenance of information
	* Applications --- By means of "Smart Contracts" which has a business logic.
	* Consensus --- Process of keeping the ledger transactions synchronized across the network (Achieved by - updating same transaction in same order.)
	* Shared --- A blockchain system has shared programs (smart contracts) to update shared ledgers but in today’s systems, where a participant’s private programs are used to update their private ledgers



### Hyperledger Fabric ###
	* Open source enterprise-grade permissioned distributed ledger technology (DLT) platform.
	* Established under the Linux Foundation (Open Governance).
	* Has a highly modular and configurable architecture.
	* First DLT to support smart contracts authored in general-purpose programming languages such as Java, Go and Node.js.
	* Support for pluggable consensus protocols that enable the platform to be more effectively customized to fit particular use cases and trust models.
	* Can leverage consensus protocols that do not require a native cryptocurrency to incent costly mining or to fuel smart contract execution.
	* Enables confidentiality through its channel architecture and private data feature.




### Modular Components in Fabric ###
	* Pluggable Ordering Service
		--- Establishes consensus on the order of transactions and then broadcasts blocks to peers.
	* Pluggable Membership Service Provider
		--- Is responsible for associating entities in the network with cryptographic identities.
	* Optional Peer-To-Peer Gossip Service
		--- Disseminates the blocks output by ordering service to other peers.
	* Smart Contracts
		--- Run within a container environment (e.g. Docker) for isolation and can be written in standard programming langs
	* Ledger
		--- Can be configured to support a variety of DBMSs.
	* Pluggable Endorsement and Validation Policy Enforcement
		--- Can be independently configured per application.



### New Approach in Fabric ###
	* Replacing order-execute fashion with *Execute-Order-Validate* model.
	* Execute a transaction and check its correctness, thereby endorsing it,
	* Order transactions via a (pluggable) consensus protocol, and
	* Validate transactions against an application-specific endorsement policy (one policy for one chaincode)before committing them to the ledger.
	* First phase (1st point) also eliminates any non-determinism, as inconsistent results can be filtered out before ordering




### Performance of Fabric ###
	* Performance of a blockchain platform can be affected by many variables such as transaction size, block size, network size, as well as limits of the hardware, etc.
	* The latest scaled Fabric to 20,000 transactions per second.



### Choosing Pluggable Consensus Protocol ###
	* When deployed within a single enterprise, or operated by a trusted authority,
		--- crash fault-tolerant (CFT) consensus protocol might be more than adequate
	* In a multi-party, decentralized use case,
		--- a more traditional byzantine fault tolerant (BFT) consensus protocol might be required.




### Application-Specific Endorsement Policy ###
### For Transaction Endorsement ###
	* Associated with *Every Chaincode* is an *Endorsement Policy* (one) that applies to *all of the smart contracts* defined within it.(not to be confused with Chaincode Definition Endorsement (LifecycleEndorsement Policy))
	* Specifies which peer nodes, or how many of them, belonging to different channel members need to *execute and validate* a transaction against a given smart contract in order for the transaction to be considered *valid*.
	* Hence, the endorsement policies define the organizations (through their peers) who must “endorse” (i.e., approve of) the execution of a proposal.
	* Each transaction need only be executed (endorsed) by the subset of the peer nodes necessary to satisfy the transaction’s endorsement policy (one policy for a one chaincode which applies to all smart contracts defined within it) before they will be accepted by other organizations(committing peer’s) onto their copy of the ledger.
	* Fabric lifecycle allows you to change an endorsement policy or private data collection configuration without having to repackage or reinstall the chaincode.
	* Smart Contracts inside the chaincode can then be executed by channel members, subject to the endorsement policy specified in the *Chaincode Definition*.



	* The *Endorsement Policy* is the *default endorsement policy*.
	* One Endorsement policy is specified for a *chaincode (smart contracts - imp.)* when it is approved and committed to the channel using the *Fabric chaincode lifecycle*.
	* *One Endorsement Policy* covers all of the *state* associated with a chaincode.
	* Endorsement policy can be specified either by reference to an endorsement policy defined in the channel configuration or by explicitly specifying a Signature policy.
	* If an endorsement policy is not explicitly specified during the approval step, the default Endorsement policy "MAJORITY Endorsement" is used which means that a majority of the peers belonging to the different channel members (organizations) need to execute and validate a transaction against the chaincode in order for the transaction to be considered valid.
	* This default policy allows organizations that join the channel to become automatically added to the chaincode policy.
	* If you don’t want to use the default endorsement policy, use the Signature policy format to specify a more complex endorsement policy. (It also allow you to include *principals*)
	* Principals are described as ‘MSP.ROLE’, where MSP represents the required MSP ID (the organization), and ROLE represents one of the four accepted roles: Member, Admin, Client, and Peer.
	* Some examples of valid principals are:
		* ‘Org0.Admin’: an administrator of the Org0 MSP


	# State-Based Endorsement Policy #
	* There are cases where it may be necessary for a Particular State (a particular key-value pair, in other words) to have a different endorsement policy.
	* For this, state-based endorsement allows the default chaincode-level endorsement policies to be overridden by a different policy for the specified keys.





### Chaincode Endorsement Policies ###
### For Chaincode Package Endorsement ###
	* The *LifecycleEndorsement Policy* governs who needs to approve a *chaincode definition*. (for chaincodes package)




### Distributed Ledger ###
	* Distributed Ledger is used to encapsulate the **Shared Information** in a network.
	* Is a combination of the two components, world state *Database* and the transaction log *History*.
	* Single ledger can have one or more smart contracts.
	* Legder physically hosted on Peer, but logically hosted on the channel.
	* 1)World State Database
		* Describes the state of the ledger at a given point in time.
		* It’s the database of the ledger.
		* The world state database could be a relational data store, or a graph store, or a temporal database.
		* A database that holds *current values* of a *set of ledger states*.
		* Ledger states are, by default, expressed as key-value pairs with the Version Number.
		* Note that Version Number is for Every State in a ledger.
		* The version number is for internal use by Hyperledger Fabric, and is incremented every time the state changes.
		* The version is checked whenever the state is updated to make sure the current states matches the version at the time of endorsement.
		* This ensures that the world state is changing as expected; that there has not been a concurrent update.
		* World State can be re-generated from the blockchain at any time.
		* LevelDB is the default and is particularly appropriate when ledger states are simple key-value pairs.
		* CouchDB is a particularly appropriate choice when ledger states are structured as JSON documents because CouchDB supports the rich queries and update of richer data types often found in business transactions.
		* Implementation-wise, CouchDB runs in a separate operating system process, but there is still a 1:1 relation between a peer node and a CouchDB instance, unlike LevelDB runs in a same operating system process.
		* All of this is invisible to a smart contract.
		* World states are in a *Namespace* so that only smart contracts within the same chaincode can access a given namespace.
	* 2)Transaction Log History
		* Blockchain is always implemented as a File.
		* Immutably records all transactions which have resulted in the current value of the world state.
		* Sequenced, tamper-resistant record of all state transitions in the fabric.
		* It’s the update history for the world state.
		* Transaction Log History (Blockchain) determines the *World State* of the Ledger.
		* Blockchain has recorded *every previous version of each ledger state* and how it has been changed.
		* Blockchain is structured as sequential log of interlinked blocks, where each block contains a sequence of transactions, each transaction representing a query or update to the world state.
		* Each block’s header includes a hash of the block’s transactions (each hash for every transaction in a current block only), as well a hash of the prior block’s header.
		* Genesis Block is the starting point for the ledger, though it does not contain any User Transactions.
		* Genesis Block contains a Configuration Transaction containing the initial state of the network channel.
		* A blockchain is not namespaced beacause,It contains transactions from many different smart contract namespaces.
	* Each participant has a copy of the ledger to every Hyperledger Fabric network they belong to.
	* Described as decentralized because it is replicated across many network participants, each of whom collaborate in its maintenance.
	* Ledgers *cannot fork* the way they do in many other distributed and permissionless blockchain networks here fabric uses Deterministic Consensus Algorithm in an Ordering Service.





### Blocks ###
	* Blocks consists of three sections:
		1) Block Header:
			* This section comprises three fields, written when a block is created.
				1) Block number: An integer starting at 0 (the genesis block), and increased by 1 for very new block appended to the blockchain.
				2) Current Block Hash:         The hash of all the transactions contained in the current block.
				3) Previous Block Header Hash: The hash from the previous block header.

		2) Block Data:
			* This section contains a list of transactions arranged in order (sequentially).
			* All transactions have an identifier (like t3,t4), a proposal (input & signature), and a response (output & endorsement) signed by a set of organizations.
			* Every Transaction consists of the following fields:
				1) Header: A metadata about transaction (for eg, name of the relevant chaincode, and its version).
				2) Signature: Contains a cryptographic signature, created by the client application. It requires the application’s private key to generate it. (Tamper-Resistant Check)
				3) Proposal: Encodes the input parameters supplied by an application to the smart contract which creates the proposed ledger update. When the smart contract runs, this proposal provides a set of input parameters,which, in combination with the current world state, determines the new world state.
				4) Response: Captures the before and after values of the world state, as a Read Write set(RW-set). It’s the output of a smart contract, and if the transaction is successfully validated, it will be applied to the ledger to update the world state.
				5) Endorsements: This is a list of signed transaction responses from each required organization sufficient to satisfy the endorsement policy (one policy for one chaincode). whereas only one transaction response is included in the transaction, there are multiple endorsements.
		3) Block Metadata:
			* This section contains the certificate and signature of the Block Creator which is used to verify the block by network nodes.
			* Subsequently, the block committer adds a Valid/Invalid Indicator for every transaction into a bitmap that also resides in the block metadata, as well as a hash of the cumulative state updates up until and including that block, in order to detect a state fork.
			* Unlike the block data and header fields, this section is not an Input to the *Block Hash Computation*.





### 3-Phase Process of UPDATE QUERY TRANSACTION WORKFLOW ###
### entire transaction workflow process is called consensus ###
	* Specifically, applications that want to update the ledger are involved in a 3-phase process, which ensures that all the peers in a blockchain network keep their ledgers consistent with each other.

	* Phase 1: --- Proposal
		* Applications generates transaction proposal which they send to each of the required set of peers (as per the *One Endorsement Policy* defined for a One Chaincode) for endorsement.
		* Each of these endorsing peers then independently executes a chaincode using the transaction proposal (consists of set of input parameters which is used in combination with its program logic to read and write the ledger) to generate a transaction proposal response (Changes to the world state are captured as a transaction proposal response, which contains a read-write set with both the states that have been read, and the new states that are to be written if the transaction is valid) which is endorsed by adding Digital Signature.
		* It does not apply this update to the ledger, but rather simply signs the entire payload using its private key and returns it to the application.
		* Once the application has received a sufficient number of signed proposal responses, the first phase of the transaction flow is complete.
		* An application can simply request a more up-to-date proposal response when the peer return inconsistent transaction responses for the same transaction proposal.

	* Phase 2: --- Ordering and Packaging transactions into Blocks
		* Orderer receives transactions containing endorsed transaction proposal responses from many applications, and orders (sequencing) the transactions and packaging them into blocks,ready for distribution to the peers.

	* Phase 3: --- Validation and Commit
		* It involves the distribution and subsequent validation of blocks from the orderer to the peers, where they can be committed to the ledger.
		* When a new block is generated, all of the peers connected to the orderer will be sent a copy of the new block.
		* Upon receipt of a block, a peer will process each transaction in the sequence in which it appears in the block.
		* For every transaction, each peer will verify that the transaction has been endorsed by the required organizations according to the *Endorsement Policy* of the single chaincode which generated the transaction.
		* This process of validation verifies that all relevant organizations have generated the same outcome or result.
		* If a transaction has been endorsed correctly, the peer will attempt to apply it to the ledger.
		* To do above step, a peer must perform a *Ledger Consistency Check* to verify that the *Current Value of the world state* matches the *Read Set of the transaction* when it was signed by the endorsing peer nodes (OR) current state of the ledger is compatible with the state of the ledger when the proposed update was generated.
		* This may not always be possible, even when the transaction has been fully endorsed.
		* Failed transactions (in consistency check) after fully endorsed, are not applied to the ledger, but they are retained for audit purposes, as are successful transactions.
		* Invalidated (Failed) transactions are still retained in the immutable block created by the orderer, but they are marked as invalid by the peer and do not update the ledger’s state.
		* If either validation or consistency check phase of transaction is failed, then the transaction is marked as *Invalid*.
		* Finally, every time a block is committed to a peer’s ledger after consistency check with ledger is successfull, that peer generates an appropriate event.
	* Events
		1) *Block Events* include the full block content.
		2) Block *Transaction Events* include summary information only, such as whether each transaction in the block has been validated or invalidated.
		3) *Chaincode Events* that the chaincode execution has produced can also be published at this time.



### Features of Fabric Ledger ###
	* Query and update ledger using key-based lookups, range queries, and composite key queries.
	* Read-only queries using a rich query language (if using CouchDB as state database).
	* Read-only history queries — Query ledger history for a key, enabling data provenance scenarios.



### Transactions ###
	* Consist of the versions of keys/values that were read in chaincode (read set) and keys/values that were written in chaincode (write set).
	* Contain signatures of every endorsing peer and are submitted to ordering service.
	* Are ordered into blocks and are “delivered” from an ordering service to peers on a channel.





### Peer ###
	* Peers can be created, started, stopped, reconfigured, and even deleted.
	* Every peer node in a channel is a *Committing Peer*.
	* To actually be an *Endorsing Peer*, the smart contract on the peer must be used by a client application to generate a digitally signed transaction response.
	* When an organization has multiple peers in a channel, a *Leader Peer* is a node which takes responsibility for distributing blocks of transactions from the orderer to the other committing peers in the organization.
	* If a peer in one organization needs to communicate with a peer in another organization, then it can use one of the *Anchor Peers* defined in the channel configuration for that organization.
	* Anchor peer can help with many different cross-organization communication scenarios.
	* A peer can be a committing peer, endorsing peer, leader peer and anchor peer all at the same time!
	* Only the anchor peer is optional.
	* For all practical purposes, there will always be a leader peer and at least one endorsing peer and at least one committing peer.
	* Peers provide the control point for access to, and management of, channels.
	* Each peer node (belongs to one org.)in a channel uses the copy of Channel Configuration to determine the operations that respective organizations` client applications can perform.
	* Each peer maintains a copy of the channel configuration for each channel of which they are a member.
	* Once Peer is started, it can join channel using the *Orderer* by raising the join request to orderer.
	* Each peer maintains a copy of the ledger for each channel of which they are a member.
	* Single peer actually hosts one or more *Instances* of the Ledger.
	* Peer can install one or more smart contracts (Instances) for a single ledger.
	* Peers also have special *System Chaincodes*.
	* Peers and orderers can communicate with each other using channel.
	* Each and every peer in the network is assigned a digital certificate by an administrator from its owning organization.
	* Peer can only run a smart contract and further can take part in the process of transaction endorsement if it is installed on it, but it can know about the interface of a smart contract by being connected to a channel.
	* Validate transactions by verifying the transaction signatures against endorsement policies and enforce the policies.
	* Prior to appending a block (commit to ledger) after validating the transactions, a versioning check is performed to ensure that states for assets that were read have not changed since chaincode execution time. (protection against the double spend).
	* At each of the committing peers, distributed transactions from orderers are recorded, whether valid or invalid, and their local copy of the ledger updated appropriately.
	* It’s not really important where the peer is physically located — it could reside in the cloud, or in a data centre owned by one of the organizations, or on a local machine — it’s the *digital certificate associated with it* that identifies it as being owned by a particular organization.
	* For Example, P3 could be hosted in Org1’s data center, but as long as the digital certificate associated with it is issued by CA2, then it’s owned by Org2.
	* If a peer happens to be down at the time of block distribution by the orderer, or joins the channel later, it will receive the blocks after reconnecting to an ordering service node, or by gossiping with another peer.
	* Peers and Applications do not need to know who the leader node is at any particular time (only ordering nodes know).



### Smart Contracts ###
	* Business logic of a blockchain application.
	* Functions as a trusted distributed application.
	* Smart Contracts is used to encapsulate the **Shared Processes** in a network.
	* A smart contract defines the rules between different organizations in executable code.
	* At the heart of a smart contract is a set of *Transaction* definitions.
	* Smart Contract defines the transaction logic that controls the *Lifecycle of a Business Object* contained in the world state.
	* Smart contracts primarily *Put, Get and Delete States* in the world state, and can also query the immutable blockchain record of transactions.
	* Are used to generate transactions.
	* More no. of related smart contracts are packaged into a *Chaincode*.
	* Every chaincode has an One Endorsement Policy that applies to all of the smart contracts defined within it. --- For Transaction Endorsement
	* Think of smart contracts as governing transactions, whereas chaincode governs how smart contracts are packaged for deployment.
	* *Chaincode Package* must have been installed on *Peers* by an administrator of the (respective peer) organization, and then defined on a *Channel*.
	* Channel Members can only execute a smart contract after the chaincode has been *defined* on a channel.
 	* Smart Contracts inside the chaincode can then be executed by channel members, subject to the endorsement policy specified in the *Chaincode Definition*.
	* Installing a smart contract shows how we think of it being *Physically Hosted* on a peer, whereas a smart contract that has been defined on a channel shows how we consider it *Logically Hosted* by the channel.
	* State transitions are a result of chaincode invocations, recorded as transactions.
	* X.509 certificates are used in smart contract (transaction responses) to digitally sign transactions.
	* Invoked by an application external to the blockchain when that application needs to interact with the ledger.
	* Chaincode interacts only with the database component of the ledger, the world state (querying it, for example), and not the transaction log.
	* World State is not updated when the smart contract is executed!
	* It is possible for a Single Smart Contract which accesses more ledger instaces in a peer (must be configured in this way)
	* Chaincode can also be used for low level system programming of Fabric.
	* Many smart contracts run concurrently in the network.
	* They may be deployed dynamically (in many cases by anyone)
	* Application code should be treated as untrusted, potentially even malicious.
	* When a chaincode is deployed, all smart contracts within it are made available to applications.
	* Smart Contract can call other smart contracts both within the same channel and across different channels. It this way, they can read and write world state data to which they would not otherwise have access due to smart contract namespaces.
	* In reality, each chaincode has its *Own World State* (of respective ledger--- check this) that is separate from all other chaincodes.
#	* Must be a only one chaincode defined for a channel. so that each chaincode for a channel has its own world state that is separate from all other chaincodes defined in different channels. suppose more chaincodes installed on a channel, it must need separate world state but it violating the one ledger per channel has one world state policy.
	* Traditionally, chaincodes are launched by the peer, and then connect back to the peer.
	* In modern approach, now possible to run *Chaincode As an External Service*, for example in a Kubernetes pod, which a peer can connect to and utilize for chaincode execution.
	* Single Chaincode has many related smart contracts. Each smart contract has many transactions in it. Each transacton in a smart contract controls the lifecyle of the business Objects in a world state.
	* Smart Contract can have the below three opreations:
		* A *Get* typically represents a *Query* to retrieve information about the current state of a business object.
		* A *Put* typically *Creates* a new business object or *Modifies* an existing one in the ledger world state.
		* A *Delete* typically represents the *Removal* of a business object from the current state of the ledger, but not its history.
	* System Chaincode:
		* Generally, chaincode can also define low-level program code which corresponds to *domain independent **System** interactions* leads to system chaincode, unrelated to these smart contracts  encode the *domain dependent rules* for business processes.
		* Different types of system chaincodes:
			1) _lifecycle --- runs in all peers and manages the installation of chaincode on your peers, the approval of chaincode definitions for your organization, and the committing of chaincode definitions to channels.
			2) Lifecycle system chaincode (LSCC) --- manages the chaincode lifecycle for the 1.x releases of Fabric.
			3) Configuration system chaincode (CSCC) ---  runs in all peers to handle changes to a channel configuration, such as a policy update.
			4) Query system chaincode (QSCC) --- runs in all peers to provide ledger APIs which include block query, transaction query etc.
			5) Endorsement system chaincode (ESCC) --- runs in endorsing peers to cryptographically sign a transaction response.
			6) Validation system chaincode (VSCC) --- validates a transaction, including checking endorsement policy and read-write set versioning.
		* It is possible for low level Fabric developers and administrators to modify these system chaincodes for their own uses.



### Orderers ###
	* Orderers, service as a *Network Administration Point* for the fabric network.
	* When orderers receives join request from peers, it uses the *Policy* in the *Channel Configuration* to determine Peer’s permissions on the requeted channel by using peer`s identity.
	* Orderer is initially configured and started by an administrators (of anyone org.) according to a *Network Configuration*.
	* Ordering service node (for eg,O4) is the actor that creates consortia(for eg,2) and channels.
	* Orderer(s) must be hosted by any one (or more) of the organization in a network as per *Network Configuration*.(2 points)
	* Also supports application channels, for the purposes of transaction ordering into blocks for distribution.
	* It can order transactions for one or more application channels.
	* Ordering service node (for eg,O4) has a copy of the network configuration, but in a *Multi-Node Configuration*, every ordering service node will have its own copy of the network configuration.
	* Ordering service node is the distribution point for transactions.
	* Ordering service node gathers endorsed transactions from applications and orders them into transaction blocks, which are subsequently distributed to every peer node in the channel.
	* Two Roles for Single Orderer:
		* At the channel level, orderer role is to gather transactions and distribute blocks inside channel according to the policies defined in channel configuration.
		* At the network level, orderer role is to provide a management point for network resources according to the policies defined in network configuration.
		* Notice again how these roles are defined by different policies within the channel and network configurations respectively.
	* Whether acting as a network management point, or as a distributor of blocks in a channel, its nodes(orderers) can be distributed as required throughout the multiple organizations in a network.
	* Ordering service nodes (multiple orderers) are connected via the *System Channel* which operates a Mini-Blockchain.
	* Orderers also enforce basic access control for channels, restricting who can read and write data to them, and who can configure them.
	* Ordering service nodes receive transactions from many different application clients concurrently.
	* Blocks created by the orderer are then saved to the orderer’s ledger & distributed to all peers that have in a channel.
	* Sequencing of transactions in a block is not necessarily the same as the *Order* received by the ordering service.
	* Importantly, ordering service puts the transactions into a *strict order*, and peers will use this order when validating and committing transactions.
	* In Raft, transactions (in the form of proposals or configuration updates) are automatically routed by the ordering node that receives the transaction to the current leader of that channel.
	* Only the Ordering Nodes need to know who the leader node is at any particular time (not by peers & applications).
	* When the orderer validation checks have been completed, the transactions are ordered, packaged into blocks, consented on, and distributed.


### Organization ###
	* Every organizations in a n/w has a preferred Certificate Authority.
	* Administrative rights of organization at a network level is decided by the *Network Configuration*.(creating consortia..)
	* When an organization has multiple peers in a channel, it can choose the peers upon which it installs smart contracts; it does not need to install a smart contract on every peer.
	* Approval of a chaincode definition occurs at the organization level.
	* A sufficient number of organizations (orgs administrator) need to approve a *Chaincode Definition*(not transactions generated by the smart contracts) (A majority, by default) before the chaincode definition can be committed to the channel and used to interact with the channel ledger. ----- *LIFECYCLE ENDORSEMENT POLICY*
	* Organization’s peers can have one or more leaders connected to the ordering service to improve resilience and scalability
	* An organization can have zero or more anchor peers defined for it.
	* Every organization has their own set of peers.
	* Every organization has client applications.
	* A new organization(suppose, if added in a channel) can use the chaincode as soon as they approve the chaincode parameters already agreed to by other members of the channel and then installs the chaincode package.
	* A newly added organization in a channel can approve the chaincode definition once and join multiple peers to the channel with the chaincode package installed.
	* If a newly added organization in a channel, wanted to change the chaincode definition, all members of a channel would need to approve a new definition for their organization, and then one of the organizations would need to commit the definition to the channel.
	* Different organizations may use different Root CAs, or the same Root CA with different Intermediate CAs.
	* Every organization participating in a channel must have an *Single MSP*( Both Node & Orderer Local MSP) defined for it.
	* An organization can also be divided into multiple Organizational Units (OU), each of which has a certain set of responsibilities, also referred to as *Affiliations*.
	* Specifying OUs is optional. If OUs are not used, all of the identities that are part of an MSP — as identified by the Root CA and Intermediate CA folders — will be considered members of the organization.
	* Organization Units (OUs) are defined in the Fabric CA client configuration file and can be associated with an identity when it is created.
	* In Fabric, NodeOUs provide a way to classify identities in a *digital certificate hierarchy*.
	* For Organization Policies, their canonical path is usually "/Channel/<Application|Orderer>/<OrgName>/<PolicyName>".
	* By joining multiple channels, an organization can participate in a so-called *network of networks*.


### Certificate Authority CA ###
	* Is used to dispense X.509 digital certificates which acts as a identities to the administrators, network nodes, etc...
	* Can also be used to sign transactions.
	* It has a built-in CA called *Fabric-CA*.
	* Fabric CA is a Private Root CA Provider capable of managing digital identities of Fabric participants that have the form of X.509 certificates.
	* Fabric CA is a custom CA *targeting the Root CA needs* of Fabric, it is *Inherently Not Capable of Providing SSL Certificates* for general/automatic use in browsers.
	* CA gives digital certificate to requesting user of respective organization by signing the certificate with CAs` *Private Key* so that requested user can be sure that it hasn’t been tampered by verifying with the *Public Key* of CA.
	* One or More CAs can be used to define the members of an organization’s from a digital perspective.
	* CAs come in two flavors: Root CAs and Intermediate CAs.
	* Intermediate CAs have their certificates issued by the Root CA or another intermediate authority, allowing the establishment of a “Chain Of Trust” for any certificate that is issued by any CA in the chain.
	* Chain Of Trust provides ability to track back to the Root CA not only allows the function of CAs to *Scale* while still providing *Security*.
	* when a User is registered with a Fabric CA, a *Role* of admin, peer, client, orderer, or member must be associated with the user.
	* When a CA issues X.509 certificates, the *OU field (Manufacturing,Distribution)* in the certificate *Specifies the Line of Business* to which the *identity belongs*.



### Applications ###
	* Applications can connect to both peers and orderers by using the channel with the help of SDK`s.
	* Single application of one organization can connect to one or more channels as per respective channel config in a network.
	* Organisations maintain the client applications.
	* X.509 certificates are used in client application (transaction proposals).
	* Client application will have an identity that associates it with an organization.
	* Client application can invoke smart contracts, Once the chaincode definition has been committed to the channel.
	* Client applications send transaction proposals (serves as input to the smart contract) to peers owned by an organization specified by the smart contract(chaincode) endorsement policy, which uses it to generate an endorsed transaction response, which is returned by the peer node to the client application. (process called as Smart Contract Invocation).
	* When Fabric SDK is used to *register* a user with the CA, *Node OU Roles(client,peer,orderer,admin) & OU Attributes* are assigned to an *registering identity* which gains a appropriate special role to the identity. (SPECIAL CASE SCENARIO)
	* It is recommended that when the user is registered with the CA, that the *admin role in Node OU* is used to designate the node administrator. Then, the identity is recognized as an *Admin of ORG* by the Node OU role value in their signcert(certificate). As a reminder, in order to leverage the admin role, the “identity classification” feature must be enabled in the config.yaml above by setting “Node OUs” to Enable: true.
	* Applications receive Events asynchronously when Smart Contract Invocation process is complete.
	* Applications can, however, connect to one or more peers to issue a query.
	* Applications can register for different events(block,transaction,chaincode) so that they can be notified when they occur.
	* Event notifications conclude the third and final phase of the transaction workflow.
	* An application program can invoke a smart contract which uses simple ledger APIs to *get, put and delete* ledger states.



### Channels ###
	* Application channels are used to provide a private communication mechanism between organizations in the consortium.
	* Channels provide an efficient sharing of infrastructure while maintaining data and communications privacy.
	* Only network administrators (organization(s)) as defined in network configuration policy, can able to create new channel.
	* Channels keep *Transactions* private from the broader network.
	* Channels can serve for one or more applications.
	* Channel must have atleast one orderer to order trasactions.
	* Any updates to network configuration after creation of channels will have no direct effect on channel configuration.
	* Participants on a Fabric network establish a sub-network where every member has visibility to a particular set of transactions.
	* Only those nodes that participate in a channel have access to the smart contract (chaincode) and data transacted, preserving the privacy and confidentiality of both.
	* Allowing a group of participants to create a separate ledger of transactions.
	* Data in a channel is completely isolated from the rest of the network, including other channels.
	* One Ledger per Channel.
	* Above point means a completely separate blockchain, and completely separate world states, including namespaces.
	* There can be multiple channels in a network.
	* Channel can have any number of organizations connected to it.
	* Channel’s ledger contains a configuration block defining policies, access control lists, and other pertinent information.
	* Contain Membership Service Provider instances allowing for crypto materials to be derived from different certificate authorities.
	* Every channel runs on a *separate* instance of the Raft protocol, which allows each instance to elect a different leader.
	* Channel creators (and channel admins) have the ability to pick a subset of the available orderers and to add or remove ordering nodes as needed (as long as only a single node is added or removed at a time).





### Private Data Collection ###
	* Collections keep *Data* private between subsets of organizations on the channel.
	* Is used to segregate the data in a private database, logically separate from the channel ledger, accessible only to the authorized subset of organizations.
	* It is a collection (like DB) between members on a channel, allowing much of the same protection as channels without the maintenance overhead of creating and maintaining a separate channel.




### To Transact on a Fabric Network, ###
	* To Transact on a Fabric Network, a member( or anyone ) needs to:
		1)Have an identity issued by a CA that is trusted by the network.
		2)Become a member of an *Organization* that is recognized and approved by the network members. The MSP is how the identity is linked to the membership of an organization. Membership is achieved by adding the member’s public key (also known as certificate, signing cert, or signcert) to the organization’s MSP.
		3)Add the MSP to either a *Consortium* on the network or a channel.
		4)Ensure the MSP is included in the *Policy Definitions* on the network.



### New Oranization(s) coming inside the Channel are *allowed* by viewing their Channel MSP.
### Channel MSP must *already* includes the MSP of a new organization to be joined in a channel.
### Above all detail must be included in a *Channel Configuration* of a channel or in a Consortium of network.
### So Channel Configuration has Channel MSP Details.

### Channel MSP defines *who* can come inside the channel but ***Channel Configuration Policy*** defines *what* operations can be done inside the channel who came through Channel MSP.




### Membership Service Provider MSP ###
	* For an identity to be *Verifiable* across the fabric network, it must come from a *Trusted Authority (MSP)*.
	* MSP is a component that defines the rules that govern the *Valid Identities* for every organization.
	* MSPs turn *Verifiable Identities* into the *Members* of a blockchain network.
	* Mapping of X.509 digital certificates to member organizations is achieved by via a structure called a (MSP).
	* Members of a Hyperledger Fabric network enroll through a trusted MSP.
	* Default MSP implementation in Hyperledger Fabric Network uses X.509 certificates as identities, adopting a traditional Public Key Infrastructure (PKI) hierarchical model.
	* PKI certificate authorities provides a list of identities, and an MSP says which of these are members of a given organization that participates in the network.
	* Implementation of the MSP requirement is a set of folders that are added to the configuration of the network.
	* MSP is used to define an organization both *Inwardly* (organizations decide who its admins are) and *Outwardly* (by allowing other organizations to validate that entities have the authority to do what they are attempting to do).
	* MSP identifies which Root CAs and Intermediate CAs are accepted to define the members of a trust domain by *Listing the Identities of their members*, or by identifying which CAs are authorized to issue valid identities for their members.
	* MSP defines Admin of the Organization, the Admin of the Node, and the Node itself should all have the same root of trust.
	* MSPs occur in Two Domains in a blockchain network:
		* Local MSP - Locally on an actor’s node
		* Channel MSP - In channel configuration




### Local MSP ###
	* Local MSP defines who has administrative or participatory rights at that level.
	* Local MSPs defines Permissions for clients and for nodes (peers and orderers).
	* Every Node and Every Orderer must have a Local MSP defined separately.
#	* Every Organization  have a Single MSP( includes both Node & Orderer Local MSP) to list the actors or nodes it trusts.
	1) Node Local MSP:
		* Define the permissions for a Node (who are the peer admins who can operate the node).
		* Node Local MSPs are represented as a *Folder Structure* on the *File System* (includes Node & User).
		* Physically and Logically, there is only one local MSP per node.
		* Peer Admins will not necessarily be Channel Admins, and vice versa.
		* The local MSPs of Clients (the account holders in the banking scenario above), allow the user to authenticate itself in its transactions as a member of a channel (e.g. in chaincode transactions), or as the owner of a specific role into the system such as an organization admin, for example, in configuration transactions.
		* This(Node Local MSP) allows for authenticating member messages *Outside the Context of a Channel* and to define the permissions over a particular node (who has the ability to install chaincode on a peer, for example).
	2) Orderer Local MSP:
		* Defined on the *File System* of the orderer node and only applies to that orderer node.
		* Physically and Logically, there is only one local MSP per node.



### Application Channel MSP ###
	* Channel MSPs contain the MSPs of the organizations of the *Channel Members* (including Orderer of channel).
	* Channel MSPs define administrative and participatory rights at the Channel Level.
	* Defines the *Relationship* between the identities of channel members (which themselves are MSPs) and the enforcement of channel level policies.
	* Channel MSPs identify who has *Authorities* at a channel level.
	* Channel MSPs are described in a *Channel Configuration*.
	* As channel MSPs are available to all nodes in the channel,they are *Logically defined Once* in the channel configuration.
	* Instantiated on the file system of every node in the channel and kept synchronized via consensus.
	* Peers and Ordering Nodes on an application channel share the *Same View* of channel MSPs.
	* While there is a copy of each channel MSP on the local file system of every node (of which they are a member), logically a channel MSP resides on and is maintained by the *Channel or the Network*.
	* If an organization wishes to join the channel, an MSP incorporating the chain of trust for the organization’s members would need to be included in the channel configuration.
	* Channel MSP configuration does not include *Keystore & Signcerts* folder(private & public key), because channel MSPs solely aim to offer Identity Validation Functionalities and not signing abilities.
	* Channel MSP includes the Revoked Certificates (This list is conceptually the same as a CA’s Certificate Revocation List (CRL), but it also relates to *revocation of membership* from the organization.)




### System Channel MSP ###
	* Includes the MSPs of all the organizations that *Participate* in an Ordering Service.


### Assets ###
	* Can be tangible (real estate and hardware)
	* Can also be intangible (contracts and intellectual property)
	* Assets can be modified using chaincode transactions.
	* Represented as a collection of key-value pairs.
	* With state changes recorded as transactions on a Channel ledger.
	* Can be represented in binary and/or JSON form.




### Ordering Service ###
	* Ordering Service will likely include *Ordering Nodes* from multiple organizaitons and *Collectively* these organizations run the ordering service, most importantly managing the *Consortium of Organizations* and the default policies that are inherited by the application channels.
	* Fabric’s design for ordering service relies on *Deterministic* consensus algorithms not a probablistic one (done in permissionless blockchains), any block validated by the peer is guaranteed to be final and correct.
	* Currently offering a CFT ordering service implementation based on the *etcd* library of the Raft protocol.
	* Network can have multiple ordering services (like CFT or BFT in same n/w) supporting different applications or application requirements. (Note this point: which is different from multiple orderer organizations having orderers like CFT1,CFT2,etc for a single ordering service like CFT for a single application requirements.)
	*Every channel runs on a separate instance of the Raft protocol, which allows each instance to elect a different leader among many ordering nodes in a single (application)channel.VERY IMPORTANT --- In Multiple ordering service cluster (each cluster for one application channel) While all Raft nodes (may be a leader ordering node or all in each application channel) must be part of the system channel, they do not necessarily have to be part of ***all*** application channels. Each application channels running a one single cluster of many ordering nodes electing a leader ordering node (may be raft node).



### Consortium ###
	* Consortium defines the *Set of Organizations* in the network who share a need to *Transact* with one another.
	* It really makes sense to group organizations together as a single consortium if they have a common goal,
	* Can have any number of organizational members.
	* Only network administrators (organization(s)) as defined in network configuration, can able to create new consortia.
	* While creating the consortium or the channel, the relevant administrators of channel set the policies that who is authorized to modify a configuration element in a channel.
	* Every consortium has a single channel for their organizational members in a consortium.
	* Consortium definition, by network administrator, is stored in the network configuration.



### Declarative Policies ###
	* How organizations manage network evolution.


### Chaincode Definition ###
	* It is a struct that contains the parameters that govern how a chaincode operates.
	* These parameters include the chaincode name, version, and the endorsement policy.
	* When a sufficient number of organizations (a majority by default) have approved to the same chaincode definition, then the definition can be committed to the channel --- "LifecycleEndorsement Policy" For Chaincode Definition Endorsement.
	* But, Endorsement policy define the organizations (through their peers) who must “endorse” (i.e., approve of) the execution of a proposal --- "Endorsement Policy" For Transaction Endorsement.
	* Smart Contracts inside the chaincode can then be executed by channel members, subject to the endorsement policy specified in the *Chaincode Definition*.
	* Committing the chaincode definition to the channel, places the endorsement policy on the channel ledger.



### Fabric Network Governance ###
	* Network is governed according to policy rules specified in *Network Configuration*.
	* Newtork can be controlled by one or more organizations.



### Network Configuration (policy) ###
	* Defines the configuration settings for the orderer.
	* Defines consortium definition.
	* N/W Config. policy can be considered more important than Orderers because, ultimately, it controls network access.
	* It gives administrative rights to organization.
	* It contains the policies that describe the starting set of administrative capabilities for the network.
	* It may change later due to addition or removal of the members of the fabric network.
	* List of Organizations (Consortium) is kept in the configuration of the “ordering system channel” that are allowed to create Channels.
	* If consortia definition is changed in n/w configuration, it will not affect the members of channel after creation of channels.
	* Policy which separates organizations that can manage resources at the network level.
	* Channel configurations remain completely separate from each other, and completely separate from the network configuration
	* Each node in the ordering service records each channel in the network configuration, so that there is a record of each channel created, at the network level.
	* Although ordering service node creates consortia and channels, the *Intelligence* of the network is contained in the *Network Configuration* that Ordering services(orderers) is obeying.



### Application Channel Governance ###
	* Channel is governed according to the *Policy Rules* specified in *Channel Configuration*.
	* Channel (channel configuration) can be controlled by one or more organizations (org`	s peers, must be member of the channel).
	* Channel configuration determines which & how many peers in channel can read and/or write information to channel ledger.
	* Administrating organization(s) has *No Rights* in channel configuration.
	* Administrating organization(s) cannot add itself to the *Channel*, must be authorized by channel members as per channel configuration.
	* Anchor peers for one org. in a channel are defined in the channel configuration for that organization(communicating org. or from org.).
	* Organization(s) who can manage resources at the channel level.
	* Number of transactions in a block depends on channel configuration parameters related to the desired size and maximum elapsed duration for a block (BatchSize and BatchTimeout parameters, to be exact).




### Modification Policy or mod_policy ###
	* Is a first class policy within a network or channel configuration that manages change.
	* The key point of understanding is that policy change in a network or channel configuration is managed by a policy (mod_policy) within the respective policy itself.
	* A uniquely powerful policy that allows network and channel administrators to manage policy change itself.
	* Mod_Policy defines a set of organizations that are allowed to change the mod_policy itself.
	* Organization(s) defined in the mod_policy inside n/w configuration policy is responsible for *Configuration Changes*
	* Mod_Policy can be configured in such a way that all organization defined in mod_policy would have to approve the change.
	* Note that separate mod_policy for both n/w & channel configuration policies within the policies respectively.




### (N/W & Channel) Configuration Transactions ###
	* Network Configuration Transaction:
		* To change a network configuration, a network administrator must submit a *Configuration Transaction* to change the network configuration.
		* It must be signed by the organizations identified in the *Mod_Policy* (with network configuration) as being responsible for network configuration change.
		* WKT, ordering service nodes (multiple orderers) are connected via the *System Channel*.
		* Using the system channel, ordering service nodes distribute *Network Configuration Transactions*.
		* These transactions are used to co-operatively maintain a consistent copy of the *Network Configuration at Each Ordering Service Node*.

	* Channel Configuration Transactions:
		* To change a channel configuration, a channel administrator must submit a *Configuration Transaction* to change the channel configuration.
		* It must be signed by the organizations identified in the *Mod_Policy* (with channel configuration) as being responsible for channel configuration change.
		* Channel configuration transactions are processed by the orderer, as it needs to know the current set of policies to execute its basic form of access control.
		* In a similar way, peer nodes in an *Application Channel* can distribute channel configuration transactions.
		* These transactions are used to maintain a consistent copy of the *Channel Configuration at Each Peer Node*.

	* Every configuration change results in a new configuration block transaction being generated.




### Policy ###
	* Policy is a set of rules that define the structure for how decisions are made and specific outcomes are reached.
	* Policies typically describe **Who** and a **What**, such as the access or rights that an individual has over an *Asset*.
	* Everything you want to do on a Fabric network is controlled by a *Policy*.
	* Policies are agreed to by the consortium members when a network is originally configured, but they can also be modified as the network evolves. For example, they describe the criteria for adding or removing members from a channel, change how blocks are formed, or specify the number of organizations required to endorse a smart contract.
	* Each policy has a **Type** which describes how the policy is expressed (Signature or ImplicitMeta) and a **Rule**.
	* Hyperledger Fabric Policy Hierarchy:
		1) System Channel         - Consortium Membership and blockchain structure
		2) Application Channel    - Transaction Networks and business logic
		3) ACLs & Smart Contracts - Transactions, data and events



### System & Application Channel Configuration & ACL ###
	* System Channel Configuration:
		* Every network begins with an ordering *System Channel*.
		* There must be exactly one ordering system channel for an ordering service.
		* It is the First Channel to be created.
		* The system channel also contains the organizations who are the members of the ordering service (ordering organizations) and those that are on the networks to transact (consortium organizations).
		* The **Policies** in the ordering system channel configuration blocks govern the consensus used by the ordering service and define how new blocks are created.
		* The system channel also governs which members of the consortium are allowed to create new channels.
	* Application Channel Configuraton:
		* The **Policies** in an application channel govern the ability to add or remove members from the channel.
		* Application channels also govern which organizations are required to approve a chaincode before the chaincode is defined and committed to a channel using the Fabric chaincode lifecyle.
		* When an application channel is initially created, it **Inherits** all the ordering service parameters from the orderer system channel by default.
		* However, those parameters (and the policies governing them) can be customized in each channel.
		* Channel Policies are defined in "configtx/configtx.yaml".
	* ACL`s
		* Provides the ability to configure *Access to Resources* by associating those resources with existing policies.
		* “Resources” could be functions on system chaincode (e.g., “GetBlockByNumber” on the “qscc” system chaincode) or other resources (e.g.,who can receive Block events).
		* ACLs refer to policies defined in an application channel configuraton and extends them to control additional resources.
		* The default set of Fabric ACLs is visible in the *configtx.yaml* file under *Application:&ApplicationDefaults* section but they can and should be overridden in a production environment.
		* The list of resources named in configtx.yaml is the complete set of all internal resources currently defined by Fabric.
	* Explicit & Implicit Sign:
		* Each policy has **Type** which describes how the policy is expressed (Signature or ImplicitMeta) and a **Rule**.
		* If you want to change anything in Fabric, the policy associated with the resource describes *who* needs to approve it, either with an *Explicit sign* off from Individuals, or an *Implicit sign* off by a Group.
		* Explicit sign offs in policies are expressed using the *Signature* syntax and implicit sign offs use the *ImplicitMeta* syntax.
		* This (ImplicitMeta Syntax) is particularly useful because the members of that group can change over time without requiring that the policy be updated.
		* Signature Policy:
			* Signature policies define specific types of users who must sign in order for a policy to be satisfie such as Org1.Peer OR Org2.Peer.
			*  The syntax supports arbitrary combinations of *AND, OR and NOutOf*.
		* ImplicitMeta Policy:
			* ImplicitMeta policies are only valid in the context of channel configuration which is based on a tiered hierarchy of policies in a configuration tree.
			* Key benefit of an ImplicitMeta policy such as **MAJORITY Admins** is that when you add a new admin organization to the channel, you do not have to update the channel policy.
			* ImplicitMeta policies are considered to be more flexible as the consortium members change.
			* The *Consortium on the Orderer* can change as new members are added or an existing member leaves with the consortium members agreeing to the changes, but no policy updates are required.
			* Recall that ImplicitMeta policies ultimately resolve the Signature sub-policies underneath them in the configuration tree.
			* *Always*, ImplicitMeta policies (Reader, Writer, and Admin ImplicitMeta policies) point to sub-policies (Reader, Writer, and Admin) defined for each organization.



### Fabric Policy Governance ###
	* System Channel:
		1) What Orderer Organizations Governs:
			* Blockchain Network Structure
			* Consensus
			* Consortium Membership
			* Consortium Member Policies policies (Readers, Writers, Admins)
		2) What Consortium Organizations Governs:
			* Channel Modification

	* Application Channel:
		1) What Orderer Organizations Governs:
			* Consensus
		2) What Consortium Organizations Governs:
			* Channel Membership
			* Organization Policies (Readers, Writers, Admins)

	* ACLs and Smart Contracts:
		1) What Orderer Organizations Governs:
			* Nothing
		2) What Consortium Organizations Governs:
			* Smart contracts
			* Ledger Data
			* Events




### Overriding Policy Definitions ###
	* Hyperledger Fabric includes default policies which are useful for getting started, developing, and testing your blockchain, but they are meant to be customized in a production environment.
	* You should be aware of the default policies in the configtx.yaml file.
	* Channel configuration policies can be extended with *Arbitrary Verbs*, beyond the default Readers, Writers, Admins Policies in configtx.yaml.
	* The orderer system and application channels are overridden by issuing a config update when you override the default policies by editing the configtx.yaml for the orderer system channel or the configtx.yaml for a specific channel.




### Identity ###
	* It determines the exact permissions over resources and access to information that actors have in a blockchain network.
	* Digital Identity === Identity + Principal
	* Principals include properties of an actor’s identity, such as the actor’s organization, organizational unit, role or even the actor’s specific identity.



### Gossip Protocol ###
	* The technical mechanism by which peers within an individual organization efficiently discover and communicate with each other when an organization have large number of peer nodes.
	* Not every peer needs to be connected to an orderer — *peers can cascade blocks to other peers using the gossip protocol*, who also can process them independently (blocks).

###################################################################################################







#################################################     *What's New in v2.0*     ####################
### Decentralized Governance for Smart Contracts ###
	* New Fabric chaincode lifecycle allows multiple organizations to come to agreement on the parameters of a chaincode, such as the chaincode endorsement policy (LifecycleEndorsement Policy), before it can be used to interact with the ledger.
	* It supports both centralized trust models (in v1.x previous lifecycle model) as well as decentralized models (in v2.0).
	* New model allows for a chaincode to be upgraded only after sufficient number of organizations have approved theupgrade.
	* Fabric lifecycle allows you to change an endorsement policy  or private data collection configuration without having to repackage or reinstall the chaincode.
	* You can now use a single chaincode package and deploy it multiple times with different names on the same channel or on different channels.
	* Chaincode packages do not need to be identical across channel members.



### Private Data Enhancements ###
	* Private data collections can now optionally be defined with an endorsement policy that overrides the chaincode-level endorsement policy for keys within the collection.



### External Chaincode Launcher ###
	* Chaincode is no longer required to be run in Docker containers, and may be executed in the operator’s choice of environment (including containers or  in a Kubernetes pod).
	* Now possible to run *Chaincode As an External Service*, for example in a Kubernetes pod, which a peer can connect to and utilize for chaincode execution.
	* *External Chaincode Launcher Feature* -- An operator can provide a set of external builder executables to override how the peer builds and launches chaincode.



### Alpine-based Docker Images ###
	* Starting with v2.0, Hyperledger Fabric Docker images will use Alpine Linux, a security-oriented, lightweight Linux distribution.



### Upgrading to Fabric v2.0 ###
	* Rolling upgrades from v1.4.x to v2.0 are supported, so that network components can be upgraded one at a time with no downtime.



### Comparison of Chaincode Lifecycle b/w v1.x & v2.0 ###
	* In v1.x versions of Fabric, one organization had the ability to set parameters of a chaincode (for instance the endorsement policy) for all other channel members, who only had the power to refuse to install the chaincode and therefore not take part in transactions invoking it.
	* In 2.0, it supports both centralized trust models (in v1.x previous lifecycle model) as well as decentralized models (in v2.0) requiring a sufficient number of organizations to agree on an endorsement policy and other details before the chaincode becomes active on a channel.

###################################################################################################








#################################################     *Justification*     #########################
### Confidentiality in Fabric N/W ###
	* One approach    - Encrypting Data -- Given enough time and computational resource, the encryption could be broken.
	* Second approach - Zero Knowledge Proofs (ZKP) -- Computing a ZKP requires considerable time and computational resources. Hence, the trade-off in this case is performance.
	* Both approaches have their trade-offs. So, Channels and Private Data Collections are used.


### Scalability and Confidentiality ###
	* Endorsing Nodes keeps the logic of the chaincode confidential to endorsing organizations. This is in contrast to the output of the chaincodes (the transaction proposal responses) which are shared with every peer in the channel, whether or not they endorsed the transaction.
	* This specialization of endorsing peers is designed to help scalability and confidentiality.


### Encryption of Transactions ###
	* To further obfuscate the data, values within chaincode can be encrypted (in part or in total) using common cryptographic algorithms such as AES before sending transactions to the ordering service and appending blocks to the ledger. Once encrypted data has been written to the ledger, it can be decrypted only by a user in possession of the corresponding key that was used to generate the cipher text.

### Separation & collaboration b/w organizations ###
	* This is a very powerful concept – Channels provide both a mechanism for the separation of organizations, and a mechanism for collaboration between organizations. All the while, this infrastructure is provided by, and shared between, a set of independent organizations.


### Need For Organizational Units ###
	* When a CA issues X.509 certificates, the *OU field (Manufacturing,Distribution)* in the certificate *Specifies the Line of Business* to which the *identity belongs*.
	* A benefit of using OUs like this is that these values can then be used in policy definitions in order to restrict access or in smart contracts for attribute-based access control.
	* Otherwise, separate MSPs would need to be created for each organization.



### Speciality of Node OU Roles ###
	* Special kind of OU called Node OU, that can be used to confer(provide) a role onto an identity.
	* This is particularly useful when you want to restrict the members of an organization to the ones holding an identity (signed by one of MSP designated CAs) with a specific Node OU role in it.
	* For example, with node OU’s you can implement a more granular endorsement policy that requires Org1 peers to endorse a transaction, rather than any member of Org1.



### Importance of Channel Config. Policy , (Eventhough Coming Identity has Admin rights defined in Channel MSP) --- No Power ###
	* For Channel MSPs, just because an actor has the role of an administrator it doesn’t mean that they can administer particular resources. The actual power a given identity has with respect to administering the system is determined by the ***policies*** that manage system resources. For example, a channel policy might specify that ORG1-MANUFACTURING administrators, meaning identities with a ***role of Admin*** and a ***Node OU of ORG1-MANUFACTURING*** (both must be viewed to add an org), have the rights to add new organizations to the channel, whereas ORG1-DISTRIBUTION administrators have no such rights (because *Node OU of ORG1-DISTRIBUTION* is different).
	* It is recommended that when the user is registered with the CA, that the *admin role in Node OU* is used to designate the node administrator. Then, the identity is recognized as an *Admin of ORG* by the Node OU role value in their signcert(certificate). As a reminder, in order to leverage the admin role, the “identity classification” feature must be enabled in the config.yaml above by setting “Node OUs” to Enable: true.



### Careful Usage of OUs ###
	* Finally, OUs could be used by different organizations in a consortium to distinguish each other. But in such cases, the different organizations have to use the same Root CAs and Intermediate CAs for their chain of trust, and assign the OU field to identify members of each organization. When every organization has the same CA or chain of trust, this makes the system more centralized than what might be desirable and therefore deserves careful consideration on a blockchain 	  network.




### D/B Channel and Private Data Collections ###
	* Channels keep *Transactions* private from the broader network whereas Collections keep *Data* private between subsets of organizations on the channel.

### Systems of Proof ###
	* In addition to being decentralized and collaborative, the information recorded to a blockchain is append-only, using cryptographic techniques that guarantee that once a transaction has been added to the ledger it cannot be modified. This property of “Immutability” makes it simple to determine the provenance of information because participants can be sure information has not been changed after the fact. It’s why blockchains are sometimes described as Systems Of Proof.


### Strict Ordering of Transactions ###
	* It’s worth noting that the sequencing of transactions in a block is not necessarily the same as the order received by the ordering service, since there can be multiple ordering service nodes that receive transactions at approximately the same time. What’s important is that the ordering service puts the transactions into a strict order, and peers will use this order when validating and committing transactions.
	* This strict ordering of transactions within blocks makes Hyperledger Fabric a little different from other blockchains where the same transaction can be packaged into multiple different blocks that compete to form a chain.



### Ledger Immutability & Finality ###
	* In Hyperledger Fabric, the blocks generated by the ordering service are *Final*. Once a transaction has been written to a block, its position in the ledger is immutably assured. As we said earlier, Hyperledger Fabric’s finality means that there are *No Ledger Forks* — validated transactions will never be reverted or dropped.


### Disadvantages in Multi-cluster Ordering Service ###
	* Every channel runs on a separate instance of the Raft protocol, which allows each instance to elect a different leader.
	* This configuration also allows further decentralization of the service in use cases where clusters are made up of ordering nodes controlled by different organizations.
	* But, While this configuration creates more overhead in the form of redundant heartbeat messages and goroutines, it lays necessary groundwork for BFT.



### Final Version Check (i.e., Committing phase) - Double Spend Problem ###
	* Final Version Check by peers in committing phase provides protection against *Double Spend Operations* and other threats that might compromise data integrity, and allows for functions to be executed against non-static variables.


### De-centralized Network ###
	* The careful use of network and channel policies allow even large networks to be well-governed. Organizations are free to add peer nodes to the network so long as they conform to the policies agreed by the network. *Network and Channel Policies* create the balance between *Autonomy and Control* which characterizes a De-Centralized Network.
	* Objects like network configurations, that are logically single, turn out to be physically replicated among a set of ordering services nodes. channel configurations, ledgers, and to some extent smart contracts which are installed in multiple places but whose interfaces exist logically at the channel level. It enables Hyperledger Fabric Blockchain Network to be both *DeCentralized* and yet *Manageable* at the same time.
	* Every channel runs on a separate instance of the Raft protocol, which allows each instance to elect a different leader. This configuration also allows further decentralization of the service in use cases where clusters are made up of ordering nodes controlled by different organizations.



###################################################################################################









###################################################################################################
### Raft Ordering Service ###
	* Raft is a crash fault tolerant (CFT) ordering service based on an implementation of Raft protocol in *etcd*.
	* It uses a “leader and follower” model, in which a leader is dynamically elected among the ordering nodes in a channel (this collection of nodes is known as the “consenter set”), and that leader replicates messages to the follower nodes.
	* Because the system can sustain the loss of nodes, including leader nodes, as long as there is a majority of ordering nodes (what’s known as a “quorum”) remaining, Raft is said to be “crash fault tolerant” (CFT).
	* Advantages of Raft Over Kafka:
		* There is no functional difference between an ordering service based on Raft versus Kafka.
		* Raft is easier to set up. (Because With Raft, everything is embedded into your ordering node.)
		* With Raft, each organization can have its own ordering nodes, participating in the ordering service, which leads to a more decentralized system. Given that, having ordering nodes run by different organizations when using Kafka (which Fabric supports) doesn’t give you much in terms of decentralization because the nodes will all go to the *same Kafka cluster* which is under the *control of a single organization*.
		* Raft is supported natively, but with kafka & zookeeper, users are required to get the requisite images and learn how to use it of their own.
		* Fabric Raft Implementation has been developed and will be supported within the Fabric developer community.
		* Raft allows the users to specify which ordering nodes will be deployed to which channel.In this way, peer organizations can make sure that, if they also own an orderer, this node will be made a part of a ordering service of that channel,
	* Note:
		* Similar to Solo and Kafka, a Raft ordering service can lose transactions after acknowledgement of receipt has been sent to a client. For example, if the leader crashes at approximately the same time as a follower provides acknowledgement of receipt. Therefore, application clients should listen on peers for transaction commit events regardless (to check for transaction validity), but extra care should be taken to ensure that the client also gracefully tolerates a timeout in which the transaction does not get committed in a configured timeframe. Depending on the application, it may be desirable to resubmit the transaction or collect a new set of endorsements upon such a timeout.


### Raft Concepts ###
	1) Log:
		* Full sequence of *Log Entry* which is a primary unit of work for Raft ordering service.
		* We consider the log consistent if a majority (a quorum, in other words) of members agree on the entries and their order, making the logs on the various orderers replicated.
	2) Consenter Set:
		* The ordering nodes actively participating in the consensus mechanism for a given channel and receiving replicated logs for the channel.
		* This can be all of the nodes available (either in a single cluster or in multiple clusters contributing to the system channel), or a subset of those nodes.
	3) Finite-State Machine (FSM):
		* Every ordering node in Raft has an FSM and collectively they’re used to ensure that the sequence of logs in the various ordering nodes is deterministic (written in the same sequence).
	4) Quorum:
		* Quorum is a majority of nodes for every consenter set.
		* If a quorum of nodes is unavailable for any reason, the ordering service cluster becomes unavailable for both read and write operations on the channel, and no new logs can be committed.
	5) Leader:
		* Leader is responsible for ingesting new log entries, replicating them to follower ordering nodes, and managing when an entry is considered committed.
		* Channel’s consenter set(All Ordering Nodes) elects a single node to be the leader.
		* This is not a special type of orderer.
		* It is only a role that an orderer may have at certain times, and then not others, as circumstances determine.
	6) Follower:
		* Followers receive the logs from the leader.
		* Followers also receive “heartbeat” messages from the leader.
		* In the event that the leader stops sending those message for a configurable amount of time, the followers will initiate a leader election and one of them will be elected the new leader.


### How leader election works in Raft ###
	* The process of electing a leader happens within the orderer’s internal processes.
	* Raft nodes are always in one of three states: follower, candidate, or leader.
	* All nodes initially start out as a follower. In this state, they can accept log entries from a leader (if one has been elected), or cast votes for leader. If no log entries or heartbeats are received for a set amount of time (for example, five seconds), nodes self-promote to the candidate state. In the candidate state, nodes request votes from other nodes. If a candidate receives a quorum of votes, then it is promoted to a leader. The leader must accept new log entries and replicate them to the followers.



### Snapshotting ###
	* If an ordering node goes down, Raft uses a process called “snapshotting” is used, in which users can define how many bytes of data will be kept in the log to keep all logs indefinitely, in order to save disk space.
	* This amount of data will conform to a certain number of blocks (which depends on the amount of data in the blocks. Note that only full blocks are stored in a snapshot).
	* For example, let’s say lagging replica R1 was just reconnected to the network. Its latest block is 100. Leader L is at block 196, and is configured to snapshot at amount of data that in this case represents 20 blocks. R1 would therefore receive block 180 from L and then make a Deliver request for blocks 101 to 180. Blocks 180 to 196 would then be replicated to R1 through the normal Raft protocol.



### Importance of System Chaincodes ###
	* It is possible for low level Fabric developers and administrators to modify these system chaincodes for their own uses.
	* However, the development and management of system chaincodes is a specialized activity, quite separate from the development of smart contracts, and is not normally necessary.
	* Changes to system chaincodes must be handled with extreme care as they are fundamental to the correct functioning of a Hyperledger Fabric network.
	* For example, if a system chaincode is not developed correctly, one peer node may update its copy of the world state or blockchain differently compared to another peer node.
	* This lack of consensus is one form of a ledger fork, a very undesirable situation.




###################################################################################################




#################################################     *Topics*    #################################
### System channel & Application Channel ###
	* Both network and channel configurations are kept consistent using the same blockchain technology that is used for user transactions – but for configuration transactions. To change a network or channel configuration, an administrator must submit a configuration transaction to change the network or channel configuration. It must be signed by organizations identified in the appropriate policy as being responsible for configuration change. This policy is called the mod_policy and we’ll discuss it later.
	* Indeed, the ordering service nodes operate a mini-blockchain, connected via the system channel we mentioned earlier. Using the system channel ordering service nodes distribute network configuration transactions. These transactions are used to co-operatively maintain a consistent copy of the network configuration at each ordering service node. In a similar way, peer nodes in an application channel can distribute channel configuration transactions. Likewise, these transactions are used to maintain a consistent copy of the channel configuration at each peer node.



### Importance of Consensus ###
	* Consensus is not merely limited to the agreed upon order of a batch of transactions; rather, it is an overarching characterization that is achieved as a byproduct of the ongoing verifications that take place during a transaction’s journey from proposal to commitment.


### Formation of Blockchain Network ###
	* In most cases, multiple organizations come together as a consortium to form the network and their permissions are determined by a set of policies that are agreed by the consortium when the network is originally configured. Moreover, network policies can change over time subject to the agreement of the organizations in the consortium, as we’ll discover when we discuss the concept of modification policy.


### careful addition of peers ###
	* More peers in a network will allow more applications to connect to it; and multiple peers in an organization will provide extra resilience in the case of planned or unplanned outages.


### Types of peers ###
	* These are the two major types of peer:
		1)Committing Peer = Every peer node in a channel is a committing peer. It receives blocks of generated transactions, which are subsequently validated before they are committed to the peer node’s copy of the ledger as an append operation.
		2)Endorsing Peer = Every peer with a smart contract can be an endorsing peer if it has a smart contract installed. However, to actually be an endorsing peer, the smart contract on the peer must be used by a client application to generate a digitally signed transaction response. The term endorsing peer is an explicit reference to this fact.
	* There are two other roles a peer can adopt:
		1)Leader peer = When an organization has multiple peers in a channel, a leader peer is a node which takes responsibility for distributing transactions from the orderer to the other committing peers in the organization. A peer can choose to participate in static or dynamic leadership selection.
		2)Anchor Peer = If a peer needs to communicate with a peer in another organization, then it can use one of the anchor peers defined in the channel configuration for that organization. An organization can have zero or more anchor peers defined for it, and an anchor peer can help with many different cross-organization communication scenarios.



### Leadership Selection for Leader Peer ###
	* A peer can choose to participate in static or dynamic leadership selection.
	* It is helpful, therefore to think of two sets of peers from leadership perspective – those that have static leader selection, and those with dynamic leader selection. For the static set, zero or more peers can be configured as leaders. For the dynamic set, one peer will be elected leader by the set. Moreover, in the dynamic set, if a leader peer fails, then the remaining peers will re-elect a leader.
	* It means that an organization’s peers can have one or more leaders connected to the ordering service. This can help to improve resilience and scalability in large networks which process high volumes of transactions.


### Issuing Digital Certificates --- CA ###
	* A Certificate Authority dispenses certificates to different actors.These certificates are digitally signed by the CA and bind together the actor with the actor’s public key (and optionally with a comprehensive list of properties). As a result, if one trusts the CA (and knows its public key), it can trust that the specific actor is bound to the public key included in the certificate, and owns the included attributes, by validating the CA’s signature on the actor’s 		  certificate.


### Node OU Roles ###
	* Special kind of OU called Node OU, that can be used to confer(provide) a role onto an identity.
	* These Node OU roles are defined in the **$FABRIC_CFG_PATH/msp/config.yaml** file.
	* Contain a list of organizational units whose members are considered to be part of organization represented by this MSP.
	* This is particularly useful when you want to restrict the members of an organization to the ones holding an identity (signed by one of MSP designated CAs) with a specific Node OU role in it. For example, with node OU’s you can implement a more granular endorsement policy that requires Org1 peers to endorse a transaction, rather than any member of Org1.
	* In order to use the Node OU roles, the “identity classification” feature must be enabled for the network. When using the folder-based MSP structure, this is accomplished by enabling “Node OUs” in the config.yaml file which resides in the root of the MSP folder.
	* There are 4 possible Node OU ROLES for the MSP:
		* client, peer, admin, orderer
		* you no longer have to explicitly place *certs* in the *admincerts* folder of the MSP directory. Rather, the *admin role* present in the user’s signcert qualifies the *identity* as an *admin user*.


### Determinism --- Smart Contracts ###
	* Smart contracts executing in a blockchain that operates with the order-execute architecture must be deterministic; otherwise, consensus might never be reached. To address the non-determinism issue, many platforms require that the smart contracts be written in a non-standard, or domain-specific language (such as Solidity) so that non-deterministic operations can be eliminated. This hinders wide-spread adoption because it requires developers writing smart contracts to learn a new language and may lead to programming errors.



### Non - determinism ###
	* For the same transaction proposal, different peers can return different results and therefore inconsistent transaction responses to the application because the chaincode is non-deterministic. Non-determinism is the enemy of chaincodes and ledgers and if it occurs it indicates a serious problem with the proposed transaction, as inconsistent results cannot, obviously, be applied to ledgers. An individual peer cannot know that their transaction result is non-deterministic — transaction responses must be gathered together for comparison before non-determinism can be detected.




### Decentralized Agreement --- Smart Contracts ###
	* Human decisions can be modeled into a chaincode process that spans multiple transactions. The chaincode may require actors from various organizations to indicate their terms and conditions of agreement in a ledger transaction. Then, a final chaincode proposal can verify that the conditions from all the individual transactors are met, and “settle” the business transaction with finality across all channel members. For a concrete example of indicating terms and conditions in private, see the asset transfer scenario in the Private data documentation.


### Permissionless Blockchain ###
	* Open permissionless system that allows unknown identities to participate in the network (requiring protocols like “proof of work” to validate transactions and secure the network),


### Consensus - Practical Byzantine Fault Tolerance ###
	* PBFT can provide a mechanism for file replicas to communicate with each other to keep each copy consistent, even in the event of corruption. Alternatively, in Bitcoin, ordering happens through a process called mining where competing computers race to solve a cryptographic puzzle which defines the order that all processes subsequently build upon.


### Private Data Collections ###
	* When a subset of organizations on that channel need to keep their transaction data confidential, a private data collection (collection) is used to segregate this data in a private database, logically separate from the channel ledger, accessible only to the authorized subset of organizations.


### MSP -- should be cleared ###
	* Network configuration NC4 uses a named MSP to identify the properties of certificates dispensed by CA4 which associate certificate holders with organization R4. NC4 can then use this MSP name in policies to grant actors from R4 particular rights over network resources. An example of such a policy is to identify the administrators in R4 who can add new member organizations to the network. We don’t show MSPs on these diagrams, as they would just clutter them up, but they are very important.


### PKI ###
	* A PKI is comprised of Certificate Authorities who issue digital certificates to parties (e.g., users of a service, service provider), who then use them to authenticate themselves in the messages they exchange in their environment. A 	  CA’s Certificate Revocation List (CRL) constitutes a reference for the certificates that are no longer valid. Revocation of a certificate can happen for a number of reasons. For example, a certificate may be revoked because the cryptographic private material associated to the certificate has been exposed.
	* There are four key elements to PKI:
		* Digital Certificates
			* A digital certificate is a document which holds a set of attributes relating to the holder of the certificate.
			* The most common type of certificate is the one compliant with the X.509 standard, which allows the encoding of a party’s identifying details in its structure.
			* Digital Certificate has Public Key whereas Private Key must be kept private.
		* Public and Private Keys
			* Public Key that is made widely available and acts as Authentication Anchor.
			* Private Key that is used to produce Digital Signatures on messages.
			* Recipients of digitally signed messages (using Private Key) can verify the Origin and Integrity of a received message by checking that the attached signature is valid under the *Public Key* of the expected sender.
		* Certificate Authorities
			* One or More CAs can be used to define the members of an organization’s from a digital perspective.
		* Certificate Revocation Lists
			* It’s just a list of references to certificates that a CA knows to be revoked for one reason or another.
			* When a third party(one org.) wants to verify another(other org.) party’s identity, it first checks the issuing CA’s CRL to make sure that the certificate has not been revoked. A verifier doesn’t have to check the CRL, but if they don’t they run the risk of accepting a compromised identity.
			* Using a CRL to check that a certificate is still valid. If an impersonator tries to pass a compromised digital certificate to a validating party, it can be first checked against the issuing CA’s CRL to make sure it’s not listed as no longer valid.


### Job of Smart Contract Developer ###
	* The job of a smart contract developer is to take an existing business process that might govern financial prices or delivery conditions, and express it as a smart contract in a programming language such as JavaScript, Go, or Java.
	* The legal and technical skills required to convert centuries of legal language into programming language is increasingly practiced by smart contract auditors.
###################################################################################################
