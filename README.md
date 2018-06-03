# Solidity Unfolder

Unfolds all local imports in a solidity file to generate a flat solidity file.


## Introduction
Manually combining all imports in a solidity file when verifying your contract source on [Etherscan](https://etherscan.io) is time-consuming and cumbersome. This tool automatically traverses the dependency graph of imports and combines them in the correct order, which is ready to be pasted into the contract verifier.

> NOTE: This tool won't work with imports that are aliased (i.e. import "./foo.sol" as bar; )


## Installation

There's no any requirements for this tool.

```
git clone <github link>
cd solidity-flattener
python3 solidity-flattener.py --help
```

## 	Contact
Feel free to [contact me](mailto:junyouliu9@gmail.com) if there's any problems. And welcome to open issues and send pull requests.