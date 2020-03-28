#################################################     *ALL TOPICS*     ##################################################
### Blockchain and its Features ###
	* decentralized --- replication of ledger across the n/w participants in a blockchain network.
	* Collaboration --- replication of ledger with, each of whom collaborate in its maintenance.
	* Systems of Proof --- "immutability" of transactions in ledger makes it simple to determine the provenance of information
	* Applications --- By means of "smart contracts" which has a business logic. 
	* Consensus --- process of keeping the ledger transactions synchronized across the network (Achieved by - updating same 			transaction in same order.)
	* Shared --- a blockchain system has shared programs (smart contracts) to update shared ledgers but in today’s systems, 		     where a participant’s private programs are used to update their private ledgers



### Hyperledger Fabric ###

	* open source enterprise-grade permissioned distributed ledger technology (DLT) platform.
	* established under the Linux Foundation (Open Governance).
	* has a highly modular and configurable architecture.
	* first DLT to support smart contracts authored in general-purpose programming languages such as Java, Go and Node.js.
	* support for pluggable consensus protocols that enable the platform to be more effectively customized to fit particular 		  use cases and trust models.
	* can leverage consensus protocols that do not require a native cryptocurrency to incent costly mining or to fuel smart 	  contract execution.
	* enables confidentiality through its channel architecture and private data feature.
	
	
	
	
### Modular Components in Fabric ###
	* pluggable ordering service
		--- establishes consensus on the order of transactions and then broadcasts blocks to peers.
	* pluggable membership service provider
		--- is responsible for associating entities in the network with cryptographic identities.
	* optional peer-to-peer gossip service
		--- disseminates the blocks output by ordering service to other peers.
	* Smart contracts
		--- run within a container environment (e.g. Docker) for isolation and can be written in standard programming langs
	* ledger
		--- can be configured to support a variety of DBMSs.
	* pluggable endorsement and validation policy enforcement
		--- can be independently configured per application. 
	
	
		
### New Approach in Fabric ###
	* Replacing order-execute fashion with execute-order-validate model.
	* execute a transaction and check its correctness, thereby endorsing it,
	* order transactions via a (pluggable) consensus protocol, and
	* validate transactions against an application-specific endorsement policy before committing them to the ledger.
	* first phase (1st point) also eliminates any non-determinism, as inconsistent results can be filtered out before ordering
	
	
	
	
### Performance of Fabric ###
	* Performance of a blockchain platform can be affected by many variables such as transaction size, block size, network 		  size, as well as limits of the hardware, etc.
	* The latest scaled Fabric to 20,000 transactions per second.



### Choosing Pluggable Consensus Protocol ###
	* when deployed within a single enterprise, or operated by a trusted authority,
		--- crash fault-tolerant (CFT) consensus protocol might be more than adequate
	*  in a multi-party, decentralized use case,
		--- a more traditional byzantine fault tolerant (BFT) consensus protocol might be required.
		
		
		
		
### Application-Specific Endorsement Policy ###
	* specifies which peer nodes, or how many of them, need to vouch for the correct execution of a given smart contract.
	* each transaction need only be executed (endorsed) by the subset of the peer nodes necessary to satisfy the transaction’s 		  endorsement policy.
	* Fabric lifecycle allows you to change an endorsement policy or private data collection configuration without having to 	   repackage or reinstall the chaincode. 
	
	
	
	
### Distributed Ledger ###
	* is a combination of the two components, world state *database* and the transaction log *history*.
	* single ledger can have one or more smart contracts.
	* legder physically hosted on Peer, but logically hosted on the channel.
	* 1)world state database
		* describes the state of the ledger at a given point in time.
		* it’s the database of the ledger.
	* 2)transaction log history
		* records all transactions which have resulted in the current value of the world state.
		* sequenced, tamper-resistant record of all state transitions in the fabric.
		* it’s the update history for the world state.
	* each participant has a copy of the ledger to every Hyperledger Fabric network they belong to.
	* described as decentralized because it is replicated across many network participants, each of whom collaborate in its 	  maintenance.
	* by default, this is a LevelDB key-value store database.
	
	
	
### Features of Fabric Ledger ###
	* Query and update ledger using key-based lookups, range queries, and composite key queries.
	* Read-only queries using a rich query language (if using CouchDB as state database).
	* Read-only history queries — Query ledger history for a key, enabling data provenance scenarios.
	
	
	
### Transactions ###
	* consist of the versions of keys/values that were read in chaincode (read set) and keys/values that were written in 		  chaincode (write set).
	* contain signatures of every endorsing peer and are submitted to ordering service.
	* are ordered into blocks and are “delivered” from an ordering service to peers on a channel.
	
	
	
	
	
### Peer ###
	* Every peer node in a channel is a *committing peer*.
	* to actually be an *endorsing peer*, the smart contract on the peer must be used by a client application to generate a 	  digitally signed transaction response.
	* When an organization has multiple peers in a channel, a *leader peer* is a node which takes responsibility for 		  distributing blocks of transactions from the orderer to the other committing peers in the organization.
	* If a peer in one organization needs to communicate with a peer in another organization, then it can use one of the 		  anchor peers defined in the channel configuration for that organization.
	* anchor peer can help with many different cross-organization communication scenarios.
	* a peer can be a committing peer, endorsing peer, leader peer and anchor peer all at the same time!
	* Only the anchor peer is optional.
	* for all practical purposes, there will always be a leader peer and at least one endorsing peer and at least one 		  committing peer.
	* each peer node (belongs to one org.)in a channel uses the copy of Channel Configuration to determine the operations that 		  respective organizations` client applications can perform.
	* each peer maintains a copy of the channel configuration for each channel of which they are a member. 
	* Once Peer is started, it can join channel using the *orderer* by raising the join request to orderer.
	* each peer maintains a copy of the ledger for each channel of which they are a member.
	* single peer can host one or more ledgers.
	* peer can install one or more smart contracts in a single ledger.
	* peers and orderers can communicate with each other using channel.
	* peer can only run a smart contract and further can take part in the process of transaction endorsement if it is 		  installed on it, but it can know about the interface of a smart contract by being connected to a channel.
	* validate transactions by verifying the transaction signatures against endorsement policies and enforce the policies.
	* Prior to appending a block (commit to ledger) after validating the transactions, a versioning check is performed to 		  ensure that states for assets that were read have not changed since chaincode execution time. (protection against the 	  double spend).
	* At each of the committing peers, distributed transactions from orderers are recorded, whether valid or invalid, and 		  their local copy of the ledger updated appropriately.
		
		
		
### Smart Contracts ###
	* business logic of a blockchain application.
	* functions as a trusted distributed application.
	* are used to generate transactions.
	* more no. of smart contracts are packaged into a *chaincode*.
	* *chaincode package* must have been installed on *peers* by an administrator of the (respective peer) organization, and 		  then defined on a *channel*.
	* installing a smart contract shows how we think of it being *physically hosted* on a peer, whereas a smart contract that 		  has been defined on a channel shows how we consider it *logically hosted* by the channel.
	* State transitions are a result of chaincode invocations, recorded as transactions.
	* X.509 certificates are used in smart contract (transaction responses) to digitally sign transactions.
	* invoked by an application external to the blockchain when that application needs to interact with the ledger.
	* chaincode interacts only with the database component of the ledger, the world state (querying it, for example), and not 		  the transaction log.
	* many smart contracts run concurrently in the network
	* they may be deployed dynamically (in many cases by anyone)
	* application code should be treated as untrusted, potentially even malicious.
	* traditionally, chaincodes are launched by the peer, and then connect back to the peer.
	* in modern approach, now possible to run *chaincode as an external service*, for example in a Kubernetes pod, which a 		  peer can connect to and utilize for chaincode execution.
	
	
	
### Orderers ###
	* orderers, service as a *network administration point* for the fabric network.
	* When orderers receives join request from peers, it uses the *channel configuration* to determine Peer’s permissions on 		  the requeted channel.
	* orderer is initially configured and started by an administrators (of anyone org.) according to a *network configuration*.
	* ordering service node (for eg,O4) is the actor that creates consortia(for eg,2) and channels.
	* orderer(s) must be hosted by any one (or more) of the organization in a network as per *network configuration*.(2 points)
	* also supports application channels, for the purposes of transaction ordering into blocks for distribution.
	* it can order transactions for one or more application channels.
	* ordering service node (for eg,O4) has a copy of the network configuration, but in a *multi-node configuration*, every 	  ordering service node will have its own copy of the network configuration.
	* ordering service node is the distribution point for transactions.
	* ordering service node gathers endorsed transactions from applications and orders them into transaction blocks, which are 		  subsequently distributed to every peer node in the channel.
	* Two roles for single orderer:
		* at the channel level, orderer role is to gather transactions and distribute blocks inside channel according to 			  the policies defined in channel configuration.
		* at the network level, orderer role is to provide a management point for network resources according to the 			  policies defined in network configuration.
		* Notice again how these roles are defined by different policies within the channel and network configurations 			  respectively.
	* Whether acting as a network management point, or as a distributor of blocks in a channel, its nodes(orderers) can be 		  distributed as required throughout the multiple organizations in a network.
	* ordering service nodes (multiple orderers) are connected via the *System Channel* which operates a mini-blockchain.  
	
	
	
### Organization ###
	* every organizations in a n/w has a preferred Certificate Authority.
	* administrative rights of organization is decided by the *network configuration*.
	* When an organization has multiple peers in a channel, it can choose the peers upon which it installs smart contracts; it 		  does not need to install a smart contract on every peer.
	* approval of a chaincode definition occurs at the organization level.
	* A sufficient number of organizations (orgs administrator) need to approve a chaincode definition(not transactions 		  generated by the smart contracts) (A majority, by default) before the chaincode definition can be committed to the 		  channel and used to interact with the channel ledger. 
	* organization’s peers can have one or more leaders connected to the ordering service to improve resilience and scalability
	* An organization can have zero or more anchor peers defined for it.
	* Every organization has their own set of peers.
	* every organization has client applications.
	* A new organization(suppose, if added in a channel) can use the chaincode as soon as they approve the chaincode 		  parameters already agreed to by other members of the channel and then installs the chaincode package. 
	* A newly added organization in a channel can approve the chaincode definition once and join multiple peers to the channel 		  with the chaincode package installed.
	* if a newly added organization in a channel, wanted to change the chaincode definition, all members of a channel would 	  need to approve a new definition for their organization, and then one of the organizations would need to commit the 		  definition to the channel.
	
	
	
### Certificate Authority CA ###
	* is used to dispense X.509 digital certificates which acts as a identities to the administrators, network nodes, etc... 
	* can also be used to sign transactions.
	* it has a built-in CA called *Fabric-CA*
	
	
### Applications ###
	* applications can connect to both peers and orderers by using the channel.
	* single application of one organization can connect to one or more channels as per respective channel config in a network.
	* organisations maintain the client applications.
	* X.509 certificates are used in client application (transaction proposals). 
	* client application will have an identity that associates it with an organization.
	* client application can invoke smart contracts, Once the chaincode definition has been committed to the channel.
	* Client applications send transaction proposals (serves as input to the smart contract) to peers owned by an organization 		  specified by the smart contract endorsement policy, which uses it to generate an endorsed transaction response, which is 		  returned by the peer node to the client application. (process called as Smart Contract Invocation)
	
	
	
	
	
### Channels ###
	* Only network administrators (organization(s)) as defined in network configuration policy, can able to create new channel.
	* channels keep *transactions* private from the broader network.
	* channels can serve for one or more applications.
	* channel must have atleast one orderer to order trasactions.
	* any updates to network configuration after creation of channels will have no direct effect on channel configuration.
	* participants on a Fabric network establish a sub-network where every member has visibility to a particular set of 		  transactions.
	* only those nodes that participate in a channel have access to the smart contract (chaincode) and data transacted, 		  preserving the privacy and confidentiality of both.
	* allowing a group of participants to create a separate ledger of transactions.
	* data in a channel is completely isolated from the rest of the network, including other channels.
	* One Ledger per Channel.
	* there can be multiple channels in a network.
	* channel can have any number of organizations connected to it.
	* channel’s ledger contains a configuration block defining policies, access control lists, and other pertinent information.
	* contain Membership Service Provider instances allowing for crypto materials to be derived from different certificate 		  authorities.
	
	
	
	
### Private Data Collection ###
	* collections keep *data* private between subsets of organizations on the channel.
	* is used to segregate the data in a private database, logically separate from the channel ledger, accessible only to the 		  authorized subset of organizations.
	* It is a collection (like DB) between members on a channel, allowing much of the same protection as channels without the 		  maintenance overhead of creating and maintaining a separate channel.
	
	
	
	
### Membership Service Provider MSP ###
	* mapping of X.509 digital certificates to member organizations is achieved by via a structure called a (MSP).
	* members of a Hyperledger Fabric network enroll through a trusted MSP.
	
	
	
	
### Assets ###
	* can be tangible (real estate and hardware)
	* can also be intangible (contracts and intellectual property)
	* assets can be modified using chaincode transactions.
	* represented as a collection of key-value pairs.
	* with state changes recorded as transactions on a Channel ledger.
	* can be represented in binary and/or JSON form.
	
	
	
	
### Ordering Service ###
	* currently offering a CFT ordering service implementation based on the *etcd* library of the Raft protocol.
	* network can have multiple ordering services (like CFT or BFT in same n/w) supporting different applications or 		  application requirements. (Note this point: which is different from multiple orderer organizations having orderers like 	    CFT1,CFT2,etc for a single ordering service like CFT for a single application requirements.)
	
	
	
### Consortium ###
	* consortium defines the set of organizations in the network who share a need to *transact* with one another.
	* It really makes sense to group organizations together as a single consortium if they have a common goal,
	* can have any number of organizational members.
	* Only network administrators (organization(s)) as defined in network configuration, can able to create new consortia.
	* Every consortium has a single channel for their organizational members in a consortium.
	* consortium definition, by network administrator, is stored in the network configuration.
	
	
	
### Declarative Policies ###
	* how organizations manage network evolution.
	
	
### Chaincode Definition ###
	* a set of parameters that establish how a chaincode will be used on a channel.
	* it has endorsement policy for a smart contract ( describes which organizations` peer should digitally sign a generated 		  transaction(not a chaincode) before they will be accepted by other organizations(committing peer’s) onto their copy of 		  the ledger.).
	* Committing the chaincode definition to the channel, places the endorsement policy on the channel ledger.



### Fabric Network Governance ###
	* network is governed according to policy rules specified in *network configuration*.
	* newtork can be controlled by one or more organizations.
	
	
	
### Network Configuration (policy) ###
	* defines the configuration settings for the orderer.
	* defines consortium definition.
	* N/W Config. policy can be considered more important than Orderers because, ultimately, it controls network access.
	* it gives administrative rights to organization.
	* it contains the policies that describe the starting set of administrative capabilities for the network.
	* it may change later due to addition or removal of the members of the fabric network.
	* if consortia definition is changed in n/w configuration, it will not affect the members of channel after creation of 		  channels.
	* policy which separates organizations that can manage resources at the network level.
	* channel configurations remain completely separate from each other, and completely separate from the network configuration
	* each node in the ordering service records each channel in the network configuration, so that there is a record of each 	   channel created, at the network level.
	* Although ordering service node creates consortia and channels, the *intelligence* of the network is contained in the 		  *network configuration* that Ordering services(orderers) is obeying.
	
	
	
### Application Channel Governance ###
	* channel is governed according to the *policy rules* specified in *channel configuration*.
	* channel (channel configuration) can be controlled by one or more organizations (org`	s peers, must be member of the 		  channel).
	* Channel configuration determines which & how many peers in channel can read and/or write information to channel ledger.
	* administrating organization(s) has *no rights* in channel configuration.
	* administrating organization(s) cannot add itself to the *channel*, must be authorized by channel members as per channel 		  configuration.
	* anchor peers for one org. in a channel are defined in the channel configuration for that organization(communicating org. 		  or from org.).
	* organization(s) who can manage resources at the channel level.
	
	
	
	
### Modification Policy or mod_policy ###
	* is a first class policy within a network or channel configuration that manages change. 
	* The key point of understanding is that policy change in a network or channel configuration is managed by a policy 		  (mod_policy) within the respective policy itself.
	* a uniquely powerful policy that allows network and channel administrators to manage policy change itself.
	* mod_policy defines a set of organizations that are allowed to change the mod_policy itself.
	* organization(s) defined in the mod_policy inside n/w configuration policy is responsible for *Configuration Changes*
	* mod_policy can be configured in such a way that all organization defined in mod_policy would have to approve the change.
	* Note that separate mod_policy for both n/w & channel configuration policies within the policies respectively. 
	
	


### (N/W & Channel) Configuration Transactions ###
	* Network Configuration Transaction:
		* To change a network configuration, a network administrator must submit a *configuration transaction* to change 			  the network configuration.
		* It must be signed by the organizations identified in the *mod_policy* (with network configuration) as being 			  responsible for network configuration change.
		* WKT, ordering service nodes (multiple orderers) are connected via the *System Channel*.
		* Using the system channel, ordering service nodes distribute *network configuration transactions*.
		* These transactions are used to co-operatively maintain a consistent copy of the *network configuration at each 			  ordering service node*.
		
	* Channel Configuration Transactions:
		* To change a channel configuration, a channel administrator must submit a *configuration transaction* to change 			  the channel configuration.
		* It must be signed by the organizations identified in the *mod_policy* (with channel configuration) as being 			  responsible for channel configuration change.
		* In a similar way, peer nodes in an *application channel* can distribute channel configuration transactions.
		* these transactions are used to maintain a consistent copy of the *channel configuration at each peer node*.
		
	* Every configuration change results in a new configuration block transaction being generated.




### Gossip Protocol ###
	* the technical mechanism by which peers within an individual organization efficiently discover and communicate with each 		  other when an organization have large number of peer nodes.


###################################################################################################







#################################################     *What's New in v2.0*     ####################
### Decentralized Governance for Smart Contracts ###
	* new Fabric chaincode lifecycle allows multiple organizations to come to agreement on the parameters of a chaincode, such 	     as the chaincode endorsement policy, before it can be used to interact with the ledger.
	* it supports both centralized trust models (in v1.x previous lifecycle model) as well as decentralized models (in v2.0).
	* new model allows for a chaincode to be upgraded only after a sufficient number of organizations have approved the 		  upgrade.
	* Fabric lifecycle allows you to change an endorsement policy or private data collection configuration without having to 	   repackage or reinstall the chaincode. 
	* You can now use a single chaincode package and deploy it multiple times with different names on the same channel or on 	   different channels.
	* Chaincode packages do not need to be identical across channel members.
	
	
	
### Private Data Enhancements ###
	* Private data collections can now optionally be defined with an endorsement policy that overrides the chaincode-level 		  endorsement policy for keys within the collection.
	
	
	
### External Chaincode Launcher ###
	* Chaincode is no longer required to be run in Docker containers, and may be executed in the operator’s choice of 		  environment (including containers or  in a Kubernetes pod).
	* now possible to run *chaincode as an external service*, for example in a Kubernetes pod, which a peer can connect to and 		  utilize for chaincode execution.
	* *external chaincode launcher feature* -- An operator can provide a set of external builder executables to override how 	   the peer builds and launches chaincode.
	
	
	
### Alpine-based Docker Images ###
	* Starting with v2.0, Hyperledger Fabric Docker images will use Alpine Linux, a security-oriented, lightweight Linux 		  distribution.
	
	
	
### Upgrading to Fabric v2.0 ###
	* rolling upgrades from v1.4.x to v2.0 are supported, so that network components can be upgraded one at a time with no 		  downtime.
	
	
	
### Comparison of Chaincode Lifecycle b/w v1.x & v2.0 ###
	* in v1.x versions of Fabric, one organization had the ability to set parameters of a chaincode (for instance the 		  endorsement policy) for all other channel members, who only had the power to refuse to install the chaincode and 		  therefore not take part in transactions invoking it. 
	* in 2.0, it supports both centralized trust models (in v1.x previous lifecycle model) as well as decentralized models (in 		  v2.0) requiring a sufficient number of organizations to agree on an endorsement policy and other details before the 		  chaincode becomes active on a channel.

###################################################################################################








#################################################     *Justification*     #########################
### Confidentiality in Fabric N/W ###
	* one approach    - Encrypting data -- Given enough time and computational resource, the encryption could be broken.
	* second approach - Zero knowledge proofs (ZKP) -- computing a ZKP requires considerable time and computational resources. 								   Hence, the trade-off in this case is performance.
	* Both approaches have their trade-offs. So, Channels and Private Data Collections are used.
	
### Encryption of Transactions ###
	* To further obfuscate the data, values within chaincode can be encrypted (in part or in total) using common cryptographic 		  algorithms such as AES before sending transactions to the ordering service and appending blocks to the ledger. Once 		  encrypted data has been written to the ledger, it can be decrypted only by a user in possession of the corresponding key 		  that was used to generate the cipher text.
	
### Separation & collaboration b/w organizations ###
	* This is a very powerful concept – channels provide both a mechanism for the separation of organizations, and a mechanism 		  for collaboration between organizations. All the while, this infrastructure is provided by, and shared between, a set of 		  independent organizations.
	
	
### D/B Channel and Private Data Collections ###
	* channels keep transactions private from the broader network whereas collections keep data private between subsets of 		  organizations on the channel.
	
### Systems of Proof ###
	* In addition to being decentralized and collaborative, the information recorded to a blockchain is append-only, using 		  cryptographic techniques that guarantee that once a transaction has been added to the ledger it cannot be modified. This 	     property of “immutability” makes it simple to determine the provenance of information because participants can be sure 	   information has not been changed after the fact. It’s why blockchains are sometimes described as systems of proof.


### Final Version Check (i.e., Committing phase) - Double Spend Problem ###
	* final Version Check by peers in committing phase provides protection against *double spend operations* and other threats 		  that might compromise data integrity, and allows for functions to be executed against non-static variables.


### De-centralized Network ###
	* The careful use of network and channel policies allow even large networks to be well-governed. Organizations are free to 		  add peer nodes to the network so long as they conform to the policies agreed by the network. *Network and channel 		  policies* create the balance between *autonomy and control* which characterizes a de-centralized network.
	* Objects like network configurations, that are logically single, turn out to be physically replicated among a set of 		  ordering services nodes. channel configurations, ledgers, and to some extent smart contracts which are installed in 		  multiple places but whose interfaces exist logically at the channel level. It enables Hyperledger Fabric Blockchain 		  Network to be both *de-centralized* and yet *manageable* at the same time. 


###################################################################################################












#################################################     *Topics*    #################################
### System channel & Application Channel ###
	* Both network and channel configurations are kept consistent using the same blockchain technology that is used for user 		  transactions – but for configuration transactions. To change a network or channel configuration, an administrator must 		  submit a configuration transaction to change the network or channel configuration. It must be signed by organizations 	  identified in the appropriate policy as being responsible for configuration change. This policy is called the mod_policy 		  and we’ll discuss it later.
	* Indeed, the ordering service nodes operate a mini-blockchain, connected via the system channel we mentioned earlier. 		  Using the system channel ordering service nodes distribute network configuration transactions. These transactions are 	  used to co-operatively maintain a consistent copy of the network configuration at each ordering service node. In a 		  similar way, peer nodes in an application channel can distribute channel configuration transactions. Likewise, these 		  transactions are used to maintain a consistent copy of the channel configuration at each peer node.
	
	
	
### Importance of Consensus ###
	* consensus is not merely limited to the agreed upon order of a batch of transactions; rather, it is an overarching 		  characterization that is achieved as a byproduct of the ongoing verifications that take place during a transaction’s 		  journey from proposal to commitment.
	
	
### Formation of Blockchain Network ###
	* In most cases, multiple organizations come together as a consortium to form the network and their permissions are 		  determined by a set of policies that are agreed by the consortium when the network is originally configured. Moreover, 		  network policies can change over time subject to the agreement of the organizations in the consortium, as we’ll discover 		  when we discuss the concept of modification policy.
	
	
### careful addition of peers ###
	* more peers in a network will allow more applications to connect to it; and multiple peers in an organization will 		  provide extra resilience in the case of planned or unplanned outages.
	
	
### Types of peers ###
	* These are the two major types of peer:
		1)Committing Peer = Every peer node in a channel is a committing peer. It receives blocks of generated 					    transactions, which are subsequently validated before they are committed to the peer node’s 				    copy of the ledger as an append operation.
		2)Endorsing Peer = Every peer with a smart contract can be an endorsing peer if it has a smart contract installed. 					   However, to actually be an endorsing peer, the smart contract on the peer must be used by a 					   client application to generate a digitally signed transaction response. The term endorsing peer 					   is an explicit reference to this fact.
	* there are two other roles a peer can adopt:
		1)Leader peer = When an organization has multiple peers in a channel, a leader peer is a node which takes 					responsibility for distributing transactions from the orderer to the other committing peers in the 					organization. A peer can choose to participate in static or dynamic leadership selection.
		
		
		
### Leadership Selection for Leader Peer ###
	* A peer can choose to participate in static or dynamic leadership selection.
	* It is helpful, therefore to think of two sets of peers from leadership perspective – those that have static leader 		  selection, and those with dynamic leader selection. For the static set, zero or more peers can be configured as leaders. 		  For the dynamic set, one peer will be elected leader by the set. Moreover, in the dynamic set, if a leader peer fails, 		  then the remaining peers will re-elect a leader.
	* It means that an organization’s peers can have one or more leaders connected to the ordering service. This can help to 		  improve resilience and scalability in large networks which process high volumes of transactions.


### Determinism --- Smart Contracts ###
	* Smart contracts executing in a blockchain that operates with the order-execute architecture must be deterministic; 		  otherwise, consensus might never be reached. To address the non-determinism issue, many platforms require that the smart 		  contracts be written in a non-standard, or domain-specific language (such as Solidity) so that non-deterministic     		  operations can be eliminated. This hinders wide-spread adoption because it requires developers writing smart contracts 		  to learn a new language and may lead to programming errors.
	
	
	
### Decentralized Agreement --- Smart Contracts ###
	* Human decisions can be modeled into a chaincode process that spans multiple transactions. The chaincode may require 		  actors from various organizations to indicate their terms and conditions of agreement in a ledger transaction. Then, a 		  final chaincode proposal can verify that the conditions from all the individual transactors are met, and “settle” the 	  business transaction with finality across all channel members. For a concrete example of indicating terms and conditions 		  in private, see the asset transfer scenario in the Private data documentation.
	
	
### Permissionless Blockchain ###
	* open permissionless system that allows unknown identities to participate in the network (requiring protocols like “proof 		  of work” to validate transactions and secure the network), 
	
	
### Consensus - Practical Byzantine Fault Tolerance ###
	* PBFT can provide a mechanism for file replicas to communicate with each other to keep each copy consistent, even in the 		  event of corruption. Alternatively, in Bitcoin, ordering happens through a process called mining where competing 		  computers race to solve a cryptographic puzzle which defines the order that all processes subsequently build upon.
	
	
### Private Data Collections ###
	* When a subset of organizations on that channel need to keep their transaction data confidential, a private data 		  collection (collection) is used to segregate this data in a private database, logically separate from the channel 		  ledger, accessible only to the authorized subset of organizations.
	
	
### MSP -- should be cleared ###
	* Network configuration NC4 uses a named MSP to identify the properties of certificates dispensed by CA4 which associate 		  certificate holders with organization R4. NC4 can then use this MSP name in policies to grant actors from R4 particular 		  rights over network resources. An example of such a policy is to identify the administrators in R4 who can add new 		  member organizations to the network. We don’t show MSPs on these diagrams, as they would just clutter them up, but they 		  are very important.
###################################################################################################	


































