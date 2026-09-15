# Compile the C++ example

First complete the [Visual Studio component checklist](../Visual_Studio_Cpp_Checklist.md).

1. Open **x64 Native Tools Command Prompt for VS 2022** from the Windows Start menu.
2. Change to this downloaded `examples` folder. Use your actual extracted path; for example:

   ```bat
   cd /d "C:\AI\Lecture_01_Companion_Files\lecture-01\examples"
   ```

3. Compile the included source:

   ```bat
   cl /nologo /EHsc /std:c++17 hello.cpp /Fe:hello.exe
   ```

4. Run the program:

   ```bat
   hello.exe
   ```

Expected output:

```text
Week 01 C++ toolchain OK | sum=42
```

The source adds 6, 12 and 24 using the C++ standard library. The compiler creates local build files such as `hello.obj` and `hello.exe`; they are not downloads bundled with the course.

If `cl` is missing, open the named developer terminal again. If a header or library is missing, inspect the C++ workload installation and its selected components. See Microsoft's [command-line build guide](https://learn.microsoft.com/en-us/cpp/build/building-on-the-command-line?view=msvc-170).
