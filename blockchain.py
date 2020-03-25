#################################################     *ALL TOPICS*     ##################################################
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
		
		
		
### Smart Contracts ###
	* business logic of a blockchain application.
	* functions as a trusted distributed application.
	* many smart contracts run concurrently in the network
	* they may be deployed dynamically (in many cases by anyone)
	* application code should be treated as untrusted, potentially even malicious.
	* traditionally, chaincodes are launched by the peer, and then connect back to the peer.
	* in modern approach, now possible to run *chaincode as an external service*, for example in a Kubernetes pod, which a 		  peer can connect to and utilize for chaincode execution.
	
	
	
	
	
### Channels ###
	*  participants on a Fabric network establish a sub-network where every member has visibility to a particular set of 		   transactions.
	*  only those nodes that participate in a channel have access to the smart contract (chaincode) and data transacted, 		   preserving the privacy and confidentiality of both.
	
	
	
	
### Private Data Collection ###
	* It is a collection (like DB) between members on a channel, allowing much of the same protection as channels without the 		  maintenance overhead of creating and maintaining a separate channel.
	
	
	
	
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




###################################################################################################












#################################################     *Topics*    #################################
### Determinism --- Smart Contracts ###
	* Smart contracts executing in a blockchain that operates with the order-execute architecture must be deterministic; 		  otherwise, consensus might never be reached. To address the non-determinism issue, many platforms require that the smart 		  contracts be written in a non-standard, or domain-specific language (such as Solidity) so that non-deterministic     		  operations can be eliminated. This hinders wide-spread adoption because it requires developers writing smart contracts 		  to learn a new language and may lead to programming errors.
	
	
	
### Decentralized Agreement --- Smart Contracts ###
	* Human decisions can be modeled into a chaincode process that spans multiple transactions. The chaincode may require 		  actors from various organizations to indicate their terms and conditions of agreement in a ledger transaction. Then, a 		  final chaincode proposal can verify that the conditions from all the individual transactors are met, and “settle” the 	  business transaction with finality across all channel members. For a concrete example of indicating terms and conditions 		  in private, see the asset transfer scenario in the Private data documentation.
	
###################################################################################################	


































