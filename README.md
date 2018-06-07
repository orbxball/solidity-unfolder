# Solidity Unfolder

Unfolds all local imports in a solidity file to generate a flat solidity file.


## Introduction
Manually combining all imports in a solidity file when verifying your contract source on [Etherscan](https://etherscan.io) is time-consuming and cumbersome. This tool automatically traverses the dependency graph of imports and combines them in the correct order, which is ready to be pasted into the contract verifier.

> NOTE: This tool won't work with imports that are aliased (i.e. import "./foo.sol" as bar; )


## Installation

There are no requirements for this tool.

```
pip install solidity-unfolder
```


## Usage

```
usage: solu [-h] [-o *.sol] *.sol *.*.*

Unfolds all local imports in a solidity file to generate a flat solidity file.
Put the output file into out/ folders.

positional arguments:
  *.sol                 target filename with imports
  *.*.*                 solidity compiler version e.g. 0.4.24

optional arguments:
  -h, --help            show this help message and exit
  -o *.sol, --output *.sol
                        output filename (default: flat.sol)
```

### Example

```
solu contract-with-imports.sol 0.4.24
```
It will output `flat.sol` (default output filename) with solidity version `0.4.24` in `out/` folder.

```
solu contract-with-imports.sol 0.4.20 --output contract-flat.sol
```
It will output `contract-flat.sol` with solidity version `0.4.20` in `out/` folder.


## 	Contact
Feel free to [contact me](mailto:junyouliu9@gmail.com) if there's any problem. And welcome to open issues and send pull requests.

Inspired by [BlockCatIO](https://github.com/BlockCatIO/solidity-flattener).

### License

MIT License (2018), Jun-You Liu
