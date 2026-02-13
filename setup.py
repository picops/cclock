from picobuild import get_cython_build_dir, Extension, find_packages, setup, cythonize


# C extensions
c_extensions = [
    Extension(
        "cclock.clock",
        ["src/cclock/clock.c"],
        extra_compile_args=[
            "-O3",
            "-march=native",
            "-Wno-unused-function",
            "-Wno-unused-variable",
        ],
        language="c",
    ),
]

# Cython extensions
cythonized_extensions = cythonize(
    [
        Extension(
            "cclock.*",
            ["src/cclock/*.pyx"],
            extra_compile_args=[
                "-O3",
                "-march=native",
                "-Wno-unused-function",
                "-Wno-unused-variable",
            ],
            language="c",
        ),
    ],
    compiler_directives={
        "language_level": 3,
        "boundscheck": False,
        "wraparound": False,
        "cdivision": True,
        "infer_types": True,
        "nonecheck": False,
        "initializedcheck": False,
    },
    build_dir=get_cython_build_dir(),
)

# Pybind extensions
pybind_extensions = []

# Build
if __name__ == "__main__":
    setup(
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        ext_modules=c_extensions + cythonized_extensions + pybind_extensions,
    )
