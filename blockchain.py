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
	* each peer maintains a copy of the ledger for each channel of which they are a member.
	* validate transactions against endorsement policies and enforce the policies.
	* Prior to appending a block (commit to ledger) after validating the transactions, a versioning check is performed to 		  ensure that states for assets that were read have not changed since chaincode execution time. (protection against the 	  double spend)
		
		
		
### Smart Contracts ###
	* business logic of a blockchain application.
	* functions as a trusted distributed application.
	* State transitions are a result of chaincode invocations, recorded as transactions.
	* invoked by an application external to the blockchain when that application needs to interact with the ledger.
	* chaincode interacts only with the database component of the ledger, the world state (querying it, for example), and not 		  the transaction log.
	* many smart contracts run concurrently in the network
	* they may be deployed dynamically (in many cases by anyone)
	* application code should be treated as untrusted, potentially even malicious.
	* traditionally, chaincodes are launched by the peer, and then connect back to the peer.
	* in modern approach, now possible to run *chaincode as an external service*, for example in a Kubernetes pod, which a 		  peer can connect to and utilize for chaincode execution.
	
	
	
	
	
### Channels ###
	* channels keep *transactions* private from the broader network.
	* participants on a Fabric network establish a sub-network where every member has visibility to a particular set of 		  transactions.
	* only those nodes that participate in a channel have access to the smart contract (chaincode) and data transacted, 		  preserving the privacy and confidentiality of both.
	* allowing a group of participants to create a separate ledger of transactions.
	* One Ledger per Channel.
	* channel’s ledger contains a configuration block defining policies, access control lists, and other pertinent information.
	* contain Membership Service Provider instances allowing for crypto materials to be derived from different certificate 		  authorities.
	
	
	
	
### Private Data Collection ###
	* collections keep *data* private between subsets of organizations on the channel.
	* is used to segregate the data in a private database, logically separate from the channel ledger, accessible only to the 		  authorized subset of organizations.
	* It is a collection (like DB) between members on a channel, allowing much of the same protection as channels without the 		  maintenance overhead of creating and maintaining a separate channel.
	
	
	
	
### Membership Service Provider MSP ###
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
	
	
### D/B Channel and Private Data Collections ###
	* channels keep transactions private from the broader network whereas collections keep data private between subsets of 		  organizations on the channel.
	
### Systems of Proof ###
	* In addition to being decentralized and collaborative, the information recorded to a blockchain is append-only, using 		  cryptographic techniques that guarantee that once a transaction has been added to the ledger it cannot be modified. This 	     property of “immutability” makes it simple to determine the provenance of information because participants can be sure 	   information has not been changed after the fact. It’s why blockchains are sometimes described as systems of proof.


### Final Version Check (i.e., Committing phase) - Double Spend Problem ###
	* final Version Check by peers in committing phase provides protection against *double spend operations* and other threats 		  that might compromise data integrity, and allows for functions to be executed against non-static variables.



###################################################################################################












#################################################     *Topics*    #################################
### Importance of Consensus ###
	* consensus is not merely limited to the agreed upon order of a batch of transactions; rather, it is an overarching 		  characterization that is achieved as a byproduct of the ongoing verifications that take place during a transaction’s 		  journey from proposal to commitment.



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
###################################################################################################	


































