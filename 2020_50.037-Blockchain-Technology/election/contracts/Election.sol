pragma solidity ^0.4.24;

contract Election {
    // Each election has ONE admin, at least TWO Candidates (passive)
    // and the remaining being voters (vote for candidates)


    address private admin; // admin needs account address to manage election

    struct Candidate {
        uint candidateId;
        string candidateName;
        Vote[] votes;
        uint voteCount;
    }

    struct Vote {
        string signature;
        string enc_nonce;
    }

    struct Voter {
        uint voterId;
        address voterAddress;
        bool hasVoted = false;
    }

    // Read/write candidates
    mapping(uint => Candidate) public candidates;
    // Store Candidates Count
    uint public candidatesCount;
    
    mapping(uint => Voter) public voters;
    uint public votersCount;



    constructor () public {
        admin = msg.sender
    }

    function addCandidate () private {
        require(msg.sender == admin)
        candidatesCount ++;
        candidates[candidatesCount] = Candidate({
                candidateId: candidatesCount,
                candidateName: "Candidate " + candidatesCount
            });
    }

    function addVoter (address _voter_address) private {
        require(msg.sender == admin)
        votersCount ++;
        voters[votersCount] = Voter({
                voterId: votersCount,
                voterAddress: _voter_address
            });

    }

    function vote (string _candidateName) private {
        require(msg.sender.hasVoted != null || undefined)
        require(msg.sender.hasVoted == false)
    }

    function getCandidates() view public returns(string[]){
        
        return(candidates);
    }

    function getVoters() view public returns(mapping){
        return(candidates);
    }

    function getElection
}