# Visual Studio for generative AI

Updated September 15, 2026. Use this checklist for the C++ setup demonstrated in Week 1.

Use **Visual Studio Community 2022** and select only **Desktop development with C++**. Keep its required core features. Select the following optional components (match names; installer order and patch numbers can change):

- MSVC v143 — VS 2022 C++ x64/x86 build tools
- C++ ATL for latest v143 build tools
- C++ Build Insights
- Just-In-Time debugger
- C++ profiling tools
- C++ CMake tools for Windows
- Test Adapter for Boost.Test
- Test Adapter for Google Test
- IntelliCode
- C++ AddressSanitizer
- Windows 11 SDK 10.0.26100.7705
- vcpkg package manager
- C++ MFC for latest v143 build tools
- C++ Modules for v143 build tools
- C++/CLI support for v143 build tools
- C++ Clang tools for Windows (19.1.5 in the reference)
- JavaScript diagnostics
- Windows 11 SDK 10.0.22621.0
- Windows 10 SDK 10.0.19041.0
- MSVC v142 — VS 2019 C++ x64/x86 build tools
- MSVC v141 — VS 2017 C++ x64/x86 build tools
- MSVC v140 — VS 2015 C++ build tools
- Windows App SDK C++ Templates

Leave **GitHub Copilot**, **Incredibuild — Build Acceleration**, and **Live Share** unchecked. Every other workload remains unchecked. The demonstration includes the Windows 10 SDK marked out of support. Check the component descriptions in your installer release.

This selection keeps several compiler versions and libraries available for the course's generative AI tasks. Community supplies the compiler toolchain, so this route needs no separate Build Tools installation.

## Why 2022

Use the established 2022 toolchain for compatibility with the CUDA versions and native extensions used in these tutorials. NVIDIA lists Visual Studio 2022 for [CUDA 12.8](https://docs.nvidia.com/cuda/archive/12.8.0/cuda-installation-guide-microsoft-windows/index.html). Visual Studio 2026 support starts with [CUDA 13.2 and Nsight 2026.1](https://docs.nvidia.com/nsight-visual-studio-edition/install-setup/index.html). Match each application's required CUDA and compiler versions. Selecting older side-by-side toolsets does not make all of them supported by every CUDA release.
