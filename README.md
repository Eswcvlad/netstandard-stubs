# Python type stubs for .NET Standard

This repository contains unofficial Python type stubs for 
[.NET Standard](https://learn.microsoft.com/en-us/dotnet/standard/net-standard),
that can be used to improve IDE experience for developers using
[Python.NET](https://github.com/pythonnet/pythonnet).

The initial type stubs were generated using the 
[pythonnet-stub-generator](https://github.com/MHDante/pythonnet-stub-generator)
project.

Docstrings are based on the official .NET API documentation, which is
available at [dotnet-api-docs](https://github.com/dotnet/dotnet-api-docs)
under a CC BY 4.0 license.

At the moment this project is focused on type stubs for .NET Standard 2.0.  

# Versioning

Versions will follow the `x.y.z` format, where `x.y` is the targeted version of
.NET Standard and `z` is the version of the stubs themselves.

So if you want to make sure, that type stubs cover only, for example, .NET
Standard 2.0, specify the version constraints like this:

```requirements
netstandard>=2.0,<2.1
```

# Installation

You can install netstandard-stubs with pip:

```shell
pip install netstandard-stubs
```
